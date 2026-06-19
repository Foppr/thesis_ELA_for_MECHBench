#!/bin/bash
#set_arrays.sh 


TOTAL_ROWS=2500      # total rows in your CSV
BATCH_SIZE=1000   # max array size

for (( offset=0; offset<TOTAL_ROWS; offset+=BATCH_SIZE )); do
    # Don't overshoot on the last batch
    remaining=$(( TOTAL_ROWS - offset ))
    size=$(( remaining < BATCH_SIZE ? remaining : BATCH_SIZE ))

    sbatch --array=1-${size} \
           --export=ALL,BIAS_NUM=${offset} \
           MECHBench/parallel.slurm
done