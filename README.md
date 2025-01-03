# Petroleum Price Query
This python script fetches the latest distribution of petroleum prices to inform mileage based billing rates. The process leverages the eia.gov API, to target the weekly petroleum prices for the US market. It filters and sorts the full JSON results to return only the latest pricing update.

Parsing the period date and price from the results and logging them in a tab-delimited text file. The output file is referenced by other programs/features in the code stack to ensure that mileage rates are kept up to date.

## Usage Example
**Powershell:** executable locally only<br>
```
python3 py_petrol_query.py
cat py_petrol_query.txt
```
**Linux:** executable anywhere on system<br>
```
python3 /usr/local/bin/py_petrol_query.py
cat /tmp/py_petrol_query.txt
```
**Output:**<br>
2024-12-30 &nbsp;&nbsp;&nbsp;&nbsp; 3.503