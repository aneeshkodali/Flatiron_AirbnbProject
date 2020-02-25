# Airbnb Project

## Table of contents

* [About the Project](#about-the-project)
* [Obtain Data](#obtain-data)
* [Scrub and Explore Data](#scrub-and-explore-data)
* [Model](#model)
* [Interpret Results](#interpret-results)
* [Future Work](#future-work)
* [Contact](#contact)


## About the Project

Members: Aneesh Kodali, Joey Mathias

This project was completed as part of Flatiron School's Data Science Fellowship program. We obtained Airbnb for the Washington DC Metro area and will attempt to predict which factors affect the price of a listing.

The project contains the following
- *Airbnb Project.ipynb*: technical notebook
- *data*: folder containing csv file as well as GEOJSON file for Folium map plots
- *scrub_and_explore.py*: contains data cleaning functions as well as function to product Folium maps
- *model.py*: contains modeling functions


## Obtain Data

We obtained files from this [site](http://insideairbnb.com/get-the-data.html). Data is as of 9/22/19.

To start, we kept variables for which we found corresponding filters on [Airbnb](img/data.png).


## Scrub and Explore Data

Our dependent variable *price* was originally categorical variable due to values contains "$", so we converted that to numeric column.

We 'dummified' many categorical variables in which we took unique values in a column and created binary columns that represented whether or not a column contained a certain value. Splitting out the *neighborhood* and *amenities* columns increased our column count to 200+!.

Using Folium library, we did some exploratory visualization of the data:

Where are most listings?

![Number of Listings](img/ExploreDataNumListings.png)

How expensive are listings?

![Listings Price](img/ExploreDataMedianPrice.png)

How many bedrooms are available?

![Number of Bedrooms](img/ExploreDataNumBedrooms.png)


## Model

We will use **Linear Regression** to predict the price of a listing. We will use R^2 to assess our model. This process included
- splitting our data into train and test sets
- scaling columns
- conducting **Simple**, **Ridge** and **Lasso** regression


## Interpret Results

Our tests produced similar R^2 values on the training set (~0.25), so we went with a model that contained the fewest variables. On the test set, our model gave an R^2 of 0.28. 

The actual output was interesting:
- having *touchless faucets* had largest effect on price (negative)
- having a *mudroom* had 2nd largest effect on price (positive)
- having *exercise equipment* had 2nd smallest effect on price (negative)
- out of neighborhoods, having a listings in *Deanwood, Burrville, Grant Park, Lincoln Heights, Fairmont Heights* had smallest effect on price (positive)

We think the poor test results are a consequence of the data itself. There are a couple of things to note:
- the data doesn't factor in occupancy rate. So an owner can put a listing on the site, but it's unclear if that listing has been reserved at that price
- since amenities are self-reported, reporting certain amenities are voluntary. So if a listing lacks a certain amenitity, it MIGHT be the case that the owner didn't feel the need to list an amenitiy
- there's the possibility that more amenities could relate to a decrease in price. The owner may not feel confident about the listing and may try to compensate by listing a lot more amenities than usual, and it may be unclear if listings have listed amenities based on the data alone.


## Future Work

As a first next step, our data would be augmented if we incorprated additional data related to booking frequency and occupancy rate. We could also look into grouping certain amenities and/or excluding certain amenities based on how frequently they appear in the data but we would have to be careful about doing so (see the notes above).

## Contact

- Connect with me on [Linkedin](https://www.linkedin.com/in/aneeshkodali)
- Read my [blog posts](https://medium.com/@aneesh.kodali)
- Check out my other [projects](https://github.com/aneeshkodali)