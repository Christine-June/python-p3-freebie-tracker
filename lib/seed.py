#!/usr/bin/env python3

from models import Dev, Company, Freebie, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///freebies.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()

dev1 = Dev(name="Esther")
dev2 = Dev(name="Ricky")
company1 = Company(name="Safaricom", founding_year=1995)
company2 = Company(name="Google", founding_year=1998)

freebie1 = Freebie(item_name="T-shirt", value=10, dev=dev1, company=company1)
freebie2 = Freebie(item_name="Mug", value=15, dev=dev2, company=company1)

session.add_all([dev1, dev2, company1, company2, freebie1, freebie2])
session.commit()

print('Database seeded successfully!')
session.close()