# utils import
import os
import pandas as pd
import requests


# ImageNet synsets tools
# -------------------------------------------------------------------------------------------------------------------


def synsets_map(root_path_dataset=None):
    '''
    Load  ImageNet meta_clsloc.mat map as csv
    :param root_path_dataset: folder path of Imagenet .csv maps
    :return: pandas
    '''
    if root_path_dataset is None:
        current_dir = os.path.dirname(os.path.realpath(__file__))
        root_path_dataset = os.path.join(os.path.dirname(os.path.dirname(current_dir)), 'data', 'ImageNet')

    for file in ['clsloc_class_labels.csv', 'det_class_labels.csv']:
        file_name = os.path.join(root_path_dataset, file)
        if os.path.isfile(file_name):
            class_map = pd.read_csv(file_name, names=['id', 'wnID', 'words'], header=0)
            return class_map

    raise Exception(" Maps files  are not available in %s !!!!. Update config.dataset_path " % root_path_dataset)


synsets_ImageNet = synsets_map()


# ImageNet mapping function
# -------------------------------------------------------------------------------------------------------------------
def synset_to_id(synset, synsets_map=None, to_categorize=True):
    '''
    Returns the ImageNet id corresponding to input synset
    :param synset: ImageNet synset (Ex: n02123394 )
    :param synsets_map: pandas synsets_ImageNet map (return of synsets_map() function)
    :param to_categorize: ImageNet range -> [1..1000] , categorization range -> [0..999]
                          to_categorrize is a parameter to select which range is desired
    :return: ImageNet id (Ex: for synset n02123394. id = 9 if to_categorize is True else id = 10)
    '''
    if synsets_map is None:
        synsets_map = synsets_ImageNet

    category_id = synsets_map[synsets_map['wnID'] == synset]['id']
    if (len(category_id)) == 0:
        return -1
    category_id = category_id.to_string(index=False)
    return int(category_id) - 1 if to_categorize else int(category_id)


# -------------------------------------------------------------------------------------------------------------------
def synset_to_words(synset, synsets_map=None):
    '''
    Returns the ImageNet category name corresponding to input synset
    :param synset: ImageNet synset (Ex: n02123394 )
    :param synsets_map: pandas synsets_ImageNet map (return of synsets_map() function)
    :return: ImageNet category name (Ex: or synset n02123394, return Persian_cat)
    '''
    if synsets_map is None:
        synsets_map = synsets_ImageNet
    category_name = synsets_map[synsets_map['wnID'] == synset]['words'].to_string(index=False)
    return category_name

# -------------------------------------------------------------------------------------------------------------------
def word_to_synset(word, synsets_map=None):
    '''
    Returns the ImageNet category name corresponding to input synset
    :param synset: ImageNet synset (Ex: n02123394 )
    :param synsets_map: pandas synsets_ImageNet map (return of synsets_map() function)
    :return: ImageNet category name (Ex: or synset n02123394, return Persian_cat)
    '''

    if synsets_map is None:
        synsets_map = synsets_ImageNet
    category_name = None
    if word in  synsets_map['words'].tolist():
         print(word)
         category_name = synsets_map[synsets_map['words'] == word]['wnID'].to_string(index=False)
    else:
        print("{} don exist.".format(word))

    return category_name

# -------------------------------------------------------------------------------------------------------------------


def id_to_synset(id_, synsets_map=None, to_categorize=True):
    '''
    Returns the ImageNet synset corresponding to input ImageNet id
    :param id_: ImageNet id
    :param synsets_map: pandas synsets_ImageNet map (return of synsets_map() function)
    :param to_categorize: ImageNet range -> [1..1000] , categorization range -> [0..999]
                          to_categorrize is a parameter to select which range is desired
    :return: ImageNet synset
    '''
    if synsets_map is None:
        synsets_map = synsets_ImageNet
    id_ = int(id_) + 1 if to_categorize else int(id_)
    return synsets_map[synsets_map['id'] == id_]['wnID'].to_string(index=False)


# -------------------------------------------------------------------------------------------------------------------


def id_to_words(id_, synsets_map=None, to_categorize=True):
    '''
    Returns the ImageNet category name corresponding to input ImageNet id
    :param id_: ImageNet id
    :param synsets_map: pandas synsets_ImageNet map (return of synsets_map() function)
    :param to_categorize: ImageNet range -> [1..1000] , categorization range -> [0..999]
                          to_categorrize is a parameter to select which range is desired
    :return: ImageNet category name
    '''
    if synsets_map is None:
        synsets_map = synsets_ImageNet
    id_ = int(id_) + 1 if to_categorize else int(id_)
    return synsets_map[synsets_map['id'] == id_]['words'].to_string(index=False)


# get functions

def search_in_ImageNet(word, verbose=False):
    if verbose:
        print("Searching {} in ImageNet synsets dataset".format(word))
        print('=' * 60)
    r = requests.get("http://www.image-net.org/search?q=" + word)
    synsets = []
    if r.status_code == 200:
        # print('==' * 100)
        if verbose:
               print("Match synset exist?:", 'href="synset?wnid=' in r.text)
        split_text = r.text.split(sep='href="synset?wnid=')
        for i in split_text[1:]:
            if '"><img src="' in i:
                # print('-'*120)
                synset = i.split(sep='"><img src="')[0]
                if synset not in synsets:
                    synsets.append(synset)
    return synsets


def synsets_child(nsynset, verbose=False):
    child = []
    r = requests.get("http://www.image-net.org/api/text/wordnet.structure.hyponym?wnid={}".format(nsynset))
    if r.status_code == 200:
        if verbose:
            print('-' * 120, nsynset)
        # print(r.text)
        split_text = r.text.split(sep='-')
        # print(split_text)
        for synset in split_text:
            child.append(synset.split(sep='\r\n')[0])
    if verbose:
        print(child)
    return child


def get_ImageNet_synsets(word, verbose=False):
    synsets = word_to_synset(word)
    if synsets is None:
          synsets = search_in_ImageNet(word, verbose=verbose)
    else:
        synsets =[synsets]
    if verbose:
        print(synsets)
        print("=" * 100)
    childs = [synsets_child(synset) for synset in synsets]
    # flatten list
    childs = [item for sublist in childs for item in sublist]
    if verbose:
        print(childs)
    return childs
