#-----------------------------------------------------------------
# SMART HEALTH ANALYZER – Data Cleaning & Insights (Using Pandas)
#-----------------------------------------------------------------
import pandas as pd

#-------------------------------------------------------------
# STEP 1: Create Expanded Health Dataset
#-------------------------------------------------------------
# I am creating a dataset with information about multiple people's health metrics.
# Each column represents a health attribute and each row represents a person.
# Some values are missing (None) to simulate real-world incomplete data.
health_data = {
    "Name": ["Aarav", "Diya", "Isha", "Rafi", "Nisha", 
             "Kabir", "Meera", "Alisha", "Sana", "Vivaan", 
             "Anaya", "Karan", "Riya", "Dev", "Bhargavi"],
    "Systolic": [120, 135, 110, None, 125, 118, 122, 130, 115, 128, 119, None, 132, 118, 126],
    "Diastolic": [80, 90, 70, None, 85, 78, 82, 88, 75, 86, 79, None, 90, 77, 84],
    "Heart_Rate": [72, 95, 68, 80, 78, 70, 85, None, 66, 88, 76, 92, 105, 70, 80],
    "Blood_Sugar": [115, 160, None, 140, 130, 120, 150, 135, 110, None, 125, 145, 155, 118, 140],
    "BMI": [24.2, 28.5, 23.1, None, 26.8, 23.5, 25.2, 27.3, 22.8, 24.5, None, 26.1, 28.0, 23.0, 24.7],
    "Oxygen": [98, 92, 95, 97, 93, 99, 96, None, 97, 94, 98, 95, 93, 97, 96],
    "Sleep_Hours": [7, 5, 8, None, 6, 8, 7, 5, 8, 7, 6, None, 5, 7, 8],
    "Water_Liters": [2.5, None, 3.0, 2.2, 1.8, 2.7, 3.1, 2.0, 2.5, 2.8, 2.3, None, 2.0, 2.7, 3.0]
}

# Converting the dictionary into a Pandas DataFrame for easier data manipulation.
df = pd.DataFrame(health_data)
print("Original Health Dataset:\n")
print(df)

#-------------------------------------------------------------
# STEP 2: Handle Missing Data
#-------------------------------------------------------------
# Missing data can lead to incorrect analysis or errors.
# I am filling missing numerical values with the mean of that column.
# This approach keeps the dataset complete while maintaining overall trends.
df.fillna(df.mean(numeric_only = True), inplace = True)
print("\nDataset After Filling Missing Values with Mean:\n")
print(df)

#-------------------------------------------------------------
# STEP 3: Iteration Example – Update BMI > 25
#-------------------------------------------------------------
# High BMI (>25) can indicate overweight or health risks.
# I am capping BMI at 25 to standardize the dataset for analysis.
# This demonstrates how iteration and condition checking works in Pandas.
for x in df.index:
    if df.loc[x, "BMI"] > 25:
        df.loc[x, "BMI"] = 25
print("\nDataset After Capping BMI at 25:\n")
print(df)

#-------------------------------------------------------------
# STEP 4: Concatenate New Entry
#-------------------------------------------------------------
# I am adding a new person to the dataset using Pandas concat.
# This simulates the dynamic addition of new health data in real-world scenarios.
new_person = pd.DataFrame({
    "Name": ["Rahul"], "Systolic":[118], "Diastolic":[78], "Heart_Rate":[72],
    "Blood_Sugar":[120], "BMI":[24], "Oxygen":[97], "Sleep_Hours":[7], "Water_Liters":[2.5]
})
df = pd.concat([df, new_person], ignore_index = True)
print("\nDataset After Adding a New Person:\n")
print(df)

#-------------------------------------------------------------
# STEP 5: Duplicates
#-------------------------------------------------------------
# Duplicate rows can distort analysis.
# I am checking for duplicates and dropping them to keep data clean and accurate.
print("\nCheck for Duplicates:\n", df.duplicated())
df.drop_duplicates(inplace = True)
print("\nDataset After Dropping Duplicates:\n")
print(df)

#-------------------------------------------------------------
# STEP 6: Identify Unhealthy People
#-------------------------------------------------------------
# I am creating a new column 'Health_Status' to classify each person's health.
# A person is marked "Unhealthy" if any key metric is outside safe limits.
# This helps in quick identification of health risks in the dataset.
df["Health_Status"] = "Healthy"
for x in df.index:
    if (df.loc[x, "Systolic"] > 120 or
        df.loc[x, "Diastolic"] > 80 or
        df.loc[x, "Heart_Rate"] > 100 or df.loc[x, "Heart_Rate"] < 60 or
        df.loc[x, "Blood_Sugar"] > 140 or
        df.loc[x, "BMI"] > 25 or
        df.loc[x, "Oxygen"] < 95):
        df.loc[x, "Health_Status"] = "Unhealthy"
print("\nDataset with Health Status:\n")
print(df)

#-------------------------------------------------------------
# STEP 7: Describe Dataset
#-------------------------------------------------------------
# I am generating descriptive statistics to understand the distribution of health metrics.
# This summary helps in quick insights like mean, min, max, and standard deviation.
print("\nHealth Summary Statistics:\n")
print(df.describe())

#-------------------------------------------------------------
# ROUND NUMERIC COLUMNS TO 2 DECIMALS
#-------------------------------------------------------------
# I am rounding all numeric columns to 2 decimal places.
# This makes the CSV file cleaner and easier to read.
numeric_cols = ["Systolic", "Diastolic", "Heart_Rate", "Blood_Sugar", "BMI", 
                "Oxygen", "Sleep_Hours", "Water_Liters"]
df[numeric_cols] = df[numeric_cols].round(2)

#-------------------------------------------------------------
# STEP 8: Save to CSV
#-------------------------------------------------------------
# Finally, I am saving the cleaned and enriched dataset to a CSV file.
# This allows us to reuse or share the dataset outside Python easily.
df.to_csv("output/Smart_Health_Analyzer_Final.csv", index=False)
print("\nCSV file 'Smart_Health_Analyzer_Final.csv' created successfully!")
