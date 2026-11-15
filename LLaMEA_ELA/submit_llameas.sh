#!/bin/bash

# --- PARAMETER CONFIGURATION ---
# Easily edit these arrays later if you want to change problems or modes
seeds=(1312 1313 1314 1315 1316)
fids=(1 6 10 15 20)
ES_CONFIGS=("1E1" "2E4" "4E8")
SLURM_FILE="ela.slurm"

# Get current date in YYYY-MM-DD format
CURRENT_DATE=$(date +%Y-%m-%d)
# -------------------------------

echo "Launching LLaMEA batch submissions..."

for seed in "${seeds[@]}"; do
    for fid in "${fids[@]}"; do
        for c in "${ES_CONFIGS[@]}"; do
            # Modified to start with the dynamic date variable
            JOB_NAME="${CURRENT_DATE}_ela_f${fid}_(${c})_seed${seed}"

            echo "Submitting: $JOB_NAME"

            sbatch --job-name="$JOB_NAME" \
                   --export=ALL,seed=$seed,fid=$fid,ES_CONFIG=$c \
                   $SLURM_FILE
        done
    done
done

echo "All 75 jobs submitted successfully! Check status with 'squeue -u $USER'"
