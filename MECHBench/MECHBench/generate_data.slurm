#!/bin/bash
#SBATCH --job-name=gen_125d5_p1
#SBATCH --mail-user=o.lydakis.simantiris@umail.leidenuniv.nl
#SBATCH --mail-type=START,END,FAIL
#SBATCH --output=logs/test_%A_%a.out
#SBATCH --error=logs/test_%A_%a.err
#SBATCH --array=1
#SBATCH --ntasks=17
#SBATCH --nodes=1
#SBATCH --mem=4096MB
#SBATCH --partition=cpu-zen4
#SBATCH --time=25:00:00



#####sbutch --cpus-per-task=8
# Purge modules
module purge
# load modules (assuming you start from the default environment)
# we explicitly call the modules to improve reproducibility
# in case the default settings change

#FOSS
module load ALICE/default
module load slurm

# ACTIVATE OPENMPI
module load OpenMPI/4.1.4-GCC-11.3.0

module load OpenGL # ig?

#PYTHON
module load Python/3.10.4-GCCcore-11.3.0

# Activate the Python virtual environment 
source $HOME/thesis/mechbench_thesis/venv_mechbench/bin/activate

# Change source directory to the home directory
cd $HOME/thesis/mechbench_thesis
# source $HOME//venv_mechbench/bin/activate

Add executable permissions to the open_radioss binaries
chmod +x /home/s3872718/thesis/mechbench_thesis/OpenRadioss_linux64/OpenRadioss/exec/starter_linux64_gf
chmod +x /home/s3872718/thesis/mechbench_thesis/OpenRadioss_linux64/OpenRadioss/exec/engine_linux64_gf
chmod +x /home/s3872718/thesis/mechbench_thesis/OpenRadioss_linux64/OpenRadioss/exec/engine_linux64_gf_ompi
chmod +x /home/s3872718/thesis/mechbench_thesis/OpenRadioss_linux64/OpenRadioss/exec/th_to_csv_linux64_gf
chmod +x /home/s3872718/thesis/mechbench_thesis/OpenRadioss_linux64/OpenRadioss/exec/anim_to_vtk_linux64_gf
Specify the path to the config file
#config=$HOME/config_1_CMA_ES.txt

# Read the property from a file based on SLURM_ARRAY_TASK_ID
# Run Number	Algorithm	Random Seed	Budget	nmmcsx	nmmcsy	volfrac	problem	optimization_type	symmetry_active	batch_size	sigma_0
#algorithm=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $2}' $config)
#random_seed=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $3}' $config)
#budget=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $4}' $config)
#problem=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $8}' $config)
#nmmcsx=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $5}' $config)
#nmmcsy=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $6}' $config)
#volfrac=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $7}' $config)
#optimization_type=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $9}' $config)
#sym_active=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $10}' $config)
#batch_size=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $11}' $config)
#sigma_0=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $12}' $config)



# echo "Running topology optimization with property: $PROPERTY"
# Replace the following line with your actual command
#python3 $HOME/Topology_Optimization/experiment_runner.py --run_number $SLURM_ARRAY_TASK_ID --algorithm $algorithm --problem $problem --optimization_type $optimization_type --symmetry_active $sym_active --random_seed $random_seed --budget $budget --sigma_0 $sigma_0 --batch_size $batch_size --volfrac $volfrac --nmmcsx $nmmcsx --nmmcsy $nmmcsy

# run script with arguments problem, n_dimentions, size (how many times n_dimentions)
python3 $HOME/thesis/mechbench_thesis/MECHBench-main/generate_data.py 1 5 500

