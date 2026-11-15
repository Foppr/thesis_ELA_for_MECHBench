#!/bin/bash

# --- PARAMETER CONFIGURATION ---
# Easily edit these arrays later if you want to change problems or modes
PROBLEMS=(1 2 3)
ES_CONFIGS=("1E1" "2E4" "4E8")
SLURM_FILE="ela.slurm"

# Get current date in YYYY-MM-DD format
CURRENT_DATE=$(date +%Y-%m-%d)
# -------------------------------

echo "Launching LLaMEA batch submissions..."

for p in "${PROBLEMS[@]}"; do
    for c in "${ES_CONFIGS[@]}"; do
        # Modified to start with the dynamic date variable
        JOB_NAME="${CURRENT_DATE}_ela_p${p}_(${c})"

        echo "Submitting: $JOB_NAME"

        sbatch --job-name="$JOB_NAME" \
               --export=ALL,PROBLEM_TYPE=$p,ES_CONFIG=$c \
               $SLURM_FILE
    done
done

echo "All 9 jobs submitted successfully! Check status with 'squeue -u $USER'"
