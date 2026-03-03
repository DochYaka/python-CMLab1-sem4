import newtonMethod
import simpleIterationMethod
import secantMethod
import graphCreate


def main():
    # graphCreate.Graph()

    intervals = [(-4, -3), (-2, -1), (0, 1), (4, 5)]

    print()

    for a, b in intervals:
        newtonMethod.newton_method(a, b)
        print()

    print("=" * 40)
    print("=" * 40)
    print("=" * 40)
    print()

    for a, b in intervals:
        simpleIterationMethod.simple_iteration_method(a, b, x0=a)
        simpleIterationMethod.simple_iteration_method(a, b, x0=b)

    for a, b in intervals:
        secantMethod.secant_method(a, b)

if __name__ == "__main__":
    main()
