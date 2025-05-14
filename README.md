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

### 5. Minería de Datos con Orange

Para la exploración y modelado, se utilizó **Orange Data Mining**, que permite flujos de trabajo visuales intuitivos para análisis exploratorio y predictivo.

### 6. Metodología de Ciencia de Datos

Se siguió la metodología **CRISP-DM**, que consta de:
- Comprensión del negocio
- Comprensión de los datos
- Preparación de los datos
- Modelado
- Evaluación
- Despliegue
