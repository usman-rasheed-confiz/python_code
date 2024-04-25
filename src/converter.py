import numpy as np
import pandas as pd

# Example: Create a NumPy array
numpy_array = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Convert to a Pandas DataFrame
# Optionally, you can add column names during conversion
df = pd.DataFrame(numpy_array, columns=["A", "B", "C"])  # Example column names

# Display the Pandas DataFrame
print("Pandas DataFrame:")
print(df)

