import random

from password_generator_exceptions import LessThanEightCharactersException

class PasswordGenerator:
    lower_case_letters = "abcdefghijklmnoptqrstuvwxyz"
    uper_case_leterrs = "ABCDEFGHIJKLMNOPTQRSTUVWXYZ"
    numbers = "1234567890"
    symbols = "!#$%&()*+,-./:;<=>?@[\]^_`{|}~"

    def __init__(self, password_length: int = 8) -> None:
        if password_length < 8:
            raise LessThanEightCharactersException("Password Length to short, minimum is 8.")
        self.template = self.lower_case_letters + self.uper_case_leterrs + self.numbers + self.symbols
        self.password_length = password_length

    def generate_password(self):
        return "".join(random.sample(self.template, self.password_length))