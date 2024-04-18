import streamlit as st
import pickle
import pandas as pd
from PIL import Image

# Set the page configuration to use the wide-view, width
st.set_page_config(
    page_title= 'Olympics Analysis', 
    page_icon=Image.open('assets/ipl_logo.jpeg'), 
    layout="centered", 
    initial_sidebar_state="collapsed")


# Teams and cities
@st.cache_data
def load_teams_and_cities():
    teams = ['Sunrisers Hyderabad',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Kings XI Punjab',
    'Chennai Super Kings',
    'Rajasthan Royals',
    'Delhi Capitals']
    cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']
    return teams,cities

teams, cities = load_teams_and_cities()

# Loading the model via pickle file
@st.cache_resource
def load_model():
    try:
        pipe = pickle.load(open('pipe.pkl','rb')) 
        return pipe 
    except FileNotFoundError:
        st.error('Model file "pipe.pkl" not found.')
        return None
    except Exception as e:
        st.error('Error loading model', e)
        return None

pipe = load_model()
if pipe is None:
    st.header('Model not loaded')
    st.stop()

# Heading Title
st.title('IPL :red[Win] Predictor')
st.divider()

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the bowling team',teams)

selected_city = st.selectbox('Select host city',cities)

target = st.number_input('Target', placeholder="Enter the Target score...", step=1)

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Score', placeholder="Enter the Current score...", step=1)
with col4:
    overs = st.number_input('Overs completed', step=0.1)
with col5:
    wickets = st.number_input('Wickets out', placeholder="wickets taken...", step=1)

st.divider()

# Input validation function
@st.cache_data
def validate_inputs(target, score, overs):
  error = False
  if target == 0:
    st.error("Invalid target input")
    error = True
  if score == 0:
    st.error("Invalid score input")
    error = True
  if overs == 0:
    st.error("Invalid overs input")
    error = True

  return error

# create data frame
@st.cache_data
def preprocess_df(batting_team, bowling_team, selected_city, target, score, overs, wickets):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets = 10 - wickets
    crr = score/overs
    rrr = (runs_left*6)/balls_left
    
    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [selected_city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets': [wickets],
        'total_runs_x': [target],
        'crr': [crr],
        'rrr': [rrr]
        })
    return input_df

# model predictoin
@st.cache_data
def model_prediction(input_df):
    try:
        result = pipe.predict_proba(input_df)
        loss = result[0][0]
        win = result[0][1]
        return loss, win
    except Exception as e:
        st.error( e)
        return None   

if st.button('Predict :green[Winning] Probability'):
            #Input Validation
            error = validate_inputs(target, score, overs)
            if not error:
                input_df = preprocess_df(batting_team, bowling_team, selected_city, target, score, overs, wickets)
                loss, win = model_prediction(input_df)
                st.divider()
                if loss is None:
                    st.error('Error predicting')
                else:
                    col1, col2 = st.columns(2)
                    with col1:
                        col1.metric(f':red[{batting_team}]', f'{str(round(win*100))} %', delta=None)
                    with col2:
                        col2.metric(f':red[{bowling_team}]', f'{str(round(loss*100))} %', delta=None)
                    

  
    