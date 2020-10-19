# importing libraries
import requests
import pandas as pd

# Reading from the csv file and converting into a dataframe object
df = pd.read_csv("Sheet1.csv")
data = df.values
# Keeping all Google search codes in a numpy array
search_code = data[:,2]
print(search_code.shape[0]) #129
''' We can see as there are 129 rows and we can request a maximum of 100 search request using each SerpStack API,
therefore we have to use two different APIs. In first iteration, we request for first 75 and in second iteration
we request for remaining products.'''

first_iter=75

# Function used for first iteration
def iter1_page_url(num):
    #It starts from index 0 to 74
    for i in range(num):
        #Accessing all the search_codes sequentially using a loop
        queries = 'site:oneill.com/fr "'+search_code[i]+'"'
        #Using the Serpstack API to get URL
        params = {
                  'access_key': 'cef36d60db1f4d4e3b818ce10a3bb064',
                  'query': queries
            }    
        api_result = requests.get('http://api.serpstack.com/search', params)
                
        api_response = api_result.json()
        
        # Some of the queries do not return a URL and give error, so handling the error.
        try:
            # A page_url list stores URL for all the products sequentially
            page_url.append(api_response['organic_results'][0]['url'])
        except:
            # Appending Null in the list when URL is not found. 
            page_url.append('Null')

# Function used for second iteration
def iter2_page_url(num):
    # It starts from index 75 and goes till the last
    for i in range(num,search_code.shape[0]):
        #Accessing all the search_codes sequentially using a loop
        queries = 'site:oneill.com/fr "'+search_code[i]+'"'
        #Using the Serpstack API to get URL
        params = {
                  'access_key': 'a0df2089b0554368db0da6b2fee8a62c',
                  'query': queries
            }    
        api_result = requests.get('http://api.serpstack.com/search', params)
                
        api_response = api_result.json()
        
        # Some of the queries do not return a URL and give error, so handling the error.
        try:
            # A page_url list stores URL for all the products sequentially
            page_url.append(api_response['organic_results'][0]['url'])
        except:
            # Appending Null in the list when URL is not found.
            page_url.append('Null')

page_url=[] # A list that stores URL of all the products

# Function calls to get results
iter1_page_url(first_iter)
iter2_page_url(first_iter)

# Creating a dictionary by Making Product Page URL as a key and the page_url list as its value.
dict = {'Product Page URL':page_url}

# Converting the dictionary into a dataframe and saving the result of all the Product Page URL in a CSV File 
df1 = pd.DataFrame(dict)
df1.to_csv('URL.csv',index=False)