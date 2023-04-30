from IPython.display import display
from plots import plots
import sklearn 
import pandas as pd


def testing(model, X_train, X_test, y_train, y_test, single_column = False):
    y_pred = model.predict(X_test)
    r2 = sklearn.metrics.r2_score(y_test, y_pred)
    print(f"The R-squared value for testing data is {r2}.")
    print(single_column)
    if (single_column == True):
        df_predict = pd.DataFrame(y_pred, columns = ['Predicted'])
        df_predict['Ground_Truth'] = y_test.values
        plots(df_predict, training_plot = True, testing_plot=False)
    else: 
        print("*"*50)
        display(y_test)
        plots(pred_data = y_pred,org_data = y_test,testing_plot=True)
