import pandas
import os

# Code to convert Json to csv using pandas
def main():
    abs_path = "/Users/sreeram/Projects/Algonomy/train"  # Absolute path to pass to the directory encoder
    directory = os.fsencode(abs_path)  # Absolute path to pass to the directory encoder
    json_list = os.listdir(directory)  # creating list of file names
    json_list.sort() # sort list by numerical order
    
    counter = 0 # to divide the numbe of csv files
    file_index = 0 # to name the csv files
    
    # iterating through the json files in the training dataset and writing it into a csv file
    # one csv file for 100 json files
    for file_to_open in json_list:
        filename = os.fsdecode(file_to_open) # open file
        print(filename) # to check progress in terminal
        json_opened = pandas.read_json(r'/Users/sreeram/Projects/Algonomy/train/'+filename) # loading the json with the file name in the current iteration
        json_opened.to_csv('/Users/sreeram/Projects/Algonomy/csv_files/dataset_csv_'+str(file_index), mode = 'a', header = False) # converting the loaded json into a csv using pandas built in library
        counter+=1 # incrementing counter to see which file is being parsed
        
        if counter % 25 == 0: # changing the file_index of the csv for every 100 jsons
            file_index+=1

if __name__ == "__main__":
    main()
