import pytest

from homework6.tasks.task2 import DeadlineError, HomeworkResult, Student, Teacher


def test_class_Teacher_is_correctly_inherited_from_class_Student():
    student = Student("Valya", "Petrova")
    teacher = Teacher("Albert", "")

    assert student.first_name != teacher.first_name


def test_do_homework_function_returns_HomeworkResult_object():
    student = Student("Valya", "Petrova")
    teacher = Teacher("Albert", "")
    hw = teacher.create_homework("Do it", 3)
    result = student.do_homework(hw, "The solution of the student")

    assert isinstance(result, HomeworkResult)


def test_do_homework_function_raises_Exception():
    student = Student("Valya", "Petrova")
    teacher = Teacher("Albert", "")
    hw = teacher.create_homework("Do it", 0)
    with pytest.raises(DeadlineError) as info:
        student.do_homework(hw, "The solution of the student")

    assert "You are late." in str(info.value)


def test_check_homework_function_returns_False():
    student = Student("Valya", "Petrova")
    teacher = Teacher("Albert", "")
    hw = teacher.create_homework("Do it", 3)
    hw_result = student.do_homework(hw, "solut")

    assert teacher.check_homework(hw_result) is False


def test_check_homework_function_returns_True():
    student = Student("Valya", "Petrova")
    teacher = Teacher("Albert", "")
    hw = teacher.create_homework("Do it", 3)
    hw_result = student.do_homework(hw, "correct_solution")

    assert teacher.check_homework(hw_result) is True


def test_check_homework_function_adds_HomeworkResult_object_to_homework_done():
    student = Student("Valya", "Petrova")
    teacher = Teacher("Albert", "")
    hw = teacher.create_homework("Do it", 3)
    hw_result = student.do_homework(hw, "correct_solution")
    teacher.check_homework(hw_result)

    assert isinstance(Teacher.homework_done[hw]["correct_solution"], HomeworkResult)


def test_reset_results_function_deletes_Homework_object_in_homework_done():
    Teacher.reset_results()
    student = Student("Valya", "Petrova")
    teacher = Teacher("Albert", "")
    hw = teacher.create_homework("Do it", 3)
    hw_result = student.do_homework(hw, "correct_solution")
    teacher.check_homework(hw_result)
    Teacher.reset_results(hw)

    assert not Teacher.homework_done


def test_reset_results_function_completely_frees_homework_done():
    student = Student("Valya", "Petrova")
    teacher = Teacher("Albert", "")
    hw = teacher.create_homework("Do it", 3)
    hw2 = teacher.create_homework("Just do it", 5)
    hw_result = student.do_homework(hw, "correct_solution")
    hw_result2 = student.do_homework(hw2, "correct_solution2")
    teacher.check_homework(hw_result)
    teacher.check_homework(hw_result2)
    Teacher.reset_results()

    assert not Teacher.homework_done


# def test_class_Teacher_is_correctly_inherited_from_class_Student():
#     student = task2.Student("Valya", "Petrova")
#     teacher = task2.Teacher("Albert", "")
#
#     assert student.first_name != teacher.first_name
#
#
# def test_do_homework_function_returns_HomeworkResult_object():
#     student = task2.Student("Valya", "Petrova")
#     teacher = task2.Teacher("Albert", "")
#     hw = teacher.create_homework("Do it", 3)
#     result = student.do_homework(hw, "The solution of the student")
#
#     assert isinstance(result, task2.HomeworkResult)
#
#
# def test_do_homework_function_raises_Exception():
#     student = task2.Student("Valya", "Petrova")
#     teacher = task2.Teacher("Albert", "")
#     hw = teacher.create_homework("Do it", 0)
#     with pytest.raises(task2.DeadlineError) as info:
#         student.do_homework(hw, "The solution of the student")
#
#     assert "You are late." in str(info.value)
#
#
# def test_check_homework_function_returns_False():
#     student = task2.Student("Valya", "Petrova")
#     teacher = task2.Teacher("Albert", "")
#     hw = teacher.create_homework("Do it", 3)
#     hw_result = student.do_homework(hw, "solut")
#
#     assert teacher.check_homework(hw_result) is False
#
#
# def test_check_homework_function_returns_True():
#     student = task2.Student("Valya", "Petrova")
#     teacher = task2.Teacher("Albert", "")
#     hw = teacher.create_homework("Do it", 3)
#     hw_result = student.do_homework(hw, "correct_solution")
#
#     assert teacher.check_homework(hw_result) is True
#
#
# def test_check_homework_function_adds_HomeworkResult_object_to_homework_done():
#     student = task2.Student("Valya", "Petrova")
#     teacher = task2.Teacher("Albert", "")
#     hw = teacher.create_homework("Do it", 3)
#     hw_result = student.do_homework(hw, "correct_solution")
#     teacher.check_homework(hw_result)
#
#     assert isinstance(
#         task2.Teacher.homework_done[hw]["correct_solution"], task2.HomeworkResult
#     )
#
#
# def test_reset_results_function_deletes_Homework_object_in_homework_done():
#     task2.Teacher.reset_results()
#     student = task2.Student("Valya", "Petrova")
#     teacher = task2.Teacher("Albert", "")
#     hw = teacher.create_homework("Do it", 3)
#     hw_result = student.do_homework(hw, "correct_solution")
#     teacher.check_homework(hw_result)
#     task2.Teacher.reset_results(hw)
#
#     assert not task2.Teacher.homework_done
#
#
# def test_reset_results_function_completely_frees_homework_done():
#     student = task2.Student("Valya", "Petrova")
#     teacher = task2.Teacher("Albert", "")
#     hw = teacher.create_homework("Do it", 3)
#     hw2 = teacher.create_homework("Just do it", 5)
#     hw_result = student.do_homework(hw, "correct_solution")
#     hw_result2 = student.do_homework(hw2, "correct_solution2")
#     teacher.check_homework(hw_result)
#     teacher.check_homework(hw_result2)
#     task2.Teacher.reset_results()
#
#     assert not task2.Teacher.homework_done
