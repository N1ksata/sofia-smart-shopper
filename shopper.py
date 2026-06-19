import json

def load_prices():
    with open('market_prices.json', 'r') as f:
        data = json.load(f)
        return data

if __name__ == "__main__":
    grocery_data = load_prices()
    print("Successfully loaded data:")
    print(grocery_data)