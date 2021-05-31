import pandas

db = pandas.read_csv("SalaryData.csv")

y = db['Salary']

x = db['YearsExperience'].values.reshape(30,1)

from sklearn.linear_model import LinearRegression

mind = LinearRegression()

mind.fit(x,y)
print("............Welcome.........")
years=input("Enter Experience of Person(in years): ")
print("Salary: " ,mind.predict([[float(years)]]))
