#!/bin/bash
#SBATCH --job-name=opt_on_mechbench
#SBATCH --mail-user=o.lydakis.simantiris@umail.leidenuniv.nl
#SBATCH --mail-type=START,END,FAIL
#SBATCH --output=logs/run_optimizers_%A_%a.out      
#SBATCH --error=logs/run_optimizers_%A_%a.err
#SBATCH --cpus-per-task=1
#SBATCH --array=1-270
#SBATCH --mem=4096MB
#SBATCH --partition=cpu-zen4
#SBATCH --time=40:00:00

LINE=$(sed -n "$((SLURM_ARRAY_TASK_ID))p" mechbench_optimizer_runs_jobs.txt)
PROBLEM=$(echo $LINE  | awk '{print $1}')
OPTIMIZER=$(echo $LINE | awk '{print $2}')
SEED=$(echo $LINE | awk '{print $3}')
# DECK_ID=$SLURM_ARRAY_TASK_ID
DECK_ID=$(( SLURM_ARRAY_TASK_ID + 1000 * SEED ))


module load ALICE/default
module load slurm

# ACTIVATE OPENMPI
module load OpenMPI/4.1.4-GCC-11.3.0

module load OpenGL # ig?
module load Miniforge3
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate conda_mechbench

chmod +x /home/s3872718/thesis/sMECHBench/alice/OpenRadioss_linux64/OpenRadioss/exec/starter_linux64_gf
chmod +x /home/s3872718/thesis/sMECHBench/alice/OpenRadioss_linux64/OpenRadioss/exec/engine_linux64_gf
chmod +x /home/s3872718/thesis/sMECHBench/alice/OpenRadioss_linux64/OpenRadioss/exec/engine_linux64_gf_ompi
chmod +x /home/s3872718/thesis/sMECHBench/alice/OpenRadioss_linux64/OpenRadioss/exec/th_to_csv_linux64_gf
chmod +x /home/s3872718/thesis/sMECHBench/alice/OpenRadioss_linux64/OpenRadioss/exec/anim_to_vtk_linux64_gf


python optimize_on_mechbench.py \
    --problem $PROBLEM \
    --optimizer $OPTIMIZER \
    --deck_id $DECK_ID \
    --seed $SEED

rm -rf /home/s3872718/thesis/sMECHBench/alice/*_deck${DECK_ID}/
