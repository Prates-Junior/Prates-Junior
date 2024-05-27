import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis

# Configurações iniciais da janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Inicializa a janela principal
janela = customtkinter.CTk()
janela.geometry("500x600") 

# Carrega as conversões disponíveis
dic_conversoes_disponiveis = conversoes_disponiveis()

# Define o título e os textos das labels
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("", 20))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem:")
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino:")

# Função para carregar moedas de destino com base na moeda de origem selecionada
def carregar_moedas_destino(moeda_selecionada):
    try:
        lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
        campo_moeda_destino.configure(values=lista_moedas_destino)
        campo_moeda_destino.set(lista_moedas_destino[0])  # Define a primeira moeda de destino como selecionada
    except KeyError:
        campo_moeda_destino.configure(values=["Moeda não disponível"])
        campo_moeda_destino.set("Moeda não disponível")

# Carrega os nomes das moedas disponíveis
moedas_disponiveis = nomes_moedas()

# Define os menus de seleção de moedas
campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=list(moedas_disponiveis.keys()),
                                                 command=carregar_moedas_destino)
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["Selecione uma moeda de origem"])

# Função para converter moedas
def converter_moeda():
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_destino.get()
    if moeda_origem and moeda_destino:
        cotacao = texto_cotacao_moeda(moeda_origem, moeda_destino)
        texto_cotacao_moeda.configure(text=f"1 {moeda_origem} = {cotacao} {moeda_destino}")

# Botão para realizar a conversão
botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda)

# Frame rolável para listar as moedas disponíveis
lista_moedas = customtkinter.CTkScrollableFrame(janela)

# Carrega e exibe a lista de moedas disponíveis
for codigo_moeda in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[codigo_moeda]
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=f"{codigo_moeda}: {nome_moeda}")
    texto_moeda.pack()

# Texto para exibir a cotação da moeda
texto_cotacao_moeda = customtkinter.CTkLabel(janela, text="")

# Adiciona os elementos na janela
titulo.pack(padx=10, pady=10)
texto_moeda_origem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10)
texto_moeda_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10)
botao_converter.pack(padx=10, pady=10)
texto_cotacao_moeda.pack(padx=10, pady=10)
lista_moedas.pack(padx=10, pady=10)

# Inicia a execução da janela
janela.mainloop()
