import pandas as pd
import numpy as np

# Create a sample DataFrame with missing values
data = {
    'Value': [10, np.nan, 15, 20, np.nan, 25, 30, np.nan, 35]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Impute missing values with the minimum value of the column
min_value = df['Value'].min()
df_min_imputed = df.fillna(min_value)

print("\nDataFrame with Minimum Imputation:")
print(df_min_imputed)
