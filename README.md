# Missing Values Imputation Program (Version 2)

This program is designed to impute missing values in datasets using a combination of deep learning (DL) and machine learning (ML) methods. It works with two input datasets and performs multivariate imputation.

## Getting Started

To use this program, follow these steps:

1. **Dataset Preparation**: Ensure that you have the required datasets in the same directory as the program file (`main.py`). The program expects two datasets:

   - `AMR-and-NSH-Buoy-Data1394.xls`: The primary dataset containing data for imputation.
   - `normalized-xls-files/preprocess-normal-dataset-excel.xls`: A supplementary dataset used for additional information.

2. **Python Environment**: Make sure you have Python 3.x installed on your system.

3. **Install Dependencies**: Install the necessary Python libraries:

   - pandas
   - seaborn
   - scikit-learn

4. **Run the Program**: Execute the program by running the main script.

## Program Overview

The program performs the following tasks:

1. **Data Loading**: It loads the required datasets into Pandas DataFrames.

2. **Multivariate Imputation**:
   - Columns related to date and time are extracted from the primary dataset.
   - The number of missing values in the supplementary dataset is displayed.

3. **Data Separation**: The program separates specific columns from the supplementary dataset into two separate DataFrames: `badataset` (Buoy Amirabad) and `bndataset` (Buoy Noshahr). These columns contain weather measurements.

4. **Date and Time Generation**: The script generates date and time values for both Gregorian and solar time based on specific patterns, and they are assigned to the corresponding series.

5. **Linear Regression and Imputation**: Linear regression and iterative imputation are set up for imputing missing values in the separated datasets. Iterative imputation is applied to both `badataset` and `bndataset`.

6. **Creating New DataFrames**: The imputed values are used to create new DataFrames for both `badataset` and `bndataset`.

7. **Combining Datasets**: The generated date and time series are concatenated with the imputed `badataset` and `bndataset` to create a combined dataset called `micedataset`.

8. **Missing Values Check**: The script calculates and prints the number of missing values for each column in the `micedataset`.

9. **Data Visualization**: A distribution plot is generated for one of the columns ("Buoy Amirabad Battery Voltage(1)") in the `micedataset` using Seaborn.

10. **CSV Output**: The final imputed dataset (`micedataset`) is saved to a CSV file named "AMR-and-NSH-Buoy-Data1394-normalized-mice.csv" in the "multivariate-method-results" directory.

## Author

- ehsanasgharzde

Feel free to reach out if you have any questions or need further assistance with this program.

