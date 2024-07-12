import pandas as pd
import numpy as np

# Create a sample DataFrame with missing values
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [5, np.nan, 7, 8, 10],
    'C': [np.nan, 2, 3, np.nan, 5]
}
df = pd.DataFrame(data)

print("Original DataFrame with Missing Values:")
print(df)

# Impute missing values with the median
df_imputed = df.fillna(df.median())

print("\nDataFrame After Imputation with Median Values:")
print(df_imputed)
