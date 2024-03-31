from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    founding_year = Column(Integer)

    def __repr__(self):
        return f'<Company(name={self.name}, founding_year={self.founding_year})>'

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'<Dev(name={self.name})>'

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    dev_id = Column(Integer, ForeignKey('devs.id'))
    company_id = Column(Integer, ForeignKey('companies.id'))
    item_name = Column(String)
    value = Column(Integer)

    dev = relationship("Dev", backref="freebies")
    company = relationship("Company", backref="freebies")

    def __repr__(self):
        return f'<Freebie(dev={self.dev}, company={self.company}, item_name={self.item_name}, value={self.value})>'
