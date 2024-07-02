import numpy as np
import matplotlib.pyplot as plt

def sigmoid(inputs):

    sigmoid_scores = [1.0/(1.0 + np.exp(-x)) for x in inputs]
    return sigmoid_scores


def line_graph(x, y, x_title, y_title):

    plt.plot(x, y)
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.show()


graph_x = np.arange(-5, 5, 0.1)
graph_y = sigmoid(graph_x)

line_graph(graph_x, graph_y, "Inputs", "Sigmoid Scores")
