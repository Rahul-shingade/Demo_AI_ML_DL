from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
my_pipeline = Pipeline([
    ('imputer' ,SimpleImputer(strategy ='median')),
    ('std_sclar', StandardScaler()),
])