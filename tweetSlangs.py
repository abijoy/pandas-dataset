import pandas as pd


df = pd.read_json(r'F:/Downloads/Dataset-for-Detection-of-Cyber-Trolls.json', lines=True)
# df.to_csv(r'F:/Downloads/Dataset-for-Detection-of-Cyber-Trolls.csv', index= None)
df.annotation = pd.DataFrame(df.annotation.values.tolist())['label']

_dict = {}

contents = df.content.tolist()
_dict['Tweet_index'] = [ i for i in range(1, len(contents)+1) ]
LabelList = []
for i in df.annotation.tolist():
    s = str(i)
    s = ''.join(c for c in s if c.isalnum())
    LabelList.append(s)

_dict['Label'] = LabelList
_dict['Tweet_text'] = contents
dataframe = pd.DataFrame(_dict)
print(dataframe)
dataframe.to_csv(r'F:/Downloads/Dataset-for-Detection-of-Cyber-Trolls-final.csv', index=False)



