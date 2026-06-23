# Planificador de eventos de un Centro de Astrofísica
Este proyecto nace de una necesidad en los centros de investigación científica: la gestión óptima de activos escasos y de alto valor. En estos entornos, recursos como telescopios de última generación, salas de experimentación con condiciones controladas y, sobre todo, el tiempo de científicos de élite, son bienes limitados que deben asignarse con precisión milimétrica. La complejidad se multiplica al tener que encajar estas disponibilidades en una agenda densa de eventos, coloquios y sesiones de observación, donde cualquier solapamiento o error de planificación puede traducirse en meses de trabajo perdido y oportunidades científicas irrecuperables.

La solución propuesta no es una mera agenda electrónica, sino un sistema de validación algorítmica inteligente. Su núcleo reside en una lógica de razonamiento que actúa como un guardián digital, previniendo de forma automática cualquier conflicto horario y asegurando que cada asignación sea viable. Pero su verdadero valor añadido está en la comprensión profunda del dominio: no solo verifica disponibilidad, sino que aplica reglas técnicas complejas. Por ejemplo, garantiza que el Telescopio Lunar, un instrumento único, sea operado exclusivamente por la especialista acreditada en esta area de el estudio de la luna, o que las sesiones en la sala de conferencias existan los recursos necesarios. Además, el sistema gestiona restricciones lógicas sofisticadas, como los co-requisitos (eventos que deben realizarse en paralelo) y las exclusiones mutuas (experimentos incompatibles que no pueden coincidir). En definitiva, se trata de una herramienta que traslada la complejidad normativa del dominio científico a la lógica computacional, liberando a los investigadores de la carga burocrática y minimizando el riesgo de error humano en la planificación, para que puedan dedicar su valioso tiempo a lo que realmente importa: la ciencia.

## 📚 Tabla de Contenidos

* [🚀 Características Principales](#-características-principales)
* [📁 Estructura del Proyecto](#-estructura-del-proyecto)
* [🔧 Instalación y Ejecución](#-instalación-y-ejecución)
* [🎯 Dominio del Programa](#-dominio-del-programa)
* [⚙️ Funcionalidades Detalladas](#️-funcionalidades-detalladas)
* [⚠️ Validaciones y Restricciones](#️-validaciones-y-restricciones)
* [🛠️ Tecnologías Utilizadas](#️-tecnologías-utilizadas)

## 🚀 Características Principales <a id="-características-principales"></a>

### 🎯 Gestión Inteligente de Eventos:
* **Agregar eventos manualmente**: Permite programar eventos científicos especificando nombre, fecha/hora de inicio y fin, sala, y recursos necesarios.
* **Búsqueda automática de horarios**: Si no se conoce un horario disponible, el sistema encuentra el próximo hueco compatible automáticamente.
* **Visualización de eventos**: Muestra todos los eventos planificados con sus detalles completos (recursos, horarios, duración).

### 🔧 Validación Avanzada de Recursos
* **Detección de conflictos horarios**: Evita que un mismo recurso (científico, telescopio, sala) sea asignado a dos eventos simultáneos.
* **Verificación de reglas técnicas**: Implementa restricciones específicas del dominio astrofísico (ej: "Telescopio Lunar → Especialista en la Luna").
* **Validación de complementarios**: Asegura que ciertos recursos solo se usen con sus complementos requeridos (ej: ciertos telescopios requieren científicos específicos).
* **Validación de exclusiones**: Previene combinaciones prohibidas entre recursos (ej: científicos que no pueden trabajar juntos).

### 📊 Persistencia de Datos
* **Almacenamiento en JSON**: Los eventos y recursos se guardan en archivos Eventos.json y Recursos.json.
* **Carga automática**: Al iniciar la aplicación, se cargan todos los eventos y recursos previamente guardados.
* **Actualización en tiempo real**: Cualquier cambio (agregar/eliminar eventos) se refleja inmediatamente en los archivos JSON.

### 🎨 Interfaz Gráfica Intuitiva
* **Desarrollada con Kivy**: Interfaz moderna y responsive con botones, listas desplegables, popups y elementos visuales.
* **Selección visual de recursos**: Los científicos y telescopios se muestran con imágenes e información detallada.
* **Feedback inmediato**: Mensajes de error claros y descriptivos para entradas inválidas.
* **Navegación sencilla**: Dos vistas principales: "Agregar evento" y "Ver eventos".

## 📁 Estructura del Proyecto <a id="-estructura-del-proyecto"></a>

* A continuacion se muestra la estructura de carpetas y archivos del proyecto:

```text
│
├── 📁 datas/                    # Datos del sistema
│   ├── Eventos.json            # Json donde se almacenan los ecentos
│   └── Recursos.json           # Json que contiene los recursos con sus datos
│
├── 📁 Imagenes_Readme/         #Imagenes de este archivo
│
├── 📁 Imagenes/                 # Assets gráficos
│   ├── Boton_Persona.png
│   ├── Boton_Recurso.png
│   ├── Persona Seleccionada.png
│   └── ... (más imágenes)
│
├── 📁 modules/                  # Módulos del sistema
│   ├── __init__.py             # Inicialización de módulos
│   ├── Backend1.py             # ✅ LÓGICA PRINCIPAL: Contiende todas las funciones del programa
│   ├── Class_vent_Agregar_Evento.py  # Componentes de UI para agregar eventos
│   ├── Class_Vent_Recursos.py        # Componentes de UI para selección de recursos
│   ├── Imagenes.py                   # Rutas de las imagenes y informacion de los personajes y recursos
│   ├── Class_Vent_Ver_Eventos.py     # Componentes de UI para ver eventos
│   ├── Stile_principal.py            # Estilos para la ventana principal
│   ├── Stile_vent_Agregar_Evento.py  # Estilos para ventana de agregar evento
│   ├── Stile_Vent_Recursos.py        # Estilos para ventana de recursos
│   └── Stile_Vent_Ver_Eventos.py     # Estilos para ventana de ver eventos
│
├── main.py                     # ✅ ARCHIVO PRINCIPAL: Punto de entrada, interfaz gráfica completa
├── README.md                   # Este archivo
```

## 🔧 Instalación y Ejecución <a id="-instalación-y-ejecución"></a>
### Paso 1: Clonar el Repositorio en tu pc y entrar a la carpeta 
**Ejecutar:**
```bash
git clone https://github.com/AdanV06/Project-Gestor-de-eventos.git
cd Project-Gestor-de-eventos
```

### Paso 2: Crear un entorno virtual
**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**En Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
 ```
### Paso 3: Insalar Dependencias
 ***Ejecutar:***
```bash
pip install -r requirements.txt
```
### Paso 4: Ejecutar la Aplicación
**Ejecutar:**
```bash
python main.py
 ```
    
## 🎯 Dominio del Programa <a id="-dominio-del-programa"></a>

Este sistema está diseñado específicamente para centros de investigación en astrofísica, donde la coordinación de recursos especializados es crítica para el éxito de experimentos y observaciones científicas.

### Catálogo Completo de Recursos
#### 👨‍🔬 Científicos Especializados
| Nombre | Especialidad | Complementario | Exclusiones | Biografia Breve |
|--------|--------------|----------------|----------------|-----------------|
| Carl Sagan | Fenomenos del sol | Telescopio solar | No trabaja con Vera Rubin o Edwin Hubble | Reconocido divulgador científico y experto en comunicación astronómica. Su trabajo en la comprensión de la atmósfera solar ha sido fundamental. |
| Vera Rubin | Materia oscura y galaxias | Telescopio de Galaxias | No trabajar con Hans Bethe o Carl Sagan | Pionera en el estudio de la materia oscura, sus observaciones de curvas de rotación galáctica revolucionaron la astrofísica moderna. |
| Henrietta Leavitt | Óptica y estrellas variables | Polarímetro, Espectrómetro, Sala de óptica | Ninguna | Descubrió la relación período-luminosidad que permite medir distancias interestelares, base del trabajo de Hubble. |
| Edwin Hubble | Expansión del universo | Telescopio de Galaxias | No trabajar con Hans Bethe o Carl Sagan | Demostró que el universo se expande, estableciendo la base de la cosmología moderna. |
| Cleo Abram | Tecnología y planetarios | Planetario | Ninguna | Especialista en divulgación tecnológica y experiencias inmersivas en planetarios. | 
| Margaret Burbidge | Geologia Lunar | Telescopio Lunar | No trabajar con Stephen Hawking | Contribuyó fundamentalmente a la comprensión de la nucleosíntesis estelar y la formación de elementos. |
| Hans Bethe | Física solar | Telescopio solar | No trabaja con Vera Rubin o Edwin Hubble | Premio Nobel por sus contribuciones a la teoría de la formación de estrellas y la física nuclear. |
| Neil Tyson | Astrofísica general | Compatible con todos los telescopios | Ninguna | Astrofísico reconocido por su habilidad para comunicar conceptos complejos al público general. |
| Stephen Hawking | Agujeros negrosc| Telescopio de agujeros negros | No trabajar con Margaret Burbidge | Legendario físico teórico cuyos trabajos sobre radiación de Hawking y singularidades transformaron nuestra comprensión del cosmos. |

#### 🔭 Telescopios y Herramientas
| Recurso | Tipo | Cantidad | Especialidad Requerida | Descripcion |
|---------|------|----------|---------------------|------------------------|
| Telescopio Lunar | Telescopio | 1 | Especialista en Luna (Margaret Burbidge o Neil Tyson) | Instrumento óptico de alta precisión diseñado específicamente para la observación detallada de la superficie lunar |
| Telescopio de Galaxias | Telescopio | 1 | Especialista en galaxias (Vera Rubin, Neil Tyson, Edwin Hubble) | Potente telescopio reflector con un espejo primario de gran diámetro, optimizado para la observación de objetos extragalácticos. Permite estudiar la morfología, rotación y composición de galaxias a distancias de millones de años luz.|
| Telescopio solar | Telescopio | 1 | Especialista solar (Hans Bethe, Neil Tyson, Carl Sagan) | Equipo especializado con filtros de densidad neutra y sistemas de óptica adaptativa para la observación segura del Sol. Permite estudiar manchas solares, protuberancias, erupciones solares y la dinámica de la corona en diferentes longitudes de onda. |
| Telescopio de agujeros negros | Telescopio | 1 | Especialista en agujeros negros (Stephen Hawking o Neil Tyson) | Telescopio de rayos X y ondas gravitacionales diseñado para la detección y estudio de objetos compactos como agujeros negros y estrellas de neutrones. Su tecnología permite observar emisiones de alta energía provenientes de discos de acreción y chorros relativistas.|
| Telescopio de Rayos Gama | Telescopio | 1 | Sin requerimientos específicos | Instrumento especializado en la detección de rayos gamma procedentes de fenómenos astrofísicos violentos como supernovas, púlsares y núcleos galácticos activos. Utiliza tecnología de centelleo y sistemas de seguimiento rápido para captar explosiones de alta energía. |
| Radio Telescopio | Telescopio | 1 | Sin requerimientos específicos | Antena parabólica de gran apertura diseñada para captar ondas de radio procedentes del espacio. Permite estudiar fenómenos como la radiación de sincrotrón, máseres cósmicos y líneas de emisión de hidrógeno neutro (21 cm). Su versatilidad lo hace apto para múltiples líneas de investigación, desde el estudio del medio interestelar hasta la detección de exoplanetas.|
| Telescopio básico | Herramienta | 20 | Solo usable en Planetario o Sala de conferencias | Telescopio didáctico de tipo refractor con montura altacimutal simple, diseñado para fines educativos y divulgativos. Su apertura moderada permite observar objetos brillantes como la Luna, planetas principales y cúmulos estelares abiertos.| 
| Polarímetro | Instrumento óptico | 1 | Solo usable por Henrietta Leavitt | Instrumento de precisión que mide el grado y ángulo de polarización de la luz procedente de fuentes astronómicas. Fundamental para estudiar campos magnéticos en el medio interestelar, discos protoplanetarios y atmósferas estelares. |
| Espectrómetro | Instrumento óptico | 1 | Solo usable por Henrietta Leavitt | Dispositivo de alta resolución que descompone la luz astronómica en sus longitudes de onda constituyentes para analizar su espectro. Permite determinar la composición química, temperatura, velocidad y presión de objetos celestes. |
| Cámara estelar | Herramienta | 1 | Sin requerimientos específicos | Cámara CCD de alta sensibilidad diseñada para la captura de imágenes astronómicas con exposición prolongada. Equipada con filtros fotométricos estándar (UBVRI) que permiten realizar fotometría precisa de objetos variables y tránsitos exoplanetarios. |
| Portátiles | Herramienta | 20 | Solo usable en Planetario o Sala de conferencias | Solo usable en Planetario o Sala de conferencias	Equipos informáticos portátiles equipados con software especializado para el procesamiento y análisis de datos astronómicos. Incluyen aplicaciones para reducción de imágenes, análisis espectral y simulación de fenómenos astrofísicos.
| Gafas virtuales | Herramienta | 20 | Solo usable en Planetario o Sala de conferencias | Solo usable en Planetario o Sala de conferencias	Dispositivos de realidad virtual inmersiva que permiten experiencias tridimensionales de entornos astronómicos simulados. Facilitan la visualización de estructuras cósmicas en 3D, viajes virtuales por el sistema solar y la recreación de fenómenos astrofísicos. |

#### 🏛️ Salas de Experimentación
| Sala | Capacidad | Uso Principal | Especialista Requerido | Descripcion | 
|------|-----------|---------------|---------------------|---------------------|
| Planetario | 1 evento | Proyecciones y simulaciones | Cleo Abram | Sala inmersiva equipada con un proyector digital de última generación y una cúpula hemisférica de 360 grados. Permite recrear el cielo nocturno, simulaciones de vuelos espaciales y visualizaciones 3D de fenómenos astronómicos complejos. |
| Sala de óptica | 1 evento | Experimentos ópticos y calibración | Henrietta Leavitt | Laboratorio especializado con bancada óptica, fuentes de luz calibradas y equipos de precisión para experimentos de óptica astronómica. Está diseñada para la calibración de instrumentos como polarímetros y espectrómetros, así como para pruebas de componentes ópticos y simulaciones de sistemas telescópicos. | 
| Cúpula de fotografía | 1 evento | Fotografía astronómica | Ninguno | Estructura circular con apertura cenital que alberga equipos fotográficos profesionales para captura de imágenes astronómicas. Está equipada con monturas motorizadas que compensan la rotación terrestre, permitiendo exposiciones prolongadas sin arrastre estelar. Ideal para sesiones de astrofotografía de cielo profundo y documentación visual de fenómenos astronómicos. | 
| Sala de conferencias | 1 evento | Presentaciones y análisis de datos | Ninguno | Espacio versátil acondicionado con sistemas de proyección de alta resolución, pizarra interactiva y mobiliario modular adaptado a diferentes configuraciones. Está diseñada para albergar presentaciones científicas, sesiones de análisis de datos en grupo y discusión de resultados de investigación. |
| Cúpula de observación | 1 evento | Observación directa con telescopios | Ninguno | Estructura giratoria con apertura variable en el techo que alberga telescopios para observación directa del cielo. Su diseño permite un seguimiento continuo de objetos celestes a lo largo de la noche, minimizando la interferencia lumínica exterior. Ofrece un entorno protegido de las condiciones climáticas y contaminación lumínica. |

#### Ejemplo de Escenario Real

* "El evento 'Observación de Cráteres Lunares' requiere:
    * Telescopio Lunar (recurso único)
    * Margaret Burbidge (especialista en Luna)
    * Cúpula de observación (sala específica)
    * Cámara estelar (equipamiento complementario)
* El sistema debe verificar que:
    * Margaret esté disponible en ese horario
    * El Telescopio Lunar no esté asignado a otro evento
    * La Cúpula de observación esté libre
    * Margaret pueda trabajar con otros científicos asignados (si los hay)
    * Se cumplan todas las reglas técnicas del telescopio"

## ⚙️ Funcionalidades Detalladas <a id="️-funcionalidades-detalladas"></a>

### 🎫 1. Agregar Evento Manualmente
**Descripción**: En esta funcion se le piden los datos al usuario para conformar su evento especficando el nombre que desea ponerle al evento,la hora de inicio, la hora de fin, la sala para llevar acabo el evento, y los rcursos necesarios(como telescopios o cientificos), todos estos campos son de varavter obligatorios introducirlos, el saltarse uno de ellos mostrara un cartel diciendo el campo que falta por completar para poder guardar el evento correctamente. 

<img src="Imagenes_Readme/Ventana Agregar Evento.png">

**Flujo de uso:**
1. **Ingresar datos básicos:**
    * Nombre del evento (hasta 45 caracteres)
    * Fecha y hora de inicio (año, mes, día, hora, minutos)
    * Fecha y hora de finalización
    * Selección de sala (desplegable con 5 opciones)
2. **Seleccionar recursos:**
    * Personal científico: Botón con icono de persona → abre ventana con 9 científicos especializados
    * Herramientas/telescopios: Botón con icono de telescopio → abre ventana con 12 tipos de equipos
    * Recursos con cantidad: Para Gafas virtuales, Portátiles y Telescopio básico → pide cantidad específica
3. **Validación y guardado:**
    * Al presionar "Guardar" se validan todos los datos
    * Si hay errores → mensaje descriptivo en popup
    * Si todo es correcto → evento se guarda en Eventos.json

### 🔍 2. Buscar Horario Automático
Esta funcionalidad representa el núcleo inteligente del sistema, automatizando la tarea más compleja para los administradores de eventos.
**Descripción**: Encuentra el próximo hueco disponible para un evento, considerando todos los recursos solicitados.

**Flujo de uso:**
1. **Configurar evento básico:**
    * Ingresar nombre y seleccionar sala
    * Seleccionar recursos necesarios (científicos y herramientas)
2. **Especificar duración:**
    * Presionar "Buscar Horario" → popup pide horas de duración
    * Sistema calcula fecha/hora de inicio y fin
4. **Resultados:**
    * Si encuentra hueco → crea evento automáticamente

**Explicasion de la logica para lograr esta funcion:**
La funcion que se encarga de lograr esto se encuentra en el archivo **Backend1.py** llamada **buscar**, la logica que se sigue es la siguiente: 
1. Si no hay ningun evento agregado antes, se agrega el evento en el momento actual(ya que es el mejor horario disponible)
2. Si hay eventos lo que se hace es ordenarlos y guardarlos en una variable, aqui pueden haber dos casos, si hay un solo evento o si hay mas de uno. Si hay un unico abento se agrega en el momento actual, si da error se agrega justo despues del evento.
3. Si hay mas de un evento ya guardado, se intenta guardar en el momento actual, si da error, se itera en cada evento guardado y se intenta agregar justo cuando termine cada evento hasta que se logre encontrar un espacio disponible.

### 👁️ 3. Ver Eventos Planificados
**Descripción**: Muestra todos los eventos guardados en una lista interactiva.

<img src="Imagenes_Readme/Ventana Ver Eventos.png">

**Características:**
* **Lista scrollable**: Muestra todos los eventos verticalmente
* **Tarjetas informativas**: Cada evento muestra:
    * Nombre del evento
    * Fecha y hora de inicio/fin
    * Lista completa de recursos asignados (con cantidades)
* **Eliminación directa**: Botón de eliminar en cada tarjeta
* **Actualización en tiempo real**: Al eliminar, se actualiza Eventos.json inmediatamente

### 👥 4. Selección de Personal Científico
**Descripción**: Interfaz especializada para seleccionar científicos con información detallada.

<img src="Imagenes_Readme/Ventana Cientificos.png">

**Funcionalidades:**
* **Ventana modal**: Popup con grid de 9 científicos
* **Información detallada**: Al seleccionar un científico, se muestra:
    * Fotografía
    * Especialidad
    * Restricciones de trabajo
* **Selección múltiple**: Pueden seleccionarse varios científicos
* **Validación visual**: Científicos seleccionados cambian de color/icono

### 🔭 5. Selección de Herramientas y Telescopios
**Descripción**: Interfaz para seleccionar equipos especializados con sus reglas específicas.

<img src="Imagenes_Readme/Ventana Medios.png">

**Funcionalidades:**
* **Categorización visual**: 12 recursos organizados en grid
* **Recursos con cantidad:**
    * Gafas virtuales, Portátiles, Telescopio básico → piden cantidad específica
    * Otros recursos → cantidad fija de 1
* **Información técnica**: Muestra descripción y requisitos de cada herramienta

### ⚠️ 6. Sistema de Validación en Tiempo Real
**Descripción**: Verifica automáticamente todas las reglas antes de guardar cualquier evento.

**Validaciones implementadas:**
* **Validación de datos básicos:**
    * Nombre no vacío y longitud máxima
    * Fechas en formato correcto
    * Fecha de inicio posterior a actual
    * Fecha de fin posterior a inicio
* **Validación de recursos:**
    * Al menos 1 científico seleccionado
    * Al menos 1 herramienta/telescopio seleccionado
    * Máximo 5 herramientas por evento
    * Sala seleccionada 
* **Validación de complementariedad:**
    * Científicos requeridos para telescopios específicos
    * Salas requeridas para ciertos equipos
    * Científicos requeridos para salas específicas
* **Validación de exclusiones:**
    * Científicos incompatibles no pueden trabajar juntos

## ⚠️ Validaciones y Restricciones <a id="️-validaciones-y-restricciones"></a>

### 🔄 Validaciones de Entrada Básica
#### 1. Validación de Fechas y Horarios:
La precisión temporal es crítica en astronomía, donde las ventanas de observación pueden ser de minutos. Por ello, el sistema valida:
* **Formato correcto**: Todas las fechas deben estar en formato numérico válido
* **Rangos lógicos:**
    * Año: entre el actual y 2040
    * Mes: 1-12
    * Día: según el mes y año 
    * Hora: 0-23
    * Minutos: 0-59
* **Consistencia temporal:**
    * Fecha de inicio debe ser posterior al momento actual(No se permiten eventos en el pasado)
    * Fecha de fin debe ser posterior a la fecha de inicio

#### 2. Validación de Nombre y Sala
La identificación única de eventos es fundamental para la trazabilidad:
* **Nombre del evento:**
    * No puede estar vacío
    * Máximo 45 caracteres 
* **Sala:**
    * Debe seleccionarse una sala 
    * Las opciones son fijas: Planetario, Cúpula de observación, Cúpula de fotografía, Sala de conferencias, Sala de óptica

#### 3. Validación de Cantidad de Recursos
El control de inventario es crucial en centros con recursos limitados:
* **Científicos**: Mínimo 1, no hay máximo
* **Herramientas/telescopios**: Mínimo 1, máximo 5 por evento
* **Recursos con cantidad (Gafas virtuales, Portátiles, Telescopio básico):**
<img src="Imagenes_Readme/Mensaje de Cantidad.png">
    * Cantidad debe ser un número entero positivo
    * No puede exceder la cantidad disponible en inventario

### 🔗 Validación de Complementxariedad (Co-requisitos)
#### 1. Telescopios que Requieren Científicos Específicos
| Telescopio | Científicos Requeridos | Mensaje de Error |
|------------|------------------------|------------------|
| Telescopio Lunar | Margaret Burbidge o Neil Tyson | "El Telescopio Lunar solo puede ser utilizado por especialistas en astros" |
| Telescopio de Galaxias | Vera Rubin, Neil Tyson o Edwin Hubble | "El Telescopio de Galaxias solo puede ser utilizado por especialistas de galaxias" |
| Telescopio solar | Hans Bethe, Neil Tyson o Carl Sagan | "El Telescopio solar solo puede ser utilizado por especialistas del sol" |
| Telescopio de agujeros negros | Stephen Hawking o Neil Tyson | "El Telescopio de agujeros negros solo puede ser usado por especialistas de agujeros negros" |
| Polarímetro | Henrietta Leavitt | "El Polarímetro solo puede ser utilizado por la especialista en óptica Henrietta Leavitt" |
| Espectrómetro | Henrietta Leavitt | "El Espectrómetro solo puede ser utilizado por la especialista en óptica Henrietta Leavitt" |

#### 2. Recursos que Requieren Salas Específicas
* Gafas virtuales → Solo en Planetario o Sala de conferencias
* Portátiles → Solo en Planetario o Sala de conferencias
* Telescopio básico → Solo en Planetario o Sala de conferencias

**Mensaje de error**: "El recurso [nombre] solo puede ser usado en la sala de conferencias o en el planetario"

#### 3. Salas que Requieren Científicos Específicos
* Planetario → Requiere Cleo Abram
* Sala de óptica → Requiere Henrietta Leavitt

**Mensajes de error:**
* "En el Planetario debe estar Cleo Abram la encargada de esta sala"
* "En la Sala de óptica debe estar la especialista Henrietta Leavitt"

### 🚫 Validación de Exclusiones Mutuas
#### 1. Científicos Incompatibles
| Grupo 1 | Grupo 2 | Razón del Conflicto |
|---------|---------|----------------------|
| Vera Rubin, Edwin Hubble | Hans Bethe, Carl Sagan | Especialistas en galaxias no pueden trbajar con especialistas en el sol |
| Margaret Burbidge | Stephen Hawking | Especialista en la Luna no pueden trabajar con especialista en agujeros negros |

**Mensaje de error**: "Los especialistas en galaxias no pueden trabajar junto a los especialistas en el sol"

## 🛠️ Tecnologías Utilizadas <a id="️-tecnologías-utilizadas"></a>

### Lenguaje de Programación
* **Python 3**: El proyecto fue creado puramente en python 

### Framework de Interfaz Gráfica
* **Kivy**: Framework de código abierto para desarrollo de aplicaciones multitouch. Permitió crear una interfaz gráfica moderna, responsive y multiplataforma con:
    * Sistema de layouts flexible (FloatLayout, BoxLayout, GridLayout)
    * Popups y ventanas modales
    * Estilización mediante lenguaje KV 

### Manejo de Datos y Persistencia
* **JSON**: Formato ligero de intercambio de datos utilizado para:
    * Recursos.json: Almacena el catálogo completo de recursos con sus propiedades, reglas y disponibilidad
    * Eventos.json: Persiste todos los eventos planificados con sus fechas, recursos asignados y detalles
* **Manejo de Fechas y Horarios**
    * datetime: Módulo estándar de Python para manejo avanzado de fechas, horas e intervalos temporales
    * calendar: Para cálculos de días en meses y validación de fechas
    * timedelta: Para operaciones aritméticas con intervalos de tiempo 

### Paradigma de Programación
* **Programación Orientada a Objetos (POO)**: Estructura del proyecto basada en clases y objetos:
    * Clase Evento: Modela eventos científicos con nombre, fechas y recursos
    * Clase Recurso: Representa científicos, telescopios y salas con sus propiedades
    * Clase Planificador: Contiene la lógica principal de validación y gestión
    * Clases de UI: Componentes reutilizables para la interfaz gráfica
