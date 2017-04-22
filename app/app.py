import base64, os, uuid, services
import numpy as np
from PIL import Image
from flask import Flask, render_template, request, jsonify
import tefla.predict as predict_mnist
from config import Config

app = Flask(__name__)
conf = Config()



@app.route("/")
def mainpage():
    if request.method == "POST":
        print(request.form)
    if request.method == "GET":
        return render_template("index.html")


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        image_data64 = request.json['image']
        # if request.json['language'] == 'english':
        #     weights = conf.mnist_weights
        # else:
        #     weights = conf.devnagri_weights
        image_data64 = image_data64.split(",")[1]
        image_filename = str(uuid.uuid4()) + ".tiff"

        image = open(image_filename, "wb")
        image.write(base64.b64decode(image_data64))
        image.close()

        with Image.open(image_filename).convert('L') as image:
            image = image.resize([28, 28])
            img = Image.fromarray(np.uint8(image))
            img.save(image_filename)

        image_path_array = np.array([image_filename])
        predictions = predict_mnist.predict(model=services.mnist_model.model,
                                            model_def=services.mnist_model,
                                            output_layer="predictions",
                                            cnf=services.mnist_cnf.cnf,
                                            weights_from=conf.all_weights,
                                            images=image_path_array,
                                            sync=True,
                                            convert=False,
                                            image_size=28,
                                            predict_type="1_crop")
        prediction = np.argmax(predictions)
        if prediction > 9:
            prediction = prediction -10
            main_result = {"prediction": prediction, "language": "Hindi"}
            main_result = [prediction,"Hindi"]
        else:
            main_result = {"prediction": prediction, "language": "English"}
            main_result = [prediction,"English"]            
        print("%s in %s" % (main_result[0], main_result[1]))

        #Cleaning Images
        os.remove(image_filename)

    return jsonify(main_result)

if __name__ == "__main__":
    app.run(debug=True)
