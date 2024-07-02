from perceptron import Perceptron
import matplotlib.pyplot as plt
import numpy as np

f = lambda x: x

class LinearUnit(Perceptron):
    def __init__(self, input_num):
        Perceptron.__init__(self, input_num, f)

def get_training_dataset():

    input_vecs = [[5], [3], [8], [1.4], [10.1]]
    labels = [5500, 2300, 7600, 1800, 11400]
    return input_vecs, labels


def train_linear_unit():

    lu = LinearUnit(1)
    input_vecs, labels = get_training_dataset()
    lu.train(input_vecs, labels, 10, 0.01)

    return lu

if __name__ == "__main__":
    linear_unit = train_linear_unit()
    print(linear_unit)

    predict_year = [[3.4], [15], [1.5], [6.3]]
    predict_year_list = [3.4, 15, 1.5, 6.3]
    predict_salary = []
    for year in predict_year:
        predict_salary.append(linear_unit.predict(year))
    for i in range(4):    
        print("work",predict_year_list[i], "years, monthly salary = %.2f" % predict_salary[i])
    
    """-----------start to draw------------"""
    input_vecs = [5, 3, 8, 1.4, 10.1]
    labels = [5500, 2300, 7600, 1800, 11400]

    fig, ax = plt.subplots()
    ax.set_title('salary prediction')
    ax.set_xlabel('working years', fontsize=15)
    ax.set_ylabel('salary', fontsize=15)
    """green color: training set"""
    ax.scatter(input_vecs, labels, color="green", alpha=0.5)
    """red color: predict set"""
    ax.scatter(predict_year_list, predict_salary, color="red", alpha=0.5)

    t = np.arange(0.0, 20.0, 0.01)
    s = linear_unit.weights * t + linear_unit.bias
    ax.plot(t,s)
    
    ax.grid(True)
    plt.show()
