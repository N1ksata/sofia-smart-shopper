# Sofia Smart Shopper: Grocery and Quality Optimizer

## Purpose
Sofia Smart Shopper is a local command-line utility designed to help consumers optimize their grocery budgets in Sofia, Bulgaria. The tool analyzes a user's custom shopping list and compares pricing data across different local supermarket tiers, specifically calculating the cost difference between basic budget items and premium, high-quality alternatives.

## Features
* Parses a local raw text shopping list containing items and quantities.
* References a supermarket price index tracking common Bulgarian staples (e.g., Sirene, Kiselo Mlyako) in Bulgarian Leva (BGN).
* Calculates the total minimum cost using budget-tier pricing.
* Calculates the total cost if upgrading the entire basket to premium-quality tiers.
* Provides a financial analysis showing the exact price difference between the two choices.

## Project Structure
* `shopper.py` - The primary Python script containing the calculation logic.
* `market_prices.json` - The local database containing supermarket pricing and quality tiers.
* `my_list.txt` - The user's custom grocery list file.

## Requirements
* Python 3.x (I'm using 3.14.5)
* No external dependencies required (uses built-in modules).
