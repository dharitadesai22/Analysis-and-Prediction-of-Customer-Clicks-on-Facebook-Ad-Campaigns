# FacebookAdCampaignAnalysis
This repository is mainly to understand the way to analyze the results obtained after performing Exploratory Data Analysis (EDA). Also, to decide the best suitable Machine Learning Algorithm to consider for training.

To run the project, these steps need to be followed:
STEP 1: Install the required libraries
        All the required dependencies along with the versions are there in requirements.txt and can be installed using command on command prompt 
        - pip install -r requirements.txt 

STEP 2: After installation, simply by executing the command 
         - <b>python main.py</b>
        python code should run, displaying the plots for prediction vs ground truth. 
        
     
DESCRIPTION OF EACH FILE 
1. EDA_Preprocessing.py - File targets on EDA analysis and preprocessing of the data. The analysis is drawn and decisions are made for further process. 
2. FeatureEngineering.py - Here we targets on calculating the few standard terminologies that contributes towards prediction. 
3. plots.py - This specific file is created to get all the required plots which took into account for analysis.
4. training.py - Here the complete training process in detail is mentioned.
5. testing.py - File is designed to test the trained model 
6. main.py - this is the MAIN file from where the code starts and each and every function is called.



Each function has separate arguments to consider, like if run directly then by default parameter will be considered and K-fold cross validation will not be performed. However, if one need to proceed then in main.py under training function the parameter can be passed to consider it. 

HAPPY LEARNING !!!
