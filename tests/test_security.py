import unittest

from app import app


class SecurityTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_pagina_inicial(self):
        self.assertEqual(self.client.get("/").status_code, 200)

    def test_busca_nao_renderiza_script(self):
        resposta = self.client.get(
            "/busca",
            query_string={"q": "<script>alert(1)</script>"}
        )
        self.assertNotIn(b"<script>alert(1)</script>", resposta.data)

    def test_saudacao_nao_executa_template(self):
        resposta = self.client.get(
            "/saudacao",
            query_string={"nome": "{{7*7}}"}
        )
        self.assertNotIn(b"Ola, 49!", resposta.data)


if __name__ == "__main__":
    unittest.main()
