"""
check_data function takes two parameters - path to a file and a list of functions (validators).
You should:
- read data from file data.txt
- validate each line according to rules. Each rule is a function, that performs some specific check
- write a report to txt file and return absolute path to that file. For each line you should report 
it if it doesn't conform with at least one rule, plus add a reason - the name of a validator that
doesn't pass (if there are more than one failed rules, get the name of the first one that fails)

Valid line should have 5 elements in this order:
email, amount, currency, account, date

You should also implement at least two rules:
- validate_line should check if a line has 5 elements
- validate_date should check if a date is valid. In our case valid date will be anything that follows
the pattern DDDD-DD-DD (four digits - two digits - two digits). Date always exists in a line, even 
if this line is corrupted in some other way.
Feel free to add more rules!

For example, input lines:
foo@example.com 729.83 EUR accountName 2021-01:0
bar@example.com 729.83 accountName 2021-01-02
baz@example.com 729.83 USD accountName 2021-01-02

check_data(filepath, [validate_date, validate_line])

output lines:
foo@example.com 729.83 EUR accountName 2021-01:0 validate_date
bar@example.com 729.83 accountName 2021-01-02 validate_line
"""
import os
from typing import Callable, Iterable
import re


def validate_line(line: str) -> bool:
    return len(line.split()) == 5


def validate_date(date: str) -> bool:
    date_pattern = "[0-9]{4}-[0-9]{2}-[0-9]{2}$"
    return bool(re.search(date_pattern, date))


def validate_sequence_in_line(line: str) -> bool:
    email_pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}"
    amount_pattern = "[0-9]+(\\.[0-9]{2})?"
    currency_pattern = "[A-Z]{3}"
    account_pattern = "[a-zA-Z0-9]+"
    date_pattern = "[0-9]{4}-[0-9]{2}-[0-9]{2}"
    patterns = [email_pattern, amount_pattern, currency_pattern, account_pattern, date_pattern]
    result_pattern = " ".join(patterns)
    return bool(re.match(result_pattern, line))


def check_data(filepath: str, validators: Iterable[Callable]) -> str:
    validated_data = []
    report_path = os.getcwd() + "\\report.txt"
    print(report_path)
    with open(filepath, "r") as filehandle, open(report_path, "w") as report:
        data_from_file = filehandle.readlines()

        for line_to_validate in data_from_file:
            for validator in validators:
                if not validator(line_to_validate):
                    validated_data.append(line_to_validate.replace("\n", " " + validator.__name__ + "\n"))
                    # can't write to the report file right here:
                    # report.write(line_to_validate.replace("\n", " " + validator.__name__ + "\n"))
                    # because it causes errors like:
                    # FAILED test_hw1.py::test_check_data_real_file -
                    # UnboundLocalError: cannot access local variable 'i' where it is not associated with a value
                    break

    with open(report_path, "w") as report:
        for line in validated_data:
            report.write(line)
    return report_path


# check_data("data.txt", [validate_date, validate_line])
# check_data("data.txt", [validate_line])
# os.remove(os.getcwd() + "\\report.txt")
# os.remove("valid.txt")
