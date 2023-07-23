"""
All pytest files should begin with test_ or end with _test

test methods should always start with test keyword

Any code should be wrapped inside a functionls

In pytest, every method is treated as one test case

We can't have same pytest method names, incase if we have,

second method result overrides the previous methods execution
"""


def test_google_login():
    print("My first google test")

def test_firefox_login():
    print("My first firefox test")