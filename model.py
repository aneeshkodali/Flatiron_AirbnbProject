

# from sklearn import preprocessing
# import itertools
import statsmodels.api as sm
import pandas as pd
# import numpy as np
from sklearn.linear_model import Lasso, Ridge, LinearRegression
from sklearn.model_selection import GridSearchCV
# from statsmodels.stats.outliers_influence import variance_inflation_factor


def scaleXData(columnList, x_train, x_test):
    '''Scales/standardizes train and test data
    by train calculations'''

    x_train_scaled = x_train.copy()
    x_test_scaled = x_test.copy()

    for column in columnList:
        
        columnMean = x_train[column].mean()
        columnStd = x_train[column].std()

        x_train_scaled[column] = (x_train_scaled[column]-columnMean)/columnStd
        x_test_scaled[column] = (x_test_scaled[column]-columnMean)/columnStd

    return x_train_scaled, x_test_scaled


def runSimpleLinearRegression(dfX, dfY):
    '''
    Args
        - dfX = dataframe of x variables
        - dfY = dataframe of y variable
    Returns regression output
    '''

    # Turn into values
    X = dfX.values
    y = dfY.values
    
    # Add constant
    X = sm.add_constant(X)
    
    mod = sm.OLS(y, X, hascont=True)
    res = mod.fit()
    return res


def makeCoefficientDF(coefTable):
    '''
    This function takes output from regression 
    and shows the coeffients as a dataframe
    '''
    coefDF = pd.DataFrame(coefTable)
    coefDF.columns = coefDF.iloc[0]
    coefDF = coefDF.drop(0)
    coefDF = coefDF.set_index(coefDF.columns[0])
    for column in coefDF.columns:
        coefDF[column] = coefDF[column].astype(float)
    return coefDF


def conductGridSearch(model, alpha_array, x_data, y_data):
	'''This function finds the best alpha for Ridge or Lasso'''
	grid = GridSearchCV(estimator = model, param_grid = dict(alpha = alpha_array))
	grid.fit(x_data, y_data)
	return grid



def runRidgeRegression(x_data, y_data, alpha=0.5):
    '''This function runs a ridge regression'''
    # Turn into values
    X = x_data.values
    y = y_data.values
    
    # Add constant
    X = sm.add_constant(X)
    
    # Construct ridge model
    ridge = Ridge(alpha=alpha).fit(x_data, y_data)
    return ridge


def runLassoRegression(x_data, y_data, alpha=0.5):
    '''This function runs a lasso regression'''
    # Turn into values
    X = x_data.values
    y = y_data.values
    
    # Add constant
    X = sm.add_constant(X)
    
    # Construct lasso model
    lasso = Lasso(alpha=alpha).fit(x_data, y_data)
    return lasso


# def see_multicollinearity(dataframe, column_list=None):

# 	if column_list is not None:
# 		dataframe = dataframe.loc[:, column_list]

# 	vif = pd.DataFrame()
# 	# For each column,run a variance_inflaction_factor against all other columns to get a VIF Factor score
# 	vif["VIF Score"] = [variance_inflation_factor(dataframe.values, i) for i in range(dataframe.shape[1])]
# 	# label the scores with their related columns
# 	vif["features"] = dataframe.columns
# 	vif.round(1)

# 	return vif




# def linear_regression_sklearn(x_data, y_data):
# 	'''This  function applys sklearn linear regression'''
# 	lin = LinearRegression().fit(x_data, y_data)
# 	return lin


# def linear_regression_sm(x_data, y_data):
#     '''This function runs a 'simple' multiple linear regression'''
#     # Turn into values
#     X = x_data.values
#     y = y_data.values
    
#     # Add constant
#     X = sm.add_constant(X)
    
#     mod = sm.OLS(y, X, hascont=True)
#     res = mod.fit()
#     labels = ['intercept'] + list(x_data.columns)
#     return res



# # def see_significant_variables_from_regression(regression, x_data, y_data):
# # 	'''This function returns variables whos pvalue is less than 0.05'''
# # 	reg_table = see_regression_output_as_table(regression, x_data, y_data)
# # 	return list(reg_table.loc[reg_table['P>|t|']<0.05].index)






# # def make_y_pred_df_from_reg(regressor, x_test_data, y_test_data):

# # 	'''This function makes a dataframe with y test data and
# #  	predicted y values using x test data'''
# #  	# Create predicted values
# #    	y_pred = regressor.predict(x_test_data)
# #  	# Make dataframe
# #    	df = pd.DataFrame([y_test_data, y_pred])
# #    	return df
 	
