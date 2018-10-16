from simulation import *
from person import *

class Logger(object):
    '''
    Utility class responsible for logging all interactions of note during the
    simulation.


    _____Attributes______

    file_name: the name of the file that the logger will be writing to.

    _____Methods_____

    __init__(self, file_name):

    write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
        basic_repro_num):
        - Writes the first line of a logfile, which will contain metadata on the
            parameters for the simulation.

    log_interaction(self, person1, person2, did_infect=None, person2_vacc=None, person2_sick=None):
        - Expects person1 and person2 as person objects.
        - Expects did_infect, person2_vacc, and person2_sick as Booleans, if passed.
        - Between the values passed with did_infect, person2_vacc, and person2_sick, this method
            should be able to determine exactly what happened in the interaction and create a String
            saying so.
        - The format of the log should be "{person1.ID} infects {person2.ID}", or, for other edge
            cases, "{person1.ID} didn't infect {person2.ID} because {'vaccinated' or 'already sick'}"
        - Appends the interaction to logfile.

    log_infection_survival(self, person, did_die_from_infection):
        - Expects person as Person object.
        - Expects bool for did_die_from_infection, with True denoting they died from
            their infection and False denoting they survived and became immune.
        - The format of the log should be "{person.ID} died from infection" or
            "{person.ID} survived infection."
        - Appends the results of the infection to the logfile.

    log_time_step(self, time_step_number):
        - Expects time_step_number as an Int.
        - This method should write a log telling us when one time step ends, and
            the next time step begins.  The format of this log should be:
                "Time step {time_step_number} ended, beginning {time_step_number + 1}..."
        - STRETCH CHALLENGE DETAILS:
            - If you choose to extend this method, the format of the summary statistics logged
                are up to you.  At minimum, it should contain:
                    - The number of people that were infected during this specific time step.
                    - The number of people that died on this specific time step.
                    - The total number of people infected in the population, including the newly
                        infected
                    - The total number of dead, including those that died during this time step.
    '''

    def __init__(self, file_name):
        # TODO:  Finish this initialization method.  The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):

        with open(self.file_name, 'w') as logger:
                logger.write("METADATA\n\n")
                logger.write("Population Size: {}\n".format(pop_size))
                logger.write("Percentage Vaccinated: {}\n".format(vacc_percentage))
                logger.write("Virus Name: {}\n".format(virus_name))
                logger.write("Mortality Rate: {}\n".format(mortality_rate))
                logger.write("Basic Reproduction Rate: {}".format(basic_repro_num))

    def log_interaction(self, person1, person2, did_infect=None,
                        person2_vacc=None, person2_sick=None):
        with open(self.file_name, "a") as f:
            f.write("Person Infected: {}\n Person was in contact with: {}\n Contact Infected: {}\n Contact Vaccinated: {}\n Already Infected With: {}\n".format(person1._id, person2._id, did_infect, person2_vacc, person2_sick))


    def log_infection_survival(self, person, did_die_from_infection):

        with open(self.file_name, "a") as f:
            f.write("Patient Infected: {}\n Killed By Virus: {}\n".format(person, did_die_from_infection))


    def log_time_step(self, time_step_number):

        with open(self.file_name, "a") as f:
            f.write("Time Steps: {}\n".format(time_step_number))
