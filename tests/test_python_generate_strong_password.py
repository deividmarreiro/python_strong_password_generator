import pytest

from python_generate_strong_password.generate_strong_password import PasswordGenerator
from python_generate_strong_password.password_generator_exceptions import LessThanEightCharactersException

def test_password_generator_default():
    password_generator = PasswordGenerator()
    assert password_generator.generate_password()

def test_password_generator_ten_password_length():
    password_generator = PasswordGenerator(password_length=10)
    assert password_generator.generate_password()

# def test_password_generator_raises_exception_on_lass_than_eight_characters():
#     with pytest.raises(LessThanEightCharactersException):
#         password_generator = PasswordGenerator(password_length=7)
