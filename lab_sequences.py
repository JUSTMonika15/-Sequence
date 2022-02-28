"""CSC 161 Lab: Sequences

Lihang Liu
Lab Section CSC 161-2 TR 2:00-3:15pm
Spring 2022
"""


def main():
    print("This program reads in financial information from a file"
          "and prints it neatly to the user's screen.")

    file_name = input("Please enter the filename of the financial data: ")
    print(" ")

    file = open(file_name, "r")
    lines = file.readlines()
    
    principal_line = lines[1]
    principal = float(principal_line[10:])
    print("The initial principal is: {0}{1:.2f}".format("$", principal))

    interest_line = lines[2]
    interest = float((interest_line[9:])) * 100
    print("Annual percentage rate is: {0}{1}".format(interest, "%"))

    time_line = lines[0]
    time = time_line[5:]
    print("Length of the term (years): {0}\n".format(time))
    
    header = ("Year    Value")
    print(header)
    print("-" * (len(header) + 4))

    num = lines[3:]
    for i in range(len(num)):
        numbers = float(num[i])
        print("{0:>2}{1:>7}{2:.2f}".format(i, "$", numbers))


if __name__ == "__main__":
    main()
