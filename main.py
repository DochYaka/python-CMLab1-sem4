import newtonMethod
import simpleIterationMethod
import secantMethod
import graphCreate


def main():
    graphCreate.Graph()

    intervals = [(-4, -3), (-2, -1), (0, 1), (4, 5)]

    for a, b in intervals:
        newtonMethod.newton_method(a, b)

    # Простые итерации (два старта: левый и правый конец)
    for a, b in intervals:
        simpleIterationMethod.simple_iteration_method(a, b, x0=a)
        simpleIterationMethod.simple_iteration_method(a, b, x0=b)


if __name__ == "__main__":
    main()
