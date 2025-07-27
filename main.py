import os
from flask import Flask, request, render_template_string
import language_tool_python

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    texto = ""
    errores = []
    if request.method == "POST":
        texto = request.form.get("texto", "")
        tool = language_tool_python.LanguageTool('es')
        matches = tool.check(texto)
        errores = [match.message for match in matches]
    return render_template_string("""
        <form method="post">
            <textarea name="texto" rows="10" cols="50">{{ texto }}</textarea><br>
            <button type="submit">Revisar</button>
        </form>
        {% if errores %}
            <h3>Errores detectados:</h3>
            <ul>
                {% for error in errores %}
                    <li>{{ error }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    """, texto=texto, errores=errores)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
