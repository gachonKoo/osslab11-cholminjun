def vector_sum(vec1, vec2):
    """
    Takes two lists (vectors) as arguments and returns a new list 
    with the corresponding elements summed up.
    (Assumes both lists are of equal length.)
    """
    # Use List Comprehension with zip to sum up elements from both lists
    result = [a + b for a, b in zip(vec1, vec2)]
    return result