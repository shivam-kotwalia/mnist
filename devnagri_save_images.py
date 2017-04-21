from __future__ import division, print_function, absolute_import

import os
import shutil
from PIL import Image
import skimage
import numpy as np
import pandas as pd


width = 28
height = 28
data_dir = os.path.join(os.getcwd(),"devnagri_data")


def save(predict_type):
    save_path = os.getcwd() + "/data_devnagri/" + predict_type + "ing" + "_28"
    if os.path.exists(save_path):
        shutil.rmtree(save_path)
    os.makedirs(save_path)
    df_main = pd.DataFrame()
    for digit_folder in os.listdir(data_dir + "/" + predict_type):
        digit = digit_folder.split("_")[1]
        image_name_array = []
        df = pd.DataFrame()
        print("In digit %s" % (digit_folder))
        for index, image in enumerate(os.listdir(data_dir + "/" + predict_type + "/" + digit_folder)):
            image_name = predict_type + "ing_" + str(digit) + "_" + str(index)
            image_name_array.append(image_name)
            shutil.copy(os.getcwd()+ "/devnagri_data/" + predict_type + "/" + digit_folder + "/" + image, save_path + "/" + image_name+".png")
        df = pd.DataFrame({'image': image_name_array, 'label': digit})
        df_main = df_main.append(df, ignore_index=True)
    df_main.to_csv('%s/%sing_labels.csv' % (save_path, predict_type), index=False)

save("test")
save("train")






# train_images =
# train_labels = mnist[0].labels
#
# validation_images = mnist[1].images.reshape(-1, height, width)
# validation_labels = mnist[1].labels
#
# test_images = mnist[2].images.reshape(-1, height, width)
# test_labels = mnist[2].labels
#
# train_images = np.vstack((train_images, validation_images))
# train_labels = np.concatenate((train_labels, validation_labels))
#
# os.makedirs(os.path.join(os.getcwd(), "data_devnagri", "images"))
# base_dir = os.getcwd() + "/data/images/"
#
# if os.path.exists(base_dir):
#     shutil.rmtree(base_dir)
#
#
# def save_images(images, dir):
#     save_path = base_dir + dir + '_28'
#     os.makedirs(save_path)
#     prefix = dir
#     for i, img_data in enumerate(images):
#         img_data2 = skimage.img_as_ubyte(img_data)
#         img = Image.fromarray(img_data2)
#         img.save('%s/%s_%d.tiff' % (save_path, prefix, i))
#
#
# def save_labels(labels, name):
#     save_path = base_dir
#     prefix = name
#     img_names = ['%s_%d' % (prefix, i) for i in range(len(labels))]
#     df = pd.DataFrame({'image': img_names, 'label': labels})
#     df.to_csv('%s/%s_labels.csv' % (save_path, name), index=False)
#
#
# save_images(train_images, 'training')
# save_labels(train_labels, 'training')
# save_images(test_images, 'validation')
# save_labels(test_labels, 'validation')
# print('done')
