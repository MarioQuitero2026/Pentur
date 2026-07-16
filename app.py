"""
Dashboard estratégico PENTUR 2036
Ejecutar:  streamlit run app.py
"""
import os
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

import config_mapa as cfg

DATA_FILE = "datos_pentur.xlsx"

st.set_page_config(page_title="PENTUR 2036 · Marco lógico", layout="wide",
                   initial_sidebar_state="expanded")

# ----------------------------- estilos ----------------------------- #
st.markdown("""
<style>
  .block-container {padding-top: 0.8rem; max-width: 100%;}
  h1, h2, h3 {font-family: 'Segoe UI', Arial, sans-serif;}
  /* sidebar (panel de control) un poco más ancho ~ 22% */
  section[data-testid="stSidebar"] {width: 340px !important;}
  /* barra de estado fija arriba del panel principal */
  .status-bar {position: sticky; top: 0; z-index: 999;
      background: #ffffff; border-bottom: 2px solid #e6e9ef;
      padding: 8px 4px 10px; margin: -4px 0 8px;
      display: flex; align-items: center; gap: 10px; flex-wrap: wrap;}
  .status-bar .pill {color:#fff; padding:5px 14px; border-radius:20px;
      font-size:.85rem; font-weight:600; white-space:nowrap;}
  .status-bar .pill-h {background:#1b2a4a;}
  .status-bar .pill-s {background:#C8102E;}
  .status-bar .dti {color:#3c4a5c; font-size:.76rem; opacity:.9;}
  .vision-band {background: linear-gradient(90deg,#0b0f19,#1b2a4a);
      color:#fff; padding:14px 20px; border-radius:10px; text-align:center;
      font-size:0.95rem; line-height:1.4; margin-bottom:6px;}
  .dti-band {background:#eef1f5; border:1px dashed #9aa7b8; color:#3c4a5c;
      padding:8px 14px; border-radius:8px; text-align:center;
      font-size:0.78rem; margin-top:6px;}
  .transv {display:inline-block; background:#fff3cd; color:#7a5b00;
      border:1px solid #ffe08a; border-radius:20px; padding:2px 12px;
      font-size:0.75rem; margin:0 4px;}
  /* botones-caja del mapa */
  div[data-testid="stButton"] > button {
      width:100%; min-height:74px; white-space:normal; line-height:1.15;
      border-radius:10px; border:1px solid rgba(0,0,0,.12);
      font-size:0.80rem; font-weight:600; padding:8px 6px;}
</style>
""", unsafe_allow_html=True)


# ----------------------------- datos ------------------------------- #
@st.cache_data(show_spinner=False)
def cargar_datos(path, mtime):
    df = pd.read_excel(path, sheet_name="lineas_de_accion")
    df.columns = [c.strip() for c in df.columns]
    for c in df.columns:
        df[c] = df[c].astype(str).str.strip()
    return df

if not os.path.exists(DATA_FILE):
    st.error(f"No se encontró **{DATA_FILE}**. Ejecuta `python generar_datos.py` primero.")
    st.stop()

df = cargar_datos(DATA_FILE, os.path.getmtime(DATA_FILE))


# ------------------------- cubo tridimensional --------------------- #
def _cubo(x, y, z, color, opacity):
    """8 vértices -> 12 triángulos de un cubo unitario en (x,y,z)."""
    X = [x, x+1, x+1, x, x, x+1, x+1, x]
    Y = [y, y, y+1, y+1, y, y, y+1, y+1]
    Z = [z, z, z, z, z+1, z+1, z+1, z+1]
    i = [0, 0, 0, 0, 4, 4, 6, 6, 1, 1, 2, 3]
    j = [1, 2, 4, 3, 5, 6, 5, 7, 5, 2, 6, 7]
    k = [2, 3, 5, 7, 6, 7, 1, 3, 6, 6, 7, 4]
    return go.Mesh3d(x=X, y=Y, z=Z, i=i, j=j, k=k, color=color,
                     opacity=opacity, flatshading=True, hoverinfo="skip")

def _aristas(x, y, z, color="#0b0f19", width=3):
    """Aristas de un cubo unitario en (x,y,z) para resaltar la porción activa."""
    e = [(0,0,0),(1,0,0),(1,1,0),(0,1,0),(0,0,0),
         (0,0,1),(1,0,1),(1,1,1),(0,1,1),(0,0,1),
         (None,None,None),(1,0,0),(1,0,1),
         (None,None,None),(1,1,0),(1,1,1),
         (None,None,None),(0,1,0),(0,1,1)]
    xs = [x+dx if dx is not None else None for dx, _, _ in e]
    ys = [y+dy if dy is not None else None for _, dy, _ in e]
    zs = [z+dz if dz is not None else None for _, _, dz in e]
    return go.Scatter3d(x=xs, y=ys, z=zs, mode="lines",
                        line=dict(color=color, width=width), hoverinfo="skip")

def figura_cubo(sel_h, sel_s):
    """Cubo Horizontes(x) × Segmentos(y) × Pilares(z); resalta la columna
    (horizonte, segmento) seleccionada a lo largo de los 4 pilares.
    Todas las celdas usan el color de su pilar; las NO activas van
    translúcidas para diferenciarlas de las activas (opacas)."""
    fig = go.Figure()
    for hx, h in enumerate(cfg.HORIZONTES_CORTO):
        for sy, s in enumerate(cfg.SEGMENTOS):
            activo = (hx == sel_h and sy == sel_s)
            for pz, pil in enumerate(cfg.PILARES):
                color = cfg.PILAR_COLOR[pil]          # mismo color siempre
                op = 0.97 if activo else 0.12          # transparencia diferencia
                fig.add_trace(_cubo(hx*1.15, sy*1.15, pz*1.15, color, op))
                if activo:
                    fig.add_trace(_aristas(hx*1.15, sy*1.15, pz*1.15))
    # etiquetas de ejes
    fig.update_layout(
        scene=dict(
            xaxis=dict(title="Horizontes", tickvals=[0.5,1.65,2.8],
                       ticktext=cfg.HORIZONTES_CORTO, showbackground=False),
            yaxis=dict(title="Segmentación", tickvals=[0.5,1.65,2.8],
                       ticktext=cfg.SEGMENTOS, showbackground=False),
            zaxis=dict(title="Pilares", tickvals=[0.5,1.65,2.8,3.95],
                       ticktext=cfg.PILARES, showbackground=False),
            camera=dict(eye=dict(x=1.7, y=1.7, z=1.1)),
            aspectmode="cube",
        ),
        margin=dict(l=0, r=0, t=0, b=0), height=340, showlegend=False,
    )
    return fig


# ------------------------------ header ----------------------------- #
st.markdown("## 🇵🇪 PENTUR 2036 — Marco lógico tridimensional")
st.caption("Plan Estratégico Nacional de Turismo del Perú · Producto 3 · "
           "IDOM / BID — herramienta de consulta interactiva")

# ---------------- panel de control (sidebar, fijo) ----------------- #
with st.sidebar:
    st.markdown("### 1 · Filtra el marco")
    sel_horizonte = st.radio("Horizonte de desarrollo", cfg.HORIZONTES, index=0)
    sel_segmento = st.radio("Segmentación territorial", cfg.SEGMENTOS, index=0)
    h_idx = cfg.HORIZONTES.index(sel_horizonte)
    s_idx = cfg.SEGMENTOS.index(sel_segmento)
    st.plotly_chart(figura_cubo(h_idx, s_idx), use_container_width=True,
                    config={"displayModeBar": False})

# ------------- barra de estado transversal (fija arriba) ----------- #
st.markdown(
    f"<div class='status-bar'>"
    f"<span class='pill pill-h'>🕓 {sel_horizonte}</span>"
    f"<span class='pill pill-s'>📍 {sel_segmento}</span>"
    f"<span class='dti'>Enfoque transversal <b>DTI</b> · Ejes: "
    f"{' · '.join(cfg.EJES_TRANSVERSALES)}</span>"
    f"</div>", unsafe_allow_html=True)

# --------------------------- mapa estratégico ---------------------- #
st.markdown("#### 2 · Mapa estratégico general")

df_h = df[df["horizonte"] == sel_horizonte]

if "nivel_sel" not in st.session_state:
    st.session_state.nivel_sel = None

def n_lineas(persp_id, nivel):
    return len(df_h[(df_h["perspectiva"] == persp_id) &
                    (df_h["nivel_pilar"] == nivel)])

# ayuda + ejes transversales (movidos aquí desde la columna derecha)
transv = " ".join(f"<span class='transv'>{t}</span>" for t in cfg.EJES_TRANSVERSALES)
st.markdown(
    f"<div style='display:flex;justify-content:space-between;align-items:center;"
    f"flex-wrap:wrap;gap:8px;margin-bottom:8px'>"
    f"<span style='font-size:.82rem;color:#3c4a5c'>👇 Haz clic en un "
    f"<b>nivel / pilar</b> para ver sus líneas de acción, indicadores y metas.</span>"
    f"<span style='font-size:.8rem'><b>Ejes transversales:</b> {transv}</span></div>",
    unsafe_allow_html=True)

st.markdown(f"<div class='vision-band'>🎯 <b>Visión 2036</b> — {cfg.VISION}</div>",
            unsafe_allow_html=True)

for persp in cfg.PERSPECTIVAS:
    with st.container(border=True):
        # banda-encabezado que agrupa: deja claro a qué perspectiva
        # pertenece cada nivel/pilar de abajo (p. ej. Competitividad
        # turística ∈ Generación de valor e innovación)
        st.markdown(
            f"<div style='background:{persp['color']};color:#fff;"
            f"padding:7px 14px;border-radius:7px;margin-bottom:10px;"
            f"display:flex;justify-content:space-between;align-items:center'>"
            f"<span style='font-weight:700;font-size:0.9rem'>{persp['titulo']}</span>"
            f"<span style='font-weight:400;font-size:0.72rem;opacity:.9'>"
            f"{persp['subtitulo']}</span></div>", unsafe_allow_html=True)
        box_cols = st.columns(len(persp["niveles"]), gap="small")
        for col, nivel in zip(box_cols, persp["niveles"]):
            with col:
                n = n_lineas(persp["id"], nivel)
                etiqueta = f"{nivel}\n({n} línea{'s' if n != 1 else ''})"
                activo = (st.session_state.nivel_sel == (persp["id"], nivel))
                if st.button(etiqueta, key=f"{persp['id']}|{nivel}",
                             type="primary" if activo else "secondary",
                             disabled=(n == 0),
                             use_container_width=True):
                    st.session_state.nivel_sel = (persp["id"], nivel)
                    st.rerun()

st.markdown(
    "<div style='text-align:center;color:#8a97a8;font-size:.72rem;margin-top:8px'>"
    "▲ lectura de abajo hacia arriba: las capacidades habilitan la gestión "
    "territorial, que genera valor para el visitante y hace posible la visión</div>",
    unsafe_allow_html=True)

st.divider()

# --------------------------- tabla de detalle ---------------------- #
st.markdown("#### 3 · Detalle: indicadores y metas")

if st.session_state.nivel_sel is None:
    st.caption("Selecciona un nivel / pilar en el mapa para desplegar su tabla de detalle.")
else:
    persp_id, nivel = st.session_state.nivel_sel
    sub = df_h[(df_h["perspectiva"] == persp_id) &
               (df_h["nivel_pilar"] == nivel)].copy()

    color = next(p["color"] for p in cfg.PERSPECTIVAS if p["id"] == persp_id)
    cc1, cc2 = st.columns([4, 1])
    with cc1:
        st.markdown(
            f"<div style='border-left:6px solid {color};padding:4px 12px'>"
            f"<span style='font-size:1.15rem;font-weight:700'>{nivel}</span><br>"
            f"<span style='color:#5b6675;font-size:.82rem'>{persp_id} · "
            f"{sel_horizonte} · segmento <b>{sel_segmento}</b></span></div>",
            unsafe_allow_html=True)
    with cc2:
        comparar = st.toggle("Comparar 3 segmentos", value=False)

    meta_col = cfg.SEG_COL[sel_segmento]
    if comparar:
        tabla = sub[["linea_accion", "indicador",
                     "meta_emergente", "meta_ascenso", "meta_referente"]]
        tabla.columns = ["Línea de acción", "Indicador",
                         "Meta · Emergente", "Meta · En ascenso", "Meta · Referente"]
    else:
        tabla = sub[["linea_accion", "indicador", meta_col]]
        tabla.columns = ["Línea de acción", "Indicador", f"Meta · {sel_segmento}"]

    st.dataframe(tabla, use_container_width=True, hide_index=True,
                 column_config={c: st.column_config.TextColumn(width="large")
                                for c in tabla.columns[:2]})

    st.download_button(
        "⬇️ Descargar esta tabla (CSV)",
        tabla.to_csv(index=False).encode("utf-8-sig"),
        file_name=f"PENTUR_{nivel}_{sel_horizonte[:12]}.csv",
        mime="text/csv")

# ----------------------------- footer ------------------------------ #
with st.sidebar:
    st.divider()
    st.markdown("### Datos")
    st.write(f"Filas cargadas: **{len(df)}**")
    st.write(f"Fuente: `{DATA_FILE}`")
    if st.button("🔄 Recargar datos"):
        st.cache_data.clear()
        st.rerun()
    st.caption("Edita el Excel (hoja *lineas_de_accion*) y pulsa *Recargar datos* "
               "para actualizar el contenido sin tocar el código.")
