from header import read_data, VALID_COUNCIL_AREAS
from pprint import pprint  # Only used for test purpose

from datetime import datetime
# This runction is to generate a nested dictionary using council names as key 
# in the outer dictionary and the inner dictionary is consist of sale date 
# and price. It will return a new dictionary contained the infomation above.
def generate_dict(data):
    sale_dict = {}
    for key_1 in data:
        date = data[key_1]['SaleDate']
        council = data[key_1]['CouncilArea']
        price = data[key_1]['Price'] 
        elem = [date, price]
        if council not in sale_dict:
            sale_dict[council] = {key_1: elem}
        else:                                 
            sale_dict[council][key_1] = elem 
    return sale_dict

# This function is to calculate the sum of sale price for different 
# councils in Melbourne for a given dictionary as input. It will retutn 
# a new dictionary in a form of {'Council name': sum of sale price}
def sum_price(stats_data):
    for key_2 in stats_data:
        if stats_data[key_2] != None:
            sum_price = sum(stats_data[key_2]) 
            stats_data[key_2] = sum_price
    return stats_data

# This function is to calculate the mean of sale price for different councils 
# in Melbourne for a given dictionary as input. It will retutn a new dictionary 
# in a form of {'Council name': mean of sale price}
def mean(stats_data): 
    for key_3 in stats_data:
        if stats_data[key_3] != None:
            n1 = len( stats_data[key_3] )
            mean = sum( stats_data[key_3] ) / n1
            stats_data[key_3] = round(mean)
    return stats_data

# This function is to calculate the min of sale price for different councils 
# in Melbourne for a given dictionary as input. It will retutn a new dictionary 
# in a form of {'Council name': min of sale price}
def minimal(stats_data):
    for key_9 in stats_data:
        if stats_data[key_9] != None:
            minimal = min( stats_data[key_9] )
            stats_data[key_9] = minimal
    return stats_data 

# This function is to calculate the max of sale price for different councils 
# in Melbourne for a given dictionary as input. It will retutn a new dictionary 
# in a form of {'Council name': max of sale price}
def maximal(stats_data):
    for key_11 in stats_data:
        if stats_data[key_11] != None:
            maximal = max( stats_data[key_11] )
            stats_data[key_11] = maximal
    return stats_data
    
# This function is to compute sale price within the range of star date and end 
# date(inclusive) in regards of 4 stats (ie. mean, maximum, minimum, sum). It 
# takes the clean dictionary and 2 dates, start date and end date respectively 
# as inputs. It will return -1 if the start date greater than end date. 
# Otherwise, it will return a new dictionary showing 4 stats of each council.
def sale_stats_by_council(data_cleaned, start_date, end_date):
    Sale_dict = generate_dict(data_cleaned) 
    stats_dict1 = dict.fromkeys(VALID_COUNCIL_AREAS) 
    stats_dict2 = stats_dict1.copy() 
    statsList = ['avg', 'max', 'min', 'sum']
    date_Start = datetime.strptime(start_date, '%d/%m/%Y')
    date_End = datetime.strptime(end_date, '%d/%m/%Y') 
    for key_4 in stats_dict2:
        stats_dict2[key_4] = dict.fromkeys(statsList) 
    if date_Start <= date_End:
        for key_5 in Sale_dict: 
            salePrice = []
            in_dict = Sale_dict[key_5] 
            for key_6 in in_dict: 
                date_test = in_dict[key_6][0]
                date0 = datetime.strptime(date_test, '%d/%m/%Y') 
                if date_Start <= date0 <= date_End:
                    salePrice.append( int(in_dict[key_6][1]) ) 
                    stats_dict1[key_5] = salePrice
        stats_dict3, stats_dict4, stats_dict5, stats_dict6 = stats_dict1.copy()\
        , stats_dict1.copy(), stats_dict1.copy(), stats_dict1.copy()
        Sum_price = sum_price(stats_dict3)
        for key_7 in Sum_price:
            sumPrice = Sum_price[key_7]
            if sumPrice != None:
                stats_dict2[key_7]['sum'] = sumPrice      
        Mean_price = mean(stats_dict4)
        for key_8 in Mean_price:
            meanPrice = Mean_price[key_8]
            if meanPrice != None:
                stats_dict2[key_8]['avg'] = meanPrice
        Min_price = minimal(stats_dict5)
        for key_10 in Min_price: 
            minPrice = Min_price[key_10]
            if minPrice != None:
                stats_dict2[key_10]['min'] = minPrice
        Max_price = maximal(stats_dict6)
        for key_12 in Max_price:
            maxPrice = Max_price[key_12]
            if maxPrice != None:
                stats_dict2[key_12]['max'] = maxPrice
        return stats_dict2
    else:
        return -1 

 
# to test your function with 'sales_data_clean_sample.csv' or another CSV file,
# change the value of this variable
test_file = 'sales_data_clean_sample.csv'
start_date = '01/01/2016'
end_date = '31/12/2017'

# you don't need to modify the code below
if __name__ == '__main__':
    data_cleaned = read_data(test_file)
    pprint(sale_stats_by_council(data_cleaned, start_date, end_date))