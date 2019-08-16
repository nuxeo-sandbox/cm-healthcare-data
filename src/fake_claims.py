from faker import Faker
import csv
import clg
import datetime
import random
import yaml
import yamlordereddictloader

fake = Faker()

cmd = clg.CommandLine(yaml.load(open('src/claims.yaml'), Loader=yamlordereddictloader.Loader))
args = cmd.parse()

lifecycles = ["New", "Assigned", "Hold",
              "Violation", "Pending", "Resolved", "Audit"]
csrs = ["csr1", "csr2", "csr3", "csr4", "csr5"]
priorities = ["Low", "Routine", "High"]
origins = ["Member", "Provider"]
claimTypes = ["Provider", "Clinic", "Hospital", "ER", "Ambulatory"]
queues = ["claim-queue-1", "claim-queue-2",
          "claim-queue-3", "claim-queue-4", "claim-queue-5"]

header = '"name","type","dc:title","ecm:currentLifeCycleState","dc:source"'
header += ',"claim:priority","claim:type","claim:origin","claim:queue","claim:totalCharge"'
header += ',"claim:assignedUser","claim:sccf","claim:messageID","claim:submitter"'
header += ',"dc:created","claim:serviceDate","claim:received","claim:holdDate"'
header += ',"dc:modified","claim:providerID","claim:memberID"'
header += ',"dc:creator","dc:contributors","dc:lastContributor"'

template = '"%s","Claim","%s","%s","Upload"'
template += ',"%s","%s","%s","%s","%s"'
template += ',"%s","%s","%s","%s"'
template += ',"%s","%s","%s","%s"'
template += ',"%s","%s","%s"'
template += ',"Administrator","%s","%s"'

# Load providers and members DB
with open(args.providers) as csvfile:
    providers = list(csv.DictReader(csvfile))
with open(args.members) as csvfile:
    members = list(csv.DictReader(csvfile))

print(header)
for row in range(args.count):
    lc = random.choice(lifecycles)
    pri = random.choice(priorities)
    origin = random.choice(origins)
    ctype = random.choice(claimTypes)
    participant = random.choice(csrs)
    q = random.choice(queues)
    contributor = "Administrator"

    assigned = ""
    if lc != "New":
        assigned = random.choice(csrs)
        contributor += "|" + assigned
    
    if lc in [ "Hold", "Violation", "Audit" ]:
        contributor += "|" + participant

    identifier = fake.ean13()
    sccf = fake.bban()
    msgId = fake.ean8()

    charge = round(random.uniform(0.0, 1000000.0), 2)

    provData = random.choice(providers)
    membData = random.choice(members)
    if origin == "Member":
        submitter = membData['dc:title']
    else:
        submitter = provData['dc:title']
    provider = provData['name']
    member = membData['name']

    identifier = fake.bban()

    originDate = fake.date_time_between(start_date="-5y", end_date="now", tzinfo=None).replace(microsecond=0)
    serviceDate = originDate.isoformat()
    originDate += datetime.timedelta(days=1)
    received = originDate.isoformat()
    originDate += datetime.timedelta(days=1)
    created = originDate.isoformat()
    hold = ""
    if lc == "Hold":
        originDate += datetime.timedelta(days=5)
        hold = originDate.isoformat()

    originDate += datetime.timedelta(days=3)
    modified = originDate.isoformat()

    print(template % (identifier, identifier, lc,
                      pri, ctype, origin, q, charge, assigned, sccf, msgId,
                      submitter, created, serviceDate, received, hold, modified,
                      provider, member, contributor, assigned))
