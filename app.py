from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
from pathlib import Path

app = Flask(__name__)
app.secret_key = "educluster-v5-secret"

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)
ALLOWED_EXTENSIONS = {"xlsx", "xls"}

state = {
    "jenjang": [],
    "pendidikan": {"SD": None, "SMP": None, "SMA": None},
    "ipm": None,
    "kemiskinan": None,
}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file(file, prefix):
    if not file or not file.filename:
        return None, "Silakan pilih file terlebih dahulu."
    if not allowed_file(file.filename):
        return None, "File harus berformat .xlsx atau .xls."
    original = secure_filename(file.filename)
    filename = f"{prefix}_{original}"
    file.save(UPLOAD_DIR / filename)
    return original, None

@app.context_processor
def common():
    return {"state": state}

@app.route("/")
def dashboard():
    return render_template("dashboard.html", title="Dashboard", step=0)

@app.route("/jenjang", methods=["GET", "POST"])
def jenjang():
    if request.method == "POST":
        selected = request.form.getlist("jenjang")
        if not selected:
            flash("Pilih minimal satu jenjang pendidikan.", "error")
            return redirect(url_for("jenjang"))
        state["jenjang"] = selected
        session["jenjang"] = selected
        return redirect(url_for("data_pendidikan"))
    return render_template("jenjang.html", title="Pilih Jenjang Pendidikan", step=1)

@app.route("/data-pendidikan", methods=["GET", "POST"])
def data_pendidikan():
    if not state["jenjang"]:
        return redirect(url_for("jenjang"))

    if request.method == "POST":
        jenjang = request.form.get("jenjang")
        file = request.files.get("file")
        original, error = save_file(file, jenjang.lower() if jenjang else "pendidikan")
        if error:
            flash(error, "error")
        else:
            state["pendidikan"][jenjang] = original
            flash(f"Data {jenjang} berhasil diunggah.", "success")
        return redirect(url_for("data_pendidikan"))

    return render_template("data_pendidikan.html", title="Data Pendidikan", step=2)

@app.route("/ipm-kemiskinan", methods=["GET", "POST"])
def ipm_kemiskinan():
    if not state["jenjang"]:
        return redirect(url_for("jenjang"))

    if request.method == "POST":
        ipm = request.files.get("ipm_file")
        kem = request.files.get("kemiskinan_file")

        if ipm and ipm.filename:
            original, error = save_file(ipm, "ipm")
            if error:
                flash(f"IPM: {error}", "error")
            else:
                state["ipm"] = original

        if kem and kem.filename:
            original, error = save_file(kem, "kemiskinan")
            if error:
                flash(f"Kemiskinan: {error}", "error")
            else:
                state["kemiskinan"] = original

        return redirect(url_for("review"))

    return render_template("ipm_kemiskinan.html", title="IPM & Kemiskinan", step=3)

@app.route("/review")
def review():
    if not state["jenjang"]:
        return redirect(url_for("jenjang"))
    return render_template("review.html", title="Review Data", step=4)

@app.route("/hasil")
def hasil():
    if not state["jenjang"]:
        return redirect(url_for("jenjang"))
    return render_template("hasil.html", title="Hasil Analisis", step=5)

@app.route("/back/<page>")
def back(page):
    routes = {
        "jenjang": "jenjang",
        "pendidikan": "data_pendidikan",
        "pendukung": "ipm_kemiskinan",
        "review": "review",
    }
    return redirect(url_for(routes.get(page, "dashboard")))

@app.route("/reset")
def reset():
    state["jenjang"] = []
    state["pendidikan"] = {"SD": None, "SMP": None, "SMA": None}
    state["ipm"] = None
    state["kemiskinan"] = None
    session.clear()
    flash("Data prototype telah direset.", "success")
    return redirect(url_for("dashboard"))

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
