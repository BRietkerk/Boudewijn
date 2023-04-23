import numpy as np

"opzet"
# dichtheid koper (kg/m**3)
pm = 8960
#Young modulus (Pa)
E = 124e9 
#Hoogte van de veer (m)
hv = 1e-6
#Hoogte van de massa (m)
hm = 2e-6  
#Lengte van de veer (m)
lv = 196e-6 
#Lengte van de massa (m)
lm = 196e-6
# breedte veer = combo[0] 
# breedte massa = combo[1]

# vul alle constante waardes van de formule van de resonantiefrequentie apart in 
constante = 0.5/np.pi * np.sqrt((2*E*hv)/(hm * pm * lm * (lv)**3))

# genereer een lijst met alle mogelijke variaties van de breedte van de veer en de massa 
combinations = []
for i in range(1, 200):
    for j in range(i, 200):
        if i + i + j == 200:
            combinations.append((i, j))
  
# vul al de nogelijke combinaties van de breedte van de veer en de massa in in de formule van de resonantiefrequentie  
results = []
combo_results = {}
for combo in combinations:
    result = constante * np.sqrt((combo[0]* 1e-6)**3 / (combo[1]* 1e-6))  
    results.append(result)
    combo_results[result] = combo

# vind de laagste waarde van de resonatiefrequentie
min_result = min(results)
min_combo = combo_results[min_result]
print("de combinatie (breedte veer, breedte massa):", min_combo, "in micrometer, zorgde voor de laagste frequentie van", min_result,"Hz.")