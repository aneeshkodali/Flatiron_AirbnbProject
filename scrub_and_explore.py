import pandas as pd
import numpy as np
import folium
import os
import json


def makeDummyColumnFromCategoricalDummyColumn(dataframe, column):
	'''This function takes a column with values of 't'/'f' and converts to 1/0'''

	# Create copy of column: if value is 't' return 1 else 0
	dataframe[column+'_EQ_T'] = np.where(dataframe[column]=='t',1,0)
	return dataframe

def getDummies(dataframe, column):
	'''This function creates dummy columns from categorical variable
	This is identical to pandas get_dummies EXCEPT we want to keep
	the original column'''
	# Create copy of the column
	column_copy = column+"_EQ"
	dataframe[column_copy] = dataframe[column]

	# Create dummy columns
	dataframe = pd.get_dummies(dataframe, columns=[column_copy], prefix = column_copy, drop_first=True)

	return dataframe

def makeDummyColumnFromMultivalueColumn(dataframe, column, character_list=None, sep=","):
	'''This function takes a column with multiple values, gets list of unique values
	and then creates dummy columns.
	Optional char_list argument is specified to strip column of any characters 
	if need be'''

	# Strip characters from column
	if character_list is not None:
		for char in character_list:
			dataframe[column] = dataframe[column].str.replace(char, "")

	# Create list of unique values
	unique_list = list(set([x.strip() for l in dataframe[column].str.split(sep) for x in l]))
	unique_list.sort()
	unique_list = [str(x) for x in unique_list if str(x) not in ['', 'nan']]

	# Iterate through our unique list (except 0th element) to create columns
	for element in unique_list[1:]:
		dataframe[column+"_EQ_"+element] = dataframe[column].apply(lambda x: (element in x)*1)

	return dataframe


def buildMap(dataframe, aggCol, aggBy, legendname, groupByCol='neighbourhood_cleansed'):
	'''
	This function builds a map of DC by neighborhood
	Args
		- dataframe
		- aggBy = method for aggregating data: 'mean', 'median', 'count', 'sum'
		- legendName = name used for legend in map
	Returns map
	'''

	# Aggregate dataframe
	map_df = dataframe.groupby(groupByCol)[aggCol].agg(aggBy).reset_index()

	# Find geo json file in data
	state_path = os.path.join(os.getcwd(),'data', 'neighbourhoods.geojson') 
	state_geojson = json.load(open(state_path))

	# Build map
	nm = folium.Map(location=[38.9072, -77.0369],zoom_start=12)

	folium.Choropleth(
		geo_data=state_geojson,
		name='choropleth',
		data=map_df,
		columns=[map_df.columns[0], map_df.columns[1]],
		key_on='feature.properties.neighbourhood',
		fill_color='YlGnBu',
		fill_opacity=0.7,
		line_opacity=0.2,
		legend_name=legendname
	).add_to(nm)

	folium.LayerControl().add_to(nm)

	return nm