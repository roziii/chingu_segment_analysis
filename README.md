# Proyecto de Análisis de Donaciones de Chingu
Este proyecto tiene como objetivo principal el análisis de datos históricos para descubrir patrones y tendencias relevantes que permitan realizar predicciones sobre el comportamiento futuro. Estas predicciones no solo facilitarán una toma de decisiones más informada, sino que también contribuirán a incrementar la atención de los usuarios hacia la plataforma, con el fin de promover su crecimiento y aumentar su rentabilidad.

Este proyecto tiene como objetivo analizar la participación de los usuarios, los ingresos generados y los resultados de los proyectos colaborativos (Voyages) dentro de la plataforma **Chingu**.
Add more
---
## Historia de Chingu.io
Chingu.io es una comunidad global sin fines de lucro que empodera a desarrolladores en formación mediante el aprendizaje colaborativo, remoto y basado en proyectos.

Fundada en 2017, la misión de Chingu es cerrar la brecha entre aprender a programar y trabajar de manera profesional, simulando entornos reales de desarrollo de software. Ofrece una oportunidad única para mejorar tanto las habilidades técnicas como las habilidades blandas trabajando en equipos distribuidos.

El núcleo de Chingu es el Programa Voyage: un sprint estructurado de seis semanas en el que los participantes se agrupan según su nivel de habilidad e intereses. Los equipos colaboran para diseñar, desarrollar y desplegar aplicaciones reales, siguiendo metodologías Ágiles y buenas prácticas de desarrollo.

Niveles del Voyage:
Nivel 1: Proyectos introductorios utilizando HTML, CSS y JavaScript.

Nivel 2: Aplicaciones front-end intermedias con frameworks como React.

Nivel 3: Aplicaciones full-stack avanzadas con componentes integrados de front-end y back-end.

Cada Voyage concluye con una exhibición pública donde los equipos presentan sus proyectos completados. Estas demostraciones muestran una amplia variedad de aplicaciones, desde herramientas de productividad hasta plataformas educativas.

Chingu funciona gracias a su comunidad, y su sostenibilidad depende del apoyo y las donaciones de los participantes y colaboradores. Para obtener más información o contribuir, visita Chingu.io.

### ¿Cómo funcionan los Voyages?
Los Voyages son programas intensivos de seis semanas donde los participantes son agrupados en equipos remotos según su nivel de habilidad, disponibilidad y preferencias tecnológicas. Cada equipo trabaja en un proyecto completo, siguiendo metodologías ágiles y utilizando herramientas modernas de desarrollo colaborativo como GitHub, Discord y Trello .

#### Proceso de participación:
##### Aplicación gratuita: Completa el formulario de inscripción en chingu.io.

##### Proyecto individual: Realiza un proyecto solo para validar tus habilidades y determinar el nivel adecuado.

##### Formación de equipos: Se te asignará a un equipo con miembros de habilidades y objetivos similares.

##### Desarrollo del proyecto: Colabora con tu equipo para diseñar, desarrollar y desplegar una aplicación real.

##### Demostración final: Presenta tu proyecto en una exhibición pública al finalizar el Voyage.

###  Certificación y Reconocimiento en Chingu.io
Chingu.io no emite certificados formales al finalizar un Voyage. Sin embargo, los participantes obtienen experiencia práctica en proyectos reales, lo cual representa una credencial sólida y verificable dentro del ámbito profesional.

#### Formas de demostrar tu participación en un Voyage
##### Repositorio en GitHub
Cada equipo desarrolla y mantiene un repositorio en GitHub como parte del proyecto. Este código representa una evidencia concreta de tu capacidad técnica y de colaboración en entornos distribuidos.

##### Proyectos Destacados
Los proyectos completados son frecuentemente compartidos en el sitio web de Chingu y sus redes sociales, brindando visibilidad adicional a los participantes destacados.

##### Perfil Profesional (CV / LinkedIn)
Es recomendable incluir tu experiencia en Chingu.io en la sección de proyectos o experiencia laboral, especificando tu rol, las tecnologías utilizadas, las metodologías aplicadas (como Agile/Scrum) y los resultados alcanzados.

##### Portafolio Personal
Puedes integrar el proyecto realizado durante el Voyage en tu portafolio web, destacando las funcionalidades implementadas, la colaboración en equipo y los aprendizajes adquiridos.

### ¿Cómo puedes apoyar a Chingu.io?
Chingu se mantiene gracias a la dedicación de voluntarios y al apoyo de su comunidad. Aunque la participación en los Voyages es gratuita, existen costos asociados al mantenimiento de la plataforma, como dominios y servicios de hosting. Puedes contribuir de las siguientes maneras:

Donaciones únicas: A través de PayPal o GoFundMe .

Donaciones recurrentes: Mediante Patreon para apoyar mensualmente.

Voluntariado: Participa como mentor, facilitador o colaborador en la comunidad.


## Estructura del Proyecto
El proyecto está organizado de manera modular para facilitar el análisis, limpieza, modelado y visualización de los datos relacionados con la plataforma Chingu.io. A continuación se describe la estructura principal:

### data/
Contiene los archivos de datos utilizados en el análisis. Incluye:

Archivos .csv con información sobre aplicaciones, transacciones, cronogramas de Voyage y donaciones.

Subcarpetas:

#### cleaned_data/: Datos depurados y listos para su análisis.

##### normalized_data/: Datos normalizados para su uso en modelos.
## Diccionario de Datos
### 1. `RedactedDonationAnalysis-Chingu_Applications_20250304.csv`

**Propósito**: Registra la información de los usuarios que se inscriben para participar en un Voyage de Chingu.

**Columnas Clave**:
- `Unique ID`: Identificador único anonimizado.
- `Timestamp`: Fecha y hora del registro.
- `Subscription Status`: Estado de suscripción al correo electrónico (no paga).
- `Voyage Role`: Rol al que aspira el solicitante.
- `Goal`, `Source`: Motivaciones y canal de descubrimiento.
- `Application Date`, `Application Age in Days`, `No. Voyages Started`, `Country`: Contexto del usuario.

---

### 2. `RedactedDonationAnalysis-Chingu_RevenueTxns_20250305.csv`

**Propósito**: Detalla todas las transacciones financieras de los usuarios, incluyendo suscripciones pagas y donaciones.

**Columnas Clave**:
- `Unique ID`: Identificador del usuario.
- `Subscription Status`: Indica si tiene suscripción **paga**.
- `Transaction Date`: Fecha de la transacción.
- `Payment Amount`, `Net Payment`, `Transaction Fee`: Detalles del monto.
- `Product`, `Payment Source`, `Certificate Voyage`: Información contextual del pago.

> **Nota**: Aquí, “Subscription Status” se refiere exclusivamente a **suscripciones pagas**.

---

### 3. `DonationAnalysis-Chingu_VoyageSchedules_20250305.csv`

**Propósito**: Define el calendario de cada Voyage.

**Columnas Clave**:
- `Name`: Código del Voyage.
- `Start Date`, `End Date`, `Solo Project Deadline`: Duración y fechas clave.
- `Description`: Observaciones adicionales.

---

### 4. `RedactedDonationAnalysis-Chingu_VoyageCompletions_20250305.csv`

**Propósito**: Registra la participación de los usuarios en proyectos grupales, su finalización y retroalimentación.

**Columnas Clave**:
- `Unique ID`, `What is your Voyage?`, `Completed Voyage?`, `Completion Status`
- `Certificate Issue Date`, `Tier`, `Team number`, `Project name`
- `Tech stack`, `GitHub URL`, `Deployed URL`
- Comentarios sobre la experiencia y recomendación

---



### modules/
Este directorio contiene scripts Python reutilizables que encapsulan la lógica de procesamiento y análisis. Incluye:

Cleaner.py, Applications_Cleaner.py, Transaction_Cleaner.py: Scripts para limpiar distintos conjuntos de datos.

EDA.py: Funciones para análisis exploratorio de datos.

ml_modeling.py: Funciones relacionadas con modelos predictivos.

Completion_Cleaner.py: Limpieza específica para datos de finalización de aplicaciones.

### Notebooks (.ipynb)
Los cuadernos Jupyter están organizados según el tipo de análisis:

Applications_EDA.ipynb, Transaction_EDA.ipynb, completion_EDA.ipynb: Análisis exploratorios.

application_completion-auto_regressive_model.ipynb: Modelado predictivo.

Transaction_Application_analysis.ipynb: Análisis cruzado entre aplicaciones y transacciones.

Abandond_transaction.ipynb: Análisis de transacciones abandonadas.

application_voyage_list_merge.ipynb: Integración de listas de aplicaciones con los datos de Voyage.

Application_table_normalization.ipynb: Normalización de tablas relacionales.

#### Abandond_transaction
Este notebook analiza las diferencias entre los registros de transacciones (transactions) y los registros de aplicaciones (applications) con el fin de detectar si existen transacciones asociadas a identificadores únicos que no aparecen en las aplicaciones.

Objetivo del Análisis
Verificar si todos los identificadores (unique_id) presentes en las transacciones también existen en las aplicaciones. Se compara:

Datos sin limpiar (raw)

Datos limpiados (cleaned)

Datos normalizados (normalized)

Resultado
Se encontraron varios identificadores presentes en el conjunto de transacciones que no están presentes en las aplicaciones, incluso después del proceso de limpieza y normalización.

```
len(transactions_UIDs) = 354  
len(normalized_UIDs_intersection) = 252  
UIDs_only_in_transaction = 354 - 252 = 102 casos detectados
```

Confirmación con la compañía
Luego de contactar con el equipo de Chingu, se confirmó que algunas aplicaciones antiguas fueron eliminadas de la base de datos original por motivos administrativos o técnicos, lo cual justifica la existencia de esas transacciones "huérfanas".

Conclusión
Este hallazgo es importante para interpretar correctamente los análisis financieros y de completitud de las aplicaciones. Se recomienda considerar estos registros al realizar inferencias o modelado predictivo.

#### Applications_EDA.ipynb — Español
##### Objetivo
El propósito de este notebook es realizar un análisis exploratorio de las aplicaciones registradas en la plataforma Chingu, para descubrir patrones, tendencias y problemas de calidad en los datos.

##### Metodología Utilizada
* Preprocesamiento de Datos

  * Limpieza de valores nulos y columnas irrelevantes

  * Uso de la clase DataCleaner_Application

* Normalización y Estandarización

  * Homogeneización de nombres de columnas

  * Clasificación de campos como género, rol en el Voyage, objetivos, etc.

* Análisis Descriptivo

  * Estadísticas generales: media, desviación estándar, percentiles

  * Conteo de valores por categoría (ej. fuentes, países, géneros)

* Análisis de Distribución

  * Evaluación de la distribución de las fechas, semanas y meses de las aplicaciones

  * Segmentación por participación en Voyages (has_voyage)
    
    ![Image](https://github.com/user-attachments/assets/e2bb4dff-d8c5-4928-adbd-5a4ec1659277)
    ![Image](https://github.com/user-attachments/assets/76c925c9-4b3d-4d56-9744-e856fc81122e)
    ![Image](https://github.com/user-attachments/assets/a655c81c-c450-4f96-b116-c9f13532eaa7)
    ![Image](https://github.com/user-attachments/assets/a7b714f7-200c-476b-a766-7b13d5f999df)
 


* Métodos Matemáticos Aplicados
* 
  * Estadísticas básicas: media, mediana, desviación estándar, conteos

  * Análisis de variables categóricas mediante frecuencias relativas

  * Conversión temporal para agrupar por semanas y meses

  * Evaluación de participación (0 o 1) como variable binaria

##### Salidas Generadas
* Conteo de participantes por rol, género y país

* Análisis de fuentes de tráfico (Google, YouTube, LinkedIn, etc.)

* Visualización del número de aplicaciones por año/mes/semana

* Exportación de datos limpios para uso posterior en modelos predictivos

#### Transaction_EDA.ipynb
##### Objetivo:
Este notebook tiene como propósito analizar los datos de transacciones de la plataforma Chingu.io. Busca entender los patrones de ingresos, fuentes de pago y comportamientos temporales en las contribuciones recibidas.

##### Metodología Aplicada:
* Preprocesamiento:

  * Limpieza de datos nulos y valores inválidos

  * Eliminación de registros sin fecha

  * Estandarización de nombres de columnas

* Estadísticas Descriptivas:

  * Cálculo de promedios, medianas, desviaciones estándar, mínimos y máximos

  * Recuento de valores para campos categóricos como estado de suscripción, producto, fuente de pago

* Análisis de Distribución:

  * Exploración de columnas clave usando histogramas y gráficos de barras

  * Análisis por año, mes y semana de transacción

* Descomposición Estacional:

  * Aplicación de técnicas estadísticas para descubrir patrones estacionales en los ingresos y comisiones

##### Técnicas Matemáticas Aplicadas:
* Estadística básica: media, mediana, percentiles, etc.

* Agrupación por tiempo: año, mes, semana

* Descomposición estacional de series temporales (seasonal_decomposition)

* Clasificación por frecuencia de ocurrencia

##### Resultados Obtenidos:
* Distribución de fuentes de ingresos

* Participación por tipo de producto (donaciones, suscripciones, certificados)

* Fluctuaciones mensuales y semanales en los ingresos

* Dataset limpio listo para modelos predictivos o dashboards

#### completion_EDA.ipynb 
##### Objetivo:
El propósito de este notebook es analizar los datos relacionados con la finalización de proyectos en el programa Voyage de Chingu. Se estudian variables como el estado de finalización, emisión de certificados, satisfacción del usuario y su relación con niveles (Tier) y roles.

##### Metodología aplicada:
* Preprocesamiento

  * Eliminación de columnas textuales y comentarios irrelevantes

  * Normalización de nombres de columnas

  * Eliminación de filas sin número de Voyage

* Tratamiento de campos clave

  * Limpieza de columnas completion_status, product, tier, etc.

  * Imputación de valores nulos con etiquetas como "undefined" o "no_product"

  * Conversión de fechas y manejo de formatos

* Análisis Descriptivo

  * Conteo total de registros: 2968

  * Satisfacción promedio del usuario: 9.26 / 10

  * Certificados emitidos: 1223

  * Clasificación por rol, tier y producto

###### Técnicas Matemáticas Aplicadas
* Estadísticas básicas: media, mediana, desviación estándar

* Frecuencias de variables categóricas

* Análisis de puntuación en escalas (de 0 a 10)

* Procesamiento de fechas para posibles análisis temporales

###### Resultados
* Exportación de dataset limpio en CSV

* Análisis de estados: Completed, Incomplete, Dropped, etc.

* Evaluación de satisfacción del usuario

* Asociación entre niveles (Tier) y finalización

##### transactions.ipynb
###### Objetivo del Proyecto:
Analizar los datos de transacciones financieras de los usuarios de Chingu.io para comprender patrones de comportamiento, segmentar clientes y predecir su disposición a pagar montos más altos.

###### Metodología Aplicada:
* Preprocesamiento de Datos

  * Limpieza de valores nulos y erróneos

  * Normalización de columnas categóricas

  * Conversión de fechas y extracción de variables temporales

* Análisis Descriptivo

  * Estadísticas básicas por producto, año y estado de suscripción

  * Distribución de montos de pago

  * Análisis de frecuencia temporal

* Visualización

  * Histogramas y boxplots

  * Series de tiempo (diarias, mensuales, anuales)

  * Matriz de correlación

 * Curvas ROC

* Segmentación de Usuarios (Clustering con K-Means)

  * Agrupación de usuarios en 3 clústeres

  * Comparación por gasto total, estado de suscripción y tipo de producto

* Modelado Predictivo

  * Clasificación binaria con regresión logística para predecir pagos altos

  * Evaluación del modelo con métricas: Accuracy, Precision, Recall, F1, AUC

###### Técnicas Matemáticas y de Machine Learning
* Estadísticas descriptivas

* K-Means Clustering

* Regresión Logística

* Binary Encoding

* Imputación y normalización

* Curvas ROC & AUC

###### Resultados Clave
* Promedio de pago: $3.27

* Los usuarios con suscripción activa y productos profesionales aportan más ingresos

* Métricas de modelo predictivo:

* Precisión del 99%

* AUC hasta 0.97

##### application_completion.ipynb
###### Objetivo:
El objetivo de este archivo es predecir si un usuario completará su proyecto Voyage utilizando datos de aplicaciones, participación y retroalimentación.

###### Metodología aplicada
* Preprocesamiento

  * Fusión de datos de aplicaciones y finalización

  * Relleno de valores nulos

  * Codificación categórica con BinaryEncoder

  * Escalado con StandardScaler

  * Reducción de Dimensionalidad

  * Aplicación de PCA para conservar el 95% de la varianza con 59 componentes

  * Identificación de los 10 atributos más influyentes

  * Selección de características con Linear SVC

  * Eliminación de atributos irrelevantes mediante penalización L1

* Entrenamiento de Modelos

  * Regresión Logística

  * Random Forest

  * Optimización de hiperparámetros con GridSearchCV

  * Separación de datos para validación y extrapolación

* Evaluación del modelo

  * Métricas usadas:

    * Matriz de confusión

    * Curva ROC

    * AUC

    * F1 Score

###### Métodos matemáticos utilizados:
* PCA

* Codificación binaria y Label Encoding

* Modelos de clasificación: Logistic Regression y Random Forest

* Grid Search CV para optimización

* Evaluación con AUC, ROC, F1 Score

###### Resultados principales
```
Modelo	 F1 Score	AUC
Logistic Regression	0.9063	0.9571
Random Forest	0.9737	0.9977
Logistic (Extra)	—	0.9681
Random Forest (Extra)	—	0.9982
```

##### Análisis enriquecido del archivo application_voyage_list_merge.ipynb (Español)
###### Objetivo:
Predecir la participación de usuarios en futuros Voyages de Chingu.io a partir de datos de aplicación, con visualización de tendencias, reducción de dimensiones, y modelos predictivos de alta precisión.

###### Datos de entrada:
* Número total de aplicaciones: 10,600

* Variable objetivo: has_voyage (0 o 1)

* Variables clave: rol, objetivo, género, origen, estado de suscripción

###### Análisis exploratorio:
* Día más activo: lunes y martes

* Roles más comunes: Developer, Product Owner, Scrum Master

* Objetivos frecuentes: encontrar equipo, mejorar CV, práctica colaborativa

###### Tendencias temporales:
* Pico de aplicaciones: años 2021 y 2022

* Roles técnicos en aumento

* Mayor cantidad de Voyages activos entre julio y noviembre

###### Modelado predictivo:
Modelo: Random Forest Classifier

Evaluación:

| Conjunto           | Precisión | F1 Score | AUC  |
|--------------------|-----------|----------|------|
| Entrenamiento/Test | 100%      | 1.00     | 1.00 |
| Extrapolación      | 100%      | 1.00     | 1.00 |


###### Reducción de dimensiones (PCA):
Componentes seleccionados: 24 (cubren 95% de la varianza)

Variables más influyentes:

país de origen

fuente de adquisición

rol, objetivo, estado de suscripción

###### Predicción de participación futura:
Se generaron datos sintéticos para predecir participación mensual por rol hasta diciembre de 2025.

Roles con mayor proyección: Developer, Product Owner

Visualización combinada: datos reales + proyecciones futuras

###### Evaluación del aprendizaje del modelo:
Error dentro de la muestra (E_in): 0.0000

Error fuera de muestra (E_out): 0.0005

Estimación de PAC bound: ±0.0375

##  Transaction & Application Combined Analysis

Este análisis tiene como objetivo combinar datos de **aplicaciones**, **transacciones** y **finalización de proyectos** para predecir tanto la **suscripción activa de los usuarios** como el **pago neto esperado**.

###  Datos combinados
- Total de registros únicos: **2,287**
- Datos fusionados desde:
  - `applications.csv`
  - `transactions.csv`
  - `completions.csv`

---

###  Selección de Características (PCA)

Se aplicó **Análisis de Componentes Principales (PCA)** a los tres conjuntos de datos para identificar variables más influyentes.

- Principales atributos:
  - `application_date`, `goal`, `source`, `product`, `tier`, `completion_status`, `net_payment`, `subscription_status`

---

###  Modelos de Clasificación

Se entrenaron tres modelos para predecir el estado de suscripción (`Activa`, `Terminada`, `Sin suscripción`).

| Modelo                | Accuracy | F1 Score | AUC     |
|------------------------|----------|----------|---------|
| Random Forest          | 94.48%   | 0.9431   | 0.9930  |
| Gradient Boosting      | 95.57%   | 0.9551   | 0.9920  |
| Logistic Regression    | 86.44%   | 0.8640   | 0.9559  |

>  **Gradient Boosting** presentó el mejor rendimiento general.

---

###  Modelado de Regresión

Se predijo el valor monetario `net_payment` usando modelos de regresión:

- **Mejor modelo**: Gradient Boosting Regressor

| Métrica       | Test Set | Extrapolación |
|---------------|----------|---------------|
| MAE           | 0.44     | 0.50          |
| R² Score      | 0.83     | 0.75          |

---

###  Archivos relacionados

- `Transaction_Application_analysis.ipynb`: análisis completo
- `merged_dataset.csv`: conjunto de datos final usado para modelado

##  Application_table_normalization.ipynb

Este módulo realiza la **normalización de columnas clave** del dataset de aplicaciones para reducir redundancias, mejorar la estructura y preparar los datos para análisis avanzados y modelado predictivo.

###  Proceso de Normalización

Se utilizó una clase personalizada `Application_Normalizer` para:

1. Leer los datos originales desde `applications.csv`
2. Crear tablas de dimensión para los siguientes campos:
   - `unique_id`
   - `subscription_status`
   - `voyage_role`
   - `gender`
   - `goal`
   - `source`
   - `country_name_from_country`
   - `application_day_of_week`
3. Reemplazar los valores originales por claves foráneas (IDs)
4. Exportar tanto la versión normalizada como la versión reconstruida

### Archivos Generados

| Archivo                                | Descripción                                          |
|----------------------------------------|------------------------------------------------------|
| `clean_applications.csv`              | Aplicaciones con claves foráneas (formato limpio)   |
| `*_table.csv`                         | Tablas de dimensión por columna (ej. `goal_table.csv`) |
| `merged_applications.csv`             | Aplicaciones reconstruidas con los valores originales |

>  Todos los archivos se encuentran en: `./data/normalized_data/`

###  Ventajas

- Menor redundancia de texto
- Mejor organización de datos
- Listo para bases de datos relacionales o entrenamiento de modelos ML

## application_completion-auto_regressive_model
Modelado Autoregresivo para Completitud de Voyage

Este módulo implementa un modelo autoregresivo basado en LSTM para predecir si un usuario completará su participación en un Voyage de Chingu.io, usando datos secuenciales históricos y enriquecimiento externo como tasa de desempleo y tendencias de búsqueda de Google.

---

### Datos y Preprocesamiento

- Total de registros: **7,929 aplicaciones únicas**
- Campos clave: `voyage_role`, `subscription_status`, `goal`, `product`, `completion_status`, `timestamp`, etc.
- Normalización:
  - BinaryEncoding aplicado a variables categóricas
  - Columnas como `completed_voyage` y `has_valid_voyage` convertidas a binario

---

### Modelos Secuenciales LSTM

Se construyeron dos modelos:

#### 1. **Predicción de `completed_voyage`**
- Datos secuenciales por `unique_id` y `timestamp`
- Modelo: `LSTMClassifier` (PyTorch)
- Exactitud de prueba (`Test Accuracy`): **99.38%**
- Visualización de predicciones secuenciales por usuario
- Manejo robusto de secuencias de longitud variable

#### 2. **Predicción de `has_valid_voyage`**
- Modelo similar con secuencias por `application_date`
- Exactitud en prueba: **99.88%**

---

### Pronósticos con Prophet

Se utilizaron modelos Prophet para pronosticar:

#### 1. **Completitud de Voyage mensual**
- Entrenado con datos de completitud mensual desde 2021
- Proyección de próximos **12 meses**
- Gráficos de tendencias, estacionalidad anual y efecto de días festivos

#### 2. **Envíos de Aplicaciones**
- Pronóstico diario basado en fechas de aplicación
- Gráfica de predicción vs. Tasa de desempleo (U.S.)

---

### Enriquecimiento Externo

- Se integró la **tasa de desempleo de EE.UU.** (`UNRATE`) desde FRED
- Se integraron datos de **Google Trends** para búsquedas de:
  - `Web Developer Job`
  - `Scrum Master`
  - `Product Owner`

> Comparaciones gráficas muestran correlación entre volumen de aplicaciones y popularidad de roles técnicos en el mercado laboral.

---

### Archivos Relacionados

| Archivo | Descripción |
|--------|-------------|
| `applications.csv` | Datos limpios de aplicación |
| `completions.csv`  | Estados de completitud |
| `application_completion-auto_regressive_model.ipynb` | Código completo del análisis |
| `multiTimeline_*.csv` | Tendencias de búsqueda Google para cada rol |

---

### Tecnologías Utilizadas

- `PyTorch`, `Prophet`, `pandas`, `matplotlib`
- `BinaryEncoder` para codificación
- `pad_sequence`, `DataLoader`, `BCEWithLogitsLoss`
- `FRED API` para tasas económicas

## Módulo `Cleaner.py`

Este módulo define la clase `DataCleaner`, desarrollada para realizar limpieza, estandarización y transformación de datos de forma automática y estructurada. Es una herramienta fundamental dentro del proyecto de análisis de la plataforma Chingu.

### Objetivos principales

- Eliminar registros duplicados o erróneos
- Normalizar columnas (fechas, texto, valores monetarios)
- Preparar los datos para análisis estadísticos y modelos predictivos
- Generar archivos limpios para uso directo en notebooks

### Funcionalidades clave

| Función | Descripción |
|--------|-------------|
| `describe_df()` | Muestra resumen general del DataFrame |
| `clean_timestamps()` | Convierte automáticamente columnas de fecha a formato `datetime` |
| `show_missing_values()` | Visualiza datos faltantes en forma numérica y gráfica |
| `handle_missing_values(column, value)` | Rellena valores nulos con un valor personalizado |
| `drop_column(columns)` | Elimina columnas específicas del conjunto de datos |
| `standardize_categorical_data(columns)` | Limpia y estandariza textos categóricos como roles o países |
| `remove_duplicates()` | Elimina registros repetidos por `Unique ID` |
| `convert_numeric_columns()` | Convierte textos numéricos a valores float |
| `convert_currency_column(columns)` | Limpia símbolos de moneda y convierte a número |
| `save_cleaned_data(path)` | Exporta el conjunto limpio en formato CSV |
| `standardize_column_names()` | Renombra columnas eliminando símbolos y espacios innecesarios |

### Beneficios

- Mejora la calidad y coherencia de los datos
- Reduce el tiempo de preparación
- Compatible con librerías de Machine Learning
- Ideal para flujos de trabajo reproducibles

### Dependencias

- pandas  
- numpy  
- matplotlib  
- seaborn  
- plotly  
- statsmodels  
- re  
- itertools

> Esta clase actúa como base para los notebooks de análisis exploratorio y modelado del proyecto Chingu.
## Módulo `Applications_Cleaner.py`

Este módulo define la clase `DataCleaner_Application`, que hereda de `DataCleaner` y está diseñada para limpiar, transformar y categorizar datos de aplicaciones dentro de la plataforma Chingu.io.

### Objetivos y Funcionalidades

- Clasificar fuentes de referencia como Google, Reddit, GitHub, etc.  
- Extraer atributos temporales (mes, semana, año) desde la fecha de aplicación  
- Detectar participación en los programas Voyage  
- Completar datos faltantes de país y código de país  
- Expandir registros con múltiples Voyages  
- Corregir inconsistencias en fechas, géneros y objetivos  
- Vincular datos de aplicación con el calendario oficial de Voyages

### Funciones Clave

| Función | Descripción |
|--------|-------------|
| `extract_application_month()` | Extrae mes y semana desde `Application Date` |
| `extract_application_date()` | Procesa la fecha del estado de suscripción |
| `categorize_source()` | Clasifica texto libre de origen a categorías conocidas |
| `apply_categorization()` | Aplica la clasificación de fuente al conjunto de datos |
| `is_participated_in_voyage()` | Agrega columna binaria para participación en Voyage |
| `standardize_sources()` | Unifica nombres de fuentes similares |
| `update_country_and_country_code()` | Reconcilia país y código de país |
| `explode_based_on_voyage_number()` | Divide filas múltiples por usuario con más de un Voyage |
| `update_voyage_details()` | Relaciona datos con el calendario de Voyages |
| `eleminate_inconsictencies()` | Corrige entradas atípicas o erróneas |
| `update_gender()` | Agrupa géneros menos comunes bajo `other` |
| `update_goal()` | Homogeneiza objetivos ambiguos |
| `standardize_column_names()` | Convierte nombres de columnas al formato snake_case |

### Dependencias

- pandas  
- numpy  
- matplotlib  
- seaborn  
- plotly  
- statsmodels  
- re  
- itertools

> Esta clase es fundamental para preparar los datos de aplicación antes de realizar análisis exploratorios o modelado predictivo.

## Módulo `Transaction_Cleaner.py`

Este módulo contiene la clase `DataCleaner_Transactions`, una extensión de `DataCleaner` enfocada en la limpieza y transformación de datos financieros dentro de la plataforma Chingu.io.

### Funciones Principales

| Función | Descripción |
|--------|-------------|
| `extract_transaction_date()` | Extrae `año`, `mes` y `semana` desde `Transaction Date` |
| `remove_rows_without_date()` | Elimina filas que no tienen fecha válida |
| `manage_subscription_status()` | Normaliza el estado de suscripción a: `active`, `ended`, `no-subscription` |
| `apply_subscription_status_cleaning()` | Aplica esta normalización sobre la columna entera |
| `manage_currency_columns(amount)` | Elimina símbolos como `$` y convierte valores a `float` |
| `apply_currency_update()` | Limpia columnas como `Net Payment`, `Payment Amount`, `Transaction Fee` |
| `remove_high_missing_columns()` | Elimina columnas con muchos datos faltantes como `payee_name`, `notes` |
| `standardize_column_names()` | Estandariza nombres de columnas a formato `snake_case` |

### Aplicaciones

- Análisis de ingresos por mes/semana
- Modelos de predicción financiera
- Evaluación del impacto de productos y campañas
- Preparación de datos para modelos de Machine Learning

### Dependencias

- pandas, numpy  
- matplotlib, seaborn, plotly  
- itertools, re  
- statsmodels.tsa.seasonal
## Módulo `Completion_Cleaner.py`

Este módulo contiene la clase `DataCleaner_completion`, especializada en la limpieza y transformación de los datos de finalización de proyectos (Voyage Completions) dentro de la plataforma **Chingu.io**. Hereda de la clase base `DataCleaner`.

### Objetivos principales

- Extraer el estado final del usuario desde cadenas con múltiples estados (ej.: `"active,inactive,complete"`)
- Eliminar registros sin número de Voyage
- Estandarizar la información de `Tier` de los participantes
- Normalizar nombres de columnas para uso en análisis y modelado

### Funciones Clave

| Función | Descripción |
|--------|-------------|
| `manage_status(status)` | Retorna el último estado desde una cadena separada por comas |
| `apply_status_management()` | Aplica esta limpieza sobre la columna `Status (from Voyage Signups Link)` |
| `remove_rows_without_voyage_number()` | Elimina filas sin información de `Voyage` |
| `update_tier(tier)` | Extrae sólo el nombre del Tier desde descripciones largas |
| `apply_tier_update()` | Limpia la columna de `Tier` en todo el conjunto |
| `standardize_column_names()` | Renombra las columnas en formato `snake_case` para compatibilidad |

### Beneficios

- Mejora la precisión al analizar la finalización de proyectos
- Facilita la integración con otros datasets (como aplicaciones o transacciones)
- Reduce errores por ambigüedad en los campos de estado

### Dependencias

- pandas  
- numpy  
- matplotlib, seaborn, plotly  
- statsmodels  
- re  
- itertools

## Módulo `EDA.py`

Este módulo define la clase `EDA`, utilizada para realizar análisis exploratorios de datos (EDA) de manera automatizada y visual. Proporciona herramientas completas para visualizar la estructura y relaciones de los datos.

### Funciones Principales

| Función | Descripción |
|--------|-------------|
| `display_column_value_counts()` | Muestra los valores más frecuentes por columna |
| `show_data_distribution()` | Genera gráficas estadísticas, incluyendo: |
| &nbsp; • Pie Charts | Para columnas categóricas con pocas clases |
| &nbsp; • Histogramas | Para columnas numéricas |
| &nbsp; • Box Plots | Para detectar outliers |
| &nbsp; • Violin Plots | Para ver la distribución y densidad |
| &nbsp; • Scatter Plots | Relación entre variables numéricas |
| &nbsp; • Scatter con línea de tendencia | Con ajuste lineal (`trendline=ols`) |
| `show_seasonal_decomposition()` | Aplica descomposición estacional (modelo aditivo) a columnas numéricas |

### Detalles Técnicos

- Utiliza `pandas`, `plotly`, `matplotlib`, `seaborn`, `statsmodels`
- Interpola y limpia automáticamente valores nulos e infinitos
- Admite múltiples columnas numéricas en análisis secuencial

### Beneficios

- Permite conocer rápidamente la estructura y problemas del dataset
- Útil como paso previo a cualquier modelo estadístico o de Machine Learning
- Ideal para análisis descriptivo y visualización en dashboards


### README.md
Documento principal del proyecto que describe su propósito, estructura y guía de uso.


## Entorno Técnico y Herramientas

Para llevar a cabo el análisis, se diseñó una arquitectura técnica robusta basada en herramientas de Big Data, automatización de flujos y minería de datos:

### 1. Contenedor Docker

Se creó un contenedor Docker personalizado llamado `docker-hadoop`, que actúa como orquestador de la infraestructura.

### 2. Clúster Hadoop

- **Nodo Principal (NameNode)**: `namenode`
- **Nodos Secundarios**: 2 nodos adicionales
- Responsable del almacenamiento distribuido de los archivos.

### 3. Ingesta con Apache NiFi

Se implementó **Apache NiFi** para automatizar el movimiento de archivos hacia el clúster Hadoop de forma eficiente y controlada.

### 4. Backup con Apache Cassandra

Se configuró un clúster de respaldo distribuido con:
- `cassandra-seed`
- `cassandra-node1`
- `cassandra-node2`

Permite replicación y redundancia de datos clave del proyecto.

### 5. BIGQuery
##  Análisis con Google BigQuery

Se utilizó Google BigQuery como motor de análisis para unir las principales fuentes de datos de la plataforma Chingu (`applications`, `transactions`, `completions`) y ejecutar consultas SQL escalables y eficientes.

###  Objetivos Principales

1. Comprender la distribución de usuarios por estado de suscripción  
2. Evaluar qué productos generan más ingresos o transacciones  
3. Calcular la tasa de finalización de proyectos según el rol en el Voyage  
4. Analizar los niveles de satisfacción a través del NPS (Net Promoter Score)

![image](https://github.com/user-attachments/assets/8b388d38-8c85-433d-b2a1-d38b2b1ff6c2)
* Recuento de usuarios por estado de suscripción
![image](https://github.com/user-attachments/assets/145578e2-11dd-4e80-acd0-06595e9f5695)
![image](https://github.com/user-attachments/assets/f6c291e3-6f6d-4972-8081-92763d05de58)
* Pago neto promedio por producto
![image](https://github.com/user-attachments/assets/7bee5f78-6d34-424f-9eb0-a295f52b75b5)
![image](https://github.com/user-attachments/assets/10d5b8c5-91e0-47cb-b912-e9283af6a3c2)
* Completion Rate by Voyage Role
![image](https://github.com/user-attachments/assets/8b29dbd7-8416-4537-8137-d2e11bba3572)
![image](https://github.com/user-attachments/assets/072e2024-345c-42df-91aa-b9f20ecbfd7b)
* Distribución de puntuaciones del NPS
![image](https://github.com/user-attachments/assets/50786f05-c71c-415d-9a01-120eca326169)
![image](https://github.com/user-attachments/assets/6d3cda07-014e-40b0-b69f-ed341662a894)
)





## 6. Dashboard Analítico de Chingu

Este dashboard fue diseñado para proporcionar una visión integral y dinámica de los datos de la plataforma Chingu, permitiendo analizar interactivamente la actividad de los usuarios, ingresos y participación en los proyectos.

### Herramientas Utilizadas

- Power BI 
- Datos procesados desde:
  - `applications.csv`
  - `transactions.csv`
  - `completions.csv`
  - `voyage_schedule.csv`

### Secciones del Dashboard

| Sección | Descripción |
|--------|-------------|
| **Análisis de Aplicaciones** | Métricas de usuarios, objetivos y fuentes de registro |
| **Ingresos y Transacciones** | Monto de pagos, productos y estado de suscripción |
| **Participación en Voyages** | Distribución de roles, estado de finalización y certificados |
| **Tendencias Temporales** | Análisis por hora, día, mes y año |
| **Análisis Geográfico** | Mapa de calor según país de origen de los usuarios |
| **Filtros Interactivos** | Por rol, género, suscripción, producto, país, entre otros |

![image](https://github.com/user-attachments/assets/f515497b-9ea5-47f6-ba35-17b16e6ec787)
![image](https://github.com/user-attachments/assets/98722acc-36a8-445c-85da-af2d5289ff5e)
![image](https://github.com/user-attachments/assets/f12ce49d-4e54-466d-acd6-6467aa6871a5)
![image](https://github.com/user-attachments/assets/0fdb6416-df8e-424f-a8a8-528050a88072)
![image](https://github.com/user-attachments/assets/16116ec0-ba6d-412b-948b-f309203b2907)
![image](https://github.com/user-attachments/assets/0e5927bb-b29e-4ca4-aa21-50dd55ec4a75).





### Aplicaciones

- Informes estratégicos para equipos de producto y marketing
- Análisis de conversión de aplicación a finalización
- Medición del impacto de campañas de adquisición
- Toma de decisiones basada en datos para crecimiento de la plataforma



### 7. Minería de Datos con Orange

##  Análisis con Orange Data Mining

Se utilizaron flujos de trabajo en **Orange Data Mining** para realizar análisis exploratorios, aprendizaje automático y evaluación de modelos de manera visual e interactiva.

---

###  Carga y Preprocesamiento de Datos

- **File / Data Table**: Lectura del archivo CSV y visualización inicial de los datos.
- **Preprocess**: Limpieza y transformación de datos incluyendo manejo de valores faltantes, normalización, codificación categórica y discretización.

---

###  Visualización de Datos

- **Heat Map**, **Bar Plot**, **Violin Plot**, **Scatter Plot**, **Line Plot**: Se aplicaron para identificar relaciones, correlaciones y distribución de variables clave.
- **Feature Statistics**: Análisis estadístico básico por atributo.

---

###  Análisis Predictivo

#### Clasificación

- **Modelos utilizados**:
  - Árbol de Decisión (Tree)
  - k-NN (k Nearest Neighbors)
  - Regresión Logística
  - Random Forest

- **Evaluación**:
  - **Test and Score**: Cálculo de precisión, recall, F1 y AUC
  - **Confusion Matrix**: Visualización del desempeño del modelo
  - **ROC Analysis**: Curva ROC para comparar modelos
  - **Rank**: Comparación entre algoritmos

#### Reducción de Dimensiones

- **PCA**: Reducción de dimensiones para visualización y preparación de entrada a modelos.

#### Clustering

- **k-Means**: Agrupamiento no supervisado para identificar segmentos de usuarios.

---

###  Resultados Clave

- Se identificaron modelos con alta precisión en la predicción de comportamiento de usuarios (ej. regresión logística con alta AUC).
- Visualizaciones revelaron correlaciones entre atributos como rol, país y resultados de finalización.
- El uso de Orange permitió una exploración rápida y visual sin necesidad de codificación manual.

---
![image](https://github.com/user-attachments/assets/a68cbd73-bb55-4e2a-b56b-8ec29d04c288)
**
###  Herramientas Utilizadas

- Orange Data Mining 3.x
- Widgets: File, Preprocess, Tree, kNN, Logistic Regression, PCA, Test and Score, Confusion Matrix, ROC, Rank, Scatter Plot, etc.

---

> Este flujo visual facilitó la validación de hipótesis rápidamente y ayudó a complementar los análisis hechos con Python y BigQuery.

### 8. Metodología de Ciencia de Datos

Se siguió la metodología **CRISP-DM**, que consta de:
- Comprensión del negocio



