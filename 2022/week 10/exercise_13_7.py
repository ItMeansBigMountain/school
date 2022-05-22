import json
import csv
 


'''
    Exercise 13.7
         - you'll need a relatively small number of tweet object's properties. Write a
            script that will extract only a small subset of a tweet's common properties and place
            those in a CSV file.


    PYTHON JSON TO CSV FORMAT DOCUMENTATION
        https://www.geeksforgeeks.org/convert-json-to-csv-in-python/
'''



# ARRAY WITH OBJECTS IN THEM TO CSV
with open('Stream_Output_File.json' , 'r'  ) as json_file:
    data = json.load(json_file)


# OPEN OUTPUT FILE
output_file = open('output_file.csv', 'w' ,  encoding='utf-8')

#  create the csv writer object
csv_writer = csv.writer(output_file)

# ITERATION
header = True
for i in range( 0 , len(data) , 1 ):
    if header == True:
        # Writing headers of CSV file
        header = data[i].keys()
        csv_writer.writerow(header)
 
    # Writing data of CSV file
    csv_writer.writerow(data[i].values())




output_file.close()