# Luchen's Sleep Tracker

### Introduction

The Sleep Tracker program aims to provide an interactive tool for users to monitor and analyze their sleep patterns. The program will be written in Python and will allow users to input their sleep data, visualize trends, and make informed decisions to improve their sleep habits.

### Goals

- Develop a Python program for tracking sleep patterns.
- Provide an interactive interface for data entry and visualization.
- Allow users to customize their sleep tracking experience.
- Store data securely and provide insights through analysis.

### Functional Requirements

1. **User Interface**

   - Command-line interface (CLI) for user interaction. _P0_
   - Prompts for data entry regarding user's information. _P0_
   - Prompts for data entry including date, sleep time, and wake time. _P0_
   - Prompts for data entry regarding sleep quality. _P1_

2. **Data Structure**

   - The internal data structure should be able to store each user's input information in an organized way separately. _P0_
   - The data structure should be easy to convert to exteral storage. _P0_

3. **Data Storage**

   - Store sleep data based on each individual user in a local file (e.g., CSV or JSON format). _P0_
   - Ensure data is stored securely and can be easily accessed for analysis. _P0_

4. **Data Analysis**

   - Calculate total sleep hours for each day. _P0_
   - Provide a summary of sleep patterns over a specified period (e.g., weekly, monthly). _P1_

5. **Data Visualization**

   - Display sleep data in a tabular format. _P1_
   - Generate visual representations (e.g., charts) to show trends and patterns. _P1_

6. **Customization**

   - Allow users to specify their preferred sleep tracking start time (e.g., 6 PM). _P2_
   - Enable customization of visualization colors and formats. _P2_

### Non-Functional Requirements

- The program should be user-friendly and easy to navigate. _P0_

- The program should handle data securely and prevent unauthorized access. _P2_

- The program should be efficient and handle large datasets without performance degradation. _P1_

### System Architecture

1. **User Interface Module - P0**

   - Handles interaction with the user through the command-line interface.
   - Collects input data and provides feedback to the user.

2. **Data Storage Module - P0**

   - Manages the storage and retrieval of sleep data
   - Ensures data is stored in a structured format (e.g., CSV, JSON).

3. **Data Analysis Module - P1**

- Processes the sleep data to calculate total sleep hours and identify patterns.
- Provides functions for summarizing and analyzing data over different periods.

4. **Data Visualization Module - P1**

- Generates visual representations of sleep data.
- Provides functions for creating charts and tables to display trends.

### Detailed Design

#### User Interface Module

- **Functions:**
  - `get_user_info()`
  - `get_date()`
  - `get_sleep_time()`
  - `get_wake_time()`
  - `get_sleep_quality()`
  
#### User Interface Module
- Use 'dictionary' as the major data structure, where `date` serves as the 'key', and list of input times (e.g., \[\[sleep_time_1, wake_time_1\], \[sleep_time_2, wake_time_2\], \[sleep_time_3, wake_time_3\]\]) as the 'value'.
