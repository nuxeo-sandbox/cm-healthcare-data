from faker import Faker
fake = Faker()

print('"name","type","dc:title","provider:identifier","address:Address","address:City","address:Name","address:State","address:ZipCode","ecm:currentLifeCycleState"')

for row in range(1000):
    name = fake.company()
    identifier = fake.bban()
    address = fake.street_address()
    city = fake.city()
    state = "NC"
    zipCode = fake.zipcode_in_state(state_abbr=state)
    title = name + " (" + identifier + ")"
    key = name.lower().replace(" ", "-").replace(",","") + "-" + identifier
    print('"%s","Provider","%s","%s","%s","%s","%s","NC","%s","approved"'
          % (key, title, identifier, address, city, name, zipCode))
