import pytest


"""scope = Function (Will run setup_and _teardown for every method) Default
scope = session (run once, teardown once"""

@pytest.fixture(scope="class")                         #(autouse=True,scope="function")
def setup_and_teardown(request):
    print("Setup code")
    driver_variable = 'some driver setup'
    request.cls.driver_variable = driver_variable
    yield
    print("teardown code")
