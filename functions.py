
#Function to remove outliers using z-score
def remove_outliers(data, col):
    col_upper = data[col].mean() + 3*data[col].std()
    col_lower = data[col].mean() - 3*data[col].std()
    df = data[(data[col]< col_upper) & (data[col]> col_lower)]
    return df 


#Function to remove outliers using percentile 

def percentile_based_outlier(data, col):
    upper_limit = data[col].quantile(0.975)
    lower_limit = data[col].quantile(0.025)
    df_percentile = data[(data[col]< upper_limit) & (data[col]> lower_limit)]
    return df_percentile 
    
def drop_all_na(data, cols):
    df = data[cols].dropna()
    return df