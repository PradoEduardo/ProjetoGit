from tkinter import * #Biblioteca Tkinter para interfaces.
from tkinter import messagebox
import qrcode
from PIL import Image, ImageDraw

def gera_qr_code():
    url = website_entry.get()

    if len(url) == 0:
     messagebox.showinfo(
        title='ERRO!',
        message='Favor insira uma URL válida')
    else:
     opcao_escolhida = messagebox.askokcancel(
        title=url,
        message= f'O endereço URL é: \n'
                 f'Endereço {url} \n'
                 f'Pronto para Salvar?')

    if opcao_escolhida:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color= 'black', back_color='white')
            img.save('QRcode.png')


janela = Tk()
janela.title('Gerador de Código QR')
janela.config(padx=100, pady=25)
janela.config(background='light gray')
janela.iconphoto(False, PhotoImage(file='codigo-qr.png'))
texto = Label (janela, bg='light gray', text= 'Insira uma URL válida e \n clique no botão para gerar um QR Code exclusivo!', font='ArialBlack 15').grid(column=1, row=0, padx=0, pady=100)
texto = Label (janela, bg='light gray', text= '\n O QR Code será exportado em formato .png \n para sua pasta de projetos Python.', font='Arial 8').grid(column=1, row=2, padx=0, pady=0)



website_label = Label(text='URL:')
website_label.grid(row=5, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=5, column=1, columnspan=2)
website_entry.focus()
add_button = Button(text='Gerar QR Code', width=36, command=gera_qr_code)
add_button.grid(row=7, column=1, columnspan=2)

janela.mainloop()
