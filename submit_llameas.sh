#!/bin/bash

# --- PARAMETER CONFIGURATION ---
# Easily edit these arrays later if you want to change problems or modes
PROBLEMS=(1 2 3)
NICHING_MODES=("None" "sharing")
MUTATION_PROMPTS=("None" "yes")
SLURM_FILE="ela.slurm"
# -------------------------------

echo "Launching LLaMEA batch submissions..."

for p in "${PROBLEMS[@]}"; do
    for n in "${NICHING_MODES[@]}"; do
        for m in "${MUTATION_PROMPTS[@]}"; do
            JOB_NAME="ela_p${p}_niching${n}_mutations${m}"

            echo "Submitting: $JOB_NAME (Problem: $p, Niching: $n, Mutations: $m)"

            sbatch --job-name="$JOB_NAME" \
                   --export=ALL,PROBLEM_TYPE=$p,NICHING=$n,MUTATION=$m \
                   $SLURM_FILE
        done
    done
done

echo "All 12 jobs submitted successfully! Check status with 'squeue -u $USER'"