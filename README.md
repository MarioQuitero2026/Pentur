# Dashboard estratégico PENTUR 2036

Herramienta de consulta interactiva del marco lógico tridimensional del PENTUR 2036
(Producto 3). Igual que el proyecto de Argentina: código Python + Streamlit.

## Estructura

```
pentur/
├── app.py              # dashboard (cubo + mapa estratégico + tablas de detalle)
├── config_mapa.py      # ESTRUCTURA FIJA (perspectivas, niveles, ejes del cubo)
├── datos_pentur.xlsx   # CONTENIDO EDITABLE (líneas de acción, indicadores, metas)
├── generar_datos.py    # regenera el Excel desde cero si hace falta
└── requirements.txt
```

## Cómo ejecutar

```bash
pip install -r requirements.txt
streamlit run app.py
```

Se abre en el navegador (por defecto http://localhost:8501).

## Flujo de uso

1. **Filtra el marco** — elige un *horizonte de desarrollo* y una *segmentación
   territorial*. El cubo resalta la porción seleccionada (los 4 pilares de ese
   horizonte × segmento).
2. **Mapa estratégico** — se despliega el mapa (Ilustración 11), con estructura
   fija de abajo (capacidades) hacia arriba (visión). Haz clic en cualquier
   **nivel / pilar**.
3. **Detalle** — aparece la tabla de indicadores y metas (Tabla 1/2/3) filtrada
   por el horizonte y el segmento activos. Puedes comparar los 3 segmentos o
   descargar la tabla en CSV.

## Actualizar el contenido (sin tocar el código)

Edita **`datos_pentur.xlsx`**, hoja `lineas_de_accion`. Ver la hoja `LÉEME`
dentro del Excel para las reglas (qué columnas son fijas y qué valores admite
cada campo). Guarda y pulsa **🔄 Recargar datos** en la barra lateral.

La estructura del mapa y del cubo (perspectivas, niveles, ejes) es fija y vive
en `config_mapa.py`. Añadir un nuevo nivel/pilar al mapa requiere ajustar ese
archivo.

## Fuente

Documento *Formulación del plan estratégico — PENTUR 2036* (IDOM, jul-2026):
3 horizontes × 10 niveles/pilares × 3 segmentos = 90 líneas de acción.
