from faker import Faker

fake = Faker('de_DE')
print(fake.name())
print(fake.address())
print(fake.email())


data = {
    "name": fake.name(),
    "email": fake.email(),
    "age": fake.random_int(min=10, max=100)
}

print(data)