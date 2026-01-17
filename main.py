import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("house-prices-dataset/train.csv")

def main():
    print(df.to_string()) # prints complete dataframe
    print(df.info()) # 81 columns, 1460 entries
    # null values in LotFrontage-259, Alley-1369, MasVnrType-872, MasVnrArea-8, BsmtQual-37, BsmtCond-37, BsmtExposure-38, BsmtFinType1-37, BsmtFinType2-38, Electrical-1, FireplaceQu-690, GarageType-81, GarageYrBlt-81, GarageFinish-81, GarageQual-81, GarageCond-81, PoolQC-1453, Fence-1179, MiscFeature-1406

    print(df.isnull().sum()) # prints column-wise null value count
    print(df['LotFrontage'].isnull().sum()) # prints null value count in mentioned column

    cols_with_missing_values = df.columns[df.isnull().any()].tolist()
    print(cols_with_missing_values) # prints list of columns with null values

    print(df.isnull().sum().to_string()) # prints column-wise null value count without truncating in terminal

    # Basic Count Bar Chart,height indicating the count (or proportion) of missing values
    # msno.bar(df, log=True)

    #Log Scale: msno.bar(df, log=True) can help visualize patterns when missing values vary greatly in count, revealing minor missing patterns.

    # Column count is high therefore only show columns with missing values

    plt.tight_layout()
    plt.title("House price features with missing values")

    #Matrix / Heatmap: While not strictly bar charts, msno.matrix() or msno.heatmap() provide context by showing where missing values occur in relation to other columns, revealing correlations
    #msno.matrix(df)
    #msno.heatmap(df)
    # To prevent overlapping by grouping
    #msno.dendrogram(df)

    # Column count reduced as total column count is 81
    df_to_plot = df[['LotFrontage', 'Alley', 'MasVnrType', 'MasVnrArea', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2', 'Electrical', 'FireplaceQu', 'GarageType', 'GarageYrBlt', 'GarageFinish', 'GarageQual', 'GarageCond', 'PoolQC', 'Fence', 'MiscFeature']]
    msno.bar(df_to_plot)

    #Adjust the subplot layout

    plt.subplots_adjust(
        left=0.1,  # the left side of the subplots of the figure
        right=0.9,  # the right side
        bottom=0.25,  # the bottom
        top=0.8,  # the top
        wspace=0.4,  # the amount of width reserved for space between subplots
        hspace=0.6  # the amount of height reserved for space between subplots
    )
    plt.show()

    # Out of 81, 19 Columns have null values
    # 4+1 Columns should be dropped as their null count is near to total entries = Alley, PoolQC, Fence, MiscFeature, MiscVal

    # 3 are numerical - LotFrontage(mean), MasVnrArea(median), GarageYrBlt(mean)

    # Rest are categorial - MasVnrType, BsmtQual, BsmtCond, BsmtExposure, BsmtFinType1, BsmtFinType2, Electrical, FireplaceQu, GarageType, GarageFinish, GarageQual, GarageCond

    # Copy the original Dataframe
    df_modified = df.copy()
    print(df_modified.to_string())

    # Remove Columns
    df_modified = df_modified.replace(['', 'NaN', ' ', 'NULL'], np.nan)
    df_modified.drop(columns=['Alley', 'PoolQC', 'Fence', 'MiscFeature', 'MiscVal'], inplace=True)

    # Compute Numerical Columns with typecasting if needed
    mean_lf = df['LotFrontage'].mean()
    median_mva = int(df['MasVnrArea'].median())
    mean_gyb = int(df['GarageYrBlt'].mean())

    df_modified.fillna({'LotFrontage': mean_lf}, inplace=True)
    df_modified.fillna({'GarageYrBlt': mean_gyb}, inplace=True)
    df_modified['MasVnrArea'] = df['MasVnrArea'].fillna(median_mva) # another format

    df_modified['GarageYrBlt'] = df_modified['GarageYrBlt'].astype(int) # It was float64 in original dataset. Computation leads to decimal 0.

    # Columns for mode imputation
    cols_to_impute = ['MasVnrType', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2', 'Electrical', 'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond']

    # Impute the missing values with the mode of each column
    for col in cols_to_impute:
        mode_value =  df_modified[col].mode()[0]
        df_modified.fillna({col: mode_value}, inplace=True)

    df_modified.to_csv("house-prices-dataset/clean_dataset.csv", index=False) # Save the new one, overrides if already exists.

    print(df_modified.info())
    print(df_modified.describe())

if __name__ == '__main__':
    main()