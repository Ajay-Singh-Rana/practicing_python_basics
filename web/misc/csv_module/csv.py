# h3avren
# k@mlesh

# The csv Module

# The ```csv``` module is used to parse and write the ```csv``` (```comman seperated values```) files. It provides various functions to read and write the csv files,out of which we will be using the ```DictWriter()``` and ```writer()```  functions to write the csv files and to read the csv files we will be using the ```DictReader()``` and the ```reader()``` functions.
# 
# So, to start we will be importing the ```csv`` module.

# importing the csv module
import csv


# printing all the functions and attributes of the csv module
print(dir(csv))

# We will be using the writer function first. So, to know how it works let us print the ```help()``` for that function.

print(help(csv.writer))

# Now that we know we need to pass a file object to the ```writer()``` function and after that we can use ```writerow()``` method to write a row to the csv file,therefore, we will be opening a file first and then we will write the first 100 numbers and their squares to that file.

with open('squares.csv','w') as file:   # opening a csv file with the context manager
    writer = csv.writer(file)   # creating a writer object
    writer.writerow(['Number','Squares'])   # writing the headers as the first row of the csv file 
    for i in range(1,101,1):
        writer.writerow([i,i**2])   # writing the numbers and squares to the file
        # writer.writerows([list of data to be written]) # is used to write multiple rows of data to the csv 

# Now, as we have written a csv file,let's confirm its success by reading the same file with the ```reader()``` function. So, again before jumping to use the reader function let's print its documentation with the ```help()``` function.  

print(help(csv.reader))

# Now that we know the reader returns an iterator to loop over. Let's read the csv file we just created.

with open('squares.csv','r',newline='') as file:    # opening a file in the read mode
    reader = csv.reader(file)
    header = next(reader)   # reading the headers of the file
    data = [line for line in reader]    # extracting the remaining data by iterating over it

print(header)  # printing the headers
print(data[0]) # printing the first element of the data

# Everything that we get as output after reading the ```csv``` file is an ```string``` type. We can convert this data to the required format using the inbuilt functions like ```int()```, ```str()``` and ```float()```.
# 
# Next, we'll be using the ```DictWriter()``` function so let's print ```help()``` on the same.

print(help(csv.DictWriter))

# Writing cubes to a file using DictWriter().

with open('cubes.csv','w') as file:     
    fieldnames = ['Numbers','Cubes']    
    # fieldnames is an argument that contains the header for the csv file and is passed to the DictWriter method when creating a writer object
    
    writer = csv.DictWriter(file,fieldnames=fieldnames) # creating a writer object with the DictWriter function takes a file object and fieldnames argument
    writer.writeheader()    # the writeheader() function is used to write the fieldnames as the Header to the csv file

    for i in range(1,101,1):
        writer.writerow({'Numbers':i,'Cubes':i**3})    # the writerow function for a DictWriter object takes a dictionary as an argument
    # writer.writerows([dicts]) # this function is used to write multiple rows at once

# Now we will be using the ```DictReader()``` to read the file. Let's print `help()` on the same.

print(help(csv.DictReader))


with open('cubes.csv','r') as file: 
    reader = csv.DictReader(file)   # creating the reader object with the DictReader() function 
    print(reader.fieldnames)    # to access the headers of the csv file we use the fieldnames object
    data = [row for row in reader] # to access the data within the reader iterator we use the keys or headers of the csv file
    print(data[0]["Numbers"],",",data[0]["Cubes"])  # this prints the first line of the data
    
    # this prints the complete list of data
    """
    for row in data:
        print(row["Numbers"],',',row["Cubes"])

    Alternatively :
    for row in reader:
        print(row["Numbers"],",",row["Cubes"])
    """

# That's it for today...see you in the next tutorial...until then a <em>H3avren</em> style Ta-Da...