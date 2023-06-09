from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D

"""

    This function creates a CNN model.

"""

def model(activation='softmax'):

    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3),
                     activation=activation,
                        input_shape=(100, 100, 1)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(2, activation=activation))

    return model


__name__ == '__main__' and print('model.py works!')
