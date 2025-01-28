import pandas as pd
#Importerarat: Länsstyrelsernas lokalytor och lokalkostnader fr o m 2017
#behövde encoda till latin-1 för att läsa filen
df = pd.read_csv(r"C:\Users\Karl1\Desktop\TUC\Data-Science2\Lanlokalkostnader.csv", sep=';', encoding='utf-8')

#print("The DataFrame :")
#print(df.head()) 

#print(df["residens (m2)"]) 

#df["Total Sales"] = df["`Lokalkostnader (kr)`"] / df["`Kontorslokalyta (m2)`"]
""" print("isNull")
isNull = df["A"].isnull().sum()
print(isNull) """

#df.dropna(inplace=True)
#new_df = df.dropna()
df["Län"].fillna("K", inplace = True)
print(df.to_string)

#df.to_csv("NyLanlokalkostnader.csv", index=False,sep='|', encoding='latin-1')