import matplotlib.pyplot as plt
from IPython.display import display
import seaborn as sns
import pandas as pd

def plots(pred_data, org_data = pd.DataFrame(), training_plot = False, testing_plot=False, cv_results=None):
    # Let's Compare Campaign with respect to different Groups

#     plt.rcParams['figure.figsize'] = (14, 4)

#     plt.subplot(1, 2, 1)
#     sns.barplot(x = data['gender'], y=data['ROAS'],
#                 hue = data['xyz_campaign_id'],
#                 palette = 'cool')
#     plt.xlabel(' ')

#     plt.subplot(1, 2, 2)
#     sns.barplot(x=data['age'], y=data['ROAS'],
#                 hue = data['xyz_campaign_id'],
#                 palette = 'cool')
#     plt.xlabel(' ')

#     plt.suptitle('Impact of Gender and Age on ROAS', fontsize = 20)
#     plt.show()


    if (training_plot == True):
        # plotting cv results
        plt.figure(figsize=(16,6))

        plt.plot(pred_data["Predicted"])
        plt.plot(pred_data["Ground_Truth"])
        plt.title("Comparison of Predicted Vs Ground Truth Values")
        plt.legend(['Predicted', 'Ground Truth'], loc='upper left')
        
    elif (testing_plot == True):
        # plotting cv results
        fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
        title = ['Clicks', 'Total_Conversion','Approved_Conversion']
        for i in range (0,3):
            ax[i].scatter(org_data[title[i]], pred_data[:, 0], color='r', alpha=0.5)
            ax[i].scatter(org_data[title[i]], org_data.Clicks, color='b', alpha=0.5)
            ax[i].set_xlabel('True values')
            ax[i].set_ylabel('Predicted values')
            ax[i].set_title(f'Target variable i - {title[i]}')
    else:
        plt.rcParams['figure.figsize'] = (15, 4)
        sns.scatterplot(x=pred_data['Impressions'], y=pred_data['Clicks'],color = 'black')
        plt.title('Relationship between Clicks and Impressions\n', fontsize = 20)
        plt.show()

        plt.rcParams['figure.figsize'] = (17, 6)
        sns.heatmap(pred_data.corr(), 
                    annot = True, linewidths = 2.0,
                   cmap = 'summer')
        plt.title('Correlation Heatmap for the KPIs\n', fontsize = 20)
        plt.show()
    
    
    
    
    
