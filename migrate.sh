#!/bin/bash

# --- Configuração ---
VENV_PATH="venv/bin/activate"

# --- Ativação do Ambiente Virtual ---
if [ -f "$VENV_PATH" ]; then
    source "$VENV_PATH"
else
    echo "ERRO: O arquivo de ativação do ambiente virtual não foi encontrado em $VENV_PATH."
    echo "Certifique-se de que o ambiente virtual está configurado corretamente."
    exit 1
fi

# --- Variáveis ---
ACTION=$1
MESSAGE=$2

# --- Função de Uso ---
show_usage() {
    echo "Uso: ./migrate.sh <ação> [mensagem]"
    echo ""
    echo "Ações disponíveis (Alembic):"
    echo "  create \"mensagem\"  -> Cria uma nova migração autogerada com a mensagem fornecida."
    echo "  apply              -> Aplica todas as migrações pendentes (upgrade head)."
    echo "  rollback           -> Reverte a última migração aplicada (downgrade -1)."
    echo ""
    [ -n "$VIRTUAL_ENV" ] && deactivate
    exit 1
}

# --- Função de Execução e Verificação de Erro ---
execute_alembic() {
    # Executa o comando Alembic e verifica o código de saída
    echo "Executando: $@"
    source "$VENV_PATH"
    "$@"
    local exit_code=$?
    if [ $exit_code -ne 0 ]; then
        echo "ERRO: O comando Alembic falhou com o código de saída $exit_code."
        # Desativa o ambiente virtual antes de sair
        [ -n "$VIRTUAL_ENV" ] && deactivate
        exit $exit_code
    fi
}

# --- Lógica de Execução ---

if [ -z "$ACTION" ]; then
    echo "ERRO: Ação não especificada."
    show_usage
fi

case "$ACTION" in
    "create")
        if [ -z "$MESSAGE" ]; then
            echo "ERRO: Você deve fornecer uma mensagem para criar uma nova migração."
            show_usage
        fi
        echo "--- Criando migração: \"$MESSAGE\" ---"
        execute_alembic alembic revision --autogenerate -m "$MESSAGE"
        ;;

    "apply")
        echo "--- Aplicando todas as migrações pendentes (upgrade head) ---"
        execute_alembic alembic upgrade head
        ;;

    "rollback")
        echo "--- Revertendo a última migração aplicada (downgrade -1) ---"
        execute_alembic alembic downgrade -1
        ;;

    *)
        echo "ERRO: Ação inválida: $ACTION"
        show_usage
        ;;
esac

echo "--- Processo Alembic Concluído. ---"

# --- Desativação do Ambiente Virtual ---
[ -n "$VIRTUAL_ENV" ] && deactivate

exit 0