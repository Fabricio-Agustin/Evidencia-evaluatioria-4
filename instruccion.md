# Estructura del Proyecto

```text
evidencia-evaluatoria-4/
│
├── main.py
│
├── test/
│   ├── __init__.py
│   └── test.py
│
└── README.md
```

---

## Encender Motor

Permite iniciar el motor del helicóptero verificando que no se encuentre previamente encendido.

## Despegar

Permite realizar el despegue si:

* El motor está encendido.
* Existe combustible suficiente.

## Volar

Permite incrementar la velocidad y altitud del helicóptero consumiendo combustible.

## Aterrizar

Permite regresar el helicóptero a tierra reduciendo la altitud y velocidad.

## Apagar Motor

Permite apagar el motor únicamente cuando el helicóptero se encuentra en tierra.

---

# Programación Orientada a Objetos

La clase `Helicoptero` implementa:

## Encapsulamiento

Los atributos se encuentran protegidos mediante el uso de atributos privados:

```python
self.__marca
self.__modelo
self.__combustible
self.__altitud
self.__velocidad
self.__motor_encendido
```

## Métodos Privados

```python
__tiene_combustible()
__consumir_combustible()
```

## Método Especial

```python
__str__()
```

Permite mostrar el estado actual del helicóptero de forma legible.

---

# Requisitos

* Python 3.10 o superior

Verificar instalación:

```bash
python --version
```

---

# Ejecución del Programa

Desde la raíz del proyecto ejecutar:

```bash
python main.py
```

Se mostrará el menú interactivo del sistema.

---

# Ejecución de Pruebas

El proyecto incluye pruebas unitarias desarrolladas con `unittest`.

Ejecutar:

```bash
python -m unittest discover -s test
```

Ejemplo de salida:

```text
........
----------------------------------------------------------------------
Ran 8 tests in 0.001s

OK
```

---

# Tecnologías Utilizadas

* Python
* unittest
* Git
* GitHub

---

# Autor

Agustín Gibaut

Trabajo práctico realizado para la Evidencia Evaluatoria N° 4 correspondiente al Módulo Programador de la carrera Desarrollo de Software del Instituto Superior Politécnico de Córdoba (ISPC).
