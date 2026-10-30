# NYS-Traffic-Data
## Team Traffic | Joseph Mele, Daniel Antunes, Jason Haimovici

This is a repository for the ENGR315 Project. It focuses on analyzing NYS Traffic Data.

# Motivation
- This repository is used to analyze New York State traffic violations by driver age, gender, location, and day of the week. The goal is to organize and analyze traffic-ticket records to identify differences across groups and times, and communicate the findings using Python through statistical methods and visualizations.

Dataset: https://catalog.data.gov/dataset/traffic-tickets-issued-four-year-window?from_hint=eyJxIjoiTmV3IHlvcmsgdHJhZmZpYyJ9
- Issued from NYS DMV 
- Relevant columns are age, gender, violation code/description, violation date, location or jurisdiction, and vehicle registration state, subject to availability and completeness in the downloaded dataset.

# Research Questions
1. Does age significantly predict traffic violations among adult male drivers?
   - We expect to find that younger drivers receive more violations than older drivers because of their inexperience.

2. Is there a relationship between gender and traffic violation types across different areas of New York?
   - We expect to find that men are more prone to aggressive and reckless crimes.

3. How do age and traffic violations correlate across different days of the week?
   - We expect to see that Friday has the highest count of people going out at night and for the peak age to lean towards young adults during the weekend as well.

Potential Benefits: Answering these questions based on the dataset could help find traffic patterns that could help enforcement policies in NYS.

# Introduction
NYS receives an uncountable amount of traffic data each day, well at least not by hand. By using Python, we can clean and analyze all of NYS's traffic records to create a meaningful dataset that can help us answer questions.

# Implementation Details: Methods, Metrics, Tools, and Plots
The tools we will be using to implement and prepare out data are Python, pandas, NumPy, Matplotlib, and SciPy. Loading the data consists of:
  - Load the dataset into python using pandas to create a data frame of our csv file
  - Determine which columns are relevant to the question being asked
  
  # Question 1
  
  ## Method
Filter the dataset to include only male drivers 18 or older. Group age ranges and count the violations within each group
  ## Metrics
    - Number of recorded violations by age
    - Percentage of the male-adult ticket sample in each age group
    - Group age differences and fitted trend/model statistics, including a p-value where appropriate
  ## Tools
    Pandas, NumPy, Matplotlib
  ## Plot
    Bar chart of violation counts by age range
    
  # Question 2
  
  ## Method
Filter the violations based on both gender and traffic violations. Plot the count of each violation over 500 for each gender and then filter by jurisdiction
  ## Metrics
    - Violation counts by gender, category, and jurisdiction
    - Percentage distribution of violation types within each gender and location
    - Chi-square
  ## Tools
    Pandas, NumPy, Matplotlib
  ## Plot
    Stacked bar charts for violation types by gender
    
  # Question 3
  
  ## Method
Take the total violations under each day of the week and separate the per age violation count under each day. The table should show a row for each age present and the number of counts at that age per each day of the week.
  ## Metrics
    - Number of violations by weekday and age group
    - Percentage of each day's violations in each age group
    - Mean or median age by weekday
    - Weekday-versus-weekend differences and relevant statistics
  ## Tools
  Pandas, NumPy, Matplotlib
  ## Plot
  Multi-line chart of ticket counts by age for each weekday

# Results

# Conclusions

# References
Data.gov — Traffic Tickets Issued: Four Year Window.
