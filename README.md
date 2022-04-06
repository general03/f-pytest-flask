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
