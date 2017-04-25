import os
import services

class Config(object):
    # mnist_weights = os.path.join(os.getcwd(), "app", "services", 'mnist_weights', "model-epoch-30.ckpt")
    # devnagri_weights = os.path.join(os.getcwd(), "app", "services", 'devnagri_weights', "model-epoch-27.ckpt")
    all_num_weights = os.path.join(os.getcwd(), "app", "services", 'main_weights', "model-epoch-19.ckpt")
    devnagri_char_weights = os.path.join(os.getcwd(), "app", "services", 'devnagri_char_weights', "model-epoch-50.ckpt")
