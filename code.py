import pandas as pd
import numpy as np
%matplotlib inline

airline = pd.read_csv('../Data/airline_passengers.csv',index_col='Month',parse_dates=True)

airline.dropna(inplace=True)

  airline.head()

  airline.plot();

from statsmodels.tsa.seasonal import seasonal_decompose

result = seasonal_decompose(airline['Thousands of Passengers'], model='multiplicative')  # model='mul' also works
result.plot();



