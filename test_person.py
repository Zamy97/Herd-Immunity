import pytest
from person import Person
# from virus import Virus
# from simulation import Simulation

def test_can_create_person():
	person = Person(0, True, None)

	assert person.is_alive == True
	assert person._id == 0
	assert person.infected == None
