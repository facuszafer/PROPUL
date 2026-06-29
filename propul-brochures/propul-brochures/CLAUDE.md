# Propul · Brochures de Espacios Publicitarios

Workspace para construir **brochures comerciales de cadenas de gimnasios** que Propul comercializa como medios publicitarios. Cada brochure presenta a una cadena (On Fit, Megatlon, Fiter, Sport Club...) como un **medio** con su catálogo de soportes/formatos, dirigido a marcas que quieran comunicar a su audiencia.

El entregable es siempre un **HTML autocontenido** (fotos embebidas en base64, fuentes desde Google Fonts CDN) que la marca puede abrir en el navegador o exportar a PDF.

---

## Estado del proyecto

| Cadena | Estado | Carpeta |
|---|---|---|
| On Fit | ✅ Terminado | `on-fit/` |
| Megatlon | ✅ Terminado | `megatlon/` |
| Fiter | ✅ Terminado | `fiter/` |
| Sport Club | ⏳ Pendiente | (crear `sport-club/` cuando arranque) |

---

## Logo oficial de Propul

El isologo/wordmark oficial de Propul (PNG, fondo transparente, trazo cyan) vive en `shared/assets/propul_logo_small.png` (900px de ancho, optimizado) y su versión base64 en `shared/assets/propul_logo_b64.txt`. **Usar siempre este archivo como `<img>`, nunca recrear el wordmark "Propul." con texto/CSS** — así se evita inconsistencia tipográfica entre brochures.

Se usa como `<img>` en 3 puntos de cada brochure (clases en On Fit como referencia):
- Sidebar (`.sidebar-logo-img`, ~24px alto)
- Chip de co-branding del header (`.cobrand-logo-img`, ~26px alto, 20px en mobile)
- Cierre CONECTÁ (`.connect-logo-img`, ~34px alto, 0.85cm en print)

Al armar una cadena nueva, reutilizar el mismo data URI (leer `shared/assets/propul_logo_b64.txt`) en vez de generar uno nuevo.

---

## Convención clave de identidad (regla maestra)

**Propul = el frame** de todos los documentos, sin importar la cadena. Sus tokens dominan la mayor parte del HTML.

**La cadena cliente = el sujeto presentado.** Sus colores/fuentes aparecen **sólo en bloques designados**: la banda "manifesto" arriba y la sección "CONECTÁ" de cierre.

**Regla de no mezcla**: la identidad de Propul nunca convive con la de la cadena en la misma sección. Cada uno tiene su territorio visual.

### Acentos de marca dentro del cuerpo (ampliación de la regla maestra)

Más allá de la banda manifesto y CONECTÁ, el accent color de la cadena (ej. `--onfit-yellow` / `--onfit-yellow-deep`) también se usa como **acento puntual** (texto, bordes finos, dots, números de sección) en bloques que hablan *de la cadena misma*, nunca como fondo y nunca mezclado con cyan/blue de Propul en el mismo elemento. Para decidir el color de un elemento, preguntar: **¿quién es el sujeto de este bloque?**

- **Sujeto = la cadena** (ej. "¿Por qué On Fit es un medio premium?", why-cards con sus métricas, Universos 1-4 del catálogo, sede-dots de Cobertura, `<em>` con el nombre de la cadena en h1/h2) → usar el accent token de la cadena.
- **Sujeto = análisis de Propul sobre la audiencia** (ej. sección Audiencia con sus tags y stats, Cierre/Próximos pasos) → se queda 100% en paleta Propul (cyan/blue/navy), sin excepción.

Aplicado en On Fit: `.why-card` (border-left + label), `.sede-dot`, `.section-number.onfit` (en "01 · Posicionamiento" y los 4 Universos — NO en "02 · Audiencia" ni "03 · Cobertura"), `.section-header h2 em`, `.doc-header h1 em`, `.soporte-card` (border-top 3px). Replicar este mismo criterio sección por sección al armar Megatlon/Fiter/Sport Club, reemplazando el token por el accent de cada cadena.

### Tokens de Propul (fijos, no cambian por cadena)
```css
--font-display: 'Outfit', sans-serif;
--font-body:    'DM Sans', sans-serif;
--navy:       #0A1628;
--blue:       #2563EB;
--blue-light: #3B82F6;
--blue-soft:  #EFF6FF;
--cyan:       #06B6D4;
--teal:       #0D9488;
/* + grises 50→900, ver el HTML de On Fit */
```

### Tokens de cadena (cambian por cliente)
On Fit ya está definido:
```css
--onfit-yellow:      #FFD60A;
--onfit-yellow-deep: #F5C400;
--onfit-black:       #0A0A0A;
--onfit-grey:        #8A8A8A;
--font-onfit:        'Montserrat', sans-serif; /* italic 900 para titulares */
```

Cada cadena nueva replica el patrón: `--[cadena]-primary`, `--[cadena]-dark`, `--[cadena]-accent`, `--font-[cadena]`.

---

## Anatomía estándar del brochure

Orden de secciones (de arriba a abajo):

1. **Sidebar** — sticky, navy, colapsable en mobile con botón "☰ Menú"
2. **Doc header** — fondo navy con radial gradients cyan/blue, chip de co-branding "Propul × [logo cadena]", titular grande, párrafo introductorio, fila de metadatos
3. **Banda manifesto de la cadena** — fondo negro (o color oscuro de la cadena), borde superior con accent color, voice propio de la cadena (Montserrat italic 900 en On Fit), KPIs base
4. **Sección 01 · ¿Por qué [cadena]?** — grid de "why-cards" con métricas clave
5. **Sección 02 · Audiencia** — bloque dual: texto descriptivo + stats card en navy
6. **Sección 03 · Cobertura** — sedes-grid con todas las sucursales
7. **Universo 1 · Digital In-Gym** — soporte cards de pantallas, displays, contenido dinámico
8. **Universo 2 · Branding Físico** — soporte cards de espacios físicos brandeables
9. **Universo 3 · Activación & Sampling** — soporte cards de acciones con contacto directo
10. **Universo 4 · Digital Extendido** — soporte cards de redes, newsletter, programa de beneficios
11. **Cierre · Próximos pasos** — bloque navy con 4 steps del proceso Propul
12. **CONECTÁ · QR back cover** — fondo negro, QR de WhatsApp, logos co-brand, 3 cols de contacto

Los **4 universos** son la columna vertebral del catálogo. Algunas cadenas tendrán todos, otras quizás no (ej. una cadena chica sin red de pantallas digitales tendrá un Universo 1 mínimo). Adaptar.

### Anatomía de una soporte card
```
.soporte-card
  .card-img-wrap         (220px alto, foto base64 O ilustración SVG on-brand)
    img                  (object-fit cover)
    .card-badges         (chips superpuestos abajo-izquierda: universo + categoría)
  .card-body
    .card-title          (Outfit 700, 1.1rem)
    .card-alt            (sinónimos del soporte, italic gris)
    .card-desc           (1 párrafo: qué es, por qué funciona, para quién es ideal)
    .card-highlights     (3-5 chips compactos con los key selling points)
    .card-specs          (grid 2-col con specs técnicas)
    .card-pricing        ("A cotizar" si no hay tarifa pública)
```

---

## Workflow estándar para una cadena NUEVA

### Paso 1: Información a recolectar
Antes de generar nada, conseguir de la cadena cliente:

1. **Logo** (PNG/JPG, alta resolución)
2. **Paleta de colores** oficial (primario, oscuro, acento)
3. **Tipografía** oficial (o Google Font equivalente — buscar en su web/CSS)
4. **Lista completa de sucursales** (por barrio/ciudad)
5. **Deck o material de ventas existente** (define su posicionamiento)
6. **Fotos de instalaciones** (recepción, sala de musculación, vestuarios, salas grupales, etc.)
7. **Soportes publicitarios que ya comercializan** (con tarifas si las publican)
8. **Número de WhatsApp** para el QR de cierre
9. **Audiencia** — tamaño aproximado, edad, NSE (si lo dan)

### Paso 2: Setup de carpeta
```
[cadena]/
  Propul_[Cadena]_Brochure.html
  assets/
    photos/         # fotos resizeadas
    logo.jpg
    source/         # deck original de la cadena, brief, etc
```

### Paso 3: Preparar assets
```python
# Resizear fotos en lote
from PIL import Image
import os
src = 'assets/photos/raw'
dst = 'assets/photos'
for f in os.listdir(src):
    img = Image.open(f'{src}/{f}')
    img.thumbnail((1400, 1400))
    name = f.rsplit('.', 1)[0]
    img.save(f'{dst}/{name}_small.jpg', 'JPEG', quality=78, optimize=True)
```

### Paso 4: Generar el HTML
- Copiar `on-fit/Propul_OnFit_Brochure.html` como base
- Adaptar tokens de la cadena (sección `:root` del CSS)
- Cambiar el bloque manifesto (logo, voice, headline, stats)
- Listar sucursales reales en la sección Cobertura
- Adaptar las soporte cards (algunas son universales: pantallas, lockers, recepción, sampling; otras son específicas)
- Embebir fotos en base64 inline
- Generar QR de WhatsApp (ver receta abajo)
- Adaptar bloque CONECTÁ con datos de contacto correctos

### Paso 5: Validación
- Revisión interna del contenido con **Adhemar** antes de presentar a la marca cliente.
- Pricing: dejar "A cotizar" salvo tarifa pública confirmada.

---

## Recetas técnicas

### Embebir foto como data URI
```python
import base64
def b64img(path):
    with open(path, 'rb') as f:
        return f'data:image/jpeg;base64,{base64.b64encode(f.read()).decode()}'
# Luego en str_replace del HTML:
# <img src="{b64img('assets/photos/foo_small.jpg')}" alt="...">
```

### Generar QR de WhatsApp (SVG inline)
```python
import qrcode, qrcode.image.svg, urllib.parse, io, re

phone = '54911XXXXXXX'  # sin + ni espacios ni símbolos
msg = urllib.parse.quote('Hola Propul, vi el brochure de [cadena] y...')
url = f'https://wa.me/{phone}?text={msg}'

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=2)
qr.add_data(url); qr.make(fit=True)
img = qr.make_image(image_factory=qrcode.image.svg.SvgPathImage)
buf = io.BytesIO(); img.save(buf)
svg = re.sub(r'<\?xml[^?]*\?>', '', buf.getvalue().decode()).strip()
svg = re.sub(r'width="[^"]*"', 'width="100%"', svg, count=1)
svg = re.sub(r'height="[^"]*"', 'height="100%"', svg, count=1)
svg = svg.replace('<path ', '<path fill="#0A0A0A" ', 1)
# inyectar `svg` dentro de la sección .connect-qr del HTML
```

Si `qrcode` no está instalado: `pip install qrcode --break-system-packages`

### Pattern de ilustración SVG on-brand (cuando falta foto)
Fondo con grilla techie Propul + ilustración stylized minimal:
```css
background:#060F1E;
background-image:
  linear-gradient(rgba(37,99,235,.12) 1px,transparent 1px),
  linear-gradient(90deg,rgba(37,99,235,.12) 1px,transparent 1px),
  radial-gradient(rgba(6,182,212,.22) 1px,transparent 1px);
background-size:32px 32px,32px 32px,16px 16px;
```
Adentro: SVG simple con colores Propul (cyan, navy) y leyenda "TU MARCA" como placeholder de branded content.

---

## Constraints técnicos del HTML final

- **Autocontenido**: imágenes en base64 inline. Sólo dependencia externa: Google Fonts CDN (aceptable).
- **Responsive**: breakpoints en 1024px (tablet), 768px (mobile), 480px (mobile chico). Sidebar colapsa en mobile.
- **Print CSS**: `@page A4` con margen 1.2cm. `-webkit-print-color-adjust: exact !important` en todo. Cards con `page-break-inside: avoid`. CONECTÁ con `page-break-before: always`.
- **Export PDF**: botón con `onclick="exportPDF()"` que cierra sidebar mobile y llama `window.print()` con setTimeout 100ms.
- **Tamaño final típico**: 2–3 MB con fotos embebidas. Aceptable.

---

## Notas operativas

- **Cualquier cambio de contenido editorial** se valida con Adhemar antes de pasar a la marca cliente.
- **Pricing**: dejar `A cotizar` salvo tarifa pública confirmada. Ej: On Fit Circuito de Pantallas $350K/sede / $6M red completa (sí está confirmado, está en su deck).
- **Mensaje pre-cargado del QR**: genérico por defecto. Si Adhemar quiere tracking por cadena, se puede personalizar ("Hola Propul, vi el brochure de [cadena]...") para identificar la fuente del lead.
- **Audiencia/KPIs**: cuando se inferieron datos (ej. edad/NSE de On Fit), dejar nota en el chat para que validen con la cadena. No inventar números duros.

---

## Skill disponible

Tenés activa la skill `propul-brand-guidelines` en `/mnt/skills/user/propul-brand-guidelines/SKILL.md` con guía oficial de identidad de Propul. Cuando Claude Code arranque, leerla si vas a generar cualquier deliverable Propul.
