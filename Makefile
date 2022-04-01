start:
	gunicorn -b 192.168.0.92:5000 app:app

dev:
	flask run
