from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import RFE
from sklearn.multioutput import MultiOutputRegressor
from sklearn.linear_model import Ridge,LinearRegression
import sklearn

def training(data, targets, test_size = 0.1, random_state=42, cross_val = False, n_features_optimal=6, method = False):
    y = data[targets]
    X = data.drop(columns = targets)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    if (method == True):
        lm = MultiOutputRegressor(LinearRegression()).fit(X_train, y_train)
        print('-'*20,'Training Scores','-'*20)
        y_pred = lm.predict(X_train)
        r2 = sklearn.metrics.r2_score(y_train, y_pred)
        print(f"The R-squared value for training data while considering all three Target variable is {r2}.")

    else:
    
        lm = LinearRegression()
        if (cross_val == True):
            scores = cross_val_score(lm, X_train, y_train, scoring='r2', cv=5)
            print(f"The cross-validation scores are {scores} .")

            folds = KFold(n_splits = 10, shuffle = True, random_state = 42)
            hyper_params = [{'n_features_to_select': list(range(1, X_train.shape[1]))}]
            lm.fit(X_train, y_train)
            rfe = RFE(lm) 
            model_cv = GridSearchCV(estimator = rfe, 
                            param_grid = hyper_params, 
                            scoring= 'r2', 
                            cv = folds, 
                            verbose = 1,
                            return_train_score=True)  
            model_cv.fit(X_train, y_train) 


            cv_results = pd.DataFrame(model_cv.cv_results_)
            display(cv_results)

    
        lm.fit(X_train, y_train)

        rfe = RFE(lm, n_features_to_select=n_features_optimal)             
        rfe = rfe.fit(X_train, y_train)
        print('-'*20,'Training Scores','-'*20)
        y_pred = lm.predict(X_train)
        r2 = sklearn.metrics.r2_score(y_train, y_pred)
        print(f"The R-squared value for training data while considering only Clicks as Target variable is {r2}.")
    
    return lm,X_train, X_test, y_train, y_test