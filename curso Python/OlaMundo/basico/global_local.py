 # GLOBAL
 variavel_global = 5


def func1():
   # LOCAL
    variavel = 1
    print("func1:", variavel)
    print("func1: ", variavel_global)


def func2():
    # LOCAL
     variavel = 2
    print("func2:", variavel)
    print("func2: ", variavel_global)


def main():
    # LOCAL
     variavel = 3
    print("Main:", variavel)
    print("Main: ", variavel_global)

    func1()
    func2()


if __name__ == "__main__":
      main()