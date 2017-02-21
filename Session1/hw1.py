import sys


def average_counter(sequence):
    """
    Function calculates the average number of occurrences for each element
    in a given sequence
    """
    length = len(sequence)
    elements = {e: 0.0 for e in sequence}
    for e in sequence:
        elements[e] += 1.0 / length
    return elements

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        sequence = file.read()
        res = average_counter(sequence)
        print(res)
