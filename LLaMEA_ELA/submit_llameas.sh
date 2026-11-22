#!/bin/bash
SLURM_FILE="ela.slurm"
CURRENT_DATE=$(date +%Y-%m-%d)

mkdir -p out_logs err_logs

echo "Launching 225-task LLaMEA job array..."
sbatch --job-name="${CURRENT_DATE}_ela_bbob" "$SLURM_FILE"

echo "Submitted! Check status with 'squeue -u $USER'"