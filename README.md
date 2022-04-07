# Command

`export PYTHONPATH=$(pwd)`
`export FLASK_ENV=development`

`pipenv run flask run`

`pipenv run pytest -sv`

# Test

Ce projet mets en avance les tests suivants :

- mock
- feature
- vérification existance de l'app Flask
- vérification des paramètres GET
- multiple assert
- catégoriser les résultats (avec l'option `-m route` par exemple)
- gérer les exceptions (pensez à bien configurer flask `app.config['PROPAGATE_EXCEPTIONS'] = True`)
- exporter les données en HTML `pipenv run pytest --cov --cov-report=html`
- utiliser les plugins pytest (ex avec `pytest-cov`)

# Test de charge

En utilisant `Locust`, il faut simplement lancer la commande `pipenv run locust --locustfile=test/locust.py` et en écrivant le test dans `test/locust.py`