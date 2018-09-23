import numpy as np
def array_generator(size, data):
    array_data = []
    for i in range(size):
        random_number1 = np.random.random()
        random_number2 = np.random.random()
        temp_data_1 = int(data * random_number1)
        temp_data_2 = int(data * random_number2)
        array_data.append(int(temp_data_1-temp_data_2))
    array_sort = sorted(array_data)
    return array_sort
