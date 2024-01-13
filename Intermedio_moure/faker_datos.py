from faker import Factory, Faker

fake = Factory.create()
fake = Faker()

fake.name()
# Genera nombres

fake.address()
# Genera teléfonos

fake.text()
    # Genera texto (se puede configurar según sea necesario)