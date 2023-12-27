from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace 'your_username', 'your_password', 'your_database', and 'your_host' with your MySQL credentials
DATABASE_URI = "mysql+mysqlconnector://franz:fcdm110503@127.0.0.1/mydb"

# Creating an SQLAlchemy engine
engine = create_engine(DATABASE_URI, echo=True)

# Creating a base class for declarative class definitions
Base = declarative_base()

# Define your data model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

# Create the table
Base.metadata.create_all(engine)

# Creating a Session
Session = sessionmaker(bind=engine)
session = Session()

# Example: Adding data to the database
new_user = User(name='John Doe', age=25)
session.add(new_user)
session.commit()

# Example: Querying the database
query_result = session.query(User).filter_by(name='John Doe').first()
print(f"User ID: {query_result.id}, Name: {query_result.name}, Age: {query_result.age}")

# Closing the session
session.close()
