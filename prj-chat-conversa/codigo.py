import flet as ft

def main(pagina):
    titulo = ft.Text("Chat Online")

    chat = ft.Column()

    def enviar_msg_tunel(mensagem):
        #adicionar mensagem no chat
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)

        pagina.update()

    pagina.pubsub.subscribe(enviar_msg_tunel)

    def envia_mensagem(e):
        pagina.pubsub.send_all(f"{nome_usuario.value}: {campo_mensagem.value}")
        #limpe campo mensagem
        campo_mensagem.value=""

        pagina.update()

    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=envia_mensagem)
    botao_mensagem = ft.ElevatedButton("Enviar mensagem", on_click=envia_mensagem)
    linha_enviar = ft.Row([campo_mensagem, botao_mensagem])
    def entrar_chat(e):
        #limpa página
        popup.open=False
        pagina.remove(botao_iniciar)
        pagina.remove(titulo)
        #Cria chat
        pagina.add(chat)
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
        pagina.add(linha_enviar)
        #Atualiza página
        pagina.update()

    titulo_popup = ft.Text("Bem-Vindo ao chat")
    nome_usuario = ft.TextField(label="Escreva seu nome")
    botao_popup = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    popup = ft.AlertDialog(open=False, modal=True, title=titulo_popup, content=nome_usuario, actions=[botao_popup])

    def abrir_popup(e):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    pagina.add(titulo)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER)