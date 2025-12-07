import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_URL = "https://open.er-api.com/v6/latest/BRL"

def obter_taxas_de_cambio():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()

        return data.get('rates', {})
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter taxas de câmbio da API: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    taxas = obter_taxas_de_cambio()

    if taxas is None:
        return render_template('index.html', error="Não foi possível conectar à API de Câmbio.")
    
    moedas_disponiveis = sorted(taxas.keys())

    valor_convertido = None
    erro_conversao = None

    if request.method == 'POST':
        try:
            valor = float(request.form['valor'])
            moeda_origem = request.form['moeda_origem']
            moeda_destino = request.form['moeda_destino']
        
            taxa_origem = taxas[moeda_origem]
            taxa_destino = taxas[moeda_destino]

            valor_em_base = valor / taxa_origem

            valor_convertido = valor_em_base * taxa_destino

            valor_convertido = f"{valor_convertido:,.2f}"
        
        except ValueError:
            erro_conversao = "O valor inserido não é um número válido."
        except KeyError:
            erro_conversao = "Erro nas moedas selecionadas."
        except Exception as e:
            erro_conversao = f"Ocorreu um erro: {e}"
    
    return render_template(
        'index.html',
        moedas=moedas_disponiveis,
        valor_convertido=valor_convertido,
        erro=erro_conversao
    )

if __name__ == '__main__':
    app.run(debug=True)
