
## Exercices


### Analyse des correspondances (AFC ou FCA en anglais et ACM ou MCA en anglais)


1. Analyse factorielle des correspondances
    1. Utilisez la commande suivante pour importer les données

        ```
import pandas as pd

import os # un package qui permet facilement d'accéder à des fichiers

data_dir = os.path.join('C:/Users/charl/OneDrive/Documents/jedha/full_time_exo/S4/student_data')
file = os.path.join(data_dir,'student-mat.csv')
data = pd.read_csv(file, sep = ';')
```


    2. Sélectionnez deux variables explicatives qualitatives dont vous souhaitez analyser les correspondances
    3. Créer un objet T qui contient le tableau de contingence des deux variables qualitatives choisies grâce à la commande `pd.crosstab`
    4. Créez un objet x1_freq et un objet x2_freq qui contiennent respectivement la fréquence d’apparition des modalités de x1 et des modalités de x2 (où x1 et x2 sont simplement des noms qu’on donne aux variables choisies) grâce à la fonction pd.value_counts
    5. Utilisez la fonction `pd.DataFrame` et grâce à ses arguments index et columns remettez dans le même ordre les index et colonnes le tableau de contigence et x1_freq et x2_freq dans un objet que vous appelerez T_sort
    6. Créez une matrice diagonale Dx1 à partir de x1_freq et une matrice Dx2 diagonale à partir de x2_freq `np.diag`
    7. Créez une matrice <img src="https://latex.codecogs.com/svg.latex?\Large&space;A=\frac{1}{n}T^{T}D_{X_{1}^{-1}" /> et une matrice <img src="https://latex.codecogs.com/svg.latex?\Large&space;B=\frac{1}{n}TD_{X_{2}^{-1}" />

 avec n le nombre d’observations, à l’aide des fonctions `np.transpose` `np.linalg.inv` et `np.matmul`
    8. Importez la fonction PCA
    9. Estimez une PCA pour la matrice AB et la matrice BA
    10. Analysez les composantes principales
2. Multiple Correspondance Analysis
    11. On utilise aussi les même données
    12. Supprimez les variables quantitatives du dataset
    13. Utilisez la fonction pd.get_dummies pour créer le tableau disjonctif complet que vous appellerez T
    14. Calculez <img src="https://latex.codecogs.com/svg.latex?\Large&space;B=T^{T}T" />

    15. Calculez le vecteur des fréquences pour chacune des variables grâce à la fonction pd.value_counts
    16. Concaténer tous les vecteurs de fréquences et créer un objet D
    17. Créer une matrice diagonale à partir du vecteur D
    18. Calculez la matrice <img src="https://latex.codecogs.com/svg.latex?\Large&space;\frac{1}{n}B\Delta^{-1}" />

    19. Trouvez les vecteurs propres de cette matrice et les valeurs propres, à quoi correspondent ces vecteurs et les valeurs associées?
