import secrets
import sys
from pathlib import Path

variaveis = [
    "CT_APP_PY_13",
    "CT_CONFIG_SETTINGS_PY_6",
    "CT_CONFIG_SETTINGS_PY_7",
    "CT_CONFIG_SETTINGS_PY_8",
    "CT_LOJA_ADMIN_PY_24",
    "CT_LOJA_ADMIN_PY_8",
    "POSTGRES_PASSWORD",
]

arquivo = Path(sys.argv[1])
arquivo.touch(mode=0o600, exist_ok=False)
arquivo.write_text(
    "".join(f"{nome}={secrets.token_hex(32)}\n" for nome in variaveis)
    + "PORTA=8544\n"
)
