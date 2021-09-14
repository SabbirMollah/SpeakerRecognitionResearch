# Speaker Recognition Research
This repository contains quick prototyping scripts for various speaker recognition related tasks.

# Projects
## EvaluateAsrDatasetOnRawnet
In this project we extract the embeddings for our entire Bangla ASR dataset by using RawNet2 with its best weights. The best weights were provided by the original authors.
## TrainBdAsrOnRawNet2
This project has two separate notebooks. We use the PrepareDataset notebook to devise our own dataset splitting strategy. This outputs the splitted datasets in text files. After that, we train the RawNet using the BanglaAsr dataset.
## TrainLargeAsrOnRawNet2
In this project, we train the RawNet2 model on the Large Asr dataset. The large Asr dataset contains data of 5 languages including Bangla ASR.
## EvaluateTimitRawNetLargeAsr
In this project, we evaluate TIMIT with the RawNet2 trained on the LargeAsr dataset.
# Credits
[Jungjee et al](https://github.com/Jungjee/RawNet) Most of the RawNet related codes were taken from this repository.