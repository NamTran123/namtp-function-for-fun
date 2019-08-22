
def linear_stride(A, p1, p2, d1):
    '''
    Translating a point in a vector .
    A  = point 
    p1 , p2 is tow point of vector . 
    d1  is the distance ratio you want to translat
    '''
    u1 = (p2[0] - p1[0], p2[1] - p1[1])
    A = (int(A[0] + d1 * u1[0]), int(A[1] + d1 * u1[1]))
    return A


def linear_shift(original_point, point_A, point_B, scale_w_vector):
    """
    :param original_point: Original points want to move, type: tuple (x, y)
    :param point_A: Starting point of vector, type: tuple(x, y)
    :param point_B: Ending point of vector, type: tuple(x, y)
    :param scale_w_vector: Length raito with vector, type: float
    :return: New point after shift, type: tuple
    """  
    direction_vector = (point_A[0] - point_A[0], point_B[1] - point_A[1])

    new_point = (int(original_point[0] + scale_w_vector * direction_vector[0]),
                 int(original_point[1] + scale_w_vector * direction_vector[1]))
    return new_point