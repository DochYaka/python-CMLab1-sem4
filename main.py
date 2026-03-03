import newtonMethod
import simpleIterationMethod
import secantMethod
import graphCreate


def main():
    graphCreate.Graph()

    intervals = [(-4, -3), (-2, -1), (0, 1), (4, 5)]

    print()

    print("Метод Ньютона\n")
    for a, b in intervals:
        newtonMethod.newton_method(a, b)
        print()

    print()

    print("Метод простых итераций\n")
    for a, b in intervals:
        simpleIterationMethod.simple_iteration_method(a, b)
        print()

    print()

    print("Метод секущих\n") 
    for a, b in intervals:
        secantMethod.secant_method(a, b)
        print()

if __name__ == "__main__":
    main()
