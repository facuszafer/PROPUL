import base64, io, re
from PIL import Image

base = r"c:\Users\andym\OneDrive\Desktop\PROPUL - ON FIT\propul-brochures\propul-brochures\megatlon\assets\photos"
html_path = r"c:\Users\andym\OneDrive\Desktop\PROPUL - ON FIT\propul-brochures\propul-brochures\megatlon\Propul_Megatlon_Brochure.html"

def resize_b64(filename, max_size=1400, quality=78):
    path = f"{base}\\{filename}"
    img = Image.open(path).convert("RGB")
    img.thumbnail((max_size, max_size), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=quality, optimize=True)
    data = base64.b64encode(buf.getvalue()).decode()
    print(f"  {filename}: {img.size} -> {len(data)//1024} KB base64")
    return data

# Mapeo: card_id → archivo
fotos = {
    "lockers": "vestuarios_megatlon.jpg",
}

print("Leyendo HTML...")
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

for card_id, filename in fotos.items():
    print(f"\nProcesando {card_id} <- {filename}")
    b64 = resize_b64(filename)
    data_uri = f"data:image/jpeg;base64,{b64}"
    pattern = rf'(<div class="soporte-card" id="{card_id}">[\s\S]*?<img src=")[^"]*(")'
    new_html, count = re.subn(pattern, lambda m: m.group(1) + data_uri + m.group(2), html)
    if count:
        html = new_html
        print(f"  OK — imagen reemplazada en card #{card_id}")
    else:
        print(f"  ERROR — card #{card_id} no encontrada")

print("\nGuardando HTML...")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Listo!")
