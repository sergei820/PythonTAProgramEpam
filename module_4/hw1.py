"""
Create classes to track homeworks.

1. Homework - accepts howework text and deadline (datetime.timedelta)
Homework has a method, that tells if deadline has passed.

2. Student - can solve homework with `do_homework` method.
Raises DeadlineError with "You are late" message if deadline has passed

3. Teacher - can create homework with `create_homework`; check homework with `check_homework`.
Any teacher can create or check any homework (even if it was created by one of colleagues).

Homework are cached in dict-like structure named `homework_done`. Key is homework, values are 
solutions. Each student can only have one homework solution.

Teacher can `reset_results` - with argument it will reset results for specific homework, without - 
it clears the cache.

Homework is solved if solution has more than 5 symbols.

-------------------
Check file with tests to see how all these classes are used. You can create any additional classes 
you want.
"""
from datetime import timedelta


class Homework:
    def __init__(self, homework_text, deadline: timedelta):
        self.homework_text = homework_text
        self.deadline = deadline

    # Homework has a method, that tells if deadline has passed.
    def deadline_has_passed(self) -> bool:
        pass


class Student:
    def __init__(self):
        pass

    # Raises DeadlineError with "You are late" message if deadline has passed
    def do_homework(self, homework: Homework):
        if homework.deadline_has_passed():
            raise DeadlineError("You are late")


class Teacher:
    def __init__(self):
        pass

    # Any teacher can create or check any homework (even if it was created by one of colleagues).
    def create_homework(self, homework_task: str, time_for_task: timedelta):  # timedelta(days=2)
        return Homework(homework_task, time_for_task)

    def check_homework(self, homework: Homework):
        pass
# Homework are cached in dict-like structure named `homework_done`. Key is homework, values are
# solutions. Each student can only have one homework solution.
#
# Teacher can `reset_results` - with argument it will reset results for specific homework, without -
# it clears the cache.
#
# Homework is solved if solution has more than 5 symbols.


class DeadlineError(Exception):
    print("You are late")
