# Propul · Brochures Workspace

Workspace de Claude Code para construir brochures comerciales de cadenas de gimnasios para Propul.

## Cómo usar esto

1. Abrí esta carpeta en tu terminal y arrancá Claude Code:
   ```bash
   cd propul-brochures
   claude
   ```
2. Claude Code lee `CLAUDE.md` automáticamente y queda con todo el contexto del proyecto cargado.
3. Pedile lo que necesites en lenguaje natural:
   - *"Ajustá el color del titular del bloque CONECTÁ del brochure de On Fit a amarillo"*
   - *"Arrancá el brochure de Megatlon. Te paso los assets en megatlon/assets/"*
   - *"Cambiá el número de WhatsApp del QR a [otro número]"*
   - *"Agregá una soporte card nueva para 'Pantallas en sala de spinning'"*

## Estructura del workspace

```
propul-brochures/
├── CLAUDE.md           ← Contexto del proyecto (Claude Code lo lee solo)
├── README.md           ← Este archivo
└── on-fit/             ← Brochure terminado (referencia + producción)
    ├── Propul_OnFit_Brochure.html
    └── assets/
        ├── photos/     ← 10 fotos resizeadas (1400px, q78)
        └── (logo embebido en el HTML)
```

Cuando arranques otra cadena, Claude Code va a crear `megatlon/`, `fiter/` o `sport-club/` siguiendo el mismo patrón.

## Para arrancar una cadena nueva

Necesitás juntar antes:

1. **Logo** de la cadena (PNG/JPG alta resolución)
2. **Colores oficiales** (primario, oscuro, acento)
3. **Lista de sucursales** completa
4. **Deck de ventas** existente (su posicionamiento, qué soportes venden hoy)
5. **Fotos de instalaciones** (las que tengas)
6. **Número de WhatsApp** para QR
7. **Tarifas públicas** si las tienen

Cuando tengas eso, pedile a Claude Code:

> "Arrancá el brochure de **Megatlon**. El logo está en `megatlon/assets/logo.png`, los colores son [...], las sucursales son [...], su deck está en `megatlon/assets/source/deck.pdf`. WhatsApp: 54911XXXXXXX."

Claude Code va a copiar el template de On Fit, adaptar tokens, embebir fotos y dejar todo listo.

## Para exportar a PDF

1. Abrí el HTML en **Chrome** (es el que mejor maneja print CSS)
2. Click en el botón **⬇ Exportar PDF** del sidebar
3. En el diálogo de impresión → **Guardar como PDF**
4. Sale A4 con cards en 2 columnas, fondos negros/navy forzados, contraportada del QR en página propia

## Tips

- El HTML es autocontenido (fotos en base64 dentro del archivo). Lo podés mandar por mail, subir a Drive o publicar en cualquier servidor — no necesita carpetas externas.
- Tamaño típico: 2–3 MB con fotos embebidas.
- Si una foto pesa demasiado al embeberla, resizearla antes con `PIL Image.thumbnail((1400, 1400))` y `quality=78`.
- Para cambios chicos (un texto, un color), pedíselo directo a Claude Code apuntando al archivo: *"En `on-fit/Propul_OnFit_Brochure.html`, cambiá X por Y"*. Mucho más barato en tokens que regenerar.
