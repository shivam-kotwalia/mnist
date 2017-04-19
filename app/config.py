import os


class Config(object):
    mnist_weights = os.path.join(os.getcwd(), "app", "services", 'weights', "model-epoch-30.ckpt")
