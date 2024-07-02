import numpy
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import np_utils
from keras import optimizers

seed = 7
numpy.random.seed(seed)

(x_train, y_train), (x_test, y_test) = mnist.load_data(path='mnist.npz')


#flatten 28*28 images to a 784 vector for each image
num_pixels = x_train.shape[1] * x_train.shape[2]
x_train = x_train.reshape(x_train.shape[0], num_pixels).astype('float32')
x_test = x_test.reshape(x_test.shape[0], num_pixels).astype('float32')

#normalize inputs from 0-255 to 0-1
x_train = x_train/255
x_test = x_test/255

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
num_classes = y_test.shape[1]


def baseline_model():
    model = Sequential()
    #model.add(Dense(num_pixels, input_dim=num_pixels, kernel_initializer='normal', activation = 'sigmoid'))
    model.add(Dense(num_pixels, input_dim=num_pixels, kernel_initializer='normal', activation = 'relu'))
    #model.add(Dense(num_pixels, kernel_initializer='normal', activation = 'relu'))
    model.add(Dense(num_classes, kernel_initializer='normal', activation='softmax'))
    #compile model
    #model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    #model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
    model.compile(loss='categorical_crossentropy', optimizer=optimizers.SGD(lr=0.1), metrics=['accuracy'])

    return model 


if __name__ == "__main__":
    #build the model
    model = baseline_model()
    #Fit the model
    model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=10, batch_size=200, verbose=2)
    #model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=10, batch_size=100, verbose=2)
    #Final evalution of the model
    scores = model.evaluate(x_test, y_test, verbose=0)
    print("Error: %.2f%%" %(100-scores[1]*100))
