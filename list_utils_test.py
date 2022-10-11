from list_utils import * 
def test_first_elements():
    original = [[0,7,3],[4,0,1]]
    assert first_elements(original) == [0,4]

original = [[0,7,3],[4,0,1]]
transposed = [[0,2],[7,0],[3,1]]
print(transpose(original))

original = [[0,2],[7,0],[3,1]]
print(transpose(original))
