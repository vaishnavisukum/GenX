import numpy as np
import pandas as pd
from scipy.stats import zscore

def is_skewed(df, threshold=0.5):
    skew_vals = df.select_dtypes(include=np.number).skew().abs()
    return skew_vals.mean() > threshold


def iqr_mask(df):
    mask = pd.Series(True, index=df.index)

    for col in df.columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        mask &= df[col].between(lower, upper)

    return mask


def zscore_mask(df, threshold=3):
    z_scores = np.abs(zscore(df))
    return (z_scores < threshold).all(axis=1)


def clean_outliers(X, y, skew_threshold=0.5, z_threshold=3):

    numeric_X = X.select_dtypes(include=np.number)

    if is_skewed(numeric_X, skew_threshold):
        mask = iqr_mask(numeric_X)
    else:
        mask = zscore_mask(numeric_X, z_threshold)

    X_clean = X[mask].reset_index(drop=True)
    y_clean = y[mask].reset_index(drop=True)

    return X_clean, y_clean