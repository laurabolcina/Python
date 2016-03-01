from lotto_better import lotto

def testing_lotto():
    generated_list = lotto(7)
    assert len(generated_list) == len(set(generated_list))
    return "testing_lotto() passed successfully"

print testing_lotto()