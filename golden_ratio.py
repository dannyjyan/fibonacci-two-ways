import math

# Equation 3
def fibonacci(n):
    phi = (1 + math.sqrt(5)) / 2  
    psi = (1 - math.sqrt(5)) / 2
    return (phi**n - (psi)**(n)) / math.sqrt(5)

# Equation 4
def equation_4_value(n, p):
    phi = (1 + math.sqrt(5)) / 2  
    Fp = fibonacci(n)
    value = Fp * (phi**(n-p)), 2
    return value


def equation_4_sequence(p, length=20):
    phi = (1 + math.sqrt(5)) / 2  
    # get previous member of sequence
    Fp = fibonacci(n)
    seq = [Fp * (phi**(n-p))for n in range(length)]
    return seq


    # Equation 5: 
def equation_5_sequence(length=20):
    phi = (1 + math.sqrt(5)) / 2
    seq = [0, 1]  
    for i in range(2, length):
        next_val = seq[i - 1] * phi
        seq.append(next_val)
    return seq

def equation_5_sequence_with_p(p, length=20):
    phi = (1 + math.sqrt(5)) / 2
    seq = [fibonacci[p]] 
    for i in range(1, length):
        next_val = seq[i - 1] * phi
        seq.append(next_val)
    return seq



# Run everything
if __name__ == "__main__":
    # Ask user for p
    while True:
        try:
            p = int(input("Enter a non-negative integer p (seed index)"))
            if p < 0:
                print("Must be greater than 0")
                continue 
            break
        except ValueError:
            print("Invalid Input, please enter an integer")
    # ask user for n
    while True:
        try:
            n = int(input("Enter a non-negative integer n (value to print)"))
            if n < 0:
                print("Must be greater than 0")
                continue 
            break
        except ValueError:
            print("Invalid Input, please enter an integer")

    #p = 1
    answer4 = equation_4_value(n,p)
    print(f"Estimating n={n} term using p={p}: {answer4}")

    seq4 = [0] + equation_4_sequence(0)
    seq5 = equation_5_sequence()
    actual = [fibonacci(n) for n in range(20)]

    # 3) Print them side by side
    print(f"\nFirst 20 terms starting at F[{0}] using Eq(4) vs Eq(5):\n")
    print("i\tEq(4):\tEq(5):\tActual:")
    for i in range(20):
        print(f"{i}\t{round(seq4[i], 2)}\t{round(seq5[i], 2)}\t{round(actual[i], 2)}")

    # 35 elements
    seq5_35 = equation_5_sequence(35)
    print(f"\nFirst 30 terms starting at F[{0}] using Eq(4) vs Eq(5):\n")
    print("i\tEq(5):")
    for i in range(35):
        print(f"{i}\t{round(seq5_35[i], 2)}")
    print("F[3]/F[2]:")
    print(seq5_35[3]/seq5_35[2])
    print("F[30]/F[29]:")
    print(seq5_35[30]/seq5_35[29])
