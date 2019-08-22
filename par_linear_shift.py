
def par_linear_shift(original_point, point_A, point_B, scale_w_vector):
    """
    :param original_point: Original points want to move, type: tuple (x, y)
    :param point_A: Starting point of vector, type: tuple(x, y)
    :param point_B: Ending point of vector, type: tuple(x, y)
    :param scale_w_vector: Length raito with vector, type: float
    :return: New point after shift, type: tuple
    """
    normal_vector = (point_A[1] - point_B[1], point_B[0] - point_A[0])

    new_point = (int(original_point[0] + scale_w_vector * normal_vector[0]),
                 int(original_point[1] + scale_w_vector * normal_vector[1]))
    return new_point