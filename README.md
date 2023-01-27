# TP 1 - Construire un crawler minimal
EVAIN Manon 

## Éxecuter le code permettant d'enregistrer le fichier avec les url visités. 

#### 1. Cloner le dépot Git
Dans l'éditeur de code de votre choix, ouvrez le dossier dans lequel vous souhaitez enregistrer les fichiers pour le TP.  
Ouvrez par la suite un terminal. 

Vous pouvez alors écrire la ligne de code suivante :  

``git clone https://github.com/evainmanon/IndextationWeb-TP2.git``

#### 2. Exécuter le fichier main
Afin d'exécuter le fichier, c'est à dire d'obtenir un fichier texte comportant la liste des 50 sites trouvés grâce au crawler.  

Pour cela, vous pouvez écrire dans le terminal la ligne de code suivante : 

``python3 main.py``

*Les changements de paramètres* 
Afin d'exécuter ce crawler, vous pouvez faire le choix de changer deux paramètres. Ces derniers se trouvent dans le fichier main.py.   
- *file_json_url* : Ce paramètre permet de donner le nom du fichier json contenant les différentes url à parcourir pour lequelle vous souhaitez obtenir l'index. Afin que l'éxécution du fichier **main.py** fonctionne, vous devez déposer le fichier .json dans le dossier du projet auparavant.   
- *number_of_docs* : Ce paramètre permet de déterminer le nombre de documents pour lesquels vous souhaitez avoir l'index. Si vous souhaitez avoir N documents, l'index se fera sur les N premiers documents du fichier .json. Si le fichier possède moins de N documents, l'exécution du fichier **main.py** vous indiquera un message d'erreur contenant le nombre d'urls contenues dans le fichier.json.

## Explication du code

#### 1. Architecture du code 
Le code est divisé en deux dossiers. un dossier *Index* qui contient l'ensemble des fichiers relatifs au fonctions permet de créer l'index. Le second dossier est le dossier *Tests*. Il permet de tester les fonctions présentent dans le fichier *Index*

#### 2. Explication des choix réalisés
Lors de l'exécution du fichier **main.py**, vous allez avoir dans votre dossier l'apparition de trois nouveaux fichiers .json.   
- **metadata.json**  : Ce fichier contient l'ensemble des données statistiques importantes concernant l'Index et les documents présent dans le fichier.json initiale.   
- **title.non_pos_index.json** : Ce fichier contient l'index non positionnel pour les deux paramètres indiqués dans le fichier **main.py**.   
- **title.non_pos_index.json** : Ce fichier contient l'index positionnel pour les deux paramètres indiqués dans le fichier **main.py**.   

Les exemples de ses trois fichiers sont présents dans ce projet, ils ont été excécutés pour les paramètres suivants :   
- *file_json_url* : "crawled_urls.json"
- *number_of_docs* : 20