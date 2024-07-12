# Cryptocurrency Price Fetcher

This Python script fetches the USD price of a cryptocurrency based on its ticker symbol using the Messari API.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:

```sh
git clone https://github.com/jorgeirun/cryptocurrency-price-fetcher.git
```

2.	Navigate to the project directory:

cd cryptocurrency-price-fetcher


3.	Install the required dependencies:

pip install requests


## Usage

Run the script and input the ticker symbol of the cryptocurrency you want to fetch the price for:

python fetch_price.py

>> Please enter coin ticker: BTC
>> BTC price is 123,456.78 USD

- Code Explanation

The script defines a function fetch_price(ticker) that:

	1.	Converts the input ticker symbol to uppercase.
	2.	Sends a GET request to the Messari API to fetch cryptocurrency data.
	3.	Parses the JSON response to find the cryptocurrency with the matching ticker symbol.
	4.	Returns the ticker symbol and its USD price if found, or None if not found.


- Error Handling

The function handles various exceptions to ensure robustness:

	•	KeyError: If a required key is not found in the JSON response.
	•	IndexError: If an index error occurs while parsing the JSON response.
	•	ConnectionError, Timeout, TooManyRedirects: If an error occurs during the HTTP request.
	•	A generic exception handler to catch any unexpected errors.


- License

This project is licensed under the MIT License.

MIT License

Copyright (c) [2024] [Jorge Irún]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.