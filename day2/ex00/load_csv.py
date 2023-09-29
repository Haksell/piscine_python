import pandas as pd
import sys


def load(path: str) -> pd.DataFrame | None:
    """Load a csv file and return a pandas DataFrame."""
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}", file=sys.stderr)
        return None
