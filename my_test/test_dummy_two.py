

def test_given_string():
    name = "murali"
    assert name in "muralikrishnan"

def test_given_greeting():
    greet = "hi"
    assert greet in "good morning", "Greetings differ -- code word failed"

def test_sum_of_two_nums():
    assert 3 + 4 == 10, "Addtion is wrong.p"