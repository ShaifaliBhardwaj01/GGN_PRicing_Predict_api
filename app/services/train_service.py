import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from xgboost import XGBRegressor
from app.core.config import MODEL_PATH, PIPELINE_PATH, DATA_PATH


def build_pipeline(num_attribs, cat_attribs):
    num_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    cat_pipeline = Pipeline([
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ])

    return ColumnTransformer([
        ("num", num_pipeline, num_attribs),
        ("cat", cat_pipeline, cat_attribs)
    ])


def train_model():
    housing = pd.read_csv(DATA_PATH)

    housing['income_cat'] = pd.cut(
        housing["median_income"],
        bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],
        labels=[1, 2, 3, 4, 5]
    )

    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

    for train_index, _ in split.split(housing, housing['income_cat']):
        housing = housing.loc[train_index].drop("income_cat", axis=1)

    labels = housing["median_house_value"].copy()
    features = housing.drop("median_house_value", axis=1)

    num_attribs = features.drop("ocean_proximity", axis=1).columns.tolist()
    cat_attribs = ["ocean_proximity"]

    pipeline = build_pipeline(num_attribs, cat_attribs)
    prepared = pipeline.fit_transform(features)

    model = XGBRegressor(verbosity=0)
    model.fit(prepared, labels)

    os.makedirs("artifacts", exist_ok=True)

    joblib.dump(model, MODEL_PATH)
    joblib.dump(pipeline, PIPELINE_PATH)

    return "Model trained"