from lotto_better import lotto

def testing_lotto():
    """ Checks if generated list and generated list with no duplicates are the same length. If they are, the function passes successfully. """
    generated_list = lotto(7)
    assert len(generated_list) == len(set(generated_list))   # set() creates an unordered list with no duplicate elements
    return "testing_lotto() passed successfully"

print testing_lotto()