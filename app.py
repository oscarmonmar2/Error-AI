from flask import Flask, render_template, request
import language_tool_python

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    errores = []
    texto_original = ""
    
    if request.method == "POST":
        texto_original = request.form["texto"]
        tool = language_tool_python.LanguageTool('es')
        matches = tool.check(texto_original)

        for match in matches:
            errores.append({
                "contexto": match.context,
                "mensaje": match.message,
                "recomendacion": match.replacements
            })

    return render_template("index.html", errores=errores, texto=texto_original)

if __name__ == "__main__":
    app.run(debug=True)
