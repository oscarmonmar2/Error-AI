import language_tool_python

def revisar_texto(texto):
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
