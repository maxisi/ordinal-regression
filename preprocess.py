import pandas as pd

d = pd.read_csv('raw_data.csv').T

# replace column names by first row
d.columns = d.iloc[0]

judges = [k for k in d.index if 'Unnamed' not in k]
judges_col = [[k]*4 for k in judges]
judges_col = [item for sublist in judges_col for item in sublist]

# drop first row
d = d.drop(d.index[0])
d.index = judges_col
# rename first column "Judge"
d.index.name = 'Judge'
d.columns.name = None

# rename Nominee column to "Category"
d = d.rename(columns={'Nominee': 'Category'})
# make index a the first column and reindex with numbers
d = d.reset_index()

d.to_csv('ranking_data.csv', index=False)

# anonymize data
d.columns = ['Judge', 'Category'] + [f'Candidate-{i}' for i in range(len(d.columns)-2)]
d['Judge'] = [f'Judge-{i}' for i in range(len(d))]

d.to_csv('ranking_data_anon.csv', index=False)