#!/bin/bash
#SBATCH -A b1045               # Allocation
#SBATCH -p short                # Queue
#SBATCH -t 04:00:00             # Walltime/duration of the job
#SBATCH -N 1                    # Number of Nodes
#SBATCH --mem=18G               # Memory per node in GB needed for a job. Also see --mem-per-cpu
#SBATCH --ntasks-per-node=6     # Number of Cores (Processors)
#SBATCH --mail-user=ascourtas@u.northwestern.edu  # Designate email address for job communications
#SBATCH --mail-type=BEGIN,END,FAIL     # Events options are job BEGIN, END, NONE, FAIL, REQUEUE
#SBATCH --output=/projects/b1045/AoT/AoT-denoiser/out.txt    # Path for output must already exist
#SBATCH --job-name="denoiser-find-anomalies"       # Name of job

# unload any modules that carried over from your command line session
module purge

# load modules you need to use
module load python/anaconda3.6

source activate denoiser

python process_data.py
