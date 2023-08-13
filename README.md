# Comparing_Trading_Algorithms

** Note: Project is currently in progress and constantly gets updated as sections are completed **

# Overview
Goal: Implement different machine-learning and basic trading algorithms to compare their performance with respect to profit, number of trades, time, and other factors.

- - - -
# Project Setup
The project is controlled by C++ code and compiled using CMake.
1. Clean Data: ptyhon function called to read in .csv files. Python helper functions cleans all the data and places into a MySQL database.
2. Manage Data: C++ code reads in cleaned data from the database and places data into a custom data structure for ETFs ans Stocks.
3. Run Trading Algorithms: Run the C++ implementation of different trading algorithms on the ETFs and Stocks and measure the performance of each algorithm with respect to profit generated, number of trades, time, and other factors
4. Output the previous results of each trading algorithm and compare them to better understand the performance of the different algorithms.
- - - -
# Instructions to Run Program
In Progress ...

## Output:
In Progress ...
- - - -
# File Structure
## src
Stores all code implementations.
* main.cpp
    * The entry point into the program. Calls all necessary code and outputs the results of the tests and comparisons.
* file: data_processing
    * Contains the python code to read in the data from CSV files and store in a MySQL database.
## data
Stores the dataset used in the project. Data is historical daily price and volume data for all US-based stocks and ETFs trading on the NYSE, NASDAQ, and NYSE MKT. The data (last updated 11/10/2017) is presented in CSV format as follows: Date, Open, High, Low, Close, Volume, OpenInt. Note that prices have been adjusted for dividends and splits.
Data source: https://www.kaggle.com/datasets/borismarjanovic/price-volume-data-for-all-us-stocks-etfs
