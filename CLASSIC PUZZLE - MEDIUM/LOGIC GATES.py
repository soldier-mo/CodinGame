n = int(input())
m = int(input())
dic = {}

# Input signals and store them in the dictionary
for i in range(n):
    input_name, input_signal = input().split()
    dic[input_name] = input_signal.replace("_", "0").replace("-", "1")

# Define logic functions
def NOT(A):
    return ~A + 2

def AND(A, B):
    return A & B

def OR(A, B):
    return A | B

def XOR(A, B):
    return A ^ B

def NAND(A, B):
    return NOT(AND(A, B))

def NOR(A, B):
    return NOT(OR(A, B))

def NXOR(A, B):
    return NOT(XOR(A, B))

# Process and print the results
for i in range(m):
    output_name, _type, input1, input2 = input().split() 
    result = "".join(str(eval(f"{_type}(int(dic[input1][i]), int(dic[input2][i]))")) for i in range(len(dic[list(dic)[0]])))
    print(output_name, result.replace("0", "_").replace("1", "-"))
