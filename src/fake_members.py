from faker import Faker
fake = Faker()

print('"name","type","dc:title","member:identifier","address:Address","address:City","address:Name","address:State","address:ZipCode"')

for row in range(1000):
    name = fake.name()
    identifier = fake.bban()
    address = fake.street_address()
    city = fake.city()
    state = "NC"
    zipCode = fake.zipcode_in_state(state_abbr=state)
    title = name + " (" + identifier + ")"
    key = name.lower().replace(" ", "-") + "-" + identifier
    print('"%s","Member","%s","%s","%s","%s","%s","NC","%s"' 
        % (key, title, identifier, address, city, name, zipCode))
