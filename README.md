# A Sleep Tracker

## 0. Credits
This project marks the culmination of my learning journey with "Code in Place 2024". I extend my heartfelt gratitude to the amazing teaching team.

I am especially grateful to Bryce for his invaluable suggestions and help in executing and assembling this project.

While there are additional features I plan to incorporate, due to time constraints and other commitments, this is not the final version. Stay tuned for future updates!

## 1. Introduction

The Sleep Tracker program aims to provide an interactive tool for users to monitor and analyze their sleep patterns. The program will be written in Python and will allow users to input their sleep data, visualize trends, and make informed decisions to improve their sleep habits.

## 2. Goals

- Develop a Python program for tracking sleep patterns.
- Provide an interactive interface for data entry and visualization.
- Allow users to customize their sleep tracking experience.
- Store data securely and provide insights through analysis.

## 3.Functional Requirements

### 3.1 User Interface

- Command-line interface (CLI) for user interaction. (P0)
- Prompts for data entry regarding user's information. (P0)
- Prompts for data entry including date, sleep time, and wake time. (P0)
- Prompts for data entry regarding sleep quality. (P1)

### 3.2 Data Structure

- The internal data structure should be able to store each user's input information in an organized way separately. (P0)
- The data structure should be easy to convert to external storage. (P0)

### 3.3 Data Storage

- Store sleep data based on each individual user in a local file (e.g., CSV or JSON format). (P0)
- Ensure data is stored securely and can be easily accessed for analysis. (P0)

### 3.4 Data Analysis

- Calculate total sleep hours for each day. (P0)
- Provide a summary of sleep patterns over a specified period (e.g., weekly, monthly). (P1)

### 3.5 Data Visualization

- Display sleep data in a tabular format. (P1)
- Generate visual representations (e.g., charts) to show trends and patterns. (P1)

### 3.6 Customization

- Allow users to specify their preferred sleep tracking start time (e.g., 6 PM). (P2)
- Enable customization of visualization colors and formats. (P2)

## 4. Non-Functional Requirements

- The program should be user-friendly and easy to navigate. (P0)
- The program should handle data securely and prevent unauthorized access. (P2)
- The program should be efficient and handle large datasets without performance degradation. (P1)

## 5. System Architecture

### 5.1 User Interface Module (P0)

- Handles interaction with the user through the command-line interface.
- Collects input data and provides feedback to the user.

### 5.2 Data Storage Module (P0)

- Manages the storage and retrieval of sleep data
- Ensures data is stored in a structured format (e.g., CSV, JSON).

### 5.3 Data Visualization Module (P1)

- Generates visual representations of sleep data.
- Provides functions for creating charts and tables to display trends.

### 5.4 Data Analysis Module (planned)

- Processes the sleep data to calculate total sleep hours and identify patterns.
- Provides functions for summarizing and analyzing data over different periods.
