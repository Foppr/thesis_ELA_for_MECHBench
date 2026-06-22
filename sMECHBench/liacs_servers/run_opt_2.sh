#!/bin/bash
set -euo pipefail

TASK_ID=$1   # replaces $SLURM_ARRAY_TASK_ID

LINE=$(sed -n "${TASK_ID}p" foppe_split_2.txt)
PROBLEM=$(echo $LINE | awk '{print $1}')
OPTIMIZER=$(echo $LINE | awk '{print $2}')
SEED=$(echo $LINE | awk '{print $3}')
DECK_ID=$(( TASK_ID + 1000 * SEED ))


source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate conda_mechbench

# NOTE: these absolute paths are ALICE-specific (/home/s3872718/thesis/...).
# Update to wherever the repo lives on the new server.
chmod +x /home/s2995387/thesis/sMECHBench/liacs/OpenRadioss_linux64/OpenRadioss/exec/starter_linux64_gf
chmod +x /home/s2995387/thesis/sMECHBench/liacs/OpenRadioss_linux64/OpenRadioss/exec/engine_linux64_gf
chmod +x /home/s2995387/thesis/sMECHBench/liacs/OpenRadioss_linux64/OpenRadioss/exec/engine_linux64_gf_ompi
chmod +x /home/s2995387/thesis/sMECHBench/liacs/OpenRadioss_linux64/OpenRadioss/exec/th_to_csv_linux64_gf
chmod +x /home/s2995387/thesis/sMECHBench/liacs/OpenRadioss_linux64/OpenRadioss/exec/anim_to_vtk_linux64_gf

python optimize_on_mechbench.py \
    --problem $PROBLEM \
    --optimizer $OPTIMIZER \
    --deck_id $DECK_ID \
    --seed $SEED

rm -rf /home/s2995387/thesis/sMECHBench/liacs/*_deck${DECK_ID}/