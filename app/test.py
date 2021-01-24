from enum import Enum
class Color(Enum):
  RED = 1
  GREEN = 2
  BLUE = 3
  
  
import pandas as pd
data = {
        'year': [2014, 2018,2020,2017], 
        'make': ["toyota", "honda","hyndai","nissan"],
        'model':["corolla", "civic","accent","sentra"],
        'color':[1, 2, 3, 4]
       }

# pass column names in the columns parameter 
df = pd.DataFrame(data).astype({"color" :Color})
print(df)

