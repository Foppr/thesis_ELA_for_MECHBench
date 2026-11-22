#!/bin/bash
#SBATCH --job-name=ela_for_bbob
#SBATCH --output=out_logs/%x_%A_%a.out
#SBATCH --error=err_logs/%x_%A_%a.err
#SBATCH --array=0-224
#SBATCH --time=01:30:00
#SBATCH --partition=gpu-short
#SBATCH --gres=gpu:1
#SBATCH --mem=40G               # System RAM allocation
#SBATCH --cpus-per-task=4       # 4 CPU cores for execution handling

# --- PARAMETER GRID (5 x 5 x 3 x 3 = 225) ---
seeds=(1312 1313 1314 1315 1316)
fids=(1 6 10 15 20)
dims=(5 10 20)                  # Update if using different dimensions (e.g., 5 15 20)
ES_CONFIGS=("1E1" "2E4" "4E8")

# Decode SLURM_ARRAY_TASK_ID (0..224) into indices
n_c=${#ES_CONFIGS[@]}
n_d=${#dims[@]}
n_f=${#fids[@]}

c_idx=$(( SLURM_ARRAY_TASK_ID % n_c ))
d_idx=$(( (SLURM_ARRAY_TASK_ID / n_c) % n_d ))
f_idx=$(( (SLURM_ARRAY_TASK_ID / (n_c * n_d)) % n_f ))
s_idx=$(( SLURM_ARRAY_TASK_ID / (n_c * n_d * n_f) ))

export seed=${seeds[$s_idx]}
export fid=${fids[$f_idx]}
export dim=${dims[$d_idx]}
export ES_CONFIG=${ES_CONFIGS[$c_idx]}

echo "Task ${SLURM_ARRAY_TASK_ID}: fid=${fid}, dim=${dim}, ES_CONFIG=${ES_CONFIG}, seed=${seed}"

# Load environment modules
module load Python/3.11.5-GCCcore-13.2.0

# Unique localhost port per array task prevents collisions on multi-GPU nodes
OLLAMA_PORT=$((11434 + SLURM_ARRAY_TASK_ID))
export OLLAMA_HOST="127.0.0.1:${OLLAMA_PORT}"
export OLLAMA_MODELS="/zfsstore/user/s2995387/.ollama/models"
mkdir -p "$OLLAMA_MODELS" out_logs err_logs

echo "Starting Ollama server daemon on ${OLLAMA_HOST}..."
SERVER_LOG="out_logs/ollama_server_${SLURM_ARRAY_JOB_ID}_${SLURM_ARRAY_TASK_ID}.log"
$HOME/ELA_for_MECHBench/ollama_system/bin/ollama serve > "$SERVER_LOG" 2>&1 &
SERVER_PID=$!

echo "Waiting for Ollama server to respond at http://${OLLAMA_HOST}..."
SUCCESS=0
for i in {1..20}; do
    if curl -s "http://${OLLAMA_HOST}/" > /dev/null; then
        echo "SUCCESS: Ollama server is up and listening!"
        SUCCESS=1
        break
    fi
    echo "Server not ready yet, retrying in 3 seconds... (Attempt $i/20)"
    sleep 3
done

if [ $SUCCESS -eq 0 ]; then
    echo "CRITICAL ERROR: Ollama server failed to start."
    cat "$SERVER_LOG"
    exit 1
fi

echo "--- Models visible to the compute node ---"
$HOME/ELA_for_MECHBench/ollama_system/bin/ollama list
echo "------------------------------------------"

$HOME/ELA_for_MECHBench/ollama_system/bin/ollama show qwen3-coder:30b > /dev/null 2>&1 || {
    echo "Model not indexed on this node. Re-verifying manifest local pointer..."
    $HOME/ELA_for_MECHBench/ollama_system/bin/ollama pull qwen3-coder:30b
}

echo "Activating virtual environment and launching Python experiment..."
source $HOME/ELA_for_MECHBench/ela_env/bin/activate

"$VIRTUAL_ENV/bin/python" ELA_for_BBOB.py

echo "Stopping Ollama server process..."
kill $SERVER_PID