import numpy as np


def matrix_multiplication(x, y):
    """
    Multiply 2 matrices of the same dtype
    """
    n_rows = x.shape[0]
    n_cols = y.shape[1]
    if x.dtype == y.dtype:
        mult_matrix = np.zeros((n_rows, n_cols), dtype=x.dtype)
    else:
        mult_matrix = np.zeros((n_rows, n_cols), dtype="complex")

    for i in range(n_rows):
        for j in range(n_cols):
            mult_matrix[i, j] = np.sum(x[i, :] * y[:, j])
    return mult_matrix


def multiplication_check(arrays):
    """
    Check if matrices in a list can be multiplied
    """
    for i in range(0, len(arrays) - 1):
        n_cols_1 = arrays[i].shape[1]
        n_rows_2 = arrays[i + 1].shape[0]
        if n_cols_1 != n_rows_2:
            return False
        return True


def multiply_matrices(arrays):
    """
    Multiply matrices in a list
    """
    if not multiplication_check(arrays):
        return None
    else:
        array = matrix_multiplication(arrays[0], arrays[1])
        for i in range(2, len(arrays)):
            array = matrix_multiplication(array, arrays[i])
    return array


def compute_2d_distance(x, y):
    """
    Compute distance between 2D vectors
    """
    return np.sqrt(np.sum(np.square(x - y)))


def compute_multidimensional_distance(x, y):
    """
    Compute distance between multidimensional vectors
    """
    return np.sqrt(np.sum(np.square(x - y)))


def compute_pair_distances(x):
    """
    Compute pair distance matrix
    """
    nvec = x.shape[0]
    distance_matrix = np.zeros((nvec, nvec))
    for i in range(nvec - 1):
        dist = np.sqrt(np.sum(np.square(x[i, ] - x[i + 1:, ]), axis=1))
        distance_matrix[i, i + 1:] = dist
        distance_matrix[i + 1:, i] = dist
    return distance_matrix


def length_vector(x):
    """
    Calculate length of a 1D vector (complex or real)
    """
    return np.real(np.sqrt(np.sum(x * np.conjugate(x))))


def transpose(x):
    """
    Transpose a matrix
    """
    transposed_x = np.zeros((x.shape[1], x.shape[0]), dtype=x.dtype)
    for i in range(len(x)):
        transposed_x[:, i] = x[i]
    return transposed_x


def conjugate_transpose(x):
    """
    Conjugate transpose a matrix
    """
    return transpose(x).conjugate()


if __name__ == "__main__":
    matrix1 = (np.random.randint(10, size=12) + np.random.randint(10, size=12) * 1j).reshape(6, 2)
    matrix2 = np.arange(1, 10).reshape((3, 3))
    matrix3 = np.eye(3)
    print("Matrix 1: ", matrix1)
    print("Matrix 2: ", matrix2)
    print("Matrix 3: ", matrix3)
    dic_fun = {
        "matrix multiplication": matrix_multiplication,
        "multiplication check": multiplication_check,
        "multiply matrices": multiply_matrices,
        "compute 2d distance": compute_2d_distance,
        "compute multidimensional distance": compute_multidimensional_distance,
        "compute pair distances": compute_pair_distances,
        "compute length of vector": length_vector,
        "transpose": transpose,
        "conjugate transpose": conjugate_transpose
    }
    var_2 = ["matrix multiplication", "compute 2d distance", "compute multidimensional distance"]
    var_multiple = ["multiply matrices", "multiplication check"]
    state = True
    print("List of available commands: ")
    for key in dic_fun.keys():
        print(key)
    try:
        while state:

            command = input("Enter your command: ").lower()
            if command == "exit":
                print("This is the end.")
                break
            array1 = input("Enter your array, separate columns by commas and rows by semicolons: ")
            array1 = [(row.split(",")) for row in array1.split(";")]
            array1 = np.array(array1, dtype=int)

            if command in var_multiple:
                array2 = input("Enter another array, separate columns by commas and rows by semicolons: ")
                array2 = [(row.split(",")) for row in array2.split(";")]
                array2 = np.array(array2, dtype=int)

                arrays = [array1, array2]

                while input("Do you want to add another array?").lower() == "yes":
                    array = input("Enter your array, separate columns by commas and rows by semicolons: ")
                    array = [(row.split(",")) for row in array.split(";")]
                    array = np.array(array, dtype=int)
                    arrays.append(array)
                print(dic_fun[command](arrays))
                continue

            if command in var_2:
                array2 = input("Enter another array, separate columns by commas and rows by semicolons: ")
                array2 = [(row.split(",")) for row in array2.split(";")]
                array2 = np.array(array2, dtype=int)
                print(dic_fun[command](array1, array2))
                continue

            print(dic_fun[command](array1))
    except KeyError or ValueError:
        print("Incorrect input of command and/or array, "
              "please take a look at the available functions and array input rules")
