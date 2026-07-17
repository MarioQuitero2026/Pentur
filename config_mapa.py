"""
Estructura FIJA del marco lógico PENTUR 2036.
El contenido (líneas de acción, indicadores, metas) vive en datos_pentur.xlsx;
aquí sólo se define el esqueleto: orden de perspectivas, niveles, pilares del
cubo, horizontes, segmentos y la paleta de color.
"""

# --- Ejes del cubo (Ilustración 2) --------------------------------- #
HORIZONTES = [
    "Activación (2027-2029)",
    "Fortalecimiento (2030-2032)",
    "Escalamiento (2033-2036)",
]
HORIZONTES_CORTO = ["Activación", "Fortalecimiento", "Escalamiento"]

SEGMENTOS = ["Emergente", "En ascenso", "Referente"]
# mapea el segmento a la columna de meta correspondiente en el Excel
SEG_COL = {
    "Emergente": "meta_emergente",
    "En ascenso": "meta_ascenso",
    "Referente": "meta_referente",
}

# Pilares de intervención (cara frontal del cubo)
PILARES = ["Oferta", "Promoción y demanda", "Infraestructura", "Gobernanza"]

# --- Estructura del mapa estratégico (Ilustración 11) -------------- #
# De arriba (visión) hacia abajo (capacidades). Cada perspectiva lista
# sus niveles/pilares en el orden en que se muestran.
# --- Paleta de marca IDOM (valores OFICIALES de la guía de identidad) --- #
# Primarios
IDOM_AZUL        = "#10069F"   # Azul IDOM (RGB 16.6.159) — máxima jerarquía
IDOM_BLANCO      = "#FFFFFF"
# Secundarios
IDOM_AZUL_CLARO  = "#00B5E2"   # Clear Blue (RGB 0.181.226) — destacados
IDOM_GRIS        = "#AFAFA7"   # gris cálido para textos
IDOM_GRIS_MEDIO  = "#86867A"   # gris para gráficos
IDOM_GRIS_CLARO  = "#EFEFED"   # gris para fondos de tablas/gráficos
IDOM_NEGRO       = "#000000"
IDOM_ROJO        = "#DA291C"   # sólo para negativos / alertas
# Complementarios (definidos por la guía para "esquemas, diagramas, dashboards")
COMP_AMARILLO    = "#F6E500"
COMP_NARANJA     = "#FFA300"
COMP_VIOLETA     = "#9B26B6"
COMP_VERDE       = "#97D700"
COMP_MAGENTA     = "#DF1995"

IDOM_PRIMARY = IDOM_AZUL       # alias usado por el chrome del dashboard

# Rampa de azules IDOM (Azul IDOM -> Azul claro IDOM) para el mapa: es el
# elemento de mayor jerarquía, por eso va en los azules corporativos.
IDOM_RAMP = ["#10069F", "#0B40B5", "#057ACB", "#00B5E2"]  # oscuro -> claro

# --- Estructura del mapa estratégico (Ilustración 11) -------------- #
# El mapa usa la rampa de AZULES IDOM (jerarquía / marca). El cubo usa la
# paleta COMPLEMENTARIA (categorías) — dos familias distintas para no
# confundir ambas vistas, ambas dentro del paraguas del Azul IDOM.
PERSPECTIVAS = [
    {
        "id": "Generación de valor e innovación",
        "titulo": "Generación de valor e innovación",
        "subtitulo": "Resultados de impacto a escala nacional",
        "color": IDOM_RAMP[0],   # Azul IDOM (cima, mayor jerarquía)
        "niveles": ["Oferta", "Demanda", "Infraestructura", "Gobernanza",
                    "Transversal"],
    },
    {
        "id": "Gestión de visitantes",
        "titulo": "Gestión de visitantes",
        "subtitulo": "Propuesta de valor: calidad, seguridad, inclusión y sostenibilidad",
        "color": IDOM_RAMP[1],
        "niveles": ["Calidad", "Seguridad", "Inclusión", "Sostenibilidad"],
    },
    {
        "id": "Gestión territorial",
        "titulo": "Gestión territorial",
        "subtitulo": "Cuatro pilares de intervención en el destino",
        "color": IDOM_RAMP[2],
        "niveles": ["Oferta", "Promoción y demanda", "Infraestructura", "Gobernanza"],
    },
    {
        "id": "Desarrollo de capacidades y condiciones",
        "titulo": "Desarrollo de capacidades y condiciones",
        "subtitulo": "Base habilitante del sistema",
        "color": IDOM_RAMP[3],   # Azul claro IDOM (base)
        "niveles": ["Sistema de inteligencia turística", "Marco normativo sectorial",
                    "Fortalecimiento del capital humano"],
    },
]

VISION = ("Al 2036, el Perú cuenta con 50 destinos turísticos competitivos y "
          "sostenibles, con oferta accesible e innovadora, infraestructura "
          "compatible con los entornos y gobernanza plena y efectiva.")

EJES_TRANSVERSALES = ["Calidad", "Seguridad", "Inclusión"]
ENFOQUE_DTI = ("Enfoque transversal — Destinos Turísticos Inteligentes (DTI): "
               "gobernanza · sostenibilidad · innovación · tecnología · accesibilidad")

# Color por pilar del cubo — paleta COMPLEMENTARIA IDOM (categorías de
# diagrama/dashboard, según la guía de identidad). Distinta de la rampa
# azul del mapa para no confundir ambas vistas.
PILAR_COLOR = {
    "Oferta": COMP_NARANJA,            # #FFA300
    "Promoción y demanda": COMP_MAGENTA,  # #DF1995
    "Infraestructura": COMP_VERDE,     # #97D700
    "Gobernanza": COMP_VIOLETA,        # #9B26B6
}
