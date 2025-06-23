# ApiHealth

## Objectif

Il s'agit dun CLI ayant pour but de tester une liste d'endpoint d'une API.

## Comment l'utiliser 

### Prérequis 

- Verifier que `Python >= 3.1` est installé, sinon vous pouvez le télécharger [ici]("https://www.python.org/downloads/")
- Installer les dépendances en lançant la commande suivante 
```python
pip install -r requirements.txt
```

---
### Utilisé 

Crée un fichier *_txt_* contenant les adresses de vos APIs sous cette forme 
```txt
https://test.api/v2/endpoint1
https://test.api/v2/endpoint2
https://test.api/v2/endpoint3
https://test.api/v3/endpoint4
https://test.api/v1/endpoint12
```
Puis lancé le script en passant votre fichier *_txt_* comme argument 
```bash
python3 main.py api_list.txt
```
### Infos retournées

- Fonctionnelle
- Code de réponse 
- Temps de réponse
- Taille de la réponse 