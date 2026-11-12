import os
"""Configuracoes do Citizen Tech Market."""
DEBUG = True
REGIAO = "sa-east-1"
BUCKET = "ct-market-notas-fiscais"

AWS_ACCESS_KEY_ID = os.environ["CT_CONFIG_SETTINGS_PY_6"]
AWS_SECRET_ACCESS_KEY = os.environ["CT_CONFIG_SETTINGS_PY_7"]
SENDGRID_API_KEY = os.environ["CT_CONFIG_SETTINGS_PY_8"]
