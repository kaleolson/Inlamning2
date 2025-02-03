import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

pivot_df = pd.read_csv(r"C:\Users\Karl1\Desktop\TUC\Data-Science2\Inlamning2-main\Inlamning2\Pivot_LanKostnader.csv", sep=';', encoding='utf-8')


#Histogram över hur länkostnaderna är fördelade
plt.hist(pivot_df["Skilland mellan 2017 och 2019"], bins=10)
plt.xlabel("Skillnad mellan 2017 och 2019")
plt.ylabel("Antal län")
plt.title("Fördelning av skillnader")
plt.show()
#--------------------------------------------------------------------------------------------------------
#Linje diagram per län
# Välj ett län att visa
lan = "AB"  # Ändra detta för att välja ett annat län
lan_data = pivot_df[pivot_df["Län"] == lan]

#Välj vilka värden som ska visas på x-axeln
x_values = [2017,2018,2019]
# Skapa linjediagram
plt.plot([2017.0, 2018.0, 2019.0], lan_data.iloc[0, 2:])

plt.xlabel("År")
plt.ylabel("Värde")
plt.title(f"Utveckling av värden för län {lan} mellan 2017 och 2019")
plt.xticks(x_values) #visar x-värden som valdes innan 
plt.show()
#--------------------------------------------------------------------------------------------------------
#Scatterplot
län_namn = list(pivot_df.keys())
values_2017 = []
for l in län_namn:
    value = pivot_df[l][0]
    values_2017.append(value)

values_2019 = []
for l in län_namn:
    value = pivot_df[l][1]
    values_2019.append(value)

# Skapa scatterplot
plt.scatter(values_2017, values_2019, color='blue')

#Jag lyckades inte med att sätta 
# Lägg till etiketter för varje punkt
""" for i, namn in enumerate(län_namn):
    plt.text(values_2017[i]*1.01, values_2019[i]*0.99, namn, fontsize=9)
  """
plt.xlabel('Värde 2017')
plt.ylabel('Värde 2019')
plt.title('Scatterplot: Värden per län 2017 vs 2019')
plt.show()
