from header import read_data, VALID_REGION_NAMES, VALID_COUNCIL_AREAS
from pprint import pprint  # Only used for test purpose


# This function is to measure the set similarity of two input strings
# The return value simScore is the set similarity score between 2 strings      

def set_similarity(s1, s2):
    a, b = set(s1.lower()), set(s2.lower())
    a_i_b = a & b
    a_u_b = a | b
    sim_score = len(a_i_b) / len(a_u_b)
    return sim_score


# This function is to check the most alike Councilname for the given input data
# based on the maximal sim score from function above. It will return the most 
# similar councilname which has the maximal sim score but will return None if 
# two counsil names have the same maximal sim score

def mostalike(name):
    score = 0
    most_alike = ''
    scorelist = []
    for x in range(11):
        sim_score = set_similarity(name, VALID_COUNCIL_AREAS[x])
        scorelist.append(sim_score)
        while sim_score > score:
            score = sim_score
            most_alike = VALID_COUNCIL_AREAS[x]
    if scorelist.count(score) > 1:
        return None
    else:
        return most_alike


# This function is to check formatting of the date (ie. if it's in dd/mm/yyyy).
# It also checks if the data range is valid (ie. days <= 31, month <= 12, year 
# = 2016 or 2017).The return value is True for valid format and False for 
# invalid format


def dateformat(date):
    date_format = True
    date_set = set(date)
    list1 = [chr(symb1) for symb1 in range(32, 47)] + \
            [chr(symb2) for symb2 in range(58, 65)] + \
            [chr(symb3) for symb3 in range(91, 97)] + \
            [chr(symb4) for symb4 in range(123, 127)]
    set1 = set(list1)
    if bool(date_set & set1) or date.isdigit():
        date_format = False
    else:
        list2 = date.split('/')
        if len(list2) != 3:
            date_format = False
        else:
            if len(list2[0]) > 2 or int(list2[0]) not in range(1, 32):
                date_format = False
            if len(list2[1]) > 2 or int(list2[1]) not in range(1, 13):
                date_format = False
            if len(list2[2]) != 4 or list2[2] not in ['2016', '2017']:
                date_format = False
    return date_format


# This function is to check the validity of the date value, which means the day
# value of each date should not exceed the maximal days in that month
# The return value will be False if any value fails.

def datevalid(date):
    date_valid = True
    mdate = date.split('/')
    year = mdate[2]
    month = mdate[1]
    day = mdate[0]
    dict2016 = {'01': 31, '02': 29, '03': 31, '04': 30, '05': 31, '06': 30, \
                '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}
    dict2017 = dict2016.copy()
    dict2017['02'] = 28
    if year == '2016' and int(day) not in range(1, dict2016[month] + 1):
        date_valid = False
    if year == '2017' and int(day) not in range(1, dict2017[month] + 1):
        date_valid = False
    return date_valid


# This function checks if all characters of a price are digits.
# It will return None if any of its character is a non-digit. 

def price_valid(price):
    if not price.isdigit():
        return None
    else:
        return price


# This function checks if the region name is a valid name within the list named,
# VALID_REGION_NAMES. It will return None if any there is no match in the list.     

def region_valid(region):
    if region not in VALID_REGION_NAMES:
        return None
    else:
        return region


# THis function is to check if a postcode is valid based on requirements in the
# instructions. It wil return None if it's not a valid postcode.

def postcode_valid(postcode):
    if len(postcode) != 4 or not postcode.isdigit() or postcode[0] != '3':
        return None
    else:
        return postcode


# This function is to clean the sales data based on the given rules in the 
# instruction with regard to price, region name, date, postcode and council 
# areas  and replace the incorrect CouncilArea. The return value is a dict with 
# cleaned data

def clean_sales_data(data_noisy):
    new_noisy_data = {}
    for key_1 in data_noisy:
        innerdict = data_noisy[key_1].copy()
        new_noisy_data[key_1] = innerdict
        price, region, postcode, date = new_noisy_data[key_1]['Price'], \
                                        new_noisy_data[key_1]['Regionname'], new_noisy_data[key_1]['Postcode'], \
                                        new_noisy_data[key_1]['SaleDate']
        new_noisy_data[key_1]['Price'] = price_valid(price)
        new_noisy_data[key_1]['Regionname'] = region_valid(region)
        new_noisy_data[key_1]['Postcode'] = postcode_valid(postcode)
        if not dateformat(date):
            new_noisy_data[key_1]['SaleDate'] = None
        else:
            if not datevalid(date):
                new_noisy_data[key_1]['SaleDate'] = None
        councilname0 = new_noisy_data[key_1]['CouncilArea']
        most_alike0 = mostalike(councilname0)
        new_noisy_data[key_1]['CouncilArea'] = most_alike0
    return new_noisy_data


# to test your function with 'noisy_data.csv' or another CSV file,
# change the value of this variable
test_file = 'sales_data_noisy_sample.csv'

# you don't need to modify the code below
if __name__ == '__main__':
    data_noisy = read_data(test_file)
    pprint(clean_sales_data(data_noisy))
