### django project

## Instalar django project

Opción #1 en debian

	sudo apt-get install virtualenv python-virtualenv

Opción #2 con pip *recomendado con pip*
	
	pip install virtualenv

#### Iniciar el entorno	
	virtualenv ENV
	cd ENV
	source bin/activate
#### Desactivar eL entorno
	deactivate
#### Instalar packeque en virtualenv en el entorno.
	pip install django
    sudo apt-get install virtualenv python-virtualenv
#### crear 
	virtualenv mi_proyecto
#### activar
cd mi_proyecto
source bin/activate
#### desactivar 
deactivate
#### instalar packeque en virtualenv
pip install django
#### crear proyecto:
django-admin.py startproject mysite
#### crear app:
cd mysite
django-admin.py startapp my_app




#### INSTALADOS POR PIP

	pip install django
	pip install cookiecutter # generador de plantillas
