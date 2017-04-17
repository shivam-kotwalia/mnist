import base64
import os
import uuid
import numpy as np
from PIL import Image
from flask import Flask, render_template, request
import services
import tefla.predict as predict_mnist

app = Flask(__name__)
#if running from wsgi
mnist_weights = os.path.join(os.getcwd(),"app/services/weights/model-epoch-30.ckpt")

#if running from app
#mnist_weights = os.path.join(os.getcwd(),"services/weights/model-epoch-30.ckpt")

#print(mnist_weights)

@app.route("/")
def mainpage(methods=["GET", "POST"]):
    if request.method == "POST":
        print(request.form)
    if request.method == "GET":
        return render_template("index.html")

@app.route("/predict" ,methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        image_folder = os.path.join(os.getcwd(), "images")
        image_name = request.json['image']
        image_name = image_name.split(",")[1]
        # print(image_name)
        fh = open("one.png", "wb")
        fh.write(base64.b64decode(image_name))
        fh.close()
        image_filename = str(uuid.uuid4()) + ".tiff"

        with Image.open("one.png").convert('L') as image:
            image = image.resize([28, 28])
            img = Image.fromarray(np.uint8(image))
            img.save(image_filename)

        image_path_array = np.array([image_filename])
        predictions = predict_mnist.predict(model=services.mnist_model.model, model_def=services.mnist_model, output_layer ="predictions", cnf = services.mnist_cnf.cnf, weights_from=mnist_weights,
                                                                                                                           images = image_path_array, sync = True, convert = False, image_size = 28, predict_type = "1_crop")
        os.remove(image_filename)
        #print(predictions)
        predict_ = np.argmax(predictions)
        print(predict_)

    return str(predict_)

if __name__ == "__main__":
    app.run(debug=True)