import pandas as pd
import numpy as np
from matplotlib.pylab import plt
from sklearn import model_selection
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("../Video Games Sales.csv")

#preproccessing yapılır
df =data.drop("index", axis=1, inplace=False)

df = df.dropna(axis=0)


le = LabelEncoder()

# Nominal veriyi numerice çevirilir
le.fit(df["Game Title"])
df["Game Title"] = le.transform(df["Game Title"])

le.fit(df["Platform"])
df["Platform"] = le.transform(df["Platform"])

le.fit(df["Genre"])
df["Genre"] = le.transform(df["Genre"])

le.fit(df["Publisher"])
df["Publisher"] = le.transform(df["Publisher"])

le.fit(df["Platform"])
df["Platform"] = le.transform(df["Platform"])



# Numeric veriyi categorical çevirilir
conditions = [(df["Rank"] >= 1) & (df["Rank"] <= 400),
              (df["Rank"] > 400) & (df["Rank"] <= 800), (df["Rank"] > 800) & (df["Rank"] <= 1200), (df["Rank"] > 1200) & (df["Rank"] <= 1600), (df["Rank"] > 1600) & (df["Rank"] <= 2000)]


labels = ["very high sale","high sale","medium sale","low sale","very low sale"]

df['Rank'] = np.select(conditions, labels)

le.fit(df["Rank"])
df["Rank"] = le.transform(df["Rank"])


# Categorical veriyi numerice çevirilir
x = df[["Publisher", "Global", "Platform", "Year"]]
y= df["Rank"]



# Kayıp verileri doldur
x = x.fillna(x.mean())

# Normalize et
scaler = StandardScaler()
x = scaler.fit_transform(x)

x_train,x_test,y_train,y_test = model_selection.train_test_split(x,y,test_size=0.4,random_state=7)


model = DecisionTreeClassifier()

model.fit(x_train,y_train)


predictions = model.predict(x_test)


print('mean squared error : ', mean_squared_error(y_test, predictions))
print('mean absolute error : ', mean_absolute_error(y_test, predictions))
print('accuracy  : ', model.score(x_test,y_test))
