import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer

# Sample dataset with missing values
data = {
    'feature1': [1, 2, np.nan, 4, 5],
    'feature2': [10, np.nan, 30, 40, 50]
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Create KNN imputer with k neighbors
k = 2
knn_imputer = KNNImputer(n_neighbors=k)

# Apply KNN imputer to the DataFrame
df_imputed = pd.DataFrame(knn_imputer.fit_transform(df), columns=df.columns)

# Display the DataFrame after imputation
print("\nDataFrame after KNN imputation:")
print(df_imputed)
 