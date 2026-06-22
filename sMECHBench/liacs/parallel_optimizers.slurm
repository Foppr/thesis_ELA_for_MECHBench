#!/bin/bash
#SBATCH --job-name=run_optimizers
#SBATCH --mail-user=o.lydakis.simantiris@umail.leidenuniv.nl
#SBATCH --mail-type=START,END,FAIL
#SBATCH --output=logs/run_optimizers_%A_%a.out      
#SBATCH --error=logs/run_optimizers_%A_%a.err
#SBATCH --cpus-per-task=1
#SBATCH --mem=4096MB
#SBATCH --partition=cpu-zen4


# LINE=$(sed -n "$((SLURM_ARRAY_TASK_ID))p" jobs.txt)

LINE_NUM=$(( SLURM_ARRAY_TASK_ID + OFFSET ))
LINE=$(sed -n "${LINE_NUM}p" "$JOBS_FILE")

PROBLEM=$(echo $LINE  | awk '{print $1}')
SIZE=$(echo $LINE     | awk '{print $2}')
MODEL=$(echo $LINE    | awk '{print $3}')
OPTIMIZER=$(echo $LINE | awk '{print $4}')
SEED=$(echo $LINE | awk '{print $5}')

echo "array $SLURM_ARRAY_TASK_ID: problem=$PROBLEM size=$SIZE model=$MODEL optimizer=$OPTIMIZER"

# source ~/miniconda3/etc/profile.d/conda.sh
# conda activate mechbench
module load ALICE/default
module load slurm

# ACTIVATE OPENMPI
module load OpenMPI/4.1.4-GCC-11.3.0

module load OpenGL # ig?
module load Miniforge3
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate conda_mechbench

python parallel_optimizers.py \
    --problem   $PROBLEM \
    --size      $SIZE \
    --model     $MODEL \
    --optimizer $OPTIMIZER \
    --seed $SEED