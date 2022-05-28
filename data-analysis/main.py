import pandas as pd
from twilio.rest import Client

account_sid = ""
auth_token  = ""
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} alguém bateu a meta, Vendedor : {vendedor}, N° de vendas : {vendas}')
        # Nessa parte é necessário o login na plataforma twilio, para cadastrar um número de envio.
        message = client.messages.create(
            to="telefone_que_recebe",
            from_="telefone_de_envio",
            body=f'No mês de {mes} alguém bateu a meta, Vendedor :{vendedor}, N° de vendas : {vendas}')
        print(message.sid)
