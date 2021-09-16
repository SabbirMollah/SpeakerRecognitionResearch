# Speaker Recognition Research

This repository contains quick prototyping scripts for various speaker recognition related tasks.

# Projects

## EvaluateAsrDatasetOnRawnet

In this project we extract the embeddings for our entire Bangla ASR dataset by using RawNet2 with its best weights. The best weights were provided by the original authors.

## TrainBdAsrOnRawNet2

This project has two separate notebooks. We use the PrepareDataset notebook to devise our own dataset splitting strategy. This outputs the splitted datasets in text files. After that, we train the RawNet using the BanglaAsr dataset.

## TrainTimitOnRawNet2

This project has two separate notebooks. We use the PrepareDataset notebook to devise our own dataset splitting strategy. This outputs the splitted datasets in text files. After that, we train the RawNet using the Timit dataset.

## Knowledge Distillation

In this project we are currently thinking of approaches to use knowledge distillation.

# Credits

[Jungjee et al](https://github.com/Jungjee/RawNet) Most of the RawNet related codes were taken from this repository.
