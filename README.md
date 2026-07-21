# 🏗️ Sistema de Presupuesto de Construcción

Programa en Python que calcula el costo total de un proyecto de construcción (materiales + mano de obra + IVA) y valida si se mantiene dentro de un presupuesto máximo permitido.

## 🧩 Situación inicial

Una empresa constructora necesita una herramienta rápida para estimar el costo de un proyecto antes de iniciarlo, considerando metros cuadrados a construir, costo por metro cuadrado, cantidad de trabajadores y costo por trabajador — y así determinar si el proyecto es viable dentro de un presupuesto máximo definido.

## 🚀 Funcionalidades implementadas

- **Ingreso validado de datos**: solicita metros cuadrados, costo por metro, cantidad de trabajadores y costo por trabajador, validando que todos los valores sean numéricos y mayores a 0 antes de continuar.
- **Cálculo de costos**: separa el costo de materiales del costo de mano de obra, y calcula el costo neto y el costo total aplicando IVA (19%).
- **Control de presupuesto**: compara el costo total contra un presupuesto máximo permitido y notifica si el proyecto se ajusta o lo excede.
- **Resumen final formateado**: muestra un resumen claro del proyecto con todos los costos, con separador de miles para mejor lectura.

## 🛠️ Tecnologías utilizadas

- Python 3

## 📂 Estructura del proyecto

Sist.presupuesto_construccion/
└── presupuesto.py # Lógica completa: validación, cálculo de costos y resumen

## ▶️ Cómo ejecutarlo

1. Clona este repositorio o descarga el archivo.
2. Ejecuta el script:
```bash
   python presupuesto.py
```
3. Ingresa el nombre del proyecto y los datos solicitados (metros cuadrados, costo por metro, trabajadores, costo por trabajador).
4. Revisa el resumen final con el desglose de costos y si el proyecto está dentro del presupuesto.

## 🧠 Decisiones de diseño

- **Constantes en mayúsculas (`IVA`, `PRESUPUESTO_MAXIMO`)**: se definieron como constantes al inicio del programa para diferenciar claramente los valores fijos del negocio de los datos variables ingresados por el usuario, y para facilitar su ajuste futuro sin buscar "números mágicos" dentro del código.
- **Bucle de validación con `try/except`**: se optó por un `while True` con validación de tipo y de rango (mayor a 0) para evitar que el programa se detenga o entregue resultados incorrectos ante datos mal ingresados.
- **Separación de costos**: se calculan por separado el costo de materiales y el de mano de obra antes de sumarlos, para que el resumen final sea más transparente y fácil de auditar.

## 👤 Autora

Abigail Betsabé Arriagada Aravena — Proyecto realizado durante la formación en Python de la asignatura Fundamentos de la programación (Duoc UC).
