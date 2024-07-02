#Plot ad hoc mnist instances

from keras.datasets import mnist
import matplotlib.pyplot as plt

#load(downloaded if needed) the MNIST dataset

(x_train, y_train), (x_test, y_test) = mnist.load_data(path='mnist.npz')

#plot 4 images as gray scale

plt.subplot(221)
plt.imshow(x_train[0], cmap=plt.get_cmap('gray'))

plt.subplot(222)
plt.imshow(x_train[1], cmap=plt.get_cmap('gray'))

plt.subplot(223)
plt.imshow(x_train[2], cmap=plt.get_cmap('gray'))

plt.subplot(224)
plt.imshow(x_train[3], cmap=plt.get_cmap('gray'))

#show the plot
plt.show()
