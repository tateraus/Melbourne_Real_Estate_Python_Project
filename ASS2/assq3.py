from header import read_data

# This function is to check the mean of the prices of the properties which 
# coordinates falls into the rectangle. It will return a rounded mean of prices

def mean_price(prices): 
    meanPrice = sum(prices) / len(prices)
    meanFinal = round(meanPrice)
    return meanFinal

# This function checks if property's coordinates from data dictionary falls 
# into the resulting rectangle with given input coordinates, width and height. 
# It will return True if property's coordinates falls into the area and False
# otherwise.

def lati_longi_in_area(La_Lo_tuple, inputCoordinates, inputWidth, inputHeight): 
    set_latitude, set_longitude = inputCoordinates  
    w, h = inputWidth, inputHeight
    data_La, data_Lo = La_Lo_tuple
    in_area = False
    if set_latitude - (h/2) <= data_La <= set_latitude + (h/2)\
        and set_longitude - (w/2) <= data_Lo <= set_longitude + (w/2):
        in_area = True
    return in_area 

# This function is to get the coordinates from data dictionary and generate 
# these infomation into a new dictionary with same keys and coordinates tuples.
# It will return the new dictionary.

def get_data_coordinates(data): 
    dict0 = {}
    for key_1 in data:
        dict0[key_1] = ( float( data[key_1]['Latitude'] ), \
                        float( data[key_1]['Longitude'] ) )
    return dict0

# This function returns the mean price of properties, given their coordinates 
# have fallen into the required rectangle which can be uniquely located using
# given coordinates, width and height. It will return None if no proporty's 
# coordinate falls into the required rectangle and return the mean otherwise.

def get_avg_price_by_georegion(data, coordinates, width, height):
    coordinate_dict = get_data_coordinates(data) 
    priceList = []
    i = 0
    for key_2 in coordinate_dict:
        tuple_lati_longi = coordinate_dict[key_2] 
        if lati_longi_in_area(tuple_lati_longi, coordinates, width, height):
            price_elem = int( data[key_2]['Price'] ) 
            priceList.append(price_elem)       
            i += 1
    if i != 0:
        avg_inArea_property_price = mean_price(priceList)
        return avg_inArea_property_price
    else:
        return None
    
# to test your function with another CSV file,
# change the value of this variable
test_file = 'sales_data_clean.csv'
coordinates = (-37.840935, 144.806457)
width = 0.2
height = 0.1

# you don't need to modify the code below
if __name__ == '__main__':
    data_cleaned = read_data(test_file)
    print(get_avg_price_by_georegion(data_cleaned, coordinates, width, height))