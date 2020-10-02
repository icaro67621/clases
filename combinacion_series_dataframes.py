import pandas as pd
import numpy as np
import random as rm
####################################
########series
#
serie1 = pd.Series([1,2,np.nan])
serie2 = pd.Series([4,5,6])
serie3 = serie1.combine_first(serie2)
print(serie3)
serie4 = serie2.combine_first(serie1)
print(serie4)

####################################
########dataframe
#

dataframe1 = pd.DataFrame([1,2,np.nan])
dataframe2 = pd.DataFrame([4,5,6])
print(dataframe1)
print(dataframe2)
dataframe3 = dataframe1.combine_first(dataframe2)
dataframe4 = dataframe2.combine_first(dataframe1)
print(dataframe3)
print(dataframe4)


