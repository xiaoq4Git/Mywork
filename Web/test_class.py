#coding=utf-8

class TestClass:

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert x == "hi"

if __name__ == '__main__':
    pass