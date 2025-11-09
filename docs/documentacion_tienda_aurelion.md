# 🛒Proyecto Tienda Aurelion – Documentación técnica

### 📚 Índice de contenidos

- [🛒Proyecto Tienda Aurelion – Documentación técnica](#proyecto-tienda-aurelion--documentación-técnica)
    - [📚 Índice de contenidos](#-índice-de-contenidos)
    - [Tema](#tema)
    - [Problema](#problema)
    - [Solución](#solución)
    - [Fuente](#fuente)
    - [Datasets: definición, columnas y tipos](#datasets-definición-columnas-y-tipos)
    - [Estructura](#estructura)
    - [Información](#información)
    - [Pasos](#pasos)
    - [Pseudocódigo](#pseudocódigo)
    - [Diagrama del flujo](#diagrama-del-flujo)
- [Interpretaciones EDA – Visualizaciones](#interpretaciones-eda--visualizaciones)
  - [distribucion\_numericas\_tabla](#distribucion_numericas_tabla)
  - [correlacion](#correlacion)
  - [ventas\_total\_por\_mes](#ventas_total_por_mes)
  - [relacion\_cantidad](#relacion_cantidad)
  - [interpretacion\_outliers](#interpretacion_outliers)

---

### Tema

Análisis y consulta interactiva de datos de ventas de la Tienda Aurelion, una tienda minorista que desea comprender mejor el comportamiento de sus ventas, productos y clientes.

### Problema

La Tienda Aurelion enfrenta dificultades para mantener un equilibrio adecuado entre el stock disponible y la demanda real de los productos. Esto genera dos problemas recurrentes:

  - _Rupturas de stock_: cuando un producto se agota y no puede ser vendido.
  - _Exceso de inventario_: cuando se compran productos que permanecen sin rotación durante mucho tiempo.

Ambas situaciones impactan negativamente en la rentabilidad del negocio:

  - Las rupturas de stock reducen las ventas y afectan la satisfacción del cliente.
  - El exceso de inventario genera costos de almacenamiento innecesarios.

### Solución

Desarrollar un programa en Python y Streamlit que permita interactuar con los datos y consultar de forma sencilla información relevante. Utilizar los datos históricos de ventas, clientes y productos para:

  - Analizar la demanda real de cada producto.
  - Identificar los productos de mayor y menor rotación.
  - Estimar la demanda futura promedio mensual.
  - Proporcionar información visual que ayude a tomar decisiones de compra y reposición más inteligentes.

**Análisis que se puede realizar**

1. Ventas totales por producto y mes.
2. Ranking de productos más vendidos.
3. Relación entre stock disponible y ventas promedio.
4. Productos con ventas decrecientes (riesgo de exceso de stock).
5. Productos con ventas crecientes (riesgo de ruptura de stock).
6. Predicción de demanda promedio mediante una regresión lineal simple.

**Resultado esperado**

Una aplicación en Streamlit que permita:

   - Visualizar métricas de ventas y rotación.
   - Detectar los productos críticos para reposición.
   - Consultar la documentación del proyecto.

### Fuente

Su origen es secundario, los datasets fueron provistos por Guayerd dentro del programa de Fundamentos de Inteligencia Artificial que desarrolla junto a IBM.

_Nota_: Estos datasets son de carácter didáctico y se proporcionan solo con fines de prueba y aprendizaje, para poder estudiar y practicar el análisis de datos y la implementación de modelos.

### Datasets: definición, columnas y tipos

| Dataset | Descripción breve | Columnas | Tipo / Escala |
|----------|------------------|-----------|----------------|
| **clientes.xlsx** | Información de los clientes | id_cliente<br>nombre_cliente<br>email<br>ciudad<br>fecha_alta | int64 (Razón)<br>object (Nominal)<br>object (Nominal)<br>object (Nominal)<br>datetime64 (Intervalo) |
| **productos.xlsx** | Información de los productos | id_producto<br>nombre_producto<br>categoria<br>precio_unitario | int64 (Razón)<br>object (Nominal)<br>object (Nominal)<br>int64 (Razón) |
| **ventas.xlsx** | Registro de cada venta realizada | id_venta<br>fecha<br>id_cliente<br>nombre_cliente<br>email<br>medio_pago | int64 (Razón)<br>datetime64 (Intervalo)<br>int64 (Razón)<br>object (Nominal)<br>object (Nominal)<br>object (Nominal) |
| **detalle_ventas.xlsx** | Detalle de cada producto vendido | id_venta<br>id_producto<br>nombre_producto<br>cantidad<br>precio_unitario<br>importe | int64 (Razón)<br>int64 (Razón)<br>object (Nominal)<br>int64 (Razón)<br>int64 (Razón)<br>int64 (Razón) |

**Comentarios:**

- **PK (Primary Key):** identificador único de cada registro.  
- **FK (Foreign Key):** columna que referencia la PK de otro dataset.  
- `id_cliente`, `id_producto` y `id_venta` son **PK** en sus respectivas tablas.  
- `ventas.id_cliente` referencia a `clientes.id_cliente`.  
- `detalle_ventas.id_venta` referencia a `ventas.id_venta`.  
- `detalle_ventas.id_producto` referencia a `productos.id_producto`.  

### Estructura

Cada dataset es estructurado; se organiza en filas que representan registros individuales y columnas que representan atributos de interés para el análisis. Contienen datos tanto cuantitativos como cualitativos. Todos ellos en formato .xlsx (Excel).

### Información

1. **Nombre del programa:** Proyecto Tienda Aurelion

2. **Objetivo:**
   Permitir la exploración interactiva de los datos de ventas, clientes y productos de la tienda, proporcionados en los siguientes dataset:
   - `clientes.xlsx`
   - `productos.xlsx`
   - `ventas.xlsx` 
   - `detalle_ventas.xlsx`
   
   Estos archivos fueron unificados en un único dataset integrado denominado `df_tienda_aurelion.csv`, que concentra toda la información relevante para su análisis. 
   
   Además, la aplicación muestra la documentación, el pseudocódigo y los diagramas de flujo del proyecto.

3. **Lenguaje y librerías utilizadas**
    - `Python 3.11`
    - Librerías: `streamlit`, `pandas`, `PIL` (para imágenes), `os` (gestión de archivos), `matplotlib`, `seaborn`, `numpy`, `pathlib`, `ydata-profiling` (para realizar un EDA automatizado), `streamlit-pandas-profiling`

4. **Entrada de datos**
    - Archivos Excel: `clientes.xlsx`, `productos.xlsx`, `ventas.xlsx`, `detalle_ventas.xlsx`
    - Archivo de documentación: `documentacion_tienda_aurelion.md`

5. **Salida / Visualización**
    - Interfaz web interactiva con menú lateral
    - Expanders utilizados en la sección Ver documentación para mostrar de forma organizada el contenido técnico (contexto, datasets, metodología, pseudocódigo y diagrama de flujo).
    - Tablas de datos y resúmenes estadísticos

6. 🟡**Funcionalidades principales**
    - Visualizar información general de cada dataset: vista previa, tipos de columnas, cantidad de registros
    - Las estadísticas descriptivas se generan con `pandas.describe(include="all")`, permitiendo visualizar medidas resumen para variables numéricas y conteos para variables categóricas.
    - Explorar la documentación del proyecto de manera organizada

7. **Estructura del programa**
    - Carga de datasets: `función load_dataset()` con caching de Streamlit. 
    - Menú lateral: selección de opciones: Información general, Estadísticas, Documentación
    - Secciones de documentación: Contexto y objetivo, Metodología, Pseudocódigo, Diagrama del flujo

### Pasos

1. **Inicio de la aplicación**  
   - Se inicializa Streamlit y se configura la página (título, ícono y diseño).  
   - Se muestra el logotipo de la tienda junto al encabezado principal de la interfaz.

2. **Carga de datasets**  
   - Se leen los archivos Excel: `clientes.xlsx`, `productos.xlsx`, `ventas.xlsx` y `detalle_ventas.xlsx` mediante **pandas**.  
   - Cada archivo se carga en un **DataFrame** independiente.  
   - La función de carga se **almacena en caché** (`st.cache_data`) para optimizar el rendimiento y evitar recargas innecesarias.

3. 🟡**Menú lateral**  
   - Se despliega un `selectbox` con las tres secciones principales de la aplicación:  
     - **Información general**  
     - **Estadísticas**  
     - **Ver documentación**

4. **Opción 1: Información general**  
   - El usuario selecciona el dataset a visualizar.  
   - Se muestra:  
     - Vista previa de los primeros registros (`head()`).  
     - Tipos de columnas y estructura del dataset.  
     - Cantidad total de filas y columnas.  
   - Cada bloque de información se organiza dentro de **expanders** para mantener una visualización ordenada.

5. **Opción 2: Estadísticas**  
   - El usuario selecciona el dataset a analizar.  
   - Se generan estadísticas descriptivas mediante `describe(include="all")`.  
   - Se incluyen métricas de variables **numéricas y categóricas**, acompañadas de resúmenes visuales.

6. **Opción 3: Ver documentación**  
   - Se lee el archivo `documentacion_tienda_aurelion.md`.  
   - El contenido se organiza en **expanders** para facilitar la lectura:  
     - Contexto y objetivo  
     - Metodología  
     - Pseudocódigo  
     - Diagrama de flujo  
   - El diagrama se adapta automáticamente al ancho del contenedor (`use_container_width=True`).

7. **Interactividad**  
   - Los **expanders** permiten ocultar o desplegar secciones para una interfaz más limpia.  
   - Los **selectboxes** ofrecen navegación dinámica entre datasets y apartados.  
   - La aplicación combina usabilidad y claridad visual para una exploración fluida de los datos.

### Pseudocódigo

```text
INICIO

1. Configurar la página de Streamlit:
    - Título: "Tienda Aurelion"
    - Ícono de la página
    - Layout: ancho completo ("wide")

2. Mostrar encabezado principal:
    - Crear dos columnas (1 y 4 proporciones)
    - Columna 1: mostrar logo de la tienda desde ./assets/logo_aurelion.png
    - Columna 2: mostrar título del proyecto y descripción general

3. Definir función para cargar archivos Excel (con caché):
    FUNCION load_dataset(ruta, hoja=0):
        SI el archivo no existe:
            Mostrar advertencia
            Retornar None
        SINO:
            INTENTAR leer el archivo Excel usando pandas
            SI tiene éxito:
                Retornar el DataFrame
            SI ocurre error:
                Mostrar mensaje de error y retornar None

4. Validar existencia de todos los archivos en ./data:
    - clientes.xlsx
    - productos.xlsx
    - ventas.xlsx
    - detalle_ventas.xlsx
    SI falta alguno:
        Mostrar advertencia en la barra lateral
    SINO:
        Mostrar mensaje de disponibilidad exitosa

5. Crear menú lateral con opciones:
    - "Información general"
    - "Estadísticas"
    - "Ver documentación"

6. SI la opción seleccionada es "Información general":
    - Mostrar selectbox con nombres de datasets
    - Cargar el dataset seleccionado
    - Mostrar:
        - Fecha y tamaño del archivo
        - Vista previa (primeras filas)
        - Tabla con nombres y tipos de columnas
        - Cantidad de registros
    - SI no se pudo cargar:
        Mostrar advertencia

7. SI la opción seleccionada es "Estadísticas":
    - Mostrar selectbox con datasets disponibles
    - Cargar el dataset seleccionado
    - Mostrar estadísticas descriptivas (`describe(include="all")`)
    - SI no se pudo cargar:
        Mostrar advertencia

8. SI la opción seleccionada es "Ver documentación":
    - Verificar existencia del archivo ./documentacion_tienda_aurelion.md
    - SI existe:
        - Leer el contenido completo
        - Dividir el texto en secciones:
            a) Contexto y objetivo
            b) Datasets de referencia
            c) Metodología e implementación
            d) Pseudocódigo
            e) Diagrama del flujo
        - Mostrar cada sección dentro de un expander
        - Mostrar la imagen del diagrama centrada y ajustada al ancho
    - SINO:
        - Mostrar advertencia de archivo no encontrado

9. Mostrar pie de página (footer):
    - Información del Sprint, autor y enlace a LinkedIn

FIN

```

### Diagrama del flujo

A continuación, se presenta el flujograma del proceso general del proyecto **Tienda Aurelion**.  
Este diagrama ilustra las principales etapas del flujo del programa, desde la carga de los datasets hasta la visualización interactiva de la información en la aplicación web.

<p align="center">
  <img src="../assets/flujograma_aurelion.jpg" alt="Flujograma Tienda Aurelion" width="600">
</p>



# Interpretaciones EDA – Visualizaciones

Esta sección describe las principales visualizaciones generadas automáticamente por la aplicación, junto con su interpretación.
Cada gráfico se encuentra guardado en la carpeta plots/ y se muestra en la sección de estadísticas del dashboard.

🔶 Distribución de variables numéricas

Estos gráficos permiten analizar la forma y dispersión de las variables numéricas del conjunto de datos unificado.

Las distribuciones de variables numéricas permiten identificar posibles asimetrías, valores extremos o zonas de concentración.
Estos patrones ayudan a tomar decisiones en torno a:

- Segmentación de clientes según comportamiento de compra.
- Estrategias de precios y descuentos.
- Control de inventario, detectando productos de alta o baja rotación.

## distribucion_numericas_tabla

A continuación, se detallan las explicaciones correspondientes a cada una de las variables analizadas.

| Variable            | Descripción visual                                                  | Patrón observado                                                                                                                                             | Interpretación                                                                                                               |
| ------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| **cantidad**        | Eje X: cantidad (1 a 5) <br> Eje Y: frecuencia (hasta ~85)          | • Las cantidades más frecuentes son 2 y 4, con picos cercanos a 80 y 70 respectivamente. <br> • Las demás cantidades (1, 3 y 5) tienen frecuencias similares, alrededor de 60. | Distribución discreta y relativamente uniforme, con un pico notable en **cantidad = 2**. La dispersión es baja.               |
| **precio_unitario** | Eje X: precio_unitario (0 a 5000) <br> Eje Y: frecuencia (hasta 60) | • Asimétrica, con concentración entre **1500 y 2500**. <br> • Pico cerca de **2000**. <br> • Pocos valores en extremos (<500 y >4000).                       | La mayoría de los productos se venden en un rango medio de precios, con pocos productos en rangos muy altos.         |
| **total_venta**     | Eje X: total_venta (0 a 25000) <br> Eje Y: frecuencia (hasta 60)    | • Distribución **sesgada a la derecha**. <br> • Alta concentración entre **0 y 10,000**, con pico entre **3,000–5,000**. <br> • Pocos casos >20,000.         | La mayoría de las ventas son bajas o moderadas; las muy altas son raras, indicando posibles *outliers* en el extremo derecho. |


## correlacion
**Variables analizadas:**
* cantidad
* precio_unitario
* total_venta

**Principales resultados:**
1. cantidad vs precio_unitario
- Correlación: -0.074 (muy baja y negativa). No existe relación significativa entre la cantidad vendida y el precio unitario. Es decir, vender más unidades no implica que el precio sea mayor o menor.

2. cantidad vs total_venta:
- Correlación: 0.6 (moderada y positiva). A mayor cantidad, tiende a aumentar el total de venta, lo cual es lógico porque más unidades generan más ingresos, aunque no es una relación perfecta.

3. precio_unitario vs total_venta:
- Correlación: 0.68 (moderada-alta y positiva). El precio unitario tiene una influencia importante en el total de venta. Productos más caros tienden a generar ventas totales más altas, incluso si la cantidad no varía mucho.

## ventas_total_por_mes

El gráfico muestra la evolución de las ventas mensuales entre enero 2024 y junio 2024.
Se observa una tendencia fluctuante, con una caída marcada en abril y una recuperación fuerte en mayo.

Resultados clave:

* **Máximo**
  - Mes: mayo 2024 - Valor: 561,832
  - Este fue el mejor mes en ventas, superando el promedio por un amplio margen.

* **Mínimo**
  - Mes: abril 2024 - Valor: 251,524
  - Abril fue el peor mes, con ventas muy por debajo del promedio.

* **Promedio**
  - Línea horizontal: 441,903 
  - Tres meses (enero, mayo y junio) estuvieron por encima del promedio, mientras que febrero, marzo y abril quedaron por debajo.

Tendencias específicas:
- Enero (529,840): Buen inicio, por encima del promedio.
- Febrero y Marzo: Descenso progresivo (407,041 → 388,263).
- Abril: Caída abrupta al mínimo (251,524).
- Mayo: Recuperación fuerte al máximo (561,832).
- Junio: Ligera baja respecto a mayo, pero sigue alto (512,917).

> Las ventas son volátiles, con un mínimo crítico en abril y un máximo en mayo.
El promedio indica que la tienda tiene un buen desempeño general, pero necesita analizar qué causó la caída en abril y el repunte en mayo (promociones, estacionalidad, campañas).

## relacion_cantidad

Diagrama de dispersión con:
- Eje X: cantidad (de 1 a 5 unidades).
- Eje Y: total_venta (hasta 25,000).
- Incluye una línea de tendencia ascendente y un valor de correlación: 0.60.

Resultados clave:
1. Correlación positiva moderada (0.60): Indica que a mayor cantidad vendida, mayor es el total de venta, aunque no es una relación perfecta.
Esto es lógico: más unidades generan más ingresos, pero hay variabilidad por el precio unitario.

2. Patrón de dispersión: Para cada cantidad (1 a 5), hay una amplia dispersión en el total de venta.
Ejemplo:
   - Cantidad = 1 → ventas entre ~1,000 y ~5,000.
   - Cantidad = 5 → ventas entre ~5,000 y >20,000.
El precio unitario influye mucho en el total, incluso con la misma cantidad.

3. Tendencia general: La línea de regresión muestra un incremento consistente: más cantidad tiende a aumentar el total de venta.

> Existe una relación clara entre cantidad y total de venta, pero no es determinante por sí sola.
El precio unitario es un factor adicional que explica la dispersión.
Para aumentar ventas totales, incrementar la cantidad ayuda, pero también es clave considerar el mix de productos y precios.

## interpretacion_outliers

A continuación se resumen los resultados de los gráficos de outliers agrupados por tipo de variable.

| Variable            | Rango observado                     | Mediana / Forma de la distribución                                                    | Interpretación                                                                                          |
|--------------------|--------------------------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| **cantidad**        | 1 a 5                                | Mediana ≈ 3; distribución simétrica; sin outliers relevantes                           | Las cantidades vendidas suelen estar entre 2 y 4; pedidos consistentes sin valores atípicos significativos. |
| **precio_unitario** | ~500 a 5000                          | Mediana ≈ 2500; distribución equilibrada; algunos puntos fuera del rango               | Los precios se concentran en el rango medio, aunque existen productos con precios extremos.              |
| **total_venta**     | 0 a >20,000                          | Mediana ≈ 8000; distribución sesgada a la derecha; múltiples outliers                  | La mayoría de las ventas son bajas o medias, pero existen transacciones extraordinarias que elevan el máximo. |
