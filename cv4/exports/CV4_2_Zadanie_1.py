#%% md
# ## Zadanie 1 (5b)
# 
# V tomto zadaní budete pracovať s datasetom Heart Failure Clinical Records, ktorý obsahuje záznamy pacientov so zlyhaním srdca, zozbierané počas obdobia ich sledovania.
# 
# Dataset je dostupný online: https://archive.ics.uci.edu/dataset/519/heart+failure+clinical+records
# 
# Na stránke nájdete aj doplňujúce informácie o premenných, ktoré dataset obsahuje. (Odporúčam prečítať :) )
# 
# **Body dostanete za odpovede na zvýraznené otázky**
# 
#%% md
# ### Úloha 1 (1b)
#%% md
# Načítajte dataset do premennej `data_hf`.
#%%
# TODO
#%% md
#    **Obsahuje dataset chýbajúce hodnoty (NA) ?**
#%% raw
# # TODO
#%% md
# **Aký typ majú vybrané premenné v datasete ? (numerické/kategorické)** (Ak by ste si pri niektorých premenných neboli istí, zdôvodnite svoju odpoveď.)
# 
# - age
# - anaemia 
# - high_blood_pressure
# - serum_sodium
# - death_event
#%% raw
# # TODO
#%% md
# **Obsahuje dataset duplicitné záznamy?**
#%% raw
# # TODO
#%% md
# ### Úloha 2 (1b)
# 
# Skúmajte premennú pohlavie ('sex'). Premenná je kódovaná hodnotami 0 a 1. ( 0 = žena, 1 = muž)
#%%
# TODO
#%% md
# **Koľko záznamov mužov a žien obsahuje dataset?**
#%% raw
# # TODO
#%% md
# **Koľko mužov a žien je nefajčiarov ? (0 = nefajčiar, 1 = fajčiar)**
#%% raw
# # TODO
#%% md
# ### Úloha 3 (1b)
# 
# Popíšte premennú vek ('age').
#%%
# TODO
#%% md
# **Aký je minimálny, maximálny a priemerný vek pacientov v datasete?**
#%% raw
# # TODO
#%% md
# **Z akého veku je v datasete najviac záznamov?**
#%% raw
# # TODO
#%% md
# ### Úloha 4 (1b)
# 
# Pridajte do datasetu novú premennú s názvom `risk`, ktorá bude predstavovať riziko úmrtia pacienta po zlyhaní srdca. Táto premenná bude kategorická a bude obsahovať hodnoty 'Low' a 'High'. 
# Premennú vytvorte na základe if-else rozhodovania podľa premenných 'age' a 'serum_creatinine':
# 
# - Ak je vek pacienta väčší ako 50 a zároveň level kreatinínu v krvnom sére ('serum_creatinine') je väčší ako 1.2 mg/dL, tak hodnota premennej 'Risk' je 'High'.
# - V opačnom prípade je hodnota 'Low'
# 
# Hint: môžete použiť metódu `apply` na vytvorenie novej premennej, v ktorej použijete lambda funkciu na definovanie podmienok.
#%%
import matplotlib.pyplot as plt
# Add the 'risk' variable
data_hw['risk'] = data_hw.apply(lambda row: 'High' if row['age'] > 50 and row['serum_creatinine'] > 1.2 else 'Low', axis=1)

# Visualize high risk by age


high_risk = data_hw[data_hw['risk'] == 'High']
plt.hist(high_risk['age'], bins='auto')
plt.title('High Risk by Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
#%% md
# Vizualizujte vysoké riziko úmrtia pre jednotlivé vekové skupiny histogramom:
# 
# Hint: Použite metódu `hist` z knižnice `matplotlib.pyplot` na vizualizáciu distribúcie veku pre pacientov s vysokým rizikom úmrtia.
#%%
# TODO
#%% md
# **V akom veku je riziko zlyhania srdca najväčšie?**
#%% raw
# # TODO
#%% md
# **Koľko záznamov (približne) je v datasete v tejto vekovej kategórii?**
#%% raw
# # TODO
#%% md
# ### Úloha 5 (1b)
# 
# Analyzujte koreláciu medzi všetkými atribútmi tohto datasetu (napr. vytvorením correlation plot)
# 
# Hint: Nenumerické atribúty môžete pred vytvorením korelačnej matice odstrániť.
# 
#%%
# TODO
#%% md
# **Ktoré atribúty majú medzi sebou najväčšiu zápornú koreláciu?** (uveďte prvé dve dvojice)
#%% raw
# # TODO
#%% md
# **Ktoré atribúty majú medzi sebou najväčšiu kladnú koreláciu?** (uveďte prvú dvojicu)
#%% raw
# # TODO
#%% md
# ----
# 
# Viac informácií o zlyhaní srdca: https://www.nhlbi.nih.gov/health/heart-failure