class EvenOnly(list):


    def append(self, integer):


        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        super().append(integer)

def no_return():
    print("I am about to raise an exception")
    raise Exception("This is always raised")
    print("This line will never execute")
    return "I won't be returned"

def call_exceptor():
    print("call_exceptor starts here...")
    no_return()
    print("an exception was raised...")
    print("...so these lines don't run")

try:
    no_return()
except:
    print("I caught an exception")
    print("executed after the exception")

def funny_division(anumber):
    try:
        return 100 / anumber
    except ZeroDivisionError:
        return "Silly wabbit, you can't divide by zero!"

def funny_division2(anumber):
    try:
        if anumber == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / anumber
    except (ZeroDivisionError, TypeError):
        return "Enter a number other than zero"
for val in (0, "hello", 50.0, 13):
    print("Testing {}:".format(val), end=" ")
    print(funny_division2(val))


def funny_division3(anumber):
    try:
            if anumber == 13:
                raise ValueError("13 is an unlucky number")
            return 100 / anumber
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError:
        print("No, No, not 13!")
        raise
try:
    raise ValueError("This is an argument")
except ValueError as e:
    print("The exception arguments were", e.args)

# -----------------------------------------------------

import random
some_exceptions = [ValueError, TypeError, IndexError, None]
try:
    choice = random.choice(some_exceptions)
    print("raising {}".format(choice))
    if choice:
        raise choice("An error")
    except ValueError:
        print("Caught a ValueError")
    except TypeError:
        print("Caught a TypeError")
    except Exception as e:
        print("Caught some other error: %s" %( e.__class__.__name__))
else:
    print("This code called if there is no exception")
finally:
    print("This cleanup code is always called")

# ---------------------------------------
# class InvalidWithdrawal(Exception):
#     pass
# raise InvalidWithdrawal("You don't have $50 in your account")


class InvalidWithdrawal(Exception):
    def __init__(self, balance, amount):
        super().__init__("account doesn't have ${}".format(
        amount))
        self.amount = amount
        self.balance = balance
    def overage(self):
        return self.amount - self.balance
#raise InvalidWithdrawal(25, 50)


try:
    raise InvalidWithdrawal(25, 50)
except InvalidWithdrawal as e:
    print("I'm sorry, but your withdrawal is "
    "more than your balance by "
    "${}".format(e.overage()))


def divide_with_exception(number, divisor):
    try:
        print("{} / {} = {}".format(
        number, divisor, number / divisor * 1.0))
    except ZeroDivisionError:
        print("You can't divide by zero")
