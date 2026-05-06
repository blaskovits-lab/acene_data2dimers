# From Data to Dimers: Engineering Acene Derivatives for Photovoltaic Singlet Fission

This repository contains the code and data used for training models to predict the scalar energies of acene derivatives from their SMILES strings (link to paper).

## Installation

1. Clone the repository

```bash
git clone https://github.com/aljamesc/acene_data2dimers.git
cd acene_data2dimers
```

2. Setup virtual environment

```bash
# create
python3 -m venv chemberta_env

# activate
source chemberta_env/bin/activate

# install packages
pip install -r requirements.txt
```
3. Download pretrained ChemBERTa (for further pretraining)

```bash
python download_seyonec_chemberta.py
```

## Usage

1. Run domain specific pretraining of ChemBERTa

```bash
cd pretrain
python pretrain.py
cd ..
# we submit as a job using pretrain.sh
```

2. Run regression finetuning and predictions on the molecule library SMILES

```bash
# for t1 model and predictions
cd finetune_predict
python finetune_t1_pred.py

# for de model and predictions
python finetune_de_pred.py

# optional: create bash scripts similar to pretrain.sh for submission
```

## Contents

- ```download_seyonec_chemberta.py``` is to download a pretrained ChemBERTa model.
- ```pretrain``` contains ```pretrain.py```, the script used for domain specific pretraining of the seyonec_chemberta model. Running this script produces ```chemberta_380k``` and this directory contains the model used for downstream supervised regression. ```380k_smiles_data.txt``` is the training data and contains canonized SMILES strings obtained from PubChem that contain an anthracene substructure, and 15750 SMILES strings generated as described in the paper.
- ```finetune_predict``` contains ```finetune_t1_pred.py``` and ```finetune_de_pred.py```, which are used to run supervised finetuning and immediate predictions for excited state energies. ```labeled_data_t1.csv``` and ```labeled_data_de.csv``` contain SMILES and respective energy labels (N=2503) computed using TD-DFT at the wB97XD/6-31G(d) level. N=928 are anthracene containing molecules obtained from the FORMED database and N=1575 are computed as described in the paper. The training and validation loss for the models employed in the paper are logged in ```loss_log_t1.csv``` and ```loss_log_t1.csv```. Predictions are performed on the SMILES in ```mol_library.smi``` (N=15750) with the results saved to ```t1_predictions.csv``` and ```de_predictions.csv```.
- ```monomer_data_1575``` contains the optimized geometries as xyz files of N=1575 monomers computed at the wB97XD/6-31G(d) level.
- ```hit_smiles.csv``` contains the 146 hit molecule SMILES as described in the paper.

## Citation

If you use this code please cite the paper.

```bash
bibtex to come
```

ChemBERTa was downloaded and initialized from Chithrananda et al.

```bash
@article{ahmad2022chemberta,
  title={Chemberta-2: Towards chemical foundation models},
  author={Ahmad, Walid and Simon, Elana and Chithrananda, Seyone and Grand, Gabriel and Ramsundar, Bharath},
  journal={arXiv preprint arXiv:2209.01712},
  year={2022}
}
```

A portion of the regression training data was obtained from the FORMED database.

```bash
@article{blaskovits2022formed,
  title={Data-driven discovery of organic electronic materials enabled by hybrid top-down/bottom-up design},
  author={Blaskovits, J. Terence and Laplaza, R. and Vela, S. and Corminboeuf, C.},
  journal={Materials Cloud Archive},
  volume={2022.162},
  year={2022},
  doi={10.24435/materialscloud:j6-e2}
}
```

## Contact

Any questions related to this work can be addressed to crossalexj@gmail.com




