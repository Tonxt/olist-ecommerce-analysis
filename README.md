# Olist E-Commerce Analysis

## Overview
Exploratory data analysis of Olist, a Brazilian e-commerce company. Using a real dataset of over 99,000 orders placed between 2016 and 2018, this project answers key business questions about revenue trends, top-performing product categories, and regional sales distribution.

## Business Questions
1. How did monthly revenue evolve between 2016 and 2018, and which month had the highest sales?
2. Which are the top 10 product categories by revenue?
3. Which are the top 10 Brazilian states by total sales?

## Key Findings
- **November 2017 was the highest-revenue month** (R$ 987,765), driven by Black Friday demand — nearly double the average monthly revenue.
- **Health & Beauty was the top-grossing category** with R$ 1,233,131 in revenue, followed by Watches & Gifts and Bed, Bath & Table.
- **São Paulo (SP) dominated regional sales** with R$ 5,067,633 — almost 3x the revenue of second-place Rio de Janeiro (RJ).
- **97% of orders were successfully delivered**, with R$ 370,145 in unrecovered revenue from cancelled or undelivered orders.

## Technologies Used
- **Python** — data processing and analysis
- **Pandas** — data manipulation, merging, and aggregation
- **Matplotlib** — data visualization
- **Jupyter Notebook** — interactive development environment
- **Git / GitHub** — version control and portfolio hosting

## Dataset
[Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) — available on Kaggle.
The dataset contains 9 CSV files covering orders, customers, products, sellers, payments, and reviews.
> Note: raw data files are excluded from this repository via `.gitignore`.

## How to Run
1. Clone this repository
2. Download the dataset from Kaggle and place the CSV files in the `data/` folder
3. Install dependencies: `pip install pandas matplotlib seaborn jupyter`
4. Open `notebooks/01_exploracion.ipynb` in Jupyter and run all cells