'''
Library
This eception handling scenario deals with the exceptional cases that arises in a typical library interface of a Town library.

About the library interface:
This is a typical interface provided in the library, which takes 3 inputs from the library members, equencially they are:
1. memberfee: Membership fee for the library for tyhe next financial year, which can be paid in installments.
2. installments: Number of installments choosen to pay the membership fee.
3. book: Name of the book the member looks for in the 'Harry Potter' section.

Note: All the above inputs except 'book' are Integers.

Write the function definition as follows, for the function 'Library', that takes all the above 3 inputs as its parameters:

The maximum permitted number of installments to pay the annual membership fee is '3'.

1. Raise ValueError exception if the input for the number of installments is greater than '3' and Print a Message.
The message to the user must be, "Maximum Permitted Number of Installments is 3",

The amount per installment is calculated by dividing the Membership fee by the number of installments.

2. Raise Zero DivisionError exception if the input for the number of installments is equal to 'O' and Print a Message.
The message to the user must be, "Number of Installments cannot be Zero." else Print the amount per installment as "Amount per Installment is 3000.0".

The 'Harry Potter' book section contains the following books only:
• Philosophers Stone
• Chamber of Secrets
• Prisoner of Azkaban
• Goblet of Fire
• Order of Phoenix Line
• Half Blood Prince
• Deathly Hallows 1
• Deathly Hallows 2

3. Raise NameError exception if the user is looking for a book other than the books mentioned above and Print a Message.
The message to the user must be, "No such book exists in this section" else Print "It is available in this section".

Note:
1. Raise the error exceptions in the same order as above.
2. If any of the exceptions occur, the statements following that should not be executed.

Input Format for Custom Testing
# In the first line, the value for the membership fee
# In the second line, the value for the number of installments
# In the third line, the value for the Name of the book
'''

Books = ["Philosophers Stone", "Chamber of Secrets", "Prinsoner of Azkaban", "Goblet of Fire", "Order of Phoenix", "Half Blood Prince", "Deathly Hallows 1", "Deathly Hallows 2"]
Harry_Potter = dict.fromkeys(Books, None)

def library(memberfee, installments, book):
    try:
        if installments > 3:
            raise ValueError("Maximum Permitted Number of Installments is 3")
        elif installments == 0:
            raise ZeroDivisionError("Number of Installments cannot be Zero")
        else:
            amount_per_installment = memberfee / installments
            print("Amount per Installment is", amount_per_installment)
        if book not in Harry_Potter:
            raise NameError("No such book exists in this section")
        else:
            print("It is available in this section")

    except ValueError as message:
        print(message)
    except ZeroDivisionError as message:
        print(message)
    except NameError as message:
        print(message)

def main():
    memberfee = int(input())
    installments = int(input())
    book = input()
    library(memberfee, installments, book)

if __name__ == "__main__":
    main()