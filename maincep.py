import requests
import tkinter as tk
import tkinter.messagebox


def busca_endereco(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        endereco = resposta.json()
        entry_rua.delete(0, tk.END)
        entry_rua.insert(0, endereco["logradouro"])
        entry_bairro.delete(0, tk.END)
        entry_bairro.insert(0, endereco["bairro"])
        entry_cidade.delete(0, tk.END)
        entry_cidade.insert(0, endereco["localidade"])
        entry_uf.delete(0, tk.END)
        entry_uf.insert(0, endereco["uf"])
    else:
        # exibe uma mensagem de erro caso o CEP não seja encontrado
        tkinter.messagebox.showerror("Erro", "CEP não encontrado")


root = tk.Tk()
root.title("Busca de endereço")

frame_cep = tk.Frame(root)
frame_cep.pack(pady=10)

label_cep = tk.Label(frame_cep, text="CEP:")
label_cep.pack(side="left")

entry_cep = tk.Entry(frame_cep)
entry_cep.pack(side="left", fill="x", expand=True)
entry_cep.bind("<Return>", lambda event: busca_endereco(entry_cep.get()))

frame_rua = tk.Frame(root)
frame_rua.pack(pady=10)

label_rua = tk.Label(frame_rua, text="Rua:")
label_rua.pack(side="left")

entry_rua = tk.Entry(frame_rua)
entry_rua.pack(side="left", fill="x", expand=True)

frame_bairro = tk.Frame(root)
frame_bairro.pack(pady=10)

label_bairro = tk.Label(frame_bairro, text="Bairro:")
label_bairro.pack(side="left")

entry_bairro = tk.Entry(frame_bairro)
entry_bairro.pack(side="left", fill="x", expand=True)

frame_cidade = tk.Frame(root)
frame_cidade.pack(pady=10)

label_cidade = tk.Label(frame_cidade, text="Cidade:")
label_cidade.pack(side="left")

entry_cidade = tk.Entry(frame_cidade)
entry_cidade.pack(side="left", fill="x", expand=True)

frame_uf = tk.Frame(root)
frame_uf.pack(pady=10)

label_uf = tk.Label(frame_uf, text="UF:")
label_uf.pack(side="left")

entry_uf = tk.Entry(frame_uf)
entry_uf.pack(side="left", fill="x", expand=True)

frame_complemento = tk.Frame(root)
frame_complemento.pack(pady=10)

label_complemento = tk.Label(frame_complemento, text="Complemento:")
label_complemento.pack(side="left")

entry_complemento = tk.Entry(frame_complemento)
entry_complemento.pack(side="left", fill="x", expand=True)

frame_numero = tk.Frame(root)
frame_numero.pack(pady=10)

label_numero = tk.Label(frame_numero, text="Nº:")
label_numero.pack(side="left")

entry_numero = tk.Entry(frame_numero)
entry_numero.pack(side="left", fill="x", expand=True)

def limpar_campos():
    entry_cep.delete(0, tk.END)
    entry_rua.delete(0, tk.END)
    entry_bairro.delete(0, tk.END)
    entry_cidade.delete(0, tk.END)
    entry_uf.delete(0, tk.END)
    entry_complemento.delete(0, tk.END)
    entry_numero.delete(0, tk.END)

button_limpar = tk.Button(root, text="Limpar", command=limpar_campos)
button_limpar.pack(side="left", padx=10)

button_buscar = tk.Button(root, text="Buscar", command=lambda: busca_endereco(entry_cep.get()))
button_buscar.pack(side="right")

root.mainloop()

