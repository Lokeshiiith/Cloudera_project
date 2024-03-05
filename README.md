# Streamlit as a CML Application

![The Streamlit logo](statics/images/Cloudera.jpeg)

A minimal example of a [Streamlit](https://www.streamlit.io/) application running as a CML or CDSW Application.
We display and chart a small dataset with Seaborn.

## Repository Structure

```bash
├── src/  
        ├── scripts/
        │   ├── download_data.py
        │   ├── install_dependencies.py
        │   └── launch_app.py
        ├── app.py
        ├── static/
        ├── .project-metadata.yaml
        ├── README.md
        └── requirements.txt
```

## Launching the project on CML

### 1.download_data.py

The `download_data.py` script facilitates the retrieval of data from the Aphrodite dataset. It contains the following URLs for accessing the data:

1. **Precipitation Data:**

   - URL: [APHRO_V1101](http://aphrodite.st.hirosaki-u.ac.jp/product/APHRO_V1101/APHRO_MA/025deg_nc/)
   - Period: 1951-2015
2. **Temperature Data:**

   - URL: [APHRO_V1101EX_R1](http://aphrodite.st.hirosaki-u.ac.jp/product/APHRO_V1101EX_R1/APHRO_MA/025deg_nc/)
   - Period: 1961-2015

**Note:**

- It's essential to exercise caution while downloading large datasets due to potential bandwidth and storage constraints.
- Users should consider the availability of existing analysis and avoid redundant data collection to optimize resource utilization.

---

### 2. install_dependencies.py

The `install_dependencies.py` script contains the necessary dependencies required for the project installation. It ensures that all essential packages are installed to enable smooth execution of the project.

---

### 3. launch_app.py

The `launch_app.py` script contains the command to run the Streamlit application. It executes the following command to open the Streamlit app:

```bash
!streamlit run app.py --server.port $CDSW_APP_PORT --server.address 127.0.0.1
```

This command launches the Streamlit application with the specified server port and address, allowing users to interact with the app through their web browsers.

Ensure that the `app.py` file contains the necessary code for your Streamlit application to function correctly.---

---

### 4 . static

All the static files needed to compute the results in background and then show the results by interface of streamlit app.

---



### 5.project-metadata.yaml

```markdown
  name: Timberline Analysis
description: To find the ranges which are in critical condition and need immediate attention
author: Cloudera Inc.
specification_version: 1.0
prototype_version: 2.0
date: "2024-02-25"

runtimes:
  - editor: Workbench
    kernel: Python 3.9
    edition: Standard

tasks:
  - type: run_session
    name: Install Dependencies
    script: scripts/install_dependencies.py
    kernel: python3
    cpu: 2
    memory: 4

  - type: start_application
    name: Application to serve UI
    short_summary: Create an application to serve the image analysis UI
    subdomain: imageanalysis
    script: scripts/launch_app.py
    environment_variables:
      TASK_TYPE: START_APPLICATION## Workflow Configuration
 
 
```

# Tasks done

### Tasks Completed

1. **Data Clipping** : Data clipping involves restricting data values to a certain range or boundary. In this context, it likely refers to the process of managing or filtering the Timberline Points data.
2. **Interpolation Methods Used** :

* Cubic
* Linear
* Inverse Distance Weighting (IDW)
* Modified Inverse Distance Weighting (MIDW)
* Nearest Neighbor

1. **Finding Mean** :

* The mean is calculated for the interpolated data points obtained using various interpolation methods.

1. **Calculating Mean in 200 Meter Range Timberlines** :

* The mean values within a 200-meter range of Timberlines are calculated. This likely involves averaging the values of the points falling within this specified range around each Timberline point.

---

# File Tree

- **./**

  - Logfiles.log
  - PrecipitaionAnalysis.ipynb :  contains step by way to clip and interpolate and get results of Precipitation analysis
  - TemperatureAnalysis.ipynb : contains step by way to clip and interpolate and get results of Temperature analysis
  - **PrecipitaionAnalysis/  for each interpolation method annual rangewise mean precipitaoin**

    - **InterpolateRangeWise/**
      - **Cubic200/**
        - AP.xlsx
        - HP.xlsx
        - J&K.xlsx
        - SK.xlsx
        - UK.xlsx
      - **IDW200/**
      - **Linear200/**
      - **MIDW200/**
      - **Nearest200/**
  - **Shp_timberline/**

    - Consisting shape files
  - 
  - **TemperatureAnalysis/**

    - **InterpolateRangeWise/  For each state monthwise Temperature for 1961-2015**
      - **AP/**
        - **Cubic200/**
          - AP_Apr_200mtrRange.xlsx
          - AP_Aug_200mtrRange.xlsx
          - AP_Dec_200mtrRange.xlsx
          - AP_Feb_200mtrRange.xlsx
          - AP_Jan_200mtrRange.xlsx
          - AP_Jul_200mtrRange.xlsx
          - AP_Jun_200mtrRange.xlsx
          - AP_Mar_200mtrRange.xlsx
          - AP_May_200mtrRange.xlsx
          - AP_Nov_200mtrRange.xlsx
          - AP_Oct_200mtrRange.xlsx
          - AP_Sep_200mtrRange.xlsx
        - **IDW200/**
        - **Linear200/**
        - **MIDW200/**
        - **Nearest200/**
      - **HP/**
        - **Cubic200/**
        - **IDW200/**
        - **Linear200/**
        - **MIDW200/**
        - **Nearest200/**
      - **J&K/**
        - **Cubic200/**
        - **IDW200/**
        - **Linear200/**
        - **MIDW200/**
        - **Nearest200/**
      - **SK/**
        - **Cubic200/**
        - **IDW200/**
        - **Linear200/**
        - **MIDW200/**
        - **Nearest200/**
      - **UK/**
  - 

  # Timberline Points Data

  The following files contain Timberline Points data captured at Timberline. The points are spaced 30 meters apart from each other and are in the format <latitude, longitude, altitude>:


  1. **AP_TL_2015.xlsx**
  2. **HP_TL_2015.xlsx**
  3. **J&K_TL_2015.xlsx**
  4. **SK_TL_2015.xlsx**
  5. **UK_TL_2015.xlsx**

  These files contain geographic coordinates and altitude information of points captured at Timberline. Each point represents a specific location with latitude, longitude, and altitude recorded.
