import pytest

"""For Running tests-

python (testfilename) -rA -html html_report_filename 

For running tests in parallel-
pip install pytest-xdist
to run- pytest testfilename -n 6

"""
@pytest.mark.smoke
def test_one():
    print("Test 1")
    a=2
    b=2
    assert a==b, f"Expected equal. a={a}, b={b}"

@pytest.mark.xpass
def test_two():
    print("Test 2")
    assert False, "Condition not met"

@pytest.mark.uat
def test_three():
    print("Test 3")

@pytest.mark.usefixtures("setup_and_teardown")
@pytest.mark.uat
class TestOtherTests:
    def test_four(self):
        print("This is test 4 which is useful to import a common setup and teardown on conftest file- which can "
              "be used across multiple files - by classifying under classes")
        hehe = self.driver_variable
        print(hehe)


