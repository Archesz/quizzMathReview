import streamlit as st
import random

# ---------- CONFIG ----------- #
st.set_page_config(page_title="FlashCards - Jovi", page_icon="🚀")

# ---------- Funções ----------- #
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -------- Sidebar ---------- #

with st.sidebar:
    st.write("**Projeto de Revisão (Jovi):**")

    st.caption("Detalhes")
    st.write("**Questões Criadas com:**")
    st.caption("LUNA: 219 Questões.")
    st.caption("By Jovi (Atosh)| Version 0.2.1")

# CSS
local_css("style.css")

# ---------------- SESSION STATE ----------------

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

if "button2_clicked" not in st.session_state:
    st.session_state.button2_clicked = False

if "q_no" not in st.session_state:
    st.session_state.q_no = 0

if "q_no_temp" not in st.session_state:
    st.session_state.q_no_temp = 0

if "questoes" not in st.session_state:
    st.session_state.questoes = [
        {"Pergunta": "O que é um ponto?", "Resposta": "um ponto é uma entidade fundamental que não tem dimensões. É considerado um objeto elementar, sem comprimento, largura ou altura.", "image": False},
        {"Pergunta": "O que é uma reta?", "Resposta": "Uma reta é um objeto geométrico fundamental. Uma linha inifita e sem curvas. É composta por uma sequência contínua de pontos.", "image": False},
        {"Pergunta": "O que é um plano?", "Resposta": "Um plano é um conceito matemático que pode ser descrito como uma superfíce plana e infinita que se estende para todas as dimensões. Composto por três pontos não colineares.", "image": False},
        {"Pergunta": "O que significa pontos colineares?", "Resposta": "São pontos que pertencem a uma mesma linha.", "image": False},
        {"Pergunta": "Defina segmento de reta:", "Resposta": "Um segmento de reta é uma reta que possui um ponto inicial e final. Ou seja, é uma reta finita, ou uma parte de uma reta.", "image": False},
        {"Pergunta": "Defina retas paralelas:", "Resposta": "Retas paralelas são retas que NUNCA se encontram. Podemos traçar uma reta perpendicular que separa ambas.", "image": False},
        {"Pergunta": "Defina retas perpendiculares: ", "Resposta": "São retas que formam um ângulo de 90º entre si.", "image": False},
        {"Pergunta": "O que é uma semireta?", "Resposta": "Uma semireta é uma reta que possui início e não possuí fim.", "image": False},
        {"Pergunta": "O que é um raio?", "Resposta": "Um raio é um segmento de reta que liga o centro de um círculo até qualquer ponto na circunferência de um círculo.", "image": False},
        {"Pergunta": "O que é uma corda?", "Resposta": "É um segmento que liga dois pontos quaisquer da circunferência sem passar pelo centro.", "image": False},
        {"Pergunta": "O que é um diametro?", "Resposta": "É um segmento que liga dois pontos da circunferência, passando pelo centro do círculo", "image": False},
        {"Pergunta": "O que é um ângulo?", "Resposta": "Um ângulo é a união de duas semirretas com um vértice comum.", "image": False},
        {"Pergunta": "O que é um vértice?", "Resposta": "Encontro de duas semiretas.", "image": False},
        {"Pergunta": "Defina ângulo agudo:", "Resposta": "É um ângulo com menos de 90º", "image": False},
        {"Pergunta": "Defina ângulo reto:", "Resposta": "É um ângulo com 90º.", "image": False},
        {"Pergunta": "Defina ângulo obtuso:", "Resposta": "É um ângulo maior que 90º.", "image": False},
        {"Pergunta": "Defina ângulo raso:", "Resposta": "É um ângulo com 180º", "image": False},
        {"Pergunta": "Quantos Graus tem um triângulo?", "Resposta": "Qualquer triângulo possuí 180º.", "image": False},
        {"Pergunta": "Quantos Graus tem um círculo?", "Resposta": "Júpiter", "image": False},
        {"Pergunta": "Quais são as classificações de um triângulo?", "Resposta": "Podemos classificar um triângulo como Escalenos (Três lados diferentes), Isósceles (Dois lados iguais) ou Equilátero (Três lados iguais).", "image": False},
        {"Pergunta": "O que são retas transversair?", "Resposta": "Retas transversais são retas que cruzam um par ou um feixe de retas paralelas.", "image": False},
        {"Pergunta": "Em que tipo de triângulo podemos aplicar o Teorema de Pitagoras?", "Resposta": "O teorema de pitagoras pode ser aplicado em triângulos retângulos.", "image": False},
        {"Pergunta": "Qual é a hipotenusa e os catetos de um triângulo retângulo?", "Resposta": "A hipotenusa é o ângulo oposto ao ângulo reto, os catetos são os demais lados.", "image": False},
        {"Pergunta": "Qual a fórmula do teorema de pitagoras?", "Resposta": "a² + b² = c²", "image": False},
        {"Pergunta": "O que é a Mediana de um triângulo?", "Resposta": "Mediana é um segmento que divide as bases do triângulo em duas partes iguais. Dessa forma temos que mediana é um segmento de reta com origem em um dos vértices do triângulo e extremidade no ponto médio do lado oposto ao vértice.", "image": False},
        {"Pergunta": "O que é a Bissetriz?", "Resposta": "Bissetriz também é um segmento de reta com origem em um dos vértices do triângulo com a outra extremidade no lado oposto a esse vértice. Sendo que ela divide ao meio o ângulo correspondente ao vértice.", "image": False},
        {"Pergunta": "O que é a altura de um triângulo?", "Resposta": "Encontramos a medida da altura de um triângulo através de um segmento de reta com origem em um dos vértices e perpendicular (forma um ângulo de 90º) ao lado oposto.", "image": False},
        {"Pergunta": "Como se calcula a área de um triângulo?", "Resposta": "A = \\frac{b \cdot h}{2}", "image": False},
        {"Pergunta": "", "Resposta": "Júpiter", "image": False},
        {"Pergunta": "", "Resposta": "Júpiter", "image": False},
    ]

# callbacks
def callback():
    st.session_state.button_clicked = True


def callback2():
    st.session_state.button2_clicked = True


# -------- Main Page -------- #
tab1, tab2, tab3 = st.tabs(["Flashcards", "Ranking", "Fontes"])

respondidas = []

def sorteiaPergunta():
    if st.session_state.questoes:
        questao = random.choice(st.session_state.questoes)
        st.session_state.questoes.remove(questao)
        return questao
    else:
        return None

with tab1:
    st.title("FlashCards")

    col1, col2 = st.columns(2)

    sortear = st.button("Sortear", on_click=callback)
    if sortear and st.session_state.button_clicked:
        questao = sorteiaPergunta()
        if questao:
            st.subheader(questao["Pergunta"])

            with st.expander("Resposta"):
                st.write(questao["Resposta"])
                if questao["image"] != False:
                    st.image(questao["Image"])
        else:
            st.warning("Todas as perguntas foram respondidas.")
