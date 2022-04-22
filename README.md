# Melbourne_Real_Estate_Python_Project
This project is dealing with a dataset of house/property sales in metropolitan Melbourne during the years 2016 and 2017.
The sales data in this project contains the following columns:
{ID: Row record ID.

Suburb: The suburb where the property is located.

Address: The property address.

Postcode: The property postcode, a 4-digit number.

CouncilArea: The municipality or council area under which the property falls.

Regionname: The region of metropolitan Melbourne under which the property falls.

Price: How much the property sold for. This value is a whole number.

SaleDate: The date of property sale, in the dd/mm/yyyy format.

Seller: The real estate agency that sold the property.

Bedrooms: Number of bedrooms.

Bathrooms: Number of bathrooms.

CarSpaces: Number of car spaces.

Landsize: Size of the land. This value is a whole number.

Latitude: The latitude geolocation coordinate of the property

Longitude: The longitude geolocation coordinate of the property}

The job starts with cleaning the noisy data with regard to the errors below:
1. Typos have occurred in the Price column, resulting in some non-numeric values.
2. People have entered Regionname values that are no longer current, valid region names. The valid regions are listed in a list called VALID_REGION_NAMES, which is given to you.
3. Some people have formatted the sale date incorrectly, such that it is either not of the form dd/mm/yyyy or contains invalid dates, such as 31/11/2016. If a date does not fall under the year 2016 or the year 2017, it is also considered invalid.
4. Some Postcode values are not valid Melbourne postcode values: they need to be 4-digit integers that start with 3.

The values in the CouncilArea column could be incorrectly spelt or contain extra characters. Examples of such incorrect values are: Morelnd; Yara; nox; aDarebin; Melbun; Honey Valley.
The program attempt to replace incorrect values with their correct council area value by using the following set similarity measure, which we use to provide a number representing the similarity (i.e. sim score below) between two strings. 
Suppose we have the following two example strings:

string1 = "Aaa bBb ccC" # The set representation of string1 is {'a', 'b', 'c', ' '}

string2 = "bbb ccc ddd" # The set representation of string2 is {'b', 'c', 'd', ' '}

Notice that for our purposes/definition case does not matter (e.g. 'A' is the same as 'a') and that space is also a character.

The set similarity (Sim) measure for string1 and string2 is given by the formula:
sim(str1, str2) = (length of the set intersection of str1 and str2)/(length of the set union of str1 and str2)


Then, with the cleaned data, the second py file calculates the following four statistics within the start_date to end_date range:
- average sale Price, rounded to the closest whole number.
- sum total Price
- minimum instance of Price
- maximum instance of Price

Then, the third task is to workout a function with Given the inputs of coordinates, width and height, and the resulting geo rectangle, which should return the average price of 
all the sold properties whose geolocation coordinates fall within the boundaries (including the edges) of the geo rectangle.

Then, the final task is to workout another function called provide_realestate_info(main_data, queried_properties), where the input queried_properties is a JSON structure. 
This input structure contains the core address information (Suburb, Address and Postcode) for a set of properties and looks like the following example:

[
 {"Suburb": "Rosanna", "Address": "7 Hylton Cr", "Postcode": 3084},
 {"Suburb": "Preston", "Address": "3/152 Tyler St", "Postcode": 3072},
 {"Suburb": "Epping", "Address": "19 Houston St", "Postcode": 3076}
]
The function provide_realestate_info will return a JSON-style dictionary structure that adds more information to the input structure as follows. For each property in this input set, 
the provide_realestate_info function should search the main dataset for a record of this property. If the record for a property is found, then add the key/value elements for the fields Price, 
Bedrooms and Landsize. If the input property record is not found, then remove it from the set.




