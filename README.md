# Global Semantic Descriptor based on Prototypes
[![Version](https://img.shields.io/badge/version-1.1.0-brightgreen.svg)](https://www.verlab.dcc.ufmg.br/global-semantic-description)
[![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)](LICENSE)

# Project #

This project contains the code and data used to generate the results reported in the paper [Prototypicality effects in global semantic description of objects](https://www.verlab.dcc.ufmg.br/global-semantic-description/wacv2019/) on the **IEEE Winter Conference on Applications of Computer Vision (WACV) 2019**. It implements a global semantic description of object using semantic prototypes of objects categories.

For more information and visual results, please access the [project page](https://www.verlab.dcc.ufmg.br/global-semantic-description/).

## Contact ##

### Authors ###

* Omar Vidal Pino - PhD student - UFMG - ovidalp@dcc.ufmg.br
* Erickson Rangel do Nascimento - Advisor - UFMG - erickson@dcc.ufmg.br
* Mario Fernando Montenegro Campos - Advisor - UFMG - mario@dcc.ufmg.br

### Institution ###

Federal University of Minas Gerais (UFMG)  
Computer Science Department  
Belo Horizonte - Minas Gerais -Brazil 

### Laboratory ###

![VeRLab](https://www.dcc.ufmg.br/dcc/sites/default/files/public/verlab-logo.png)

**VeRLab:** Laboratory of Computer Vision and Robotics   
https://www.verlab.dcc.ufmg.br

## Citation ##

If you are using GSDP descriptor for academic purposes, please cite:
     
     O. Vidal Pino, E. R. Nascimento and M. F. M. Campos, 
     Prototypicality Effects in Global Semantic Description of Objects,
     2019 IEEE Winter Conference on Applications of Computer Vision (WACV), 
     Waikoloa Village, HI, USA, 2019, pp. 1233-1242, doi: 10.1109/WACV.2019.00136.
     
### Bibtex entry ###

>@InProceedings{vidal2019wacv,  
>title = {Prototypicality Effects in Global Semantic Description of Objects},  
booktitle = {2019 IEEE Winter Conference on Applications of Computer Vision (WACV)},  
>author = {Omar Vidal Pino and Erickson R. Nascimento and Mario F. M. Campos},  
>Year = {2019},  
>Address = {Waikoloa Village, HI, USA},  
>month = {January},  
>pages = {1233-1242},  
>volume = {},  
>number = {},  
>doi = {10.1109/WACV.2019.00136}
>}

     

## GSDP package ##
![Version 3.0](https://img.shields.io/pypi/pyversions/Django.svg)

### Dependencies ###

* Keras 2.3  _(Tested with 2.3.1)_  
* Tensorflow 2.1 _(Tested with 2.1.0)_
* Matplotlib 2.0 _(Tested with 2.0.2)_  
* H5py 2.7 _(Tested with 2.7.0)_ 
* Pandas 0.20 _(Tested with 0.20.3)_ 

### Installation ###

Installation for Python 3 environment (Python3 and pip3 active):

    git clone git clone https://github.com/ovidalp/gsdp.git
    cd gsdp/
    pip install -r requirements.txt 
    ./prepare_data.sh
    pip install .
   
Installation without Python 3 environment:

    git clone git clone https://github.com/ovidalp/gsdp.git
    cd gsdp/
    pip3 install -r requirements.txt 
    ./prepare_data.sh
    pip3 install .
    
Read more at [GSDP documentation](https://verlab.github.io/gsdp/).
