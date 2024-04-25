import os

import pandas as pd

input = os.environ["INPUT"]
output = os.environ["OUTPUT"]

df = pd.read_excel(input, index_col=1)

df.dropna(axis=1, how='all', inplace=True)

df.to_csv(output, index=True, encoding='utf-8')
