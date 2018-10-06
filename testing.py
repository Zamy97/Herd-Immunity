
pop_size = "100"
vacc_percentage = "15"

def write_metadata(pop_size, vacc_percentage):

    with open("NEWFILE", 'w') as logger:
            logger.write("METADATA\n\n")
            logger.write("Population Size: {}\n".format(pop_size))
            logger.write("Percentage Vaccinated: {}\n".format (vacc_percentage))
            logger.write(pop_size + '\t' + vacc_percentage)
            logger.write(pop_size, vacc_percentage, end="\t")



write_metadata(pop_size, vacc_percentage)
