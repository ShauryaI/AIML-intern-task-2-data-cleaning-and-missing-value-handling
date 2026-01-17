# AIML-intern-task-2-data-cleaning-and-missing-value-handling

## Actions Performed ##

1. Load dataset and identify missing values using .isnull().sum().
 - Dataset used - House Prices Dataset
 - Column with null value count has been detected
 - NaN, None, NA - are considered as null
2. Visualize missing data patterns using simple bar charts.
 - This is achieved with the help of missingno library
 - The missingno library in Python is a data visualization tool used to quickly and effectively understand the presence, distribution, and correlation of missing (NaN or null) values within a pandas DataFrame
 - >>> pip install missingno
 - 19/81 columns found to be with null values.
3. Apply mean/median imputation for numerical columns.
 - 3/19 are numerical columns
 - Mean or median imputation involves replacing missing values in a numerical column with the mean or median of the non-missing values in that same column.
 - Method recommended when missing data % is less than 5%
 - Mean works well when data is evenly spread
 - Median works well when there are extreme values.
 - Above 5%, method changes, for now mean is performed for LotFrontage column
4. Apply mode imputation for categorical columns.
 - Mode imputation is a simple data cleaning technique that fills missing values in a dataset by replacing them with the mode (most frequent category or value) of that specific variable.
5. Remove columns with extremely high missing values.
 - Percentage of missing value - (Number of Missing Values / Total Rows) * 100
 - Threshold ranges from 50-75%
 - Remove if the information it holds is not critical
 - Missing data pattern
   - if Missing Completely At Random - MCAR - imputation or simple removal of rows might be appropriate for low-missing-percentage columns.
   - if not MCAR, removing the entire column might be the safest way to avoid introducing bias into your analysis or model
   - Rule followed
     - < 10% - Impute with mean, median, mode, or use advanced methods like K-Nearest Neighbors (KNN) imputation.
     - 10% -50% - Evaluate importance. Consider advanced imputation or carefully weigh the impact of removing the column entirely.
     - > 70% - Remove the column in most cases, as it offers limited predictive power and imputation is unreliable.
 - 5/19 are selected for removal. MiscVal removed due to removal of MiscFeature
 - Empty strings (""), strings that literally say "NaN", "N/A", or "null", strings with hidden whitespace (e.g., " "). should be converted to null first before removing so that dropna can work
 - For complete removal, use drop.
6. Validate dataset after cleaning.
 - After cleaning, now we have
 - 76 columns
 - 1460 entries same as before
 - All are non-null values
7. Compare before vs after dataset size and quality.
 - Dataset size definitely reduced due to column removal.
 - We have a file with no missing values.
 - Due to mode computing in 2 columns, we have wrong data also to an extreme extent.
 - Example: 
 - Fixing columns - BsmtQual, BsmtCond, BsmtExposure, BsmtFinType1, BsmtFinType2 and GarageType, GarageFinish, GarageQual, GarageCond is correct as all have NA and fixed equally
 - Fixing columns - 
   - MasVnrType with mode computation will result in having values and respective MasVnrArea will remain 0 as 0 in not a null value, and it was not fixed with mean.
   - MasVnrType column contains 872 null values so removing these rows will result in data loss.
   - FireplaceQu with mode computation will result in having values and respective Fireplaces will remain 0 as 0 in not a null value, and it was not fixed with mean.
   - FireplaceQu column contains 690 null values so removing these rows will result in data loss.
 - Removing columns -
 - MiscVal has also been removed due to removal of MiscFeature
 - PoolArea can be removed due to PoolQC. It does not add any value as compared to total entries.
 - Cleaned file needs further data analysis for better output.
 - LotFrontage is eligible for more complex imputation like KNN.

## Deliverables: ##
1. Cleaned dataset file - house-prices-dataset/clean_dataset.csv
2. Notebook with cleaning steps - clean_dataset.ipynb