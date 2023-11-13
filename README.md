# Proyecto Final - Design Patterns

## Integrantes Grupo 2.
+ Gisela Elizabeth Osorio Tibán
+ Luis Fernando Campos Sánchez

## Reserva de citas médicas
Aplicación de consola en python para la reserva de citas médicas, enfocado en los exámenes de laboratorio clínico.

## Diagrama de clases de dominio.
![Proyecto-Page-1 drawio](https://github.com/GissOsorio/proyecto-design-patterns/assets/17515471/f4edac7a-e047-4fa5-8a11-28646880b0a3)

## Patrones implementados y la justificación para usarlos 
+ Herencia entre Persona, Paciente y Apoderado
+ **Singleton** para leer el archivo de texto, generalmente no es necesario aplicar el patrón Singleton directamente, pero lo aplicamos para hacer la referencia como si fuese una base de datos.
+ **State** para los estados de la clase examen, por el momento hay dos estados, Nuevo y Guardado

## Clean Code y SOLID
+ Se hizo el uso de código claro e intuitivo además bloques pequeños de código que además nos ayudaran a la creación de unit test claros y funcionales. A continuación un ejemplo.

Código

```python
def es_fecha_futura(self, fecha_hora_examen):
	ahora = datetime.now()
	return fecha_hora_examen > ahora   
```

Unit Test

```python
def test_es_fecha_futura(self):  
	examen = Examen
	examen.horario_apertura = self.HORARIO_APERTURA_EARLY
	examen.horario_cierre = self.HORARIO_CIERRE_EARLY

	es_fecha_futura = examen.es_fecha_futura(examen, self.FECHA_HORA_EXAMEN)
	self.assertEqual(es_fecha_futura, False)     
```

## Cómo ejecutar el código en ambiente local
La forma más común de ejecutar los scripts de Python es usar la línea de comandos o la terminal. Veamos los pasos para ejecutar los scripts con Python.

+ Instalar Python desde la Microsoft Store, la version mas actual.
+ Abra su línea de comando o terminal.
+ Navegue hasta el directorio donde se encuentra su secuencia de comandos de Python.
+ Ejecute el script con el comando **python main.py** .

Hecho. Puede ver el resultado en la siguiente línea.
Puede ejecutar los scripts de Python con los pasos anteriores independientemente de su sistema operativo. Los pasos anteriores funcionan con todos los principales sistemas operativos.
En el caso de los **UnitTests**  es similar, ejecute el script que desee por ejemplo **python TestMain.py** o **python TestHorarioAtencionLaboratorio.py** .