#!/usr/bin/env bash
# Script de build para Render

# Interrompe em caso de erro
set -o errexit  

# Instala dependências
pip install -r requirements.txt

# Aplica migrações
python manage.py migrate --noinput

# Coleta arquivos estáticos
python manage.py collectstatic --noinput
