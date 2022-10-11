import pytest

import Staff
import System

username = 'calyam'
password = '#yeet'
username2 = 'hdjsr7'
username3 = 'yted91'
course = 'cloud_computing'
assignment = 'assignment1'
profUser = 'goggins'
profPass = 'augurrox'
studentU = 'yted91'
studentP = 'imoutofpasswordnames'


# Tests if the program can handle a wrong username
def test_login(grading_system):
    username = 'thtrhg'
    password = 'fhjhjdhjdfh'
    grading_system.login(username, password)


# Tests if the program can handle an incorrect password
def test_check_password(grading_system):
    test = grading_system.check_password(username, password)
    test2 = grading_system.check_password(username, '#yeet')
    test3 = grading_system.check_password(username, '#YEET')
    if test == test3 or test2 == test3:
        assert False
    if test != test2:
        assert False


# This tests to see if the system correctly updates a student's grade
def test_change_grade(grading_system):
    grading_system.login(profUser, profPass)
    grading_system.usr.change_grade(studentU, course, 'assignment1', 50)
    grades = grading_system.usr.check_grades(studentU, course)
    check_grade = 0
    for grade in grades:
        if grade[0] == "assignment1":
            check_grade = grade[1]
    if check_grade == 50:
        assert True
    else:
        assert False


# This function allows the staff to create a new assignment.
# Verify that an assignment is created with the correct due date in the correct course in the database.
def test_create_assignment(grading_system):
    grading_system.login(profUser, profPass)
    grading_system.usr.create_assignment("augur_is_awesome", "10/10/22", "software_engineering")
    grading_system.login(studentU, studentP)
    assignments = grading_system.usr.view_assignments("software_engineering")
    temp_assignment = "0"
    for assignment in assignments:
        if assignment[0] == "augur_is_awesome":
            temp_assignment = assignment[0]
    if temp_assignment != "0":
        assert True
    else:
        assert False


def test_add_student(grading_system):
    grading_system.login(profUser, profPass)
    try:
        grading_system.usr.add_student(studentU, "databases")
        grading_system.login(studentU, studentP)
        assert grading_system.usr.check_grades("databases")[1] == "N/A"
    except:
        assert False


def test_drop_student(grading_system):
    grading_system.login(profUser, profPass)
    try:
        grading_system.usr.drop_student("hdjsr7", "databases")
        try:
            grading_system.login("hdjsr7", "pass1234")
            grading_system.check_grades("databases")
        except:
            assert True
    except:
        assert False


def test_submit_assignment(grading_system):
    grading_system.login(studentU, studentP)
    grading_system.usr.submit_assignment("databases", "assignment1", "UGHGHGHHHGHSD", "1/25/56")
    grading_system.login(profUser, profPass)



def test_check_on_time():
    assert False


def test_check_grades():
    assert False


def test_view_assignments():
    assert False


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
