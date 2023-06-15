import streamlit as st
import random
import pandas as pd
import git
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

    st.divider()

    st.write("Atualizações: ")
    st.markdown("- [x] Inserido opções de diferentes disciplinas.")
    st.markdown("- [x] Inserido opção de inserir um novo conceito.")

    st.write("Próximas Atualizações: ")
    st.markdown("- [ ] Inserir as imagens para ajudar com as respostas.")
    st.markdown("- [ ] Inserir mais matérias.")
    

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

# callbacks
def callback():
    st.session_state.button_clicked = True

def callback2():
    st.session_state.button2_clicked = True

def adicionar_pergunta(disciplina, assunto, pergunta, resposta, img):
    # Ler o arquivo CSV existente
    df = pd.read_csv('flashs.csv')

    # Criar um novo DataFrame com a nova pergunta
    nova_pergunta = pd.DataFrame({"Disciplina": [disciplina], "Assunto": [assunto], 'Pergunta': [pergunta], 'Resposta': [resposta], "Imagem": 0, "Selecionada": 0})
    
    # Adicionar a nova pergunta ao DataFrame existente
    df = pd.concat([df, nova_pergunta], ignore_index=True)

    # Salvar o DataFrame atualizado de volta ao arquivo CSV
    df.to_csv('flashs.csv', index=False)

df = pd.read_csv("flashs.csv")

# -------- Main Page -------- #
tab1, tab2, tab3, tab4 = st.tabs(["Flashcards", "Ranking", "Sugerir Nova pergunta", "Banco de Perguntas"])

respondidas = []

def sorteiaPergunta(df, disciplina, assunto):
    questoes = df.query(f"Disciplina == '{disciplina}' and Assunto == '{assunto}' and Selecionada == 0")
    questoes_list = []

    for i in range(0, len(questoes)):
        questoes_list.append([questoes.iloc[i]["Pergunta"], questoes.iloc[i]["Resposta"], questoes.iloc[i]["Imagem"]])

    questao = random.choice(questoes_list)
    return questao

with tab1:
    st.title("FlashCards")

    disciplina = st.selectbox("Selecione a Disciplina: ", ["Matemática", "Física", "Biologia", "Química"])
    
    if disciplina:
        assuntos = list(df.query(f"Disciplina == '{disciplina}'")["Assunto"].unique())
        assunto = st.selectbox("Selecione o Assunto:", assuntos)

    col1, col2 = st.columns(2)

    sortear = st.button("Sortear", on_click=callback)    

    if sortear and st.session_state.button_clicked:
        questao = sorteiaPergunta(df, disciplina, assunto)
        if questao:
            st.subheader(questao[0])

            with st.expander("Resposta"):
                st.markdown(questao[1])
                if questao[2] != 0:
                    st.image(questao[2], width=None)
        else:
            st.warning("Todas as perguntas foram respondidas.")

with tab2:
    st.write("Em breve :)")
    st.write("1. Jovi")

with tab3:
    st.write("Sugerir inserção: ")
    st.write("Essa etapa ainda está em ajustes, não funciona no momento. Para sugestões contate o jovi diretamente: (19) 99539-7660")

    disciplina = st.selectbox("Disciplina: ", ["Matemática", "Física", "Biologia"])
    
    if disciplina:
        assuntos = list(df.query(f"Disciplina == '{disciplina}'")["Assunto"].unique())
        assunto = st.selectbox("Assunto:", assuntos)

    pergunta = st.text_input("Qual seria a pergunta?")
    resposta = st.text_input("E qual seria a resposta?")
    nao_sei = st.checkbox("Não sei a resposta.")
    tem_img = st.checkbox("Possui uma imagem?")
    if tem_img:
        st.text_input("Insir o link da imagem.")

    inserir = st.button("Sugerir")

    if inserir:
        if nao_sei:
            st.text("n sei")

        questao = adicionar_pergunta(disciplina, assunto, pergunta, resposta, 0)

        st.success("Pergunta sugerida!")
        st.balloons()

with tab4:
    discp = st.selectbox("Matéria", ["Matemática", "Física", "Biologia"], key="filter")

    if disciplina:
        assuntos = list(df.query(f"Disciplina == '{discp}'")["Assunto"].unique())
        assunto = st.selectbox("Assunto:", assuntos, key="assuntos")
    
        if assunto:
            questoes = df.query(f"Disciplina == '{discp}' and Assunto == '{assunto}'")
            perguntas = list(questoes["Pergunta"])
            respostas = list(questoes["Resposta"])

            pergunta = st.selectbox("Perguntas: ", perguntas)
            if(pergunta):
                st.write(respostas[perguntas.index(pergunta)])
    
