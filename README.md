# 🚀 Evaluación Parcial 1 (EP1)

## Definición de Acuerdos de Nivel de Servicio (SLA/SLO) y Despliegue Base

---

## 📖 Descripción

En esta evaluación asumirás el rol de **Consultor SRE (Site Reliability Engineer)** encargado de establecer los cimientos de una estrategia de observabilidad.

Se te asignará un rubro de negocio específico (por ejemplo: Banco, Clínica, Fintech, E-commerce o Contabilidad), para el cual deberás:

* Definir el nombre de la organización.
* Construir un contexto empresarial ficticio.
* Analizar métricas operacionales.
* Modelar indicadores y objetivos de nivel de servicio.
* Diagnosticar el estado del presupuesto de error (*Error Budget*).

La organización creada será utilizada como **caso de estudio durante todo el semestre**, sirviendo de base para futuras evaluaciones.

---

## 🎯 Objetivos de la Evaluación

El propósito de esta actividad es:

* Analizar telemetría base proveniente de infraestructura en la nube (AWS).
* Comprender la relación entre **SLI**, **SLO** y **SLA**.
* Calcular y evaluar presupuestos de error (*Error Budget*).
* Interpretar métricas de disponibilidad y rendimiento.
* Elaborar un informe técnico ejecutivo basado en evidencia.

---

## 📑 Contenido

* [Prerrequisitos](#-prerrequisitos)
* [Configuración del Entorno](#️-configuración-del-entorno)
* [Ejecución del Simulador](#-ejecución-del-simulador)
* [Interpretación de Resultados](#-interpretación-de-resultados)
* [Limpieza del Entorno AWS](#-limpieza-del-entorno-aws)

---

# 📋 Prerrequisitos

Antes de comenzar, asegúrate de contar con:

| Requisito         | Versión                             |
| ----------------- | ----------------------------------- |
| Sistema Operativo | Linux (Ubuntu o Debian recomendado) |
| Python            | 3.10 o superior                     |
| Git               | Última versión estable              |

Verifica tu instalación:

```bash
python3 --version
git --version
```

---

# ⚙️ Configuración del Entorno

## 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/Fco-Quiroga/ADY1103-Monitoreo-Observabilidad.git

cd ADY1103-Monitoreo-Observabilidad/02_Ev_Parcial_1-Definicion_Acuerdos
```

## 2️⃣ Ejecutar el simulador

```bash
python3 app.py
```

---

# 🎮 Ejecución del Simulador

Al iniciar el programa se desplegará un menú con distintos rubros de negocio:

1. Banco
2. Clínica
3. Fintech
4. E-commerce
5. Contabilidad

### Procedimiento

1. Selecciona el rubro que deseas analizar.
2. Ingresa el número correspondiente.
3. Presiona **Enter**.
4. El simulador generará métricas de forma aleatoria.
5. Al finalizar, se mostrará una **Evidencia de Ejecución** con los indicadores necesarios para desarrollar la actividad.

---

# 📈 Interpretación de Resultados

La evidencia generada contiene métricas agrupadas en tres categorías fundamentales para la observabilidad.

## 🟢 Disponibilidad

Permite evaluar la estabilidad del servicio.

Incluye:

* Solicitudes exitosas.
* Errores de cliente (4xx).
* Errores de servidor (5xx).

Estas métricas sirven como base para el cálculo de indicadores de disponibilidad y confiabilidad.

---

## 🟡 Rendimiento

Permite analizar la experiencia percibida por el usuario.

Incluye:

* Latencia promedio.
* Percentil p50.
* Percentil p90.
* Percentil p95.

Los percentiles ayudan a identificar comportamientos anómalos y degradaciones del servicio.

---

## 🔵 Impacto en el Negocio

Permite evaluar el resultado funcional de las operaciones.

Incluye:

* Operaciones intentadas.
* Operaciones completadas exitosamente.
* Conversión comercial.

Estas métricas conectan el rendimiento técnico con los resultados de negocio.

---

# 🧹 Limpieza del Entorno AWS

> ⚠️ **Importante:** Una vez obtenidas todas las evidencias necesarias, elimina los recursos utilizados para evitar el consumo innecesario de créditos en AWS Academy Learner Lab.

## Paso 1: Terminar la instancia EC2

1. Accede a la consola de AWS.
2. Dirígete al servicio **EC2**.
3. Selecciona la instancia creada para la evaluación.
4. Haz clic en:

```text
Instance State → Terminate Instance
```

5. Confirma la acción.

---

## Paso 2: Finalizar el Learner Lab

1. Regresa a la plataforma **AWS Academy Learner Lab**.
2. Ubica el botón rojo:

```text
End Lab
```

3. Haz clic para finalizar completamente el laboratorio.

---

> ✅ Realizar ambos pasos garantiza que no continúe el consumo de créditos asociados al laboratorio.

---

## 👨‍💻 Autor

**ADY1103 - Monitoreo y Observabilidad**

Evaluación Parcial 1 — Definición de Acuerdos de Nivel de Servicio (SLA/SLO) y Despliegue Base.
