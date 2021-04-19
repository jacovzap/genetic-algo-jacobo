
# ALGORITMO GENETICO 

Los Algoritmos Geneticos(AGs)son metodos adaptativos que pueden usarse para resolver problemas de busqueda y optimizacion. Estan basados en el proceso genetico de los organismos vivos. A lo largo de las generaciones,las poblaciones evolucionan en la naturaleza de acorde con los principios de la seleccion natural y la supervivencia de los mas fuertes, postulados por Darwin(1859). Por imitacion de este proceso, los Algoritmos Geneticos son capaces de ir creando soluciones para problemas del mundo real.La evolucion de dichas soluciones hacia valores optimos del problema depende en buena medida de una adecuada codificacion de las mismas.

## IMPLEMENTACION 

Se implemento un algoritmo genetico simple, con un metodo de seleccion por torneo, donde cada uno de los cromosomas consta de 20 genes y esta formado por 0s y 1s. Tomando como un fitness value la cantida de 1s en un cromosoma se obtuvieron los siguientes resultados:

### EJECUTANDO EL ALGORITMO 20 VECES

Se ejecuto el programa 20 veces para observar en que generacion se encontro por primera vez al cromosoma mas fuerte, el resultado que nos arrojo fue: 
> 6.4

### EJECUTANDO EL ALGORITMO SIN CROSSOVER 
Ejecutando el algoritmo con un crossover de 0 y una mutacion de 0.17, la media de generaciones para encontrar un cromosoma incremento a: 
> 39.9

### EJECUTANDO EL ALGORITMO SIN MUTACION
Ejecutando el algoritmo con un crossover de 0.7 y una mutacion de 0, la media de generaciones para encontrar un cromosoma fue: 
> 7.6
Sin embargo se pudo observar que sin la mutacion, rara vez algunos cromosomas no llegaban a alcanzar el cromosoma mas poderoso, ni otorgandoles ilimitadas generaciones

### PROBANDO CON DIFERENTES CONFIGURACIONES PARA CROSSOVER Y MUTACION 
* Pc = 0,9  Pm = 0.001  ==> 6.45
* Pc = 0,3  Pm = 0.001  ==> 12.5
* Pc = 0,5  Pm = 0.001  ==> 8.85
* Pc = 0,5  Pm = 0.005  ==> 7.35
* Pc = 0,1  Pm = 0.05  ==> 10.15

Podemos deducir que entre mas alta sea la probabilidad de crossover, menos generaciones se necesitara para resolver el problema

### PROBANDO CON DIFETENTES TIPOS DE CONFIGURACION 
Hasta el momento se habia trabajado con una poblacion de 100 cromosomas. Variando este numero obtenemos los siguientes resultados: 
Para Pc = 0,7  Pm = 0.001

* Poblacion: 50 ===> 18.55
* Poblacion: 100 ===> 6.45
* Poblacion: 150 ===> 5.65
* Poblacion: 200 ===> 5.35

Viendo los resultados podemos observar que entre mas grande sea la poblacion menos generaciones se necesitaran para resolver el problema, esto gracias a que por la aletoriedad y tamanio de la poblacion hay mas posibilidades de encontrar mejores cromosomas desde un inicio.

### PARA UNA POBLACION DE 100, GRAFICAR LA MEJOR, PEOR Y EL PROMEDIO DEL FITNESS FUNCTION

![Screenshot](https://lh3.googleusercontent.com/y4xj4s5aTYK3YOEkqL8spL_ildS0Rc2tWwmsmADmqaJ22PQsWXCoO6gQh3hiTwwRsFEG9SiV5nRqoHjYjuXtLW6JxHI8RhMIt2q2lNUcrYsHY7AE6zgy5YhVeExSGv3Fzk5TL7giSnRB69mRpP7WKK4-4kMhWpCGzPIIc5BcYM0zUcBR0h_FIHSl_wwcldolvj-gHDmWkfDFC2YVvIDEbFr_U1b1iauZ6JLdzBGOO-oLukmWjYAOJFQ2qljR9LIo-sTuTFur4t5YEdFSFYh0XJlDTA80RunW6fDid7wb1T4oJ7IFidklrO5Gyp1Ax8gvcRxFkqtyob9IsuQxYDjF35sXwVTbaJsKu_h7bT743DmJNEUpqt3dNDRDZTnOGpNzgySEIoODRXMILv4acALWblVOFdN-Asp1liUNkYKrIwgbCePPjPNcRLcbtmUd3i6QRkzCC0xkqIIaoDGZlCPfbJ4y_vyf9-xQOAWnni7MerAGr_f3PsOedFiAZ1P2R8yOThFgKUmjmsfmNuojDWhBRFAuGFAs1sSvLXA10yLw6XoQeRuWebn3rIMWhvI_H1PdKSJf-8F2LKybthuXFMSszHiNGXEoARn3HOxMUOOYKaNTXCCrEuB_BrR3Di6nzdudG2J_z_c_6q2QuLw5PyV7OQyQf7yW9q9A5J_VAHbfAfmdvZvZNv-Zkt8t2FGXBL_WkxWBn5nHMDsPSmwOCcAVnMch=w1161-h892-no?authuser=0)
Format: ![Alt Text](url)

Todos los cromosomas convergieron en supercromosomas en la generacion 17

## POROTOS:
Se programo una funcion que pudiese encontrar el cromosoma mas poderoso donde los genes de este no estuviesen comprendidos por 0s y 1s sino, en un rango de numeros del 1 al 9. Para solucionar este problema se programo un fitness_function mas discriminativo, bajo la formula:

> fitness_value = Sumatoria(10 - gen.value) / 9

Esto se hizo con el motivo de que el valor del fitness de una supercromosoma iguale a 20, al igual que una supercromosoma binaria, de este modo, se podrian reutilizar algunas funciones.

Ejecutando el codigo 20 veces obtuvimos los siguientes resultados:
Para Poblacion: 100, Pc: 0.7, Pm = 0.001

> [204, 178, 357, 243, 297, 179, 133, 144, 235, 284, 463, 498, 148, 325, 274, 279, 132, 250, 269, 316]

dando un promedio de 260.4

### PARA UNA POBLACION DE 100, GRAFICAR LA MEJOR, PEOR Y EL PROMEDIO DEL FITNESS FUNCTION

![Screenshot](https://lh3.googleusercontent.com/hJoxVN3nUSXBWfOtkkAeUJIn36cp6VhK6i6dNE3zW6LQUSnsjXyMDuVHMC6kN22A-b40LE6fXtyXYNR0SvDd7-A4VEAE5ju6FNukrunM0EEAw7qC-jxbu0G_ONZxBWoWVxYh6TkzmCk_zPiKg0xatw-TEwz0o7mztI5OglhYii-NFlTMt-g7XQR5jwypqw3fgHQbaGwsSmvLDxHjIaxOnQcgttJKTeEFIBNC872SdDljiSFVZDWXDVDBUHzNtcw_rUHSX7Iypp_Y7w618u6IoqTZgJFii9RU5FVUA2a8mzPeUxP0HqRZDBWkLvUSr92vv9qz3CV5fdPlqSPFIfFybl3ETqAHxaIsO_Lpsg3ghHL9jvaqWwyjR4WKLtspIbD8n2Zrop9AnB0-CQ_PCkVAf391MAtSynFDG8uKZe-7nvotBEVTyhPmRwjpnBmaPZ8oirrOHfX5lIzbN_koRstVLRylD6bi2dOGPdSYw2sRsV3_G6A8fyASr9zY_n2xvtuVfPB22bqvVRRj0uUKKrW_KfiiJQUKRX_Nt6SaeLvYM7tHxxi65DicxQIHulBrDvRk-Ds5lfbFK6Kp-RvONpDzbGYSrCL7BI1_OPzCP21UlIH6-xbrkpvrnr8B6FkZ1-VNYMGh5GXQxxKCdAh71z4_4Agdd_2W_TxyMfChWeZ4wQ-DJvjpXXNm8jS30P893Cb7x-gXgJHcLqxwcdFUWVd8iZmN=w1193-h890-no?authuser=0)
Format: ![Alt Text](url)

Todos los cromosomas convergieron en supercromosomas en la generacion 276

## REQUIREMENTS 
> Se recomienda tener instalada la version 3 de python

## EXECUTE 
> python3 main.py

