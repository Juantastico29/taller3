from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    promedio = None
    estado = None
    errores = []

    if request.method == "POST":
        try:
            nota1 = float(request.form.get("nota1", 0))
            nota2 = float(request.form.get("nota2", 0))
            nota3 = float(request.form.get("nota3", 0))
            asistencia = float(request.form.get("asistencia", 0))

            # Validaciones simples según el enunciado
            if not (10 <= nota1 <= 70 and 10 <= nota2 <= 70 and 10 <= nota3 <= 70):
                errores.append("Las notas deben estar entre 10 y 70.")
            if not (0 <= asistencia <= 100):
                errores.append("La asistencia debe estar entre 0 y 100.")

            if not errores:
                promedio = (nota1 + nota2 + nota3) / 3

                if promedio >= 40 and asistencia >= 75:
                    estado = "Aprobado"
                else:
                    estado = "Reprobado"

        except ValueError:
            errores.append("Debes ingresar valores numéricos válidos.")

    return render_template(
        "ejercicio1.html",
        promedio=promedio,
        estado=estado,
        errores=errores
    )


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    nombre_mas_largo = None
    largo_nombre = None
    errores = []

    if request.method == "POST":
        nombre1 = request.form.get("nombre1", "").strip()
        nombre2 = request.form.get("nombre2", "").strip()
        nombre3 = request.form.get("nombre3", "").strip()

        # Validar que no estén vacíos
        if not nombre1 or not nombre2 or not nombre3:
            errores.append("Debes ingresar los tres nombres.")
        # Validar que sean diferentes
        if nombre1 and nombre2 and nombre3:
            if len({nombre1.lower(), nombre2.lower(), nombre3.lower()}) < 3:
                errores.append("Los tres nombres deben ser diferentes.")

        if not errores:
            # Buscar el nombre con más caracteres
            lista_nombres = [nombre1, nombre2, nombre3]
            nombre_mas_largo = max(lista_nombres, key=len)
            largo_nombre = len(nombre_mas_largo)

    return render_template(
        "ejercicio2.html",
        nombre_mas_largo=nombre_mas_largo,
        largo_nombre=largo_nombre,
        errores=errores
    )


if __name__ == "__main__":
    app.run(debug=True)
