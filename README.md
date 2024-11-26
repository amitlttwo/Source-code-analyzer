# Source-code-analyzer

## URL Parameter Finder Tool

This repository contains a Python-based tool designed to analyze web pages and identify JavaScript input parameters embedded in the source code. The tool processes a list of URLs provided in a text file, fetches the source code of each page, and detects patterns such as var <variable> = cfpParam("<parameter>");. It then generates actionable results, including the final URLs for detected parameters, all presented in a professional, color-coded format.

#### Features

* Automated Analysis: Processes a list of URLs and analyzes the source code for specific patterns.
* Parameter Detection: Identifies JavaScript input parameters and generates corresponding final URLs.
* Color-Coded Output: Uses professional color schemes for better readability and usability.
* Error Handling: Provides detailed error messages for invalid or inaccessible URLs.
* User-Friendly Interface: Interactive prompt to input the file path for URLs.

### How to Use

#### Clone the repository:
```
git clone https://github.com/amitlttwo/Source-code-analyzer.git
```
#### Navigate to the project directory:

```
cd Source-code-analyzer
```
#### Install the dependencies:
```
pip install -r requirements.txt
```
#### Run the script:
```
python3 SCA-detector.py
```

Provide the path to the text file containing URLs when prompted.

#### Example Input File urls.txt
```
https://example1.com
https://example2.com/page
https://example3.com/home
```

#### Output
For each URL, the tool will:
* Highlight detected parameters.
* Provide corresponding final URLs in a readable format.
* Display errors or warnings for invalid URLs.

##### Requirements
Python 3.x
Dependencies listed in requirements.txt

#### Author
This tool was created by Amit Kumar (@amitlt2).
