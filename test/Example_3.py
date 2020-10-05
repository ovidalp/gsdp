'''
GSDP Example 3:
GSDP Image Description using VGG16 Keras-model.
'''


from gsdp import GlobalSemanticDescriptor
from gsdp import TEST_PATH
from keras.preprocessing.image import load_img
from keras.models import model_from_json
# session config
#import tensorflow as tf
# from tensorflow.compat.v1 import ConfigProto
# from tensorflow.compat.v1 import InteractiveSession
# conf = ConfigProto()
# conf.gpu_options.allow_growth = True
# sess = InteractiveSession(config=conf)
# tf.compat.v1.keras.backend.set_session(sess)

#others
from tqdm import tqdm

# Model
gsdp = GlobalSemanticDescriptor('ResNet50')
# print extractor config
# gsdp.extractor.config.print()

# Load PIL image
img_test = TEST_PATH + '/imgs/image.jpg'
image = load_img(img_test, target_size=gsdp.extractor.input_shape_2D)

# Base Model feature extraction
VGG16_feature = gsdp.base_feature(image,verbose=False)
print('VGG16 feature shape: ', VGG16_feature.shape)
#print('VGG16 feature shape: ', VGG16_feature[:10])
#print(gsdp.extractor.config.print())

# GSDP feature extraction
#for _ in tqdm(range(1000)):
#    GSDP_feature = gsdp.feature(image)
GSDP_feature = gsdp.feature(image)
print('GSDP feature shape: ', GSDP_feature.shape)
#print('GSDP feature shape: ', GSDP_feature[:10])

