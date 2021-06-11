#Author: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Date: 2021/06/11
#Description:
    #These codes I improved from Professor's document and translate to English to.
    # Number recognition program using Keras (deep learning)
    # In this practice, I use and update some functions:
    # 1. Using TensorFlow backend
    # 2. Using MNIST dataset
    # 3. Build model using Keras
    # 4. Write function to convert physical image to array vector
    # 5. Run model and predict function to regcognize the number
    # 6. Use pyplot to show processing and predict result
    # 7.Test some cases to recognize number
#Step 1. Import some necessarily library
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import np_utils
from keras.datasets import mnist
import cv2

# Step 2. Load MNIST Dataset
#Load data from the MNIST dataset, including 60,000 training sets and 10,000 test sets.
# Then divide the training set to 2 parts: 50,000 for training set and 10,000 data for validation set.
(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_val, y_val = X_train[50000:60000,:], y_train[50000:60000]
X_train, y_train = X_train[:50000,:], y_train[:50000]
#print to see data
print(X_train.shape)

# Step 3. Reshape the data to the correct size required by keras
# Input data for the Convolutional Neural Network model is a 4-dimensional tensor (N, W, H, D),
#in this MNIST dataset is a grayscale image so W = H = 28, D = 1,
#N is the number of images for each training session.
#Because the image data above has the size of (N, 28, 28) ie (N, W, H)
#so need to reshape to N 28 28 * 1 size to match the size required by keras.
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_val = X_val.reshape(X_val.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)

# Step 4. One hot encoding label (Y)
#This step converts the one-hot encoding label Y of the example
#image number 5 into a vector [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
Y_train = np_utils.to_categorical(y_train, 10)
Y_val = np_utils.to_categorical(y_val, 10)
Y_test = np_utils.to_categorical(y_test, 10)
#print result to see
print('Original data y', y_train[0])
print('y after one-hot encoding ',Y_train[0])

# Step 5. Model definition
#1.Model = Sequential() to tell keras that we will layer layers on top of each other to create models.
# Example input -> CONV -> POOL -> CONV -> POOL -> FLATTEN -> FC -> OUTPUT
#2.In the first layer, We need to specify the input_shape of the image, input_shape = (W, H, D),
#   we use grayscale image size (28.28) so input_shape = (28, 28, 1)
#3.When adding a Convolutional Layer, we need to specify the parameters: K (number of layers),
#  kernel size (W, H), activation function to use.
#  structure: model.add(Conv2D(K, (W, H), activation='function_name_activation'))
#4.When adding a Maxpooling Layer, specify the size of the kernel, model.add(MaxPooling2D(pool_size=(W, H)))
#5.Flatten step from tensor to vector just add flatten layer.
#6.To add Fully Connected Layer (FC) need to specify the number of nodes in the layer and the activation
# function used in the layer, structure: model.add(Dense(number_node_activation='activation_function_name'))

model = Sequential()

# Add Convolutional layer with 32 kernels, kernel size 3*3
# use sigmoid function as activation and specify input_shape for first layer
model.add(Conv2D(32, (3, 3), activation='sigmoid', input_shape=(28, 28, 1)))

# Add Convolutional layer
model.add(Conv2D(32, (3, 3), activation='sigmoid'))

# Add Max pooling layer
model.add(MaxPooling2D(pool_size=(2, 2)))

# Flatten layer convert from tensor to vector
model.add(Flatten())

# Add Fully Connected layer with 128 nodes and use sigmoid . function
model.add(Dense(128, activation='sigmoid'))

# Output layer with 10 nodes and use softmax function to convert to probability.
model.add(Dense(10, activation='softmax'))

# Step 6. Compile model, specify which loss_function to use, method
# is used to optimize the loss function.
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Step 7. Train model with data
H = model.fit(X_train, Y_train, validation_data=(X_val, Y_val),
          batch_size=32, epochs=10, verbose=1)

# Step 8. Plot loss, accuracy of training set and validation set
fig = plt.figure()
numOfEpoch = 10
plt.plot(np.arange(0, numOfEpoch), H.history['loss'], label='training loss')
plt.plot(np.arange(0, numOfEpoch), H.history['val_loss'], label='validation loss')
plt.plot(np.arange(0, numOfEpoch), H.history['accuracy'], label='accuracy')
plt.plot(np.arange(0, numOfEpoch), H.history['val_accuracy'], label='validation accuracy')
plt.title('Accuracy and Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss|Accuracy')
plt.legend()

# Step 9. Model evaluation with test set data
score = model.evaluate(X_test, Y_test, verbose=0)
#print result to see
print(score)
#[0.033531852066516876, 0.9901999831199646]
# We will use the evaluation result of the mode with the test set to make the final result of the model.
# That is, our model predicts digits with 99% accuracy with the MNIST dataset.
# That is, predicting about 100 images will be wrong by 1 image.

# Step 10. Number prediction
# create conv_image_to_data function to convert image file to array 28x28
def conv_image_to_data(filename):
    img_array = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    img_pil = Image.fromarray(img_array)
    img_28x28 = np.array(img_pil.resize((28, 28), Image.ANTIALIAS))

    img_array = (img_28x28.flatten())

    img_array  = img_array.reshape(-1,1).T

    return img_array
#call conv_image_to_data to test image digit-5.png
data=conv_image_to_data("ch27_images\digit-5.png")
#show image into chart
plt.imshow(data.reshape(28,28), cmap='Blues')
#call predict function
y_predict = model.predict(data.reshape(1,28,28,1))
#get number recognition and show into title of Chart
plt.title('Predict number is '+str(np.argmax(y_predict)))
plt.show()