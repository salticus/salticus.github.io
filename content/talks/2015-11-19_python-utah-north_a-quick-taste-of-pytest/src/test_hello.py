
import pytest
import hello

# test_hello.py
@pytest.mark.parametrize('who', [
            "Ladies and gentlemen",
             "Students and professionals",
             "Hackers and engineers"])
def test_greet(who):
    greeting = hello.greet(who)
    assert greeting == "{}, good evening!".format(who)

