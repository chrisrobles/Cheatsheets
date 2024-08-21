def create_adder(x):
    def adder(y):
        print(x)
        print(y)
    return adder
add_10 = create_adder(10)
add_10(3)