from IPython.display import display
from plots import plots
import sklearn 
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix
import numpy as np

def testing(model, X_train, X_test, y_train, y_test, single_column = False):
    y_pred = model.predict(X_test)
    r2 = sklearn.metrics.r2_score(y_test, y_pred)
    print(f"The R-squared value for testing data is {r2}.")
    if (single_column == True):
        df_predict = pd.DataFrame(y_pred, columns = ['Predicted'])
        df_predict['Ground_Truth'] = y_test.values
        print("Clicks Prediction")
        display(df_predict)
        plots(df_predict, training_plot = True, testing_plot=False)
        
    else: 
        df_pred = pd.DataFrame(y_pred, columns=['Pred_clicks','Pred_total_conv','Pred_Approv_conv'])
        df_pred = pd.concat([y_test, df_pred])
#         display(df_pred)
        plots(pred_data = y_pred,org_data = y_test,testing_plot=True)
    
    

