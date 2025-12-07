# Conversor de Moedas Web (Flask & ExchangeRate-API)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-2.3-green)
![License](https://img.shields.io/badge/License-MIT-orange)
![API](https://img.shields.io/badge/API-ExchangeRate--API-blueviolet)

Este projeto é um conversor de moedas simples baseado em uma interface web, desenvolvido com Python e o micro-framework Flask. Ele demonstra a integração com uma API pública para buscar taxas de câmbio em tempo real e realizar cálculos de conversão.

---

## Funcionalidades

* **Busca em Tempo Real:** Obtém as taxas de câmbio atualizadas da ExchangeRate-API.
* **Conversão Bidirecional:** Permite converter qualquer moeda disponível para qualquer outra.
* **Interface Simples:** Interface web intuitiva (HTML/CSS) para facilitar a entrada de dados.
* **Base BRL:** A API está configurada para buscar todas as taxas com base no Real Brasileiro (BRL).

---

## Tecnologias Utilizadas

* **Python 3.x**
* **Flask**
* **Requests**
* **HTML & CSS**
* **Jinja**

---

## Integração com API

Este projeto utiliza a API pública e gratuita da **ExchangeRate-API**.

* **Endpoint Principal:** `https://open.er-api.com/v6/latest/BRL`

A integração demonstra o tratamento de requisições, parsing (leitura) de JSON e tratamento básico de erros (como falha na conexão).

---

## Pré-requisitos

- Python 3.x
- Pip
- Navegador web

---

## Como rodar o projeto

```bash
git clone https://github.com/Jhonatasgrs/conversor-moedas
cd conversor-moedas

