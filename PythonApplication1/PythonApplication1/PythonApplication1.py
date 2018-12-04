import numpy
from keras.models import Sequential

from keras.layers import Dense
from keras.utils import np_utils

#задаем seed для повторяемости
numpy.random.seed(42)

# Загружаем данные
(X_train, y_train), (X_test, y_test) = mnist.load_data()