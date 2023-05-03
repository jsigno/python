sum = lambda a, b: a + b
assert sum(1,4) == 5, "sum(1,4) is not returning 5 like it should"

# ^ changing (a-b) will causing an error which will give an AssertionError

def test_add():
    assert sum(-20,20) == 0
    assert sum(30,20) == 50
    assert sum(400, 322) == 722
    print ("all adding correctly")
test_add()

