import language_tool_python

def revisar_texto(texto):
    errores.append({
    'mensaje': m.message,
    'contexto': m.context,
    'sugerencia': m.replacements[0] if m.replacements else 'No disponible'
})
    tool = language_tool_python.LanguageTool('es')
    errores = tool.check(texto)

    print(f"\n✅ Se encontraron {len(errores)} errores:")
    for i, error in enumerate(errores, 1):
        print(f"\n🔸 Error {i}:")
        print(f"   Texto: '{error.context}'")
        print(f"   Problema: {error.message}")
        print(f"   Recomendación: {', '.join(error.replacements)}")

def main():
    print("📝 Detector de errores en documentos o texto copiado\n")
    print("1. Analizar un archivo .txt")
    print("2. Pegar texto manualmente")
    opcion = input("\nElige una opción (1 o 2): ")

    if opcion == "1":
        ruta = input("📂 Ingresa la ruta del archivo: ")
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                contenido = f.read()
            revisar_texto(contenido)
        except FileNotFoundError:
            print("❌ Archivo no encontrado.")
    elif opcion == "2":
        print("\n✂️ Pega tu texto (escribe 'FIN' en una nueva línea para terminar):")
        lineas = []
        while True:
            linea = input()
            if linea.strip().upper() == "FIN":
                break
            lineas.append(linea)
        texto = "\n".join(lineas)
        revisar_texto(texto)
    else:
        print("❌ Opción no válida.")

if __name__ == "__main__":
    main()
import os
from flask import Flask, request, render_template
import language_tool_python

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    texto = ""
    errores = []
    if request.method == "POST":
        texto = request.form.get("texto", "")
        tool = language_tool_python.LanguageTool('es', remote_server='https://api.languagetool.org')
        matches = tool.check(texto)
        errores = [match.message for match in matches]
    return render_template("index.html", texto=texto, errores=errores)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
matches = tool.check(texto)
for i, match in enumerate(matches, start=1):
    print(f"🔸 Error {i}:")
    print(f"   Texto: '{match.context}'")
    print(f"   Problema: {match.message}")
    print(f"   Recomendación: {match.replacements[0] if match.replacements else 'No disponible'}")
from flask import Flask, request, render_template
import language_tool_python

app = Flask(__name__)

tool = language_tool_python.LanguageTool('es', remote_server='https://api.languagetool.org')

@app.route('/', methods=['GET', 'POST'])
def index():
    errores = []
    texto = ''
    if request.method == 'POST':
        texto = request.form['texto']
        matches = tool.check(texto)
        for m in matches:
            errores.append({
                'mensaje': m.message,
                'contexto': m.context,
                'sugerencia': m.replacements[0] if m.replacements else 'No disponible'
            })
    return render_template('index.html', errores=errores, texto=texto)
