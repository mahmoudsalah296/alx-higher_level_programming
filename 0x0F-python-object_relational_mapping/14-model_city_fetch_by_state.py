#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State, City).filter(State.id == City.state_id).all()
    for state, city in result:
        print(f'{state.name}: ({city.id}) {city.name}')
    session.close()
