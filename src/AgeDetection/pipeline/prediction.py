import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
    
    def predict(self):
        # Load model
        model = load_model(os.path.join("model", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        # Assuming your output layer has 3 neurons for 3 classes
        result = model.predict(test_image)
        predicted_class = np.argmax(result, axis=1)[0]

        class_labels = ['18-20', '21-30', '31-40', '41-50', '51-60']  # Modify this list according to your actual class labels

        prediction = class_labels[predicted_class]
        
        return [{"image": prediction}]

