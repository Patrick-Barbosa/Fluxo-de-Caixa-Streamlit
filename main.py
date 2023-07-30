## IMPORTS

## CORE IMPORTS
import streamlit as st
from PIL import Image
import pandas as pd
from datetime import datetime

# Obtendo a data e hora atual
## LOGIN IMPORTS
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

##
# Criptografar Senhas
#hashed_passwords = stauth.Hasher(['insira a senha aqui']).generate()
##

st.set_page_config(
    page_title="Fluxo de Caixa",
    page_icon=":moneybag:",
    layout="wide",
    menu_items={
        'Get Help': 'https://docs.streamlit.io',
        'About': "Feito por: Patrick barbosa, saiba mais no link:  https://github.com/patrick-barbosa"
    }
)

# Código de Login
config = yaml.load(open('config.yaml'), Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# data_hora_atual = datetime.now()
name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    # LOGADO
    st.title(f'Bem Vindo ao fluxo de caixa, *{name}*!')
    
    with st.container():
        st.write('Descreva as informações da venda abaixo:')
        col1, col2, col3= st.columns([2, 2, 1])
        with col1:
            st.text_input("Produto")
        with col2:
            st.selectbox("Forma de Pagamento", options=['Cartão de Crédito', 'Cartão de Débito', 'Voucher', 'Pix', 'Dinheiro', 'Pagamento Online'], placeholder="Selecione a Forma de Pagamento")
        with col3:
            st.number_input("Quantidade", step = 1)

    
    






    
    
    ## SIDEBAR
    with st.sidebar:
        authenticator.logout('Logout', 'main', key='unique_key')
    ##
    # with open('database.xlsx', 'rb') as f:
    #     file_data = f.read()
    #     st.download_button('Baixar arquivo Excel', file_data, file_name='estudo.xlsx')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')