import pandas as pd
from flask import Flask, request, render_template, send_file, jsonify
import os

app = Flask(__name__, template_folder='/home/ianlee/Área de Trabalho/analise-vendas/templates')

# Rota para exibir o formulário de upload
@app.route('/')
def index():
    return render_template('upload.html')

# Rota para processar o upload e gerar resultados
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Nenhum arquivo selecionado"}), 400

    try:
        # Lê o arquivo CSV enviado
        df = pd.read_csv(file)
    except Exception as e:
        return jsonify({"error": f"Erro ao processar o arquivo: {str(e)}"}), 500

    # Calcular o total de vendas
    df['Receita_Total'] = df['Quantidade'] * df['Preco_Unitario']
    df['Lucro_Total'] = df['Quantidade'] * (df['Preco_Unitario'] - df['Custo_Unitario'])

    # Calcular o total de vendas e lucro
    total_vendas = df['Receita_Total'].sum()
    total_lucro = df['Lucro_Total'].sum()

    # Resumo por categoria
    resumo_categorias = df.groupby('Categoria').agg({
        'Receita_Total': 'sum',
        'Lucro_Total': 'sum'
    }).reset_index().to_dict(orient='records')

    # Verifica se o diretório existe, caso contrário, cria
    updated_file_dir = '/home/ianlee/Área de Trabalho/analise-vendas/Data'
    os.makedirs(updated_file_dir, exist_ok=True)
    updated_file_path = os.path.join(updated_file_dir, 'updated_vendas.csv')

    # Salvar o arquivo atualizado
    df.to_csv(updated_file_path, index=False)

    # Exibir os resultados para o usuário
    return render_template('resultado.html', 
                           total_vendas=total_vendas, 
                           total_lucro=total_lucro, 
                           resumo_categorias=resumo_categorias, 
                           tabela=df.to_html(classes='table table-striped', index=False),
                           updated_file_path=updated_file_path)

# Rota para permitir o download do arquivo atualizado
@app.route('/download')
def download():
    updated_file_path = '/home/ianlee/Área de Trabalho/analise-vendas/Data/updated_vendas.csv'
    return send_file(updated_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
