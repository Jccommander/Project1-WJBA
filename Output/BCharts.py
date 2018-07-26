#dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#read CSV
education_data = pd.read_csv("../Output/Edu_Data.csv")
education_data.head()
for row in education_data