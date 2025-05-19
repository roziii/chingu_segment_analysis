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
###  Gestión del Proyecto – Tablero de Progreso

El desarrollo del proyecto se organiza mediante un tablero de seguimiento visual en GitHub, dividido en diferentes columnas que representan el estado de cada tarea. Esta estructura permite mantener una visión clara del avance y facilita la colaboración entre miembros del equipo.

<p align="center">
  <img src="/assets/fig_1.png" alt="image" />
  <br><em>fig_1</em>
</p>

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

## Applications_EDA.ipynb

### 🎯 Objetivo
El propósito de este notebook es realizar un análisis exploratorio de las aplicaciones registradas en la plataforma Chingu, para descubrir patrones, tendencias y problemas de calidad en los datos.

---

### 🧰 Metodología Utilizada

#### Preprocesamiento de Datos
- Limpieza de valores nulos y columnas irrelevantes
- Uso de la clase `DataCleaner_Application`

#### Normalización y Estandarización
- Homogeneización de nombres de columnas
- Clasificación de campos como género, rol en el Voyage, objetivos, etc.

<p align="center">
  <img src="/assets/fig_4.png" alt="Distribución de género en aplicaciones registradas" />
  <br><em>fig_4</em>
</p>

#### Análisis Descriptivo
- Estadísticas generales: media, desviación estándar, percentiles
- Conteo de valores por categoría (por ejemplo: fuentes, países, géneros)

---

### 🧮 Métodos Matemáticos Aplicados

- Estadísticas básicas: media, mediana, desviación estándar, conteos
- Análisis de variables categóricas mediante frecuencias relativas
- Conversión temporal para agrupar por semanas y meses
- Evaluación de participación (`0` o `1`) como variable binaria

---

### 📊 Análisis de Distribución

#### Distribución temporal
- Evaluación de la distribución de las fechas, semanas y meses de las aplicaciones

<p align="center">
  <img src="/assets/fig_8.png" alt="Histograma del año de registro de aplicaciones" />
  <br><em>fig_8</em>
</p>

#### Participación en Voyages
- Segmentación por usuarios con o sin participación (`has_voyage`)

<p align="center">
  <img src="/assets/fig_9.png" alt="Distribución binaria de participación en proyectos Voyage" />
  <br><em>fig_9</em>
</p>

---

### 📈 Visualizaciones Específicas

#### 1. Distribución de `subscription_status`

<p align="center">
  <img src="/assets/fig_2.png" alt="Porcentaje de usuarios activos e inactivos según su estado de suscripción" />
  <br><em>fig_2</em>
</p>

#### 2. Distribución de `voyage_role`

<p align="center">
  <img src="/assets/fig_3.png" alt="Distribución de roles solicitados por los participantes (Developer, Product Owner, etc.)" />
  <br><em>fig_3</em>
</p>

#### 3. Distribución de `goal`

<p align="center">
  <img src="/assets/fig_5.png" alt="Motivaciones principales de los usuarios para unirse a Chingu" />
  <br><em>fig_5</em>
</p>

#### 4. Histograma de `application_age_in_days`

<p align="center">
  <img src="/assets/fig_6.png" alt="Antigüedad en días de las aplicaciones registradas" />
  <br><em>fig_6</em>
</p>

#### 5. Histograma de `no_voyages_started`

<p align="center">
  <img src="/assets/fig_7.png" alt="Cantidad de Voyages iniciados por cada usuario" />
  <br><em>fig_7</em>
</p>

---

### 📤 Salidas Generadas

- Conteo de participantes por rol, género y país
- Análisis de fuentes de tráfico (Google, YouTube, LinkedIn, etc.)
- Visualización del número de aplicaciones por año/mes/semana
- Exportación de datos limpios para uso posterior en modelos predictivos


## Transaction_EDA.ipynb

### 🎯 Objetivo
Este notebook tiene como propósito analizar los datos de transacciones de la plataforma Chingu.io. Busca entender los patrones de ingresos, fuentes de pago y comportamientos temporales en las contribuciones recibidas.

---

### 🧰 Metodología Aplicada

#### Preprocesamiento
- Limpieza de datos nulos y valores inválidos
- Eliminación de registros sin fecha
- Estandarización de nombres de columnas

#### Estadísticas Descriptivas
- Cálculo de promedios, medianas, desviaciones estándar, mínimos y máximos
- Recuento de valores para campos categóricos como estado de suscripción, producto y fuente de pago

<p align="center">
  <img src="/assets/fig_10.png" alt="Distribución de estado de suscripción: active, no-subscription y ended" />
  <br><em>fig_10</em>
</p>

<p align="center">
  <img src="/assets/fig_11.png" alt="Distribución de fuentes de pago: Discord, Stripe, Buy Me a Coffee, etc." />
  <br><em>fig_11</em>
</p>

<p align="center">
  <img src="/assets/fig_12.png" alt="Distribución de productos comprados en la plataforma (suscripciones, donaciones, certificados, etc.)" />
  <br><em>fig_12</em>
</p>

<p align="center">
  <img src="/assets/fig_13.png" alt="Distribución de certificados por Voyage (V47, V48, etc.) o sin certificado" />
  <br><em>fig_13</em>
</p>

<p align="center">
  <img src="/assets/fig_14.png" alt="Histograma de comisiones por transacción (transaction_fee)" />
  <br><em>fig_14</em>
</p>

---

### 📊 Análisis de Distribución
- Exploración de columnas clave usando histogramas y gráficos de barras
- Análisis por año, mes y semana de transacción

---

### 📉 Descomposición Estacional
- Aplicación de técnicas estadísticas para descubrir patrones estacionales en los ingresos y comisiones

---

### 🧮 Técnicas Matemáticas Aplicadas
- Estadística básica: media, mediana, percentiles, etc.
- Agrupación por tiempo: año, mes, semana
- Descomposición estacional de series temporales (`seasonal_decomposition`)
- Clasificación por frecuencia de ocurrencia

---

### 📤 Resultados Obtenidos
- Distribución de fuentes de ingresos
- Participación por tipo de producto (donaciones, suscripciones, certificados)
- Fluctuaciones mensuales y semanales en los ingresos
- Dataset limpio listo para modelos predictivos o dashboards


## completion_EDA.ipynb

### 🎯 Objetivo
El propósito de este notebook es analizar los datos relacionados con la finalización de proyectos en el programa Voyage de Chingu. Se estudian variables como el estado de finalización, emisión de certificados, satisfacción del usuario y su relación con niveles (Tier) y roles.

---

### 🧰 Metodología Aplicada

#### Preprocesamiento
- Eliminación de columnas textuales y comentarios irrelevantes
- Normalización de nombres de columnas
- Eliminación de filas sin número de Voyage

#### Tratamiento de Campos Clave
- Limpieza de columnas `completion_status`, `product`, `tier`, etc.
- Imputación de valores nulos con etiquetas como `"undefined"` o `"no_product"`
- Conversión de fechas y manejo de formatos

---

### 📊 Análisis Descriptivo
- Conteo total de registros: **2968**
- Satisfacción promedio del usuario: **9.26 / 10**
- Certificados emitidos: **1223**
- Clasificación por rol, nivel (Tier) y tipo de producto

<p align="center">
  <img src="/assets/fig_15.png" alt="Distribución de finalización de los proyectos (Yes, No, undefined, TBD)" />
  <br><em>fig_15</em>
</p>

<p align="center">
  <img src="/assets/fig_16.png" alt="Distribución de productos asociados a los usuarios que completaron el Voyage" />
  <br><em>fig_16</em>
</p>

<p align="center">
  <img src="/assets/fig_17.png" alt="Histograma de satisfacción del usuario (escala de 0 a 10)" />
  <br><em>fig_17</em>
</p>

---

### 🧮 Técnicas Matemáticas Aplicadas
- Estadísticas básicas: media, mediana, desviación estándar
- Frecuencias de variables categóricas
- Análisis de puntuación en escalas (de 0 a 10)
- Procesamiento de fechas para análisis temporales

---

### 📤 Resultados
- Exportación de dataset limpio en CSV
- Análisis de estados: `Completed`, `Incomplete`, `Dropped`, etc.
- Evaluación de satisfacción del usuario
- Asociación entre niveles (Tier) y finalización

## Análisis de Transacciones – `transactions.ipynb`

### Objetivo del Proyecto

Analizar los datos de transacciones realizadas por usuarios de Chingu.io para:

- Detectar patrones de comportamiento de compra.
- Segmentar usuarios en grupos basados en sus hábitos financieros.
- Predecir su disposición a pagar montos más altos.

---

### Metodología Aplicada

#### 1. Preprocesamiento de Datos

- Limpieza de valores nulos y erróneos.
- Normalización de columnas categóricas.
- Conversión de fechas y extracción de variables temporales.

#### 2. Análisis Descriptivo

##### Frecuencia diaria de transacciones

Crecimiento progresivo de actividad desde 2023 hasta inicios de 2025.

<p align="center">
  <img src="assets/fig_18.png" alt="Frecuencia diaria de transacciones" />
  <br><em>fig_18</em>
</p>

##### Frecuencia mensual de transacciones

Tendencia clara de aumento sostenido desde finales de 2023.

<p align="center">
  <img src="assets/fig_19.png" alt="Frecuencia mensual de transacciones" />
  <br><em>fig_19</em>
</p>

##### Frecuencia anual de transacciones

2024 lidera ampliamente en volumen total de transacciones.

<p align="center">
  <img src="assets/fig_20.png" alt="Frecuencia anual de transacciones" />
  <br><em>fig_20</em>
</p>

##### Distribución de montos de pago

Distribución multimodal. El grupo principal está entre $2.5 y $2.7.

<p align="center">
  <img src="assets/fig_21.png" alt="Distribución de montos de pago" />
  <br><em>fig_21</em>
</p>

##### Gasto total por producto

El mayor ingreso proviene de la suscripción Junior Professional.

<p align="center">
  <img src="assets/fig_22.png" alt="Gasto total por producto" />
  <br><em>fig_22</em>
</p>

---

### Modelado Predictivo

Se entrenó un modelo de regresión logística para predecir si un usuario realizará un pago alto.

##### Interpolación: comparación de pago neto real vs predicho

<p align="center">
  <img src="assets/fig_23.png" alt="Interpolación de pago neto" />
  <br><em>fig_23</em>
</p>

##### Extrapolación: predicción más allá del rango observado

<p align="center">
  <img src="assets/fig_24.png" alt="Extrapolación de pago neto" />
  <br><em>fig_24</em>
</p>

Evaluación del Modelo:
- Precisión: 99%
- AUC: 0.97
- MSE: 0.03
- R²: 0.90

---

### Segmentación de Usuarios

Mediante K-Means Clustering, se agruparon usuarios en 3 clústeres diferenciados por:

- Nivel de gasto.
- Estado de suscripción.
- Tipo de producto adquirido.

---

### Resultados Clave

- Pago promedio: $3.27 USD
- Los usuarios con suscripciones activas y productos profesionales generan más ingresos.
- El modelo predictivo muestra excelente rendimiento.
- Hay una clara evolución de crecimiento en la actividad financiera durante 2024.

### application_completion.ipynb

#### Objetivo:
El objetivo de este archivo es predecir si un usuario completará su proyecto Voyage utilizando datos de aplicaciones, participación y retroalimentación.

#### Metodología aplicada
* **Preprocesamiento**
  - Fusión de datos de aplicaciones y finalización
  - Relleno de valores nulos
  - Codificación categórica con BinaryEncoder
  - Escalado con StandardScaler
  - Reducción de Dimensionalidad
    - Aplicación de PCA para conservar el 95% de la varianza con 59 componentes
    - Identificación de los 10 atributos más influyentes
  - Selección de características con Linear SVC
  - Eliminación de atributos irrelevantes mediante penalización L1

* **Entrenamiento de Modelos**
  - Regresión Logística
  - Random Forest
  - Optimización de hiperparámetros con GridSearchCV
  - Separación de datos para validación y extrapolación

* **Evaluación del modelo**
  - Métricas usadas:
    - Matriz de confusión
    - Curva ROC
    - AUC
    - F1 Score

##### ROC Curvas

<p align="center">
  <img src="assets/fig_25.png" alt="ROC Curve - Logistic Regression" />
  <br><em>ROC Curve - Logistic Regression</em>
</p>

<p align="center">
  <img src="assets/fig_27.png" alt="ROC Curve - Logistic Regression (Extra)" />
  <br><em>ROC Curve - Logistic Regression (Extra)</em>
</p>

<p align="center">
  <img src="assets/fig_28.png" alt="ROC Curve - Random Forest" />
  <br><em>ROC Curve - Random Forest</em>
</p>

<p align="center">
  <img src="assets/fig_31.png" alt="ROC Curve - Random Forest (Extra)" />
  <br><em>ROC Curve - Random Forest (Extra)</em>
</p>

##### Matrices de Confusión

<p align="center">
  <img src="assets/fig_26.png" alt="Confusion Matrix - Logistic Regression (Extra)" />
  <br><em>Confusion Matrix - Logistic Regression (Extra)</em>
</p>

<p align="center">
  <img src="assets/fig_30.png" alt="Confusion Matrix - Random Forest (Extra)" />
  <br><em>Confusion Matrix - Random Forest (Extra)</em>
</p>

#### Métodos matemáticos utilizados:
- PCA
- Codificación binaria y Label Encoding
- Modelos de clasificación: Logistic Regression y Random Forest
- Grid Search CV para optimización
- Evaluación con AUC, ROC, F1 Score

#### Resultados principales

| Modelo                   | F1 Score | AUC    |
|--------------------------|----------|--------|
| Logistic Regression      | 0.9063   | 0.9571 |
| Random Forest            | 0.9737   | 0.9977 |
| Logistic (Extra)         | —        | 0.9681 |
| Random Forest (Extra)    | —        | 0.9982 |

##  Análisis Enriquecido del Proyecto `application_voyage_list_merge.ipynb`

###  Objetivo
Predecir la participación de usuarios en futuros Voyages de Chingu.io a partir de datos de aplicación, transacciones y finalización de proyectos, utilizando visualización, reducción de dimensiones y modelos de aprendizaje automático.

---

## 1.  Análisis Exploratorio

- **Días de mayor aplicación**: lunes y martes  
- **Roles más comunes**: Developer, Product Owner, Scrum Master  
- **Objetivos frecuentes**: mejorar CV, encontrar equipo, experiencia colaborativa

<p align="center">
  <img src="assets/fig_32.png" alt="fig_32" />
</p>

<p align="center">
  <img src="assets/fig_33.png" alt="fig_33" />
</p>

---

## 2.  Tendencias Temporales

- Pico de aplicaciones: años **2021 y 2022**
- Aumento de roles técnicos
- Mayor participación en Voyages entre **julio y noviembre**

<p align="center">
  <img src="assets/fig_34.png" alt="fig_34" />
</p>

<p align="center">
  <img src="assets/fig_35.png" alt="fig_35" />
</p>

<p align="center">
  <img src="assets/fig_36.png" alt="fig_36" />
</p>

<p align="center">
  <img src="assets/fig_37.png" alt="fig_37" />
</p>

<p align="center">
  <img src="assets/fig_38.png" alt="fig_38" />
</p>

---

## 3.  Modelado Predictivo: `has_voyage`

Variable objetivo: `has_voyage` (0 o 1)

**Modelo utilizado**: `Random Forest Classifier`

| Dataset         | Precisión | F1 Score | AUC  |
|-----------------|-----------|----------|------|
| Test            | 100%      | 1.00     | 1.00 |
| Extrapolación   | 100%      | 1.00     | 1.00 |

<p align="center">
  <img src="assets/fig_39.png" alt="fig_39" />
</p>

<p align="center">
  <img src="assets/fig_40.png" alt="fig_40" />
</p>

<p align="center">
  <img src="assets/fig_41.png" alt="fig_41" />
</p>

<p align="center">
  <img src="assets/fig_42.png" alt="fig_42" />
</p>

---

## 4.  Reducción de Dimensiones (PCA)

- **Componentes retenidos**: 24 (95% de la varianza)
- **Variables más influyentes**: país de origen, fuente, rol, objetivo, estado de suscripción

<p align="center">
  <img src="assets/fig_43.png" alt="fig_43" />
</p>

---

## 5. 🔗 Datos Combinados: Aplicación + Transacciones

- Total de usuarios únicos: **2,287**
- Archivos: `applications.csv`, `transactions.csv`, `completions.csv`

---

## 6.  Selección de Características (PCA Combinado)

<p align="center">
  <img src="assets/fig_44.png" alt="fig_44" />
</p>

<p align="center">
  <img src="assets/fig_45.png" alt="fig_45" />
</p>

<p align="center">
  <img src="assets/fig_46.png" alt="fig_46" />
</p>

<p align="center">
  <img src="assets/fig_47.png" alt="fig_47" />
</p>

<p align="center">
  <img src="assets/fig_48.png" alt="fig_48" />
</p>

---

## 7.  Modelos de Clasificación: `subscription_status`

| Modelo                | Accuracy | F1 Score | AUC     |
|------------------------|----------|----------|---------|
| Random Forest          | 94.48%   | 0.9431   | 0.9930  |
| **Gradient Boosting**  | **95.57%** | **0.9551** | **0.9920** |
| Logistic Regression    | 86.44%   | 0.8640   | 0.9559  |

<p align="center">
  <img src="assets/fig_49.png" alt="fig_49" />
</p>

<p align="center">
  <img src="assets/fig_50.png" alt="fig_50" />
</p>

<p align="center">
  <img src="assets/fig_51.png" alt="fig_51" />
</p>

<p align="center">
  <img src="assets/fig_52.png" alt="fig_52" />
</p>

<p align="center">
  <img src="assets/fig_53.png" alt="fig_53" />
</p>

<p align="center">
  <img src="assets/fig_54.png" alt="fig_54" />
</p>

<p align="center">
  <img src="assets/fig_55.png" alt="fig_55" />
</p>

<p align="center">
  <img src="assets/fig_56.png" alt="fig_56" />
</p>

<p align="center">
  <img src="assets/fig_57.png" alt="fig_57" />
</p>

<p align="center">
  <img src="assets/fig_58.png" alt="fig_58" />
</p>

<p align="center">
  <img src="assets/fig_59.png" alt="fig_59" />
</p>

<p align="center">
  <img src="assets/fig_60.png" alt="fig_60" />
</p>

---

## 8.  Modelado de Regresión: `net_payment`

**Modelo utilizado**: `Gradient Boosting Regressor`

| Métrica       | Test Set | Extrapolación |
|---------------|----------|---------------|
| MAE           | 0.44     | 0.50          |
| R² Score      | 0.83     | 0.75          |

<p align="center">
  <img src="assets/fig_61.png" alt="fig_61" />
</p>

<p align="center">
  <img src="assets/fig_62.png" alt="fig_62" />
</p>

---

##  Archivos Relacionados

- `application_voyage_list_merge.ipynb`: análisis de postulaciones
- `Transaction_Application_analysis.ipynb`: análisis combinado
- `merged_dataset.csv`: dataset final para modelado


## application_completion-auto_regressive_model

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

#### 1. Predicción de `completed_voyage`

- Datos secuenciales por `unique_id` y `timestamp`
- Modelo: `LSTMClassifier` (PyTorch)
- Exactitud de prueba: **99.38%**

<p align="center">
  <img src="assets/fig_63.png" alt="fig_63" />
  <br><em>fig_63 - Secuencia de predicción para completed_voyage</em>
</p>

#### 2. Predicción de `has_valid_voyage`

- Modelo similar con secuencias por `application_date`
- Exactitud en prueba: **99.88%**

---

### Pronósticos con Prophet

Se utilizaron modelos Prophet para pronosticar:

#### 1. Completitud de Voyage mensual

- Entrenado con datos de completitud mensual desde 2021
- Proyección de próximos 12 meses

<p align="center">
  <img src="assets/fig_64.png" alt="fig_64" />
  <br><em>fig_64 - Pronóstico de completitud</em>
</p>

#### 2. Envíos de Aplicaciones vs. Desempleo

<p align="center">
  <img src="assets/fig_65.png" alt="fig_65" />
  <br><em>fig_65 - Completitud vs Tasa de Desempleo (EE.UU.)</em>
</p>

<p align="center">
  <img src="assets/fig_66.png" alt="fig_66" />
  <br><em>fig_66 - Aplicaciones vs Tasa de Desempleo (EE.UU.)</em>
</p>

---

### Enriquecimiento Externo

Se integraron variables externas para mejorar la capacidad predictiva:

- **Tasa de desempleo de EE.UU.** (`UNRATE`)
- **Tendencias de Google**:
  - Búsquedas de `Web Developer Job`
  - Búsquedas de `Scrum Master`
  - Búsquedas de `Product Owner`

<p align="center">
  <img src="assets/fig_67.png" alt="fig_67" />
  <br><em>fig_67 - Aplicaciones vs Interés en Web Developer</em>
</p>

<p align="center">
  <img src="assets/fig_68.png" alt="fig_68" />
  <br><em>fig_68 - Aplicaciones vs Interés en Scrum Master</em>
</p>

<p align="center">
  <img src="assets/fig_69.png" alt="fig_69" />
  <br><em>fig_69 - Aplicaciones vs Interés en Product Owner</em>
</p>

---

### Resultados de Modelos LSTM

| Modelo                | Métrica        | Valor     |
|------------------------|----------------|-----------|
| LSTM - `completed_voyage` | Accuracy       | 99.38%    |
| LSTM - `has_valid_voyage` | Accuracy       | 99.88%    |

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

## 5. BIGQuery

### Análisis con Google BigQuery

Se utilizó Google BigQuery como motor de análisis para unir las principales fuentes de datos de la plataforma Chingu (`applications`, `transactions`, `completions`) y ejecutar consultas SQL escalables y eficientes.

---

### Objetivos Principales

1. Comprender la distribución de usuarios por estado de suscripción  
2. Evaluar qué productos generan más ingresos o transacciones  
3. Calcular la tasa de finalización de proyectos según el rol en el Voyage  
4. Analizar los niveles de satisfacción a través del NPS (Net Promoter Score)

---

### Recuento de usuarios por estado de suscripción

<p align="center">
  <img src="assets/fig_70.png" alt="Image 70" />
  <br><em>Consulta de unión de tablas</em>
</p>

<p align="center">
  <img src="assets/fig_71.png" alt="Image 71" />
  <br><em>Distribución de usuarios por estado de suscripción</em>
</p>

---

### Pago neto promedio por producto

<p align="center">
  <img src="assets/fig_72.png" alt="Image 72" />
  <br><em>Consulta por producto</em>
</p>

<p align="center">
  <img src="assets/fig_73.png" alt="Image 73" />
  <br><em>Promedio de pago neto y cantidad de transacciones</em>
</p>

| Producto                           | Pago Promedio (USD) | Cantidad de Transacciones |
|------------------------------------|----------------------|----------------------------|
| SUBSCRIPTION - Professional        | 9.02                 | 513                        |
| DONATION                           | 8.97                 | 1275                       |
| SUBSCRIPTION - Junior Professional | 2.72                 | 9437                       |
| PRODUCT - Voyage Certificate       | 2.57                 | 1185                       |

---

### Completion Rate por rol en el Voyage

<p align="center">
  <img src="assets/fig_74.png" alt="Image 74" />
  <br><em>Consulta por rol</em>
</p>

<p align="center">
  <img src="assets/fig_75.png" alt="Image 75" />
  <br><em>Tasa de finalización por rol</em>
</p>

| Rol              | Completions | Aplicaciones Totales | Completion Rate (%) |
|------------------|-------------|-----------------------|----------------------|
| Unknown          | 152         | 631                   | 24.09                |
| Scrum Master     | 44          | 192                   | 22.92                |
| Developer        | 1433        | 6514                  | 22.00                |
| UI/UX Designer   | 73          | 563                   | 12.97                |
| Product Owner    | 77          | 680                   | 11.32                |
| Data Scientist   | 29          | 686                   | 4.23                 |

---

### Distribución de Net Promoter Score (NPS)

<p align="center">
  <img src="assets/fig_76.png" alt="Image 76" />
  <br><em>Consulta NPS</em>
</p>

<p align="center">
  <img src="assets/fig_77.png" alt="Image 77" />
  <br><em>Distribución de NPS</em>
</p>

| NPS Score | Usuarios |
|-----------|----------|
| 10        | 8905     |
| 9         | 1092     |
| 8         | 628      |
| 7         | 149      |
| 6         | 203      |
| 5         | 49       |
| 3         | 288      |
| null      | 1096     |

---

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

<p align="center">
  <img src="assets/fig_79.png" alt="Distribución de aplicaciones por género, objetivo, fuente y fecha" />
  <br><em>fig_79</em>
</p>

<p align="center">
  <img src="assets/fig_80.png" alt="Distribución de certificados emitidos por Voyage y por rol" />
  <br><em>fig_80</em>
</p>

<p align="center">
  <img src="assets/fig_81.png" alt="Versión extendida de certificados emitidos por rol y estado" />
  <br><em>fig_81</em>
</p>

<p align="center">
  <img src="assets/fig_82.png" alt="Evolución del NPS a lo largo del tiempo y promedio por Voyage" />
  <br><em>fig_82</em>
</p>

<p align="center">
  <img src="assets/fig_83.png" alt="Participantes por Voyage, tasa de finalización y emisión de certificados por año" />
  <br><em>fig_83</em>
</p>

<p align="center">
  <img src="assets/fig_84.png" alt="Embudo del recorrido del usuario por país" />
  <br><em>fig_84</em>
</p>

### Aplicaciones

- Informes estratégicos para equipos de producto y marketing
- Análisis de conversión de aplicación a finalización
- Medición del impacto de campañas de adquisición
- Toma de decisiones basada en datos para crecimiento de la plataforma


## 7. Minería de Datos con Orange

## Análisis con Orange Data Mining

Se utilizaron flujos de trabajo en **Orange Data Mining** para realizar análisis exploratorios, aprendizaje automático y evaluación de modelos de manera visual e interactiva.

---

### Carga y Preprocesamiento de Datos

- **File / Data Table**: Lectura del archivo CSV y visualización inicial de los datos.
- **Preprocess**: Limpieza y transformación de datos incluyendo manejo de valores faltantes, normalización, codificación categórica y discretización.

---

### Visualización de Datos

- **Heat Map**, **Bar Plot**, **Violin Plot**, **Scatter Plot**, **Line Plot**: Se aplicaron para identificar relaciones, correlaciones y distribución de variables clave.
- **Feature Statistics**: Análisis estadístico básico por atributo.

---

### Análisis Predictivo

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

### Resultados Clave

- Se identificaron modelos con alta precisión en la predicción de comportamiento de usuarios (ej. regresión logística con alta AUC).
- Visualizaciones revelaron correlaciones entre atributos como rol, país y resultados de finalización.
- El uso de Orange permitió una exploración rápida y visual sin necesidad de codificación manual.

---

<p align="center">
  <img src="assets/fig_85.png" alt="Flujo de trabajo en Orange: carga de datos, visualización, clustering y clasificación" />
  <br><em>fig_85</em>
</p>

##  Herramientas Utilizadas

- Orange Data Mining 3.x
- Widgets: File, Preprocess, Tree, kNN, Logistic Regression, PCA, Test and Score, Confusion Matrix, ROC, Rank, Scatter Plot, etc.

---

> Este flujo visual facilitó la validación de hipótesis rápidamente y ayudó a complementar los análisis hechos con Python y BigQuery.

## 8. Infraestructura Docker para Procesamiento de Datos

Se utilizó Docker para desplegar una arquitectura distribuida basada en contenedores, facilitando el análisis y almacenamiento de datos en gran escala.

###  Contenedores Desplegados

| Contenedor         | Imagen                      | Función                          |
|--------------------|-----------------------------|----------------------------------|
| `hadoop-docker`    | Configuración personalizada | Orquestador del clúster Hadoop   |
| `namenode`         | `bde2020/hadoop-namenode`   | Nodo maestro HDFS                |
| `datanode1`        | `bde2020/hadoop-datanode`   | Nodo de almacenamiento           |
| `datanode2`        | `bde2020/hadoop-datanode`   | Nodo de almacenamiento           |
| `nifi`             | `apache/nifi:1.24.0`        | Ingesta y automatización de datos|
| `cassandra-seed`   | `cassandra:4.1`             | Nodo semilla de Cassandra        |
| `cassandra-node1`  | `cassandra:4.1`             | Nodo de datos                    |
| `cassandra-node2`  | `cassandra:4.1`             | Nodo de datos                    |

###  Resumen Técnico

- **Hadoop** permite almacenamiento distribuido con NameNode y DataNodes.
- **NiFi** automatiza flujos ETL (por ejemplo, CSV hacia HDFS).
- **Cassandra** almacena datos críticos con replicación entre nodos.

> Todos los contenedores están gestionados desde Docker Desktop.

###  Flujo de Datos con Apache NiFi

Este flujo implementado en **Apache NiFi** automatiza la ingesta, transformación y almacenamiento de los archivos CSV utilizados en el análisis de datos de la plataforma **Chingu.io**.

####  Descripción del Flujo

1. **GetFile**  
   - Escanea el directorio `/opt/nifi/input` para detectar archivos nuevos (como `applications.csv`, `transactions.csv`, etc.).

2. **ConvertRecord**  
   - Convierte los archivos CSV a registros estructurados utilizando `CSVReader` y `JsonRecordSetWriter`.

3. **RouteOnAttribute**  
   - Clasifica los archivos en función de su nombre (`filename`) y los redirige según el contenido:
     - `applications.csv` → tabla `applications_backup`
     - `transactions.csv` → tabla `transactions_backup`
     - `completions.csv` → tabla `completions_backup`
     - `voyage_schedule.csv` → tabla `voyage_schedule_backup`
     - `merged_applications_transactions.csv` → tabla combinada

4. **PutCassandraRecord**  
   - Inserta los datos directamente en las tablas correspondientes de **Apache Cassandra**.

5. **PutHDFS** *(en paralelo)*  
   - Crea una copia de seguridad en el sistema distribuido HDFS (`/user/nifi`).

---

#### Componentes Principales

| Componente           | Función                                               |
|----------------------|--------------------------------------------------------|
| `GetFile`            | Detección de nuevos archivos CSV                      |
| `ConvertRecord`      | Conversión a registros estructurados                  |
| `RouteOnAttribute`   | Enrutamiento según el tipo de archivo                 |
| `PutCassandraRecord` | Inserción en Cassandra                                |
| `PutHDFS`            | Almacenamiento en Hadoop HDFS                         |

---

#### Servicios Utilizados

- `CSVReader` como lector de registros
- `JsonRecordSetWriter` como escritor intermedio
- `CassandraConnectionProvider` para conexión con Cassandra
- Atributos como `filename` para lógica condicional

> Este flujo permite un manejo robusto, escalable y automatizado del pipeline de datos desde su origen hasta el almacenamiento distribuido.


### 9. Metodología de Ciencia de Datos

Se siguió la metodología **CRISP-DM** (Cross Industry Standard Process for Data Mining), ampliamente adoptada en proyectos de ciencia de datos. Esta metodología se estructura en seis fases principales:

- **Comprensión del negocio**  
  Se definieron los objetivos principales: analizar la participación de usuarios, predecir la finalización de proyectos y optimizar las estrategias de donación en Chingu.io.

- **Comprensión de los datos**  
  Se exploraron múltiples fuentes de datos (aplicaciones, transacciones y finalizaciones), identificando su estructura, calidad y relaciones clave entre tablas.

- **Preparación de los datos**  
  Se realizó limpieza, estandarización, transformación y fusión de datasets utilizando scripts personalizados (`Cleaner.py`, `Applications_Cleaner.py`, etc.), así como flujos en Apache NiFi.

- **Modelado**  
  Se aplicaron modelos de regresión logística, Random Forest, PCA, k-Means, y modelos autoregresivos (LSTM) para predicción de comportamiento y segmentación de usuarios.

- **Evaluación**  
  Se analizaron métricas como Accuracy, F1, AUC y matriz de confusión para validar el rendimiento de los modelos. También se utilizaron herramientas visuales (Orange, Power BI).

- **Despliegue**  
  Los resultados se documentaron en notebooks, dashboards, y archivos `.md`, y se integraron como parte de una infraestructura reproducible usando Docker, BigQuery y Cassandra.

> Esta metodología estructurada permitió asegurar la trazabilidad, calidad y valor analítico en cada etapa del proyecto.




