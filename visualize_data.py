from matplotlib import pyplot as plt
import numpy
import os
import pandas
import ast
from collections import defaultdict
import operator

def main():
    abs_path = "/Users/sreeram/Projects/Algonomy/csv_files"  # Absolute path to pass to the directory encoder
    directory = os.fsencode(abs_path)  # Absolute path to pass to the directory encoder
    csv_list = os.listdir(directory)  # creating list of file names
    csv_list.sort() # sort list by numerical order

    # dictionary to store spec_key:frequency  (i.e size:10, color:15 etc)
    spec_attribute_count = defaultdict(int)

    # dictionary to store spec_values:frequency (i.e: black:15, large:10 etc)
    spec_value_count = defaultdict(int)
    
    counter = 0
    # loop through each csv file in the folder and add addtributes and values to the respective dictionary
    for csv_to_open in csv_list:
        if counter == 0: # skips the first iteration of each csv file in order to not skip the NAND
            counter+=1
            continue
        csv_name = os.fsdecode(csv_to_open) #Decoding directory of files to get a list of file nams 
        spec_read_file = pandas.read_csv(r'/Users/sreeram/Projects/Algonomy/csv_files/'+csv_name, usecols= [5]) # Reading the csv files and extracting the spec column
        
        # Loop to generate a dictionary with counts of attributes and their values
        for rows in spec_read_file.itertuples(): # iterate over the row in each csv file
            dict_data = ast.literal_eval(rows._1) # convert each row into a dictionary
            
            for attribute in dict_data.keys():
                if attribute in spec_attribute_count: # attribute is already in the dictionary so add a count
                    spec_attribute_count[attribute]+=1
                else: # new attribute detected. make a dictionary entry
                    spec_attribute_count[attribute] = 1
            
            # Similar to the previous loop but for value counts
            for value in dict_data.values(): 
                if value in spec_value_count:
                    spec_value_count[value]+=1
                else:
                    spec_value_count[value] = 1
        
        print("CSV Done : ",counter)
        counter+=1

    # Graphing the data as histograms to visualize
    spec_value_count_sorted = dict(sorted(spec_value_count.items(), key=operator.itemgetter(1),reverse=True))    
    ind = numpy.arange(len(spec_value_count_sorted))
    plt.bar(ind, list(spec_value_count_sorted.values()))
    plt.xticks(ind, list(spec_value_count_sorted.keys()))
    plt.title("Values vs Counts")
    plt.ylabel("Count")
    plt.show()
    
    spec_attribute_count_sorted = dict(sorted(spec_attribute_count.items(), key=operator.itemgetter(1),reverse=True))
    plt.bar(spec_attribute_count_sorted.keys(), spec_attribute_count_sorted.values(), color ='g')
    plt.title("Atrributes vs Counts")
    plt.ylabel("Count")
    plt.show()


if __name__ == "__main__":
    main()


