import faker
fake = faker.Faker(locale='ru_RU')

for _ in range(10):
    print(fake.name())