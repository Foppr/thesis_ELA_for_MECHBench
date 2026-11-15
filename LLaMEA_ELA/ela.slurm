#!/bin/bash
#SBATCH --job-name=ela_for_mechbench
#SBATCH --output=out_logs/%x_%j.out
#SBATCH --error=err_logs/%x_%j.err
#SBATCH --time=04:00:00
#SBATCH --partition=gpu-short
#SBATCH --gres=gpu:a100:1       # Allocates 1 NVIDIA A100 GPU
#SBATCH --mem=40G               # System RAM allocation
#SBATCH --cpus-per-task=4       # 4 CPU cores for execution handling

# Load environment modules
module load Python/3.11.5-GCCcore-13.2.0

# This tells BOTH the server and the Python client library to use 127.0.0.1 instead of 'localhost'
export OLLAMA_HOST="127.0.0.1:11434"
export OLLAMA_MODELS="/zfsstore/user/s2995387/.ollama/models"
mkdir -p "$OLLAMA_MODELS"

echo "Starting Ollama server daemon on the compute node..."
SERVER_LOG="out_logs/ollama_server_${SLURM_JOB_ID}.log"
$HOME/ELA_for_MECHBench/ollama_system/bin/ollama serve > "$SERVER_LOG" 2>&1 &
SERVER_PID=$!

# ... (Keep Sections 1, 2, and 3 exactly the same)

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

# FORCE COMPUTE NODE TO RESPOND TO MODEL
# If for some reason it's still not showing up, this forces a local sync link
$HOME/ELA_for_MECHBench/ollama_system/bin/ollama show qwen3-coder:30b > /dev/null 2>&1 || {
    echo "Model not indexed on this node. Re-verifying manifest local pointer..."
    $HOME/ELA_for_MECHBench/ollama_system/bin/ollama pull qwen3-coder:30b
}

echo "Activating virtual environment and launching Python experiment..."
source $HOME/ELA_for_MECHBench/ela_env/bin/activate

python3 ELA_for_MECHBench.py

echo "Stopping Ollama server process..."
kill $SERVER_PID
