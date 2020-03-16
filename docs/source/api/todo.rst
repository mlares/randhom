***********
To do list
***********



ideas a desarrollar
===================

"diseñar" tests.  Idealmente tienen que atacar una cuestión en particular y descartar de a un problema a la vez.

Por ejemplo:

si le doy de entrada todos archivos iguales, me tiene que dar un número la media (fijo, o que puede ser conocido) y cero la varianza
si reemplazo la simu (que tiene un espectro dado) por un random, me tiene que dar la 2PCF=0
ese es fácil, pero hay que pensar tests más interesantes (y más difíciles para que se nos ocurran).  
La idea es que la implementación sea fácil.  Otra cosa es ir pensando tests de visualización, por ejemplo:
graficar la xi(r) calculada para diferentes cajas (o densidades) junto con la "xi_true"
Vayamos armando listas de estas cosas, y después vamos atacando de a una.    Mi idea es hacerlo
bien sistemático para ya no tener dudas (las dudas ya se llevaron mucho tiempo).  

Hay que identificar claramente los pasos (bueno, yo sobre todo)
y producir check tests que permitan ir validando cada paso.  Si hay un error, puede estar desde la generación de los
randoms hasta el plot de la varianza.  Lo podríamos normalizar así: (corregime)
generar los randoms con el método X

-calcular las 2PCF (nbodykit)
-calcular los multipolos
-calcular las medias y las varianzas (sd.py)

y luego los tests:

-T1. (cómo se puede probar esto?)
-T1-2. antes de calcular la 2PCF, graficar un slice de los randoms para ver cómo lucen
-T2-3. visualizar las 2PCF y compararlas con la xi_true
-T3-4.   :-? ...
-T4-5. poner el mismo file repetido
-T5. graficar todos los multipolos, la media y la SD como banda de error



Team work  
=========

- Organizar códigos.   Tratar de armar un solo repositorio, e ir
  poniendo los códigos "limpios" en *randhom*


Development
===========

- Complete documentation: it is generated automatically from
  metacomments, using Sphinx.


  Asserts:

  * What to do is data files are missing
  * Prevent variable overflows and division by zero

  
  
TOX
===

Use `TOX <https://tox.readthedocs.io/en/latest/>`_ to:


 * check if package installs correctly with different Python versions and interpreters
 * run tests in each of the environments
 * act as a frontend to Continuous Integration servers (TRAVIS)
  

