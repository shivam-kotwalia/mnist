import os


class Config(object):
    mnist_weights = os.path.join(os.getcwd(), "app", "services", 'mnist_weights', "model-epoch-30.ckpt")
    devnagri_weights = os.path.join(os.getcwd(), "app", "services", 'devnagri_weights', "model-epoch-27.ckpt")
