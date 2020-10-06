#!/bin/bash
# sysinfo_page - A script to download and prepare models data

# USAGE:
# ./prepare_data.sh
# Get app computer vision current version
MAJOR=$(grep '__MAJOR__ =' gsdp/__init__.py | awk '{print  $3}')
MINOR=$(grep '__MINOR__ =' gsdp/__init__.py | awk '{print  $3}')
PATCH=$(grep '__PATCH__ =' gsdp/__init__.py | awk '{print  $3}')
GSDP_VERSION="$MAJOR.$MINOR.$PATCH"
MNIST_DATA="https://www.dropbox.com/sh/4cc354mmrgmzfkw/AACNLRkfcxFXPyLd7pcVqr_Ua?dl=0"
CIFAR_DATA="https://www.dropbox.com/sh/8zo0vinzjw7dkon/AACDvzF33SW5gvPknb5HYu7ua?dl=0"
RESNET_DATA="https://www.dropbox.com/sh/68rfgo9r6mstuwi/AACNeHsgoHdVlDv7yo400SJja?dl=0"
VGG16_DATA="https://www.dropbox.com/sh/niwle7omleobxli/AAAqKsV-Hs3rd0eTMQnncbQoa?dl=0"

echo "========================================================"
echo " Downloading necessary GSDP package data  "
echo " Current GSDP package version : $GSDP_VERSION           "
echo "========================================================"

prepare_data() {
  local OUT_DIR
  MODEL_NAME=$1
  DATA_LINK=$2
  OUT_DIR="models/"$MODEL_NAME
 # OUT_TGZ=$1"_logs_"$APP_VERSION"_$MTC800_ID-$_day-$_time.tar.gz"
  TMP_FILE=$MODEL_NAME".zip"
  echo "Downloading data/prototypes of '"$MODEL_NAME" model as /"$TMP_FILE"'..."
  wget $DATA_LINK -O $TMP_FILE
  echo "Copying all data  to '"$OUT_DIR"' directory ..."
  unzip $TMP_FILE -d $OUT_DIR
  echo "Remove temporary file: '"$TMP_FILE"'..."
  rm $TMP_FILE
}
prepare_data "MNIST" $MNIST_DATA
prepare_data "CIFAR" $CIFAR_DATA
prepare_data "ResNet50" $RESNET_DATA
prepare_data "VGG16" $VGG16_DATA