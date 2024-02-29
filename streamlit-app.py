import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
st.title("Amazon Sales Prediction using Linear, Ridge and Lasso Regressions")
st.write("Select the variable for prediction:")