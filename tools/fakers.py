from faker import Faker


class Fake:
    def __init__(self, faker: Faker):
        self.faker = faker

    def text(self) -> str:
        return self.faker.text()

    def uuid4(self) -> str:
        return self.faker.uuid4()

    def email(self) -> str:
        return self.faker.email()

    def sentence(self) -> str:
        return self.faker.sentence()

    def password(self) -> str:
        return self.faker.password()

    def last_name(self) -> str:
        return self.faker.last_name()

    def first_name(self) -> str:
        return self.faker.first_name()

    def middle_name(self) -> str:
        return self.faker.first_name()

    def estimate_time(self) -> str:
        return f"{self.integer(start=1, end=10)} weeks"

    def integer(self, start: int = 1, end: int = 100) -> int:
        return self.faker.random_int(start, end)

    def max_score(self) -> int:
        return self.integer(start=50, end=100)

    def min_score(self) -> int:
        return self.integer(start=1, end=30)


fake = Fake(faker=Faker())