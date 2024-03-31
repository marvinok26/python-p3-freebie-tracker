from models import Base, Company, Dev, Freebie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add sample data
company1 = Company(name="Company A", founding_year=2000)
company2 = Company(name="Company B", founding_year=2010)
dev1 = Dev(name="Developer 1")
dev2 = Dev(name="Developer 2")

freebie1 = Freebie(dev=dev1, company=company1, item_name="T-shirt", value=10)
freebie2 = Freebie(dev=dev2, company=company2, item_name="Stickers", value=5)

session.add_all([company1, company2, dev1, dev2, freebie1, freebie2])
session.commit()

print("Sample data added successfully.")
