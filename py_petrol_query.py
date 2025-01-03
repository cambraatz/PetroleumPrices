#!/usr/bin/env python3

import http.client
import json
import os

''' logic to fetch data from EIA '''
def fetch_prices(connURL,endPoint):
    conn = None

    try:
        # establish http connection...
        conn = http.client.HTTPSConnection(connURL)

        # request/response to API endpoint...
        conn.request("GET", endPoint)
        response = conn.getresponse()

        # return JSON data on success...
        if response.status == 200:
            data = response.read()
            return json.loads(data)
        # log error and return none...
        else:
            print('Error:', response.status)
            return None
        
    # log exception errors and return none...
    except Exception as e:
        print('Error:', e)
        return None
    
    # close connection if open (always runs)...
    finally:
        if conn:
            conn.close()

''' initialize request parameters '''
# define constants...
apiKey = "beQDZtHErIg0pcEBV27VDcAx1E8uzHInvpxUU5xy"
frequency = "weekly"
target = "value"
product = "EPD2D"
duoArea = "NUS"
orderBy = "period"
sortDir = "desc"

query_params = {
    "api_key": "beQDZtHErIg0pcEBV27VDcAx1E8uzHInvpxUU5xy",
    "frequency": "weekly",
    "data[]": "value",
    "facets[product][]": "EPD2D",
    "facets[duoarea][]": "NUS",
    "sort[0][column]": "period",
    "sort[0][direction]": "desc"
}

# establish target and request URL...
connURL = "api.eia.gov"
baseURL = "https://api.eia.gov/v2/petroleum/pri/gnd/data/?"
query_string = "&".join(f"{key}={value}" for key,value in query_params.items())
endPoint = baseURL + query_string

# define output file info...
targetDir = "" #"/tmp"
fileName = "py_petrol_query.txt"

''' logic to store data '''
# fetch data...
data = fetch_prices(connURL,endPoint)

# when valid...
if data:
    try:
        # parse out period and value from JSON...
        period = data["response"]["data"][0]["period"]
        value = data["response"]["data"][0]["value"]

        # log data to output file...
        output_file = os.path.join(targetDir,fileName)
        with open(output_file, "w") as f:
            f.write(f'{period}\t{value}')
        
        # verify completion...
        print(f'Petroleum data written to {output_file}')

    # handle query errors...
    except KeyError as e:
        print(f'Key error: {e}. The response may not contain expected keys.')

# log error message...
else:
    print("Failed to fetch petroleum data")