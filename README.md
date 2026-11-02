# 🐍 Python Learning Journey & Code Portfolio

¡Bienvenido a la documentación de mi ruta de aprendizaje en Python! Este repositorio contiene todos los proyectos, ejercicios y conceptos desarrollados a lo largo de los distintos módulos de formación. Cada módulo está diseñado bajo una temática específica para aplicar conceptos fundamentales y avanzados del lenguaje mediante problemas prácticos.

---

## 📑 Tabla de Contenido

1. [Módulo 00: Growing Code (Fundamentos de Python)](./Python_Module_00)
2. [Módulo 01: Code Cultivation (Programación Orientada a Objetos)](./Python_Module_01)
3. [Módulo 02: Garden Guardian (Gestión de Excepciones y Robustez)](./Python_Module_02)
4. [Módulo 03: Data Quest (Estructuras de Datos y Colecciones)](./Python_Module_03)
5. [Módulo 04: Data Archivist (Operaciones de Archivos y Streams)](./Python_Module_04)
6. [Módulo 05: The Codex (Entornos Virtuales, Entorno y Paquetes)](./Python_Module_05bis)
7. [Módulo 06: Code Nexus (Arquitectura Abstracta y Patrones de Diseño)](./Python_Module_06bis)
8. [Módulo 09: Cosmic Data (Validación de Datos con Pydantic v2)](./Python_Module_09)
9. [Estándares de Código y Herramientas](#estándares-de-código-y-herramientas)

---

## 🌿 Módulo 00: Growing Code (Fundamentos de Python)

**Temática:** Datos de huertos comunitarios (*Garden Data*).  
**Objetivo:** Dominar la sintaxis básica, control de flujo, funciones y tipado estático inicial.

### Conceptos Clave
- Entrada/Salida nativa (`input()`, `print()`).
- Conversión de tipos y operaciones aritméticas básicas.
- Control de flujo con condicionales (`if/elif/else`) y bucles (iterativos con `for`/`range` y recursivos).
- Anotaciones de tipos (`type hints`) e integración con `mypy`.

### Ejercicios Desarrollados
- **ex0 (`ft_hello_garden.py`)**: Introducción a la primera función Python de bienvenida.
- **ex1 (`ft_garden_name.py`)**: Manejo de entrada por teclado y formateo de cadenas.
- **ex2 (`ft_plot_area.py`)**: Cálculo del área de una parcela rectangular.
- **ex3 (`ft_harvest_total.py`)**: Suma y acumulado de cosechas diarias.
- **ex4 (`ft_plant_age.py`)**: Validación condicional de días para determinar madurez de cosecha.
- **ex5 (`ft_water_reminder.py`)**: Lógica condicional para alertas de riego.
- **ex6 (`ft_count_harvest_iterative.py` / `ft_count_harvest_recursive.py`)**: Comparación práctica entre enfoque iterativo y recursivo.
- **ex7 (`ft_seed_inventory.py`)**: Uso estricto de anotaciones de tipos (`seed_type: str`, `quantity: int`, `unit: str`) y metodos de cadenas (`capitalize()`).

---

## 🌻 Módulo 01: Code Cultivation (Programación Orientada a Objetos)

**Temática:** Gestión y simulación de un ecosistema de jardín digital.  
**Objetivo:** Comprender la estructura de programas, modularidad y los pilares de la POO en Python.

### Conceptos Clave
- Patrón `if __name__ == "__main__":` y shebang (`#!/usr/bin/env python3`).
- Definición de clases, atributos de instancia e instanciación.
- Encapsulamiento y ocultamiento de datos usando convenciones de visibilidad (atributos protegidos `_attribute`).
- Métodos de acceso y modificación (`getters`/`setters`) con validación de estado.
- Herencia simple y uso de `super()` para reutilización de código.
- Métodos estáticos (`@staticmethod`) y de clase (`@classmethod`).
- Clases anidadas (*Nested Classes*) para tracking y analítica interna.

### Ejercicios Desarrollados
- **ex0 (`ft_garden_intro.py`)**: Punto de entrada de un script y ejecuciones directas.
- **ex1 (`ft_garden_data.py`)**: Primera clase `Plant` y presentación ordenada de atributos.
- **ex2 (`ft_plant_growth.py`)**: Métodos `grow()` y `age()` para simular crecimiento temporal.
- **ex3 (`ft_plant_factory.py`)**: Constructor `__init__` parametrizado para instanciación rápida.
- **ex4 (`ft_garden_security.py`)**: Encapsulamiento de datos e imposición de restricciones (edades/alturas no negativas).
- **ex5 (`ft_plant_types.py`)**: Herencia especializada con subclases `Flower`, `Tree` y `Vegetable`.
- **ex6 (`ft_garden_analytics.py`)**: Integración avanzada con `@staticmethod`, `@classmethod`, subclase `Seed` y clase interna de estadísticas.

---

## 🛡️ Módulo 02: Garden Guardian (Gestión de Excepciones y Robustez)

**Temática:** Sensores agrícolas y pipelines de datos resilientes.  
**Objetivo:** Desarrollar software a prueba de fallos capaz de gestionar imprevistos en tiempo de ejecución.

### Conceptos Clave
- Bloques `try / except / else / finally` para manejo limpio de errores.
- Elevar excepciones explícitamente (`raise`).
- Jerarquía de excepciones integradas (`ValueError`, `TypeError`, `ZeroDivisionError`, `FileNotFoundError`).
- Creación de excepciones personalizadas heredando de `Exception`.
- Garantía de limpieza de recursos e invariantes mediante el bloque `finally`.

### Ejercicios Desarrollados
- **ex0 (`ft_first_exception.py`)**: Conversión segura de tipos al procesar temperaturas de campo.
- **ex1 (`ft_raise_exception.py`)**: Validación de rangos térmicos aceptables para plantas (0°C a 40°C) elevando excepciones.
- **ex2 (`ft_different_errors.py`)**: Captura diferenciada y múltiple de distintas excepciones del sistema.
- **ex3 (`ft_custom_errors.py`)**: Diseño de excepciones personalizadas de dominio (`GardenError`, `PlantError`, `WaterError`).
- **ex4 (`ft_finally_block.py`)**: Garantía de cierre de sistemas de riego mediante `finally` ante cualquier fallo.

---

## 🎒 Módulo 03: Data Quest (Estructuras de Datos y Colecciones)

**Temática:** Plataforma de analítica de videojuegos.  
**Objetivo:** Dominar la selección, uso eficiente y manipulación de las colecciones nativas de Python.

### Conceptos Clave
- Listas y paso de parámetros mediante CLI (`sys.argv`).
- Tuplas (inmutabilidad, empaquetado/desempaquetado y cálculo de distancias 3D).
- Conjuntos (`set`) y teoría de conjuntos (Unión, Intersección, Diferencia).
- Diccionarios (`dict`) para mapas clave-valor, procesamiento y agregaciones.
- Generadores (`yield`) y procesamiento diferido (*lazy evaluation*) con `next()`.
- Comprehensions de listas y diccionarios para transformaciones concisas y eficientes.

### Ejercicios Desarrollados
- **ex0 (`ft_command_quest.py`)**: Lectura e inspección de argumentos en la línea de comandos (`sys.argv`).
- **ex1 (`ft_score_analytics.py`)**: Procesamiento estadístico de puntuaciones enviadas por argumento (máximos, mínimos, promedios).
- **ex2 (`ft_coordinate_system.py`)**: Representación de coordenadas 3D con Tuplas y cálculo de distancia euclidiana con `math.sqrt`.
- **ex3 (`ft_achievement_tracker.py`)**: Análisis de logros entre jugadores usando operaciones de conjuntos (`union`, `intersection`, `difference`).
- **ex4 (`ft_inventory_system.py`)**: Gestión de inventario de juego, cálculo de porcentajes y análisis de abundancia usando Diccionarios.
- **ex5 (`ft_data_stream.py`)**: Flujos masivos de eventos en tiempo real utilizando funciones generadoras (`yield`).
- **ex6 (`ft_data_alchemist.py`)**: Filtrado y transformación rápida de datos con *List* y *Dict Comprehensions*.

---

## 📜 Módulo 04: Data Archivist (Operaciones de Archivos y Streams)

**Temática:** Preservación digital en los *Cyber Archives*.  
**Objetivo:** Dominar el ciclo de vida de archivos, streams I/O y Context Managers.

### Conceptos Clave
- Apertura, lectura y escritura de archivos (`open()`, `read()`, `write()`, `close()`).
- Redirección e interacción con Streams Estándar (`sys.stdin`, `sys.stdout`, `sys.stderr`).
- Vaciado de búfer con `io.flush()`.
- Manejo seguro de archivos y prevención de fugas de recursos usando Gestores de Contexto (`with`).

### Ejercicios Desarrollados
- **ex0 (`ft_ancient_text.py`)**: Recuperación y lectura segura de archivos de texto en disco.
- **ex1 (`ft_archive_creation.py`)**: Transformación e inserción de caracteres de preservación (`#`) guardando en un nuevo archivo.
- **ex2 (`ft_stream_management.py`)**: Canalización explícita de errores a `sys.stderr` e interacción sin usar `input()`.
- **ex3 (`ft_vault_security.py`)**: Encapsulamiento de operaciones I/O dentro de la función `secure_archive()` con la sentencia `with`.

---

## 🧪 Módulo 05: The Codex (Entornos Virtuales, Entorno y Paquetes)

**Temática:** El laboratorio del Alquimista (Toolchain de desarrollo en Python).  
**Objetivo:** Crear proyectos reproducibles, gestionar dependencias, configurar con variables de entorno y dominar la empaquetación e importación en Python.

### Conceptos Clave
- Entornos virtuales (`venv`) e insulación de paquetes.
- Gestión de dependencias con `pip` (`requirements.txt`) y `Poetry` (`pyproject.toml`).
- Carga de secretos y variables de entorno usando `.env` y `python-dotenv`.
- Estructura de paquetes Python con `__init__.py` y control de exposición de módulos.
- Importaciones absolutas vs. relativas.
- Detección y resolución de dependencias circulares (*Circular Imports*).

### Ejercicios Desarrollados
- **ex0 (`construct.py` / `loading.py`)**: Detección de entorno virtual y carga comprobada de librerías externas (`pandas`, `numpy`).
- **ex1 (`oracle.py`)**: Lectura dinámica de configuración por entornos de desarrollo/producción evitando credenciales en código.
- **ex2 (`alchemy/`)**: Configuración de un paquete básico e interfaz de exportación restringida vía `__init__.py`.
- **ex3 (`alchemy/potions.py`, `transmutation/`)**: Resolución de importaciones anidadas, absolutas y relativas dentro de subpaquetes.
- **ex4 (`grimoire/`)**: Demostración y prevención de colapsos por importaciones circulares (`light_spellbook` vs `dark_spellbook`).

---

## ⚡ Módulo 06: Code Nexus (Arquitectura Abstracta y Patrones de Diseño)

**Temática:** Motor de procesamiento de datos y simulador de combate cibernético.  
**Objetivo:** Aplicar principios avanzados de POO, clases abstractas, tipado estructural y patrones de diseño orientados a la mantenibilidad.

### Conceptos Clave
- Módulo `abc`: Clases Base Abstractas (`ABC`) y decorador `@abstractmethod`.
- Polimorfismo por subtipado e interfaces comunes.
- Tipado estructural (*Duck Typing*) usando `typing.Protocol`.
- **Patrón Abstract Factory:** Separación del código del cliente de las clases concretas instanciadas.
- **Interfaces de Capacidad (*Capabilities*):** Adición de habilidades componibles fuera de la jerarquía principal.
- **Patrón Strategy:** Selección e intercambio dinámico de algoritmos/comportamientos en tiempo de ejecución.

### Ejercicios Desarrollados
- **ex0 (`data_processor.py`)**: Definición de la interfaz `DataProcessor` y sus implementaciones (`NumericProcessor`, `TextProcessor`, `LogProcessor`).
- **ex1 (`data_stream.py`)**: Procesamiento polimórfico de listas con múltiples tipos heterogéneos en tiempo de ejecución.
- **ex2 (`data_pipeline.py`)**: Sistema de plugins exportadores con `ExportPlugin(Protocol)` para CSV y JSON.
- **ex3 (`battle.py` / `capacitor.py` / `ex3/`)**: Sistema de entidades abstractas (`Creature`), capacidades externas (`TransformCapability`) y factorías (`FlameFactory`, `TransformCreatureFactory`).
- **ex4 (`tournament.py` / `ex4/`)**: Implementación del patrón Estrategia (`BattleStrategy`, `NormalStrategy`, `AggressiveStrategy`) para definir conductas de combate.

---

## 🚀 Módulo 09: Cosmic Data (Validación de Datos con Pydantic v2)

**Temática:** Observatorio de Datos Cósmicos.  
**Objetivo:** Dominar el modelado, parseo, coerción y validación rigurosa de datos en Python moderno utilizando Pydantic v2.

### Conceptos Clave
- Modelado declarativo heredando de `pydantic.BaseModel`.
- Restricciones de campos y metadatos con `pydantic.Field` (longitudes, rangos, valores por defecto).
- Coerción automática de tipos (ej. strings ISO a `datetime`).
- Validaciones personalizadas a nivel de modelo completo con `@model_validator(mode='after')`.
- Tipos enumerados (`enum.Enum`) en modelos de datos.
- Modelos anidados (*Nested Models*) y listas de modelos.

### Ejercicios Desarrollados
- **ex0 (`space_station.py`)**: Modelo `SpaceStation` con restricciones de rangos, opcionales y tipos fecha/hora.
- **ex1 (`alien_contact.py`)**: Modelo `AlienContact` usando Enums y validaciones personalizadas avanzadas con `@model_validator` para reglas intercampo.
- **ex2 (`space_crew.py`)**: Gestión de misiones espaciales (`SpaceMission`) con tripulación anidada (`CrewMember`), aplicando reglas de seguridad estrictas según rango y duración.

---

## 🛠️ Estándares de Código y Herramientas

A lo largo de todo el desarrollo se han aplicado los estándares oficiales de calidad de código en la comunidad de Python:

- **Estilo de Código:** Cumplimiento estricto de **PEP 8** validado mediante la herramienta `flake8`.
- **Análisis Estático de Tipos:** Verificación continua de tipos con `mypy` sin advertencias ni errores.
- **Compatibilidad:** Código escrito exclusivamente para **Python 3.10+**.
- **Control de Versiones:** Estructura modular preparada para despliegues profesionales y repositorios limpios sin archivos temporales (`.gitignore` correctamente configurado).

---
*Documentación generada para resumir los aprendizajes prácticos y la evolución arquitectónica en la ruta de desarrollo en Python.*
