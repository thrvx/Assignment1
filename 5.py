import pandas as pd
from sklearn.impute import SimpleImputer

# Example DataFrame
data = {
    'A': [1, 2, None, 4, 4],
    'B': ['cat', 'dog', 'dog', None, 'cat']
}
df = pd.DataFrame(data)

# Define the imputer for numerical features
numerical_imputer = SimpleImputer(strategy='most_frequent')

# Apply the imputer to numerical columns
df['A'] = numerical_imputer.fit_transform(df[['A']])

# Define the imputer for categorical features
categorical_imputer = SimpleImputer(strategy='most_frequent')

# Apply the imputer to categorical columns
df['B'] = categorical_imputer.fit_transform(df[['B']])

print(df)
