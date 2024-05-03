
![Logo](https://raw.githubusercontent.com/tesvn7/web-image-hosting/main/ipl_cover.webp)


# IPL Match Prediction  |  🌍 [Live](https://lr-ipl-win-predictor.streamlit.app)

This project is aimed at predicting the outcome of IPL matches based on certain input parameters such as batting team, bowling team, host city, target score, current score, overs completed, and wickets out. It utilizes a machine learning model trained on historical IPL match data to make predictions.


## Web App Features

1. Selecting Input Parameters: Choose the `batting team`, `bowling team`, `host city`, `target score`, `current score`, `overs completed`, and `wickets out` using the respective dropdown menus and input fields.

2. Predicting Outcome: Click on the `Predict Winning Probability` button to obtain the predicted probabilities of winning and losing for the selected input parameters.

## Screenshot

<img src="https://raw.githubusercontent.com/tesvn7/web-image-hosting/main/ipl-win-predictor.png" width="100%" /> 

## Backend

### Project Structure
---

1. `ipl_prediction.ipynb`: This Jupyter Notebook file contains the code for data preprocessing, model training, and evaluation.

2. `app.py`: This Python script implements the Streamlit web application for user interaction and prediction.

3. `pipe.pkl`: This is a serialized machine learning pipeline saved using pickle, containing the trained model.

4. `assets/ipl_logo.jpeg`: This directory contains the logo image used in the Streamlit app.

### Project Overview
----
The `app.py` script launches a Streamlit web app to get user input and run the model. Select the batting team, bowling team, match venue, target score, current score, overs bowled, and wickets fallen. Click Predict to see the win probability percentages for each team.

The core modeling pipeline is defined in `ipl_match_probability.ipynb` python notebook. It loads and preprocesses IPL match data, trains a logistic regression model, and outputs win probabilities via `pipe.pkl` pipeline file.

### Model Features
---

The model considers the following features:

- Batting team
- Bowling team 
- Match venue
- Runs left to win
- Balls (overs) left 
- Wickets fallen
- Target score
- Current run rate
- Required run rate


## Dependencies

- Python 3.12
- Streamlit
- pandas
- scikit-learn


## Installation

```bash
git clone https://github.com/tesvn7/ipl-win-predictor
cd ipl-win-predictor
pip install -r requirements.txt
```



## Running the App

```bash
streamlit run app.py
```
    
## Data Source  

The dataset is scraped from Cricsheet and contains ball-by-ball data for IPL matches 2008-2020 :

https://www.kaggle.com/datasets/ramjidoolla/ipl-data-set

## Project credit
- [Nitish Singh]

## Authors
- [@tesvn7]
