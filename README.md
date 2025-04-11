🌍 Air Quality Analysis in India
This project analyzes air quality data across various cities and states in India. It explores pollutant patterns, outlier detection, and regional pollution severity using Python and key data science libraries. The goal is to draw meaningful insights into pollution distribution and monitoring efforts.

📦 Dataset
Source: air_quality.csv (cleaned and used as air_quality_cleaned.csv)
Columns:
  -City, State, Station
  -Pollutant ID
  -Pollutant Min, Max, Avg
  -Last Update
  -Latitude, Longitude

🎯 Objectives
  -📊 Compare average pollutant levels across top cities
  -📦 Visualize distribution and spread of each pollutant
  -🔍 Explore correlation between PM2.5 and PM10
  -🌡️ Detect outliers using statistical methods
  -🧭 Analyze state-wise pollution severity
  -🧬 Discover pollutant relationships through heatmaps
  -🧁 Check dataset composition using a pie chart

🧰 Tools & Technologies
  *Language: Python 3
  *Libraries Used:
      *pandas – data handling
      *numpy – numerical operations
      *matplotlib, seaborn – visualization
      *scipy – for statistical analysis (if needed)
      
📌 Key Features
  *Data cleaning: Handling missing values and invalid coordinates
  *Outlier detection using Z-scores
  *Geographical validation for latitude and longitude
  *Custom visualizations:
      *Bar charts, Line plots, Box plots, Scatter plots
      *Heatmaps and Pie charts

🧪 Sample Outputs
  *📉 PM2.5 outliers detected using Z-score
  *📈 Top states with peak pollution levels
  *🔗 Strong correlation between PM2.5 and PM10
  *🧁 Pie chart showing pollutant monitoring distribution

🔍 Instructions to Run
1. Clone or download this repository.
2. Make sure Python 3.x is installed.
3. Install the required libraries:

    ```bash pip install pandas numpy matplotlib seaborn```
   
4. Place air_quality.csv in the working directory.
5.Run the analysis script:

    ```bash python air_quality_analysis.py```

   
🎓 Academic Relevance
This project is part of the INT375 – Data Science Toolbox: Python Programming course:
* Python programming foundations
* Data cleaning and manipulation (NumPy, Pandas)
* Data visualization (Matplotlib, Seaborn)
* Exploratory Data Analysis (EDA)
* Statistical evaluation and insights

👩‍💻 Author:
Name: Priya Kumari
Course: INT375
📄 License: Educational use only.

