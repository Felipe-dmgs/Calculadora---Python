# app.py

import streamlit as st
from calculadora_backend import Backend # Importa a classe do outro arquivo

# Instancia o backend
calc = Backend()

# --- Configuração da Página ---
st.set_page_config(page_title="Calculadora", layout="centered")

st.title("Calculadora com Streamlit 🎈")

# --- Gerenciamento de Estado ---
# Usamos o st.session_state para manter o valor da expressão entre os re-runs
if 'expression' not in st.session_state:
    st.session_state.expression = ""

# --- Funções da Interface ---

# Função para lidar com o clique de um botão
def handle_click(button_value):
    # Se o valor for 'C', limpa a expressão
    if button_value == 'C':
        st.session_state.expression = ""
    # Se for '=', calcula o resultado
    elif button_value == '=':
        try:
            # Sua lógica de separar a string
            # Adicionamos espaços para garantir a separação correta
            parts = st.session_state.expression.split()
            if len(parts) != 3:
                st.session_state.expression = "ERRO"
                return

            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])

            result = ""
            if operator == '+':
                result = calc.somar(num1, num2)
            elif operator == '-':
                result = calc.subtrair(num1, num2)
            elif operator == '×': # Usamos o caractere de multiplicação
                result = calc.multiplicar(num1, num2)
            elif operator == '÷': # Usamos o caractere de divisão
                result = calc.dividir(num1, num2)[0] # Pegamos apenas o quociente

            # Formata o resultado para remover o .0 se for inteiro
            if isinstance(result, float) and result.is_integer():
                st.session_state.expression = str(int(result))
            else:
                st.session_state.expression = str(result)

        except Exception as e:
            st.session_state.expression = "ERRO"
    # Adiciona o valor do botão à expressão
    else:
        # Adiciona espaços ao redor dos operadores para facilitar o split
        if button_value in ['+', '-', '×', '÷']:
            st.session_state.expression += f" {button_value} "
        else:
            st.session_state.expression += button_value

# --- Layout da Calculadora ---
# --- Layout da Calculadora (CORRIGIDO) ---

# Visor da calculadora
st.text_input("Cálculo", st.session_state.expression, key="display", disabled=True)

# Define as linhas de botões
button_rows = [
    ['7', '8', '9', '÷'],
    ['4', '5', '6', '×'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Cria os botões em uma grade
for row in button_rows:
    cols = st.columns(4)
    for i, button_label in enumerate(row):
        # --- INÍCIO DA CORREÇÃO ---
        # Cria uma chave segura para o botão, substituindo caracteres especiais
        key_safe_label = button_label
        if button_label == '÷':
            key_safe_label = 'divide'
        elif button_label == '×':
            key_safe_label = 'multiply'
        elif button_label == '-':
            key_safe_label = 'subtract'
        elif button_label == '+':
            key_safe_label = 'add'
        
        # Usa a chave segura (key_safe_label) para o parâmetro key, 
        # mas o rótulo original (button_label) para o que é exibido.
        if cols[i].button(button_label, key=f"btn_{key_safe_label}", use_container_width=True):
            handle_click(button_label)
            st.rerun()
            
        # --- FIM DA CORREÇÃO ---
st.markdown("---")
st.subheader("Outras Funções")

# --- Seção para Bhaskara ---
with st.expander("Calcular Fórmula de Bhaskara"):
    st.latex("ax^2 + bx + c = 0")
    colA, colB, colC = st.columns(3)
    a = colA.number_input("Valor de a", value=1.0, format="%.2f")
    b = colB.number_input("Valor de b", value=-5.0, format="%.2f")
    c = colC.number_input("Valor de c", value=6.0, format="%.2f")

    if st.button("Calcular Bhaskara"):
        if a == 0:
            st.error("O valor de 'a' não pode ser zero.")
        else:
            x1, x2 = calc.bhaskara(a, b, c)
            st.success(f"As raízes são: **x₁ = {x1}** e **x₂ = {x2}**")