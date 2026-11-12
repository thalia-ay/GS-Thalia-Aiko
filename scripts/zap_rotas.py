import pickle

import requests


def zap_started(zap, target):
    base = target.rstrip("/")
    sessao = requests.Session()
    sessao.trust_env = False
    sessao.proxies = {
        "http": "http://127.0.0.1:8091",
        "https": "http://127.0.0.1:8091",
    }

    rotas = [
        ("/", {"nome": "cidadao"}),
        ("/busca", {"q": "certidao"}),
        ("/produto", {"id": "1"}),
        ("/saudacao", {"nome": "cidadao"}),
        ("/ir", {"url": "/busca"}),
        ("/arquivo", {"nome": "termos.txt"}),
        ("/diagnostico", {"host": "127.0.0.1"}),
        ("/calc", {"expr": "2+2"}),
        ("/consulta-externa", {"url": base + "/"}),
        ("/admin/relatorio", {"mes": "01"}),
    ]

    for rota, parametros in rotas:
        resposta = sessao.get(
            base + rota,
            params=parametros,
            timeout=30,
            allow_redirects=False,
        )
        print("Cadastro GET:", rota, resposta.status_code)

    corpos = [
        (
            "/login",
            "usuario=teste&senha=teste",
            "application/x-www-form-urlencoded",
        ),
        ("/config", "tema: claro\n", "application/yaml"),
        (
            "/importar",
            pickle.dumps({"itens": []}, protocol=4),
            "application/octet-stream",
        ),
        (
            "/admin/nfe",
            "<nfe><emitente>Teste</emitente><valor>10</valor></nfe>",
            "application/xml",
        ),
    ]

    for rota, corpo, tipo in corpos:
        resposta = sessao.post(
            base + rota,
            data=corpo,
            headers={"Content-Type": tipo},
            timeout=30,
            allow_redirects=False,
        )
        print("Cadastro POST:", rota, resposta.status_code)

    resposta = sessao.get(
        base + "/admin/painel",
        headers={"Authorization": "Bearer teste-invalido"},
        timeout=30,
        allow_redirects=False,
    )
    print("Cadastro GET: /admin/painel", resposta.status_code)
