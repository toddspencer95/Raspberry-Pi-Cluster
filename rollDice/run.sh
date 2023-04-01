#!/bin/bash
#SBATCH --nodes=1                 # Request 1 node
#SBATCH --ntasks-per-node=1       # Request 1 task per node
#SBATCH --cpus-per-task=1         # Request 1 CPU per task
#SBATCH --time=00:10:00           # Set a time limit for your job (hh:mm:ss)

cd $SLURM_SUBMIT_DIR

python3 rollDie.py
