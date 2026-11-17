"""Interfaz web demostrativa para la clase Producto."""

from flask import Flask, render_template

from src.producto import Producto

app = Flask(__name__)


@app.get("/")
def inicio():
    ejemplo = Producto("P001", "Teclado", 350, 10)
    return render_template("index.html", ejemplo=ejemplo)
