import numpy as np
import pandas as pd
from typing import Optional, List, Any

def array_to_dataframe(data: Any, columns: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Converts a 2D array-like structure to a Pandas DataFrame.

    Parameters:
    data (Any): A 2D array-like structure containing the data.
    columns (List[str], optional): List of column names for the DataFrame.

    Returns:
    pd.DataFrame: A DataFrame containing the data from the 2D array-like structure.
    """
    # Convert data to a NumPy array if it's not already one
    if not isinstance(data, np.ndarray):
        data = np.array(data)

    # Validate that the data is indeed 2D
    if data.ndim != 2:
        raise ValueError("Input data must be a 2D array-like structure.")

    # Check if column names are provided and match the number of columns in the data
    if columns and len(columns) != data.shape[1]:
        raise ValueError("The length of 'columns' must match the number of columns in the data.")

    # Create and return the DataFrame
    return pd.DataFrame(data, columns=columns,dtype=np.int64)
