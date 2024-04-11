
# 1. Introduction

This folder contains python code for exploring the datasets available for the Redback Operations Sports Performance Analysis project.

# 2. Code

The .py and .ipynb files in the directory include two main types of programs:

- Data exploration programs. These include basic predictive models used to determine whether the data is likely to be useful for producing reliable models.

- Strava export programs. These are several different implementations for extracting data from Strava. The data is extracted using the Strava API  and using web scraping. Ultimately, the most reliable method was to performa data dump from the Strava UI and then to clean that data after that.

# 3. Data

There is a /data folder in this directory which contains the data used in this project. 

The data is stored in a .csv, .xlsx format. The .csv and .xlsx files are extracts that were created in previous trimesters.

The files are as follows:  

cyclist_data_23T2.csv - This file contains the cyclist data for the 2023 T2 Redback Operations project. This inclused data for multiple workouts but there are some issues with some fields such as the duration fields whicg have invalid data.

A thourough description of the data and the issues with this file is located at https://redback-operations.atlassian.net/wiki/spaces/RO/pages/18087940/Cycling+Data+Description.

The process for downloading a dump of Strava files for an account is found at https://support.strava.com/hc/en-us/articles/216918437-Exporting-your-Data-and-Bulk-Export. A video that explains more options on exporting Sta=rava files individually or in bulk is available at https://www.youtube.com/watch?v=IbWMFikIGLo.
