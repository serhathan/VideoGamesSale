import pandas as pd
from matplotlib.pylab import plt

data = pd.read_csv("Video Games Sales.csv")

df =data.drop("index", axis=1, inplace=False)
df = df.dropna(axis=0)

print(data.info())


#Zaman İçinde Her Bölgede Toplam Satış

salesByYear = df.groupby("Year").sum()[["North America", "Europe", "Japan", "Rest of World"]]

plt.plot(salesByYear.index, salesByYear["North America"], label="North America")
plt.plot(salesByYear.index, salesByYear["Europe"], label="Europe")
plt.plot(salesByYear.index, salesByYear["Japan"], label="Japan")
plt.plot(salesByYear.index, salesByYear["Rest of World"], label="Rest of World")
plt.xlabel("Yıl")
plt.ylabel("Satış (Milyon Dolar)")
plt.title("Zaman İçinde Her Bölgede Toplam Satış")
plt.legend()
plt.show()


#Yayıncıya Göre Satış


publisherSales = df.groupby('Publisher')['Global'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(15,8))
plt.bar(publisherSales.index, publisherSales.values)

plt.xlabel('Yayıncı')
plt.ylabel('Toplam Satış')
plt.title('Yayıncıya Göre Satışlar')
plt.xticks(rotation=45)
plt.show()



#Oyun Türüne Göre Satış

genreSales = df.groupby('Genre')['Global'].mean().sort_values(ascending=False).head(10)


plt.bar(genreSales.index, genreSales.values)

plt.xlabel('Tür')
plt.ylabel('Ortalama Satış')
plt.title('Türe Göre Satışlar')
plt.xticks(rotation=45)

plt.show()


#PieChart Bölgenin satış oranı
salesByRegion = df[['North America', 'Europe', 'Japan', 'Rest of World']]

totalSales = salesByRegion.sum(axis=0)

plt.pie(totalSales, labels=totalSales.index)
plt.show()



#Aksiyon vs Adventur Oyun Satışı Yıla Göre

salesByYearAndGender = df.groupby(["Year", "Genre"]).sum()[["North America", "Europe", "Japan", "Rest of World"]]

actionSales = salesByYearAndGender.loc[salesByYearAndGender.index.get_level_values(1) == "Action"]
adventureSales = salesByYearAndGender.loc[salesByYearAndGender.index.get_level_values(1) == "Adventure"]

plt.plot(actionSales.index.get_level_values(0), actionSales["North America"], label="Action")
plt.plot(adventureSales.index.get_level_values(0), adventureSales["North America"], label="Adventure")
plt.xlabel("Yıl")
plt.ylabel("Satış (Milyon Dolar)")
plt.title("Action ve Adventure Türünün Yıla Göre Satış Kıyaslaması")
plt.legend()
plt.show()



