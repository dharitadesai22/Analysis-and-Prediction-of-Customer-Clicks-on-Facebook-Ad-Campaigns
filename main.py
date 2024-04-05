import EDA_Preprocessing as ep
from plots import plots
from FeatureEngineering import featureEngg as fe
from training import training
from testing import testing

if __name__ == "__main__":
    data = ep.data('data.xlsx', debug_output=True)
    df = ep.preprocessing(data)
    df = fe(df)
    df = ep.preprocessAfterFeatureEngg(df)
    
    plots(df)
    
    ## training for 1 target variable - [Clicks]
    model, X_train, X_test, y_train, y_test = training(df, ['Clicks'])
    testing(model, X_train, X_test, y_train, y_test, True)
    
    ## training from multiple target variable - ['Clicks', 'Total_Conversion','Approved_Conversion']
    model, X_train, X_test, y_train, y_test = training(df, ['Clicks', 'Total_Conversion','Approved_Conversion'], method=True)
    testing(model, X_train, X_test, y_train, y_test)
    