#!/bin/bash

# --- Configurações ---
VENV_DIR="venv"
VENV_ACTIVATE_PATH="$VENV_DIR/bin/activate"
REQUIREMENTS_FILE="requirements.txt"

# --- Função para tratamento de erros de execução ---
check_error() {
    local exit_code=$?
    if [ $exit_code -ne 0 ]; then
        echo "❌ ERRO: O comando anterior falhou com o código de saída $exit_code."
        exit $exit_code
    fi
}

# --- Lógica de Execução ---

echo "--- Iniciando processo de configuração ---"

# 1. Tentar ativar o ambiente virtual existente
if [ -f "$VENV_ACTIVATE_PATH" ]; then
    echo "✅ Ambiente virtual '$VENV_DIR' encontrado. Ativando..."
    source "$VENV_ACTIVATE_PATH"
    check_error
    
    # 2. Instalar dependências (mesmo que já exista, para garantir atualizações)
    echo "📦 Instalando/Atualizando dependências do $REQUIREMENTS_FILE..."
    pip install --upgrade pip
    pip install -r "$REQUIREMENTS_FILE"
    check_error
    
else
    # 3. Criar e configurar o ambiente virtual
    echo "⚙️ Ambiente virtual '$VENV_DIR' não encontrado. Criando..."
    python3 -m venv "$VENV_DIR"
    check_error
    
    echo "✅ Ativando ambiente virtual..."
    source "$VENV_ACTIVATE_PATH"
    check_error
    
    # 4. Instalar dependências
    if [ -f "$REQUIREMENTS_FILE" ]; then
        echo "📦 Instalando dependências do $REQUIREMENTS_FILE..."
        pip install --upgrade pip
        pip install -r "$REQUIREMENTS_FILE"
        check_error
    else
        echo "⚠️ Aviso: O arquivo '$REQUIREMENTS_FILE' não foi encontrado. Nenhuma dependência instalada via pip."
    fi
fi

echo "--- Configuração Concluída. ---"
echo "O ambiente virtual está agora ativo. Para desativar, execute 'deactivate'."