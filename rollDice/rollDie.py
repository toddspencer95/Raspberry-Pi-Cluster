from csv import writer
import random
import socket
from datetime import datetime
import fcntl

# Get Time
time = str(datetime.now())

# Get Node name
name = socket.gethostname()

# Roll the die
result = random.randint(1, 6)

# Populate Row Contents
row = [time, name, result]

# Write the result to a file
# Open our existing CSV file in append mode
# Create a file object for this file
try:
    with open('results.csv', 'a') as f_object:
   
	# Acquire an exclusive lock on the file
    	fcntl.flock(f_object.fileno(), fcntl.LOCK_EX)

	# Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
    
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(row)

	# Release the lock on the file
    	fcntl.flock(f_object.fileno(), fcntl.LOCK_UN)
    
        # Close the file object
        f_object.close()

except Exception as e:
    f = open('log.txt', 'w')
    f.write('An exceptional thing happed - %s' % e)
    f.close()
