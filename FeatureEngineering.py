def featureEngg(data):
    # Performing Feature Engineering to understand the Campaigns in Detail

    # lets create a Column to understand CTR
    data['ClickThroughRate'] = ((data['Clicks']/data['Impressions'])*100)

    # lets create a column to understand CPC
    data['CostPerClick'] = (data['Spent']/data['Clicks'])

    # lets create a column to understand Conversion Rate
    data['ConversionRate'] = (data['Approved_Conversion']/data['Total_Conversion'])

    # lets create a column to understand the Cost per Conversion
    data['CostPerConversion'] = (data['Spent']/data['Approved_Conversion']) 
    
    # lets add More Features to Understand the Return on Investment also known as ROAS(Return on Ad Spend)

    # lets calculate the Conversion Value, Let's Assume that the Value of Sales if 100 Dollars
    data['ConversionValue'] = data['Approved_Conversion']*100

    # lets calculate the ROAS Which is the Target Variable for us
    data['ROAS'] = round(data['ConversionValue']/data['Spent'], 2)

    # lets Calculate CPM to understand the Brand Awareness from Campaigns
    data['CostPerMille'] = round((data['Spent']/data['Impressions'])*1000, 2)
    
    
    return data