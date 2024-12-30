#!/bin/bash

# Stoppe das Skript, falls ein Fehler auftritt
set -e

# Überprüfen, ob eine Python-Version angegeben wurde
if [ -z "$1" ]; then
  echo "Bitte eine Python-Version angeben (z. B. 3.12.0)."
  exit 1
fi

PYTHON_VERSION=$1

# Überprüfen, ob pyenv installiert ist
if ! command -v pyenv &> /dev/null; then
  echo "pyenv ist nicht installiert. Bitte installiere pyenv zuerst."
  exit 1
fi

# Überprüfen, ob die angegebene Python-Version installiert ist
if ! pyenv versions | grep "$PYTHON_VERSION" &> /dev/null; then
  echo "Python-Version $PYTHON_VERSION ist nicht installiert. Installiere sie mit 'pyenv install $PYTHON_VERSION'."
  exit 1
fi

# Setze die gewünschte Python-Version
pyenv shell $PYTHON_VERSION

# Erstelle eine virtuelle Umgebung
echo "Erstelle virtuelle Umgebung..."
python -m venv venv

# Aktiviere die virtuelle Umgebung
echo "Aktiviere virtuelle Umgebung..."
source venv/bin/activate

# Installiere Pakete aus requirements.txt, falls vorhanden
if [ -f "requirements.txt" ]; then
  echo "Installiere Pakete aus requirements.txt..."
  pip install -r requirements.txt
else
  echo "Keine requirements.txt gefunden. Die Umgebung wurde ohne zusätzliche Pakete erstellt."
fi

echo "Die virtuelle Umgebung wurde erfolgreich eingerichtet."
