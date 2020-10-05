from __future__ import print_function
# keras
from keras.applications.imagenet_utils import decode_predictions
# gsdp
from .base import Extractor
from ..utils.imagenet_tools import synset_to_id


class SimpleExtractor(Extractor):
    """
    Class for feature extractor using custom models
    """

    def __init__(self, config):
            """
            Constructor
            """
            # ------------------------------------------------------------
            # Call base init function
            super(SimpleExtractor, self).__init__(config)
    # --------------------------------------------------------------------------------------------

    def top1_highest_prediction(self, img, from_path=False, processed_img=False, verbose=False):
            '''
            Top1 Category prediction
            :param img: PIL image or image path
            :param from_path: flag  to   set  the  image  input   type
            :param processed_img:  preprocessing flag
            :param verbose: logs
            :return: Category prediction
            '''
            if processed_img is False:
                img = self._input_preprocessing(img, from_path=from_path)

            # get the predicted probabilities for each class
            prob = self.model.predict_proba(img, verbose=verbose)[0]

            #if prob.shape[-1] > 1:
            category_index = prob.argmax(axis=-1)  #category_index= self.model.predict_classes(img, verbose=verbose)[0]
            probability = prob.max(axis=-1)

            return category_index, probability
# ------------------------------------------------------------------------------------------------
#  END  Simple extractor
# ------------------------------------------------------------------------------------------------


class ImageNetExtractor(Extractor):
    """
    Class for feature extractor using Keras ImageNet models
    """

    def __init__(self, config):
            """
            Constructor
            """
            # ------------------------------------------------------------
            # Call base init function
            super(ImageNetExtractor, self).__init__(config)
    # ---------------------------------------------------------------------------------------------

    def top1_highest_prediction(self, img, from_path=False, processed_img=False, verbose=False, proba = False):
            '''
            Top1 Category prediction
            :param img: PIL image or image path
            :param from_path: flag  to   set  the  image  input   type
            :param processed_img:  pre-processing flag
            :param verbose: logs
            :return: Category prediction
            '''
            if processed_img is False:
                img = self._input_preprocessing(img, from_path=from_path)
            # get the predicted probabilities for each class
            yhat = self.model.predict(img, verbose=verbose)
            #print(yhat)
            # retrieve the most likely result, e.g. highest probability
            pred = decode_predictions(yhat, top=1)
            inID, label, prob = pred[0][0]
            category_index = synset_to_id(inID)
            #print('%s %s %s (%.2f%%)' % (inID, str(category_index), label, prob * 100))
            if verbose:
                print('%s %s %s (%.2f%%)' % (inID, str(category_index), label, prob * 100))
            return category_index, prob
    # ------------------------------------------------------------------------------------------------
#  END  ImageNet extractor
