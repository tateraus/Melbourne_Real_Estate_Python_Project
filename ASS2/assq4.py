from header import read_data
from pprint import pprint  # Only used for test purpose
import json

# This function is to check whether the input json structure components can be 
# found in the cleaned data file. It will return a new dictionary with full 
# data infomation from the cleaned data and organized by its original key. For
# example, if for first component in json file, we find 2 matches with key '1'
# and '100', we will return both of these 2 matches with their keys in a dict.

def search_entry(inner_dict, main_data):
    dict0 = {}
    for key_1 in main_data: 
        if ( inner_dict['Suburb'] == main_data[key_1]['Suburb'] ) and \
        ( inner_dict['Address'] in main_data[key_1]['Address'] ) and \
        ( inner_dict['Postcode'] == int(main_data[key_1]['Postcode']) ): 
            dict0[key_1] = main_data[key_1] 
    return dict0 

# This function is to extract required information from a matched dictionary 
# with full infomation and to form a single component of the final returned 
# json structure. It will take a correctly formated dictionary as an input 
# (ie. all the value type are properly selected). It will return a single 
# component of the required json structure consisting of key/value pairs in a 
# dictionary format.

def complete_json_inner_dict(formatEntryData):
    keys = ('Address', 'Bedrooms', 'Landsize', 'Postcode', 'Price', 'Suburb')
    dict2 = dict.fromkeys(keys) 
    for key_2 in dict2:  
        for key in formatEntryData: 
            dict2[key_2] = formatEntryData[key][key_2]
    return dict2 

# This function is to convert the value type into the required output value 
# type. It will take an dictionary (ie. here is the returning dictionary from
# serach_entry()) as input and convert 4 values into integer. It will return 
# the input dictionary with some value types converted.

def dict_valtype_convert(dictionary):
    for key in dictionary:
        dictionary[key]['Postcode'] = int( dictionary[key]['Postcode'] )
        dictionary[key]['Price'] = int( dictionary[key]['Price'] )
        dictionary[key]['Bedrooms'] = int( dictionary[key]['Bedrooms'] )
        dictionary[key]['Landsize'] = int( dictionary[key]['Landsize'] )
    return dictionary

# This function is to return a json structure with more added information. It
# will take the original json structure and cleaned data file as inputs. If it
# has found a single match for the json components in the data file, it will 
# return the components with more detailed value. If it hasn't found a match or 
# the matched records in data file more than one, it will remove the components
# from the original json structure and returns the matched results.

def provide_realestate_info(main_data, queried_properties): 
    json_list = json.loads(queried_properties)
    final_json_list = []
    for num in range(len(json_list)): 
        inner_dict = json_list[num] 
        entry_in_data = search_entry(inner_dict, main_data) 
        if len( entry_in_data ) == 1:
            typeRightEntryData = dict_valtype_convert(entry_in_data)
            ToAddJsonElem = complete_json_inner_dict(typeRightEntryData) 
            final_json_list.append(ToAddJsonElem) 
    return final_json_list
  
# Change these variables to test your function with another CSV file
# or with another test case
test_file = 'sales_data_clean.csv'
queried_properties_test = '[{"Suburb": "Rosanna", "Address": "7 Hylton Cr", \
"Postcode": 3084},{"Suburb": "Preston", "Address": "3/152 Tyler St", \
"Postcode": 3072},{"Suburb": "Epping", "Address": "19 Houston St", \
"Postcode": 3076}]'

# You don't need to modify the code below
if __name__ == '__main__':
    data_cleaned = read_data(test_file)
    pprint(provide_realestate_info(data_cleaned, queried_properties_test))