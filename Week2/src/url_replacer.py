"""url_replacer: is a python file that is responsible for containing functionality to replace a 
given string's spaces with the character sequence '%20'. 

Sourced from Cracking the Coding Interview Chapter 1 Question 3."""


def replacer(input: str):
    """replacer() is a function declaration that is intended for the use for this week's challenge.
    In this functions students will be expected to implement their solution to the problem
    without having to need to modifying existing test cases.

    @param input (str): input string that is responsible for being read by
    STDIN.
    @return str: final string after modification.
    """
    return


def main():
    while True:
        entered_in = input("Enter space delimitated string: ")
        output = replacer(entered_in)
        print("Before modification: " + entered_in)
        print("After modification: " + output)
        if input("Enter q to exit :") == "q":
            break


if __name__ == "__main__":
    main()
