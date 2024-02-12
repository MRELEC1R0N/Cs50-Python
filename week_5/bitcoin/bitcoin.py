import requests
import sys


def main():
    if len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
            print(bit_price(n))
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")


def bit_price(n):
    try:
        response = requests.get(f'https://api.coindesk.com/v1/bpi/currentprice.json')
        result = response.json()
        total = n*result["bpi"]["USD"]["rate_float"]
        return f"${total:,.4f}"
    except requests.RequestException:
        return None

if __name__ == "__main__":
    main()
