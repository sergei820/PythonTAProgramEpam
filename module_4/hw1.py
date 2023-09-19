"""
Create classes to track homeworks.

1. Homework - accepts howework text and deadline (datetime.timedelta)   -   Done
Homework has a method, that tells if deadline has passed.

2. Student - can solve homework with `do_homework` method.              -   Done
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
import datetime


class Homework:
    def __init__(self, homework_text, deadline: datetime.timedelta.days):
        self.homework_text = homework_text
        self.deadline = deadline

    def deadline_has_passed(self) -> bool:
        if self.deadline < 0:
            return True
        else:
            return False


class Student:
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework: Homework, solution_text: str):
        if homework.deadline_has_passed():
            raise DeadlineError("You are late")
        result = Result(homework, solution_text)
        result.author = self
        return result


class Result:
    def __init__(self, homework: Homework, solution: str):
        self.homework = homework
        self.solution = solution


class Teacher:
    homework_done = {}

    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    def create_homework(homework_task: str, time_for_task):
        return Homework(homework_task, time_for_task)

    def check_homework(self, result: Result):
        if len(result.solution) > 5:
            if Teacher.homework_done.get(result.homework) is None:
                Teacher.homework_done[result.homework] = set()
                Teacher.homework_done[result.homework].add(result)
            else:
                Teacher.homework_done[result.homework].add(result)
            return True
        else:
            Teacher.homework_done[result.homework] = set()
            return False

    @staticmethod
    def reset_results():
        Teacher.homework_done.clear()


class DeadlineError(Exception):
    def __init__(self, message="You are late"):
        self.message = message
