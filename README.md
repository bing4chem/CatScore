# CatScore

This repo provides code for "CatScore: Automatic Evaluation of Catalyst Design" by Bing Yan. This repo is based off [T5Chem](https://github.com/HelloJocelynLu/t5chem) by Jieyu Lu and Yingkai Zhang. Note that this repo can be found at https://github.com/bing4chem/CatScore.

## Dependencies

The code has been tested on Python 3.8 and PyTorch 1.12.1.

* Python 3.8: `conda create --prefix ../conda_catscore python=3.8`
* PyTorch: https://pytorch.org/get-started/locally/ `conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=11.6 -c pytorch -c conda-forge`

In addition, install dependencies using

```
pip install -r requirements.txt
```

## Installation

```
python setup.py install
cd t5chem
export WORKING_DIR=$(pwd)
```


## Usage

Note that we always assume the working directory to be `WORKING_DIR`:

```
cd ${WORKING_DIR}
```

## Train a catalyst design model and generate from it

This project provides an automatic evaluation metric for catalyst design models, so we first need a catalyst design model. We will train such a model by finetuning a pretrained codet5. I am using the 1 percent setting (see my report for more details) as an example. For other settings simply change `1percent` to other percentages:

```
stdbuf -oL -eL python run_trainer.py --data_dir ../data/AHO/1percent/ --output_dir aho_1percent_catpred_val/ --task_type product --num_epoch 100 --pretrain Salesforce/codet5-small --num_classes 2 > log.train.aho.1percent.catpred.val 2>&1&
```

Next, we generate catalysts using the trained model.

```
stdbuf -oL python run_prediction_nostd.py --data_dir ../data/AHO/catpred/ --model_dir aho_1percent_catpred_val/ --task_type product --prediction may2_best_catpred_1percent.csv --output_logits 1
mkdir ../data/AHO/1percattest_best
python extract_test.py may2_best_catpred_1percent.csv ../data/AHO/aho_dataset_test.csv ../data/AHO/1percattest_best
```

## Train a product prediction model

The core idea in CatScore is to use a product prediction model to replace running real chemistry experiments to test how good the designed catalysts are. Therefore, we need to train a product prediction model.

```
stdbuf -oL -eL python run_trainer.py --data_dir ../data/AHO/1percentprod/ --output_dir aho_1percent_prodpred_val/ --task_type product --num_epoch 100 --pretrain Salesforce/codet5-small --num_classes 2 > log.train.aho.1percent.prodpred.val 2>&1&
```

## Compute CatScore

To compute CatScore, we use the predicted catalysts by the catalyst design model as input, and evaluate the likelihood of producing the target product under the product prediction model:

```
stdbuf -oL python run_prediction_nostd.py --data_dir ../data/AHO/1percattest_best/ --model_dir aho_1percent_prodpred_val/ --task_type product --prediction may2_best_cattest_1percent_catpred_1percent_prodpred.csv --output_logits 1
```

Now we can compute CatScore of the system by simply taking the average log likelihood:

```
python compute_catscore.py may2_best_cattest_1percent_catpred_1percent_prodpred.csv
```
