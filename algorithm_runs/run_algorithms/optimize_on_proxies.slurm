#!/bin/bash
#SBATCH --job-name=proxy_algo_opt
#SBATCH --mail-user=f.van.berkel@umail.leidenuniv.nl
#SBATCH --mail-type=START,END,FAIL
#SBATCH --output=out_logs/opt_on_proxies_%x_%A_%a.out
#SBATCH --error=err_logs/opt_on_proxies_%x_%A_%a.err
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --partition=cpu-skylake
#SBATCH --time=08:00:00
#SBATCH --array=0-14

module load ALICE/default
module load slurm

# ACTIVATE OPENMPI
module load OpenMPI/4.1.4-GCC-11.3.0

module load OpenGL

# ! --------------------------------------------------------------------- !
source $HOME/thesis_ELA_for_MECHBench/sMECHBench/smechbench_env/bin/activate

# Define seeds and export the one corresponding to this array task index
SEEDS=(1312 1313 1314 1315 1316 1317 1318 1319 1320 1321 1322 1323 1324 1325 1326)
export SEED=${SEEDS[$SLURM_ARRAY_TASK_ID]}

echo "Running array task $SLURM_ARRAY_TASK_ID with SEED=$SEED"

python optimize_on_proxies.py