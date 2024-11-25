import re
import requests
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def find_parameters(source_code, base_url):
    """
    Finds input parameters in JavaScript-like patterns from the given source code.
    """
    pattern = r'var\s+(\w+)\s*=\s*cfpParam\("(\w+)"\);'
    matches = re.findall(pattern, source_code)
    found_parameters = []
    for var_name, param in matches:
        full_url = f"{base_url}#{param}="
        found_parameters.append((param, full_url))
    return found_parameters

def process_urls(file_path):
    """
    Processes each URL from the input file and checks for the desired pattern.
    """
    try:
        with open(file_path, "r") as file:
            urls = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(Fore.RED + "Error: File not found. Please check the file path.")
        return

    print(Fore.CYAN + "\nStarting analysis...\n")
    for url in urls:
        print(Fore.YELLOW + f"Checking URL: {url}")
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                parameters = find_parameters(response.text, url)
                if parameters:
                    print(Fore.GREEN + f"  Found parameters in {url}:")
                    for param, final_url in parameters:
                        print(Fore.BLUE + f"    - Parameter: {param}")
                        print(Fore.MAGENTA + f"      Final URL: {final_url}")
                else:
                    print(Fore.RED + "  No matching parameters found.")
            else:
                print(Fore.RED + f"  Unable to fetch the page. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"  Error: {e}")

    print(Fore.CYAN + "\nAnalysis complete.")

def main():
    """
    Main function to run the tool.
    """
    print(Fore.CYAN + "Welcome to the URL Parameter Finder Tool!")
    print(Style.BRIGHT + "This tool finds specific input parameters in JavaScript source code.")
    file_path = input(Fore.YELLOW + "Enter the path to your URLs text file: ").strip()
    process_urls(file_path)

if __name__ == "__main__":
    main()
