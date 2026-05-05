#!/usr/bin/env python
import subprocess
import sys
import os

def main():
    print("=" * 50)
    print("Calculadora de Métodos Numéricos")
    print("=" * 50)
    print()
    
    # Instalar dependencias
    print("📦 Instalando dependencias...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("✅ Dependencias instaladas")
    print()
    
    # Ejecutar Streamlit
    print("🚀 Iniciando aplicación...")
    print("La aplicación se abrirá en tu navegador en http://localhost:8501")
    print()
    
    os.system("streamlit run ui/Menu.py")

if __name__ == "__main__":
    main()
