Langues / Languages README:  
Si le texte est écrit normalement : Français  
*If the text is written in italic : English*
____
# GRANDPY BOT, the grandpa robot (French)

Grandpy-bot est une application simulant un robot grand-père. Posez lui
des questions sur des lieux, des personnages ou bien d'autre choses encore et
il vous répondera.  
PS: SI vous lui posez une question sur un lieu et que ce dernier a assez de
notoriété, il vous affichera même une carte !  

Ce projet est en Français et fonctionne avec l'API Française de wikipedia et l'api Javascript de Google Maps.
____
*Grandpy-bot is an app simulating a Grandpa robot. You can ask him question about places, characters or lot of other stuff and he will answer you.*  
*PS: If you ask him a question about a place and the place have enought notority, he will even diplay you a map!*  

*Project in french and working with French wiki API and the Javascript API of Google Maps*  
____
## Enjoy the app online on Heroku ;-)

https://grandpy-bot-6889.herokuapp.com

____
## On local Machine:

- Assurez vous d'avoir python 3 et pip installé sur votre machine
- Clonez ce dépôt sur votre Machine locale
- Installez et initialisez pipenv
- Renseigner votre Clé API Google maps Javascript en variable d'environnement "API_KEY = votre_clé" dans votre fichier .env
- Lancer le shell de pipenv
- Exécutez main.py
- Ouvrer votre navigateur et rendez vous à 'http://localhost:5000/'
___
- *Make sure you have python 3 and pip installed on your machine*
- *Fork this repository on your local machine*
- *Install and init pipenv*
- *Put in your API Key of Google maps Javascript in the .env file this way : "API_KEY = your_key"*
- *Init the pipenv shell*
- *Run main.py*
- *Open your favorite explorer and go to Url 'http://localhost:5000/'
____
## Commands :

Installer pipenv / *install pipenv* :
``` py -m pip install pipenv ```

Installer toutes les dépendances du projet / *Install all requirements of the project* :
``` py -m pipenv install ```

Lancer le shell pipenv / *init the pipenv shell* :
``` py -m pipenv shell ```
___
#### Packages used :

[packages]
flask = "*"
gunicorn = "*"
requests = "*"

[dev-packages]
pytest = "*"
flake8 = "*"
flask-testing = "*"
blinker = "*"

[requires]
python_version = "3.9"


