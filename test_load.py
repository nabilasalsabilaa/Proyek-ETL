import pytest
import os
import pandas as pd
from utils.load import save_to_csv

def test_save_to_csv(tmp_path):
    df = pd.DataFrame({'col1': [1, 2], 'col2': ['a', 'b']})
    file_path = tmp_path / "test_products.csv"
    save_to_csv(df, filename=str(file_path))
    assert os.path.exists(file_path)
    df_loaded = pd.read_csv(file_path)
    assert list(df.columns) == list(df_loaded.columns)