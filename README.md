# exploration de données

¡Bienvenido!

Este es mi proyecto final para la materia de mineria de datos

## Lenguajes

* Python3
* JavaScript
* CSS
* HTML

## Librerias

* Flask
* Material icons
* Sass

### Flask

[Flask](https://flask.palletsprojects.com/en/1.1.x/)  es un marco de aplicación web WSGI ligero. Está diseñado para que la puesta en marcha sea rápida y sencilla, con la capacidad de escalar a aplicaciones complejas.

#### Instalación Flask

>pip install flask

#### Ejecucion

>flask run  

### Sass

[Sass](https://sass-lang.com/) es un preprocesador de css que nos ayudara a construir de manera mas rapida y eficiente los estilos de la pagina.

#### Instalación Sass

> sudo npm install -g sass

#### Compilado

Un solo archivo
> sass static/styles/scss/main.scss  static/styles/css/main.css

Compilado de varios archivos
> sass --watch /static/styles/scss:static/styles/css

#### Creacion de hojas de estilos

Cada archivo nuevo se debera crear en styles/scss en su respectiva carpeta con la extension .scss se creara un archivo conocido como partial ejemplo `_styles.scss` empezando el nombre con guion bajo.

> nota: despues de crear el partial se importa en el archivo main.scss ejemplo `@import 'styles'`

### Material Design

[Material Design](https://material.io/resources/icons/?icon=query_builder&style=baseline) Material design es una normativa de diseño en esta ocasion solo usaremos los iconos que nos proporciona.

es tan facil de usar que solo tendras que copiar el codigo del icono que quieras usar:

> < span class="material-icons">
android
< /span >
