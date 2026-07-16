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
# NOTA: el mapa usa una rampa de AZULES (una sola familia = "un solo marco"),
# deliberadamente distinta de la paleta categórica del cubo (rojo/naranja/
# teal/púrpura de PILAR_COLOR), para que el usuario no confunda ambas vistas.
PERSPECTIVAS = [
    {
        "id": "Generación de valor e innovación",
        "titulo": "Generación de valor e innovación",
        "subtitulo": "Resultados de impacto a escala nacional",
        "color": "#0D2B45",   # navy más oscuro (cima)
        "niveles": ["Competitividad turística", "Arribos y viajes",
                    "Inversión pública", "Aporte al PIB"],
    },
    {
        "id": "Gestión de visitantes",
        "titulo": "Gestión de visitantes",
        "subtitulo": "Propuesta de valor: calidad, seguridad, inclusión y sostenibilidad",
        "color": "#1D4E74",
        "niveles": ["Calidad", "Seguridad", "Inclusión", "Sostenibilidad"],
    },
    {
        "id": "Gestión territorial",
        "titulo": "Gestión territorial",
        "subtitulo": "Cuatro pilares de intervención en el destino",
        "color": "#2E6DA4",
        "niveles": ["Oferta", "Promoción y demanda", "Infraestructura", "Gobernanza"],
    },
    {
        "id": "Desarrollo de capacidades y condiciones",
        "titulo": "Desarrollo de capacidades y condiciones",
        "subtitulo": "Base habilitante del sistema",
        "color": "#5A7C99",   # azul acero más claro (base)
        "niveles": ["Sistema de inteligencia turística", "Marco normativo sectorial"],
    },
]

VISION = ("Al 2036, el Perú cuenta con 50 destinos turísticos competitivos y "
          "sostenibles, con oferta accesible e innovadora, infraestructura "
          "compatible con los entornos y gobernanza plena y efectiva.")

EJES_TRANSVERSALES = ["Calidad", "Seguridad", "Inclusión"]
ENFOQUE_DTI = ("Enfoque transversal — Destinos Turísticos Inteligentes (DTI): "
               "gobernanza · sostenibilidad · innovación · tecnología · accesibilidad")

# color por pilar del cubo (coherente con el mapa)
PILAR_COLOR = {
    "Oferta": "#C8102E",
    "Promoción y demanda": "#E8710A",
    "Infraestructura": "#00838F",
    "Gobernanza": "#6A1B9A",
}
