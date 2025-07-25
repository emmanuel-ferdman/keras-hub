from keras_hub.src.api_export import keras_hub_export
from keras_hub.src.layers.preprocessing.image_converter import ImageConverter
from keras_hub.src.models.dinov2.dinov2_backbone import DINOV2Backbone


@keras_hub_export("keras_hub.layers.DINOV2ImageConverter")
class DINOV2ImageConverter(ImageConverter):
    backbone_cls = DINOV2Backbone
