#
def get_p_distance(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be of the same length")
    return sum(el1 != el2 for el1, el2 in zip(list1, list2))

def get_p_distance_matrix(list1,list2,list3,list4):
    lists = list1,list2,list3,list4
    n = len(lists)
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dist = get_p_distance(lists[i], lists[j])
            matrix[i][j] = dist
            matrix[j][i] = dist
    return matrix
   
