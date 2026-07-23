#!/bin/bash

# example submission script

#SBATCH --job-name=de_finetune_pred
#SBATCH --account=x # <--- replace with your allocation account
#SBATCH --gpus-per-node=1               
#SBATCH --cpus-per-task=8       
#SBATCH --mem=16G                   
#SBATCH --time=0-00:10              
#SBATCH --output=de_%j.out    
#SBATCH --error=de_%j.err  

module load gcc arrow python rdkit scipy-stack

source ../chemberta_env/bin/activate 

python finetune_de_pred.py
