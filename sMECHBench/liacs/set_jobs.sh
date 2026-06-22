#!/bin/bash

BATCH_SIZE=${1:-1000}

# mkdir -p logs

submit_file() {
    local jobs_file=$1
    local time_limit=$2
    local label=$3

    local TOTAL
    TOTAL=$(wc -l < "$jobs_file")

    local N_BATCHES=$(( (TOTAL + BATCH_SIZE - 1) / BATCH_SIZE ))

    for (( batch=0; batch<N_BATCHES; batch++ )); do
        local OFFSET=$(( batch * BATCH_SIZE ))
        local END=$(( BATCH_SIZE < TOTAL - OFFSET ? BATCH_SIZE : TOTAL - OFFSET ))

        sbatch \
            --array=1-${END} \
            --time=${time_limit} \
            --export=ALL,OFFSET=${OFFSET},JOBS_FILE=${jobs_file} \
            --job-name="${label}_batch_${batch}" \
            parallel_optimizers.slurm


    done
}

# submit_file "jobs_p_1and2.txt" "1:30:00" "short"
# submit_file "jobs_p3.txt"  "6:00:00" "long"
# submit_file "jobs_p_1and2_bn.txt" "2:00:00" "bn_p1and2"
submit_file "jobs_long_bn.txt" "6:00:00" "bn_p3"