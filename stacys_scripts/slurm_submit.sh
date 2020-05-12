#!/bin/bash
#SBATCH -A b1045                # Allocation
#SBATCH -p buyin                # Queue
#SBATCH -t 24:00:00             # Walltime/duration of the jo
#SBATCH --output=sat_2.out
#SBATCH --job-name="sat.out"       # Name of job
#SBATCH --mem=10G


# PROCESSING AOT
# Waggle scripts available at: https://github.com/waggle-sensor/data-tools

#module purge all
#module load /software/Modules/3.2.9/modulefiles/python/anaconda3.6
#source activate my-env

# USER INPUT
START_DATE="2018-01-01"
END_DATE="2019-06-30"
ALL_AOT="/projects/b1045/AoT/AoT_Chicago.complete.2019-09-06/"
SLICE_AOT="../data/AoT_Chicago.complete.recent.csv"
NEW_DIR="AoT_Chicago.complete.2019-09-06.from-$START_DATE-to-$END_DATE"

echo "Starting AOT manipulation..."

# slice dates
#python3 /home/asm0384/AoT_processing/data-tools.git/trunk/slice-date-range/slice-date-range.py $ALL_AOT $START_DATE $END_DATE


# make sure the path is an output of the previous script
#gunzip /projects/b1045/AoT/$NEW_DIR/data.csv.gz
#echo "1/7: Unzipped data file"

#make a copy to save just in case, drop stuff from drop file
#cp /projects/b1045/AoT/$NEW_DIR/data.csv /projects/b1045/AoT/$NEW_DIR/data_drop.csv
#echo "2/7: Copy Done"

# drop the variables that aren't specified – f1 = filein f2= fileout
#python3 /home/asm0384/drop_unneeded_variables.py /projects/b1045/AoT/$NEW_DIR/data.csv /projects/b1045/AoT/$NEW_DIR/data_drop.csv
python3 drop_unneeded_variables.py $SLICE_AOT ../data/data_drop.csv
echo "3/7: Dropped unused variables"

# copy dropped dataset with a switched header
# TODO: ask Stacy why this was again -- I think it was something with the waggle tools
#sed '1s/.*/timestamp,node_id,subsystem,sensor,parameter,value_hrf,value_raw/' /projects/b1045/AoT/$NEW_DIR/data_drop.csv > /projects/b1045/AoT/$NEW_DIR/data_head_diff.csv
sed '1s/.*/timestamp,node_id,subsystem,sensor,parameter,value_hrf,value_raw/' ../data/data_drop.csv > ../data/data_head_diff.csv
echo "4/7: Changed header"

#save original dataset with original
cp $SLICE_AOT ../data/data_original.csv
echo "5/7: Saved original dataset"

# make the new headed dataset the target for the next scripts 
mv ../data/data_head_diff.csv ../data/data.csv
echo "6/7: Manipulating dataset"

#Actually reduce the timestep of the 6 month dataset
python3 ../../data-tools/data-reduction-tool/dataReduction.py -v 10000 -i ../data/ -t 30m
echo "7/7: Completed time averaging"
echo "Completed AOT processing!"
