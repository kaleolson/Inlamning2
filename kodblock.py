import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
#Importerarat: Länsstyrelsernas lokalytor och lokalkostnader fr o m 2017
#behövde encoda till latin-1 för att läsa filen
df = pd.read_csv(r"C:\Users\Karl1\Desktop\TUC\Data-Science2\Inlamning2-main\Inlamning2\Lanlokalkostnader.csv", sep=';', encoding='utf-8')

#Kollar om det är några rader som är null
print("Kolumner som har nullvärden:")
print(df.isnull().sum())
#kollar om det finns några nullvärden i kolumnen "Län"
print("isNull")
isNull = df["År"].isnull().sum()
print(isNull)

#Fyller i det år som saknades
df["År"] = df["År"].fillna(2019)
print(df.to_string)

#Skapa en pivot-tabell för att sammanställa värden
pivot_df = df.pivot_table(values="Summa lokalkostnader (kr)", index = "Län", columns = "År", aggfunc = "sum")

#Ändrar datan i kolumneran till float och gör om "," till "."
tempKol = [2017,2018,2019]
pivot_df[tempKol] = pivot_df[tempKol].apply(lambda x: x.str.replace(',', '.').astype(float))

#Tar fram skillnaden mellan 2017 och 2019 i en ny kolumn
pivot_df["Skilland mellan 2017 och 2019"] = round(pivot_df[2019.0] - pivot_df[2017.0])

print("Totala årskostnader på län i en pivot:")
print(pivot_df)   

#skapa en ny fil för pivot-datan. behövde använda utf-8-sig för att få fram svenska tecken
pivot_df.to_csv("Pivot_LanKostnader.csv",sep=';', encoding='utf-8-sig')

#skapa en ny fil för rensad data
df.to_csv("NyLanlokalkostnader.csv", index=False,sep=';', encoding='utf-8-sig')

