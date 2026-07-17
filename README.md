# Dashboard estratégico PENTUR 2036

Herramienta de consulta interactiva del marco lógico tridimensional del PENTUR 2036
(Producto 3).
## Estructura

```
pentur/
├── app.py              # dashboard (cubo + mapa estratégico + tablas de detalle)
├── config_mapa.py      # ESTRUCTURA FIJA (perspectivas, niveles, ejes del cubo)
├── datos_pentur.xlsx   # CONTENIDO EDITABLE (líneas de acción, indicadores, metas)
├── generar_datos.py    # regenera el Excel desde cero si hace falta
└── requirements.txt
```


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
