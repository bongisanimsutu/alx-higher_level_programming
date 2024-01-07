#!/usr/bin/python3


def matrix_mul(m_a, m_b):

    # list type
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')

    # list of lists
    for row in m_a:
        if type(row) is not list:
            raise TypeError('m_a must be a list of lists')
    for row in m_b:
        if type(row) is not list:
            raise TypeError('m_b must be a list of lists')

    # no empty lists
    if len(m_a) is 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) is 0:
        raise ValueError("m_b can't be empty")

    # no empty lists inside lists
    for row in m_a:
        if len(row) is 0:
            raise ValueError("m_a can't be empty")
    for row in m_b:
        if len(row) is 0:
            raise ValueError("m_b can't be empty")

    # matricies only contain ints or floats
    for row in m_a:
        for value in row:
            if type(value) is not int and type(value) is not float:
                raise TypeError('m_a should contain only integers or floats')
    for row in m_b:
        for value in row:
            if type(value) is not int and type(value) is not float:
                raise TypeError('m_b should contain only integers or floats')

    # matricies are rectangular
    row_len = len(m_a[0])
    for row in m_a:
        if len(row) is not row_len:
            raise TypeError('each row of m_a must be of the same size')
    row_len = len(m_b[0])
    for row in m_b:
        if len(row) is not row_len:
            raise TypeError('each row of m_b must be of the same size')

    # matrix multiplication failure - width of m_a in columns is not equal to
    # height of m_b in rows
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []
    for a_row in range(len(m_a)):
        new_row = []
        # m_a width must equal m_b height
        for b_col in range(len(m_b[0])):
            sum = 0
            for a_col in range(len(m_a[0])):
                prod = m_a[a_row][a_col] * m_b[a_col][b_col]
                sum += prod
            new_row.append(sum)
        new_matrix.append(new_row)
    return new_matrix
