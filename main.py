import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
import threading
import renomeador


class RenomeadorApp:

    def __init__(self, root):

        self.root = root
        self.root.title("JMBA Softwares - Renomeador Inteligente de Fotos 1.0")
        self.root.geometry("800x500")
        self.root.minsize(700, 450)

        self.pasta = tk.StringVar()

        self.criar_interface()

    # ==========================================================
    # INTERFACE
    # ==========================================================

    def criar_interface(self):

        frame_topo = ttk.Frame(self.root, padding=10)
        frame_topo.pack(fill="x")

        ttk.Label(
            frame_topo,
            text="Pasta:"
        ).grid(
            row=0,
            column=0,
            sticky="w"
        )

        self.entry_pasta = ttk.Entry(
            frame_topo,
            textvariable=self.pasta
        )

        self.entry_pasta.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=(0, 5)
        )

        frame_topo.columnconfigure(0, weight=1)

        self.bt_selecionar = ttk.Button(
            frame_topo,
            text="Selecionar...",
            command=self.selecionar_pasta
        ).grid(
            row=1,
            column=1
        )

        self.bt_iniciar = ttk.Button(
            self.root,
            text="Iniciar",
            command=self.iniciar
        )

        self.bt_iniciar.pack(
            pady=(0, 10)
        )

        ttk.Label(
            self.root,
            text="Log"
        ).pack(
            anchor="w",
            padx=10
        )

        self.log = ScrolledText(
            self.root,
            height=18,
            state="disabled"
        )

        self.log.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 10)
        )

        self.status = ttk.Label(
            self.root,
            text="Pronto.",
            anchor="w"
        )

        self.status.pack(
            fill="x",
            padx=10,
            pady=(0, 10)
        )

    # ==========================================================
    # LOG
    # ==========================================================

    def escrever_log(self, texto, substituir=False):

        self.root.after_idle(
            self._escrever_log,
            texto,
            substituir
        )

    def _escrever_log(self, texto, substituir=False):

        self.log.configure(state="normal")

        if substituir:

            try:

                ultima = self.log.index("end-2l")
  
                self.log.delete(ultima, "end-1c")

            except:

                pass

        self.log.insert("end", texto + "\n")

        self.log.see("end")

        self.log.configure(state="disabled")


    def alterar_status(self, texto):

        self.root.after(
            0,
            lambda: self.status.config(text=texto)
        )

    def habilitar_botao(self, habilitado=True):

        self.root.after(
            0,
            lambda: self.bt_iniciar.config(
                state="normal" if habilitado else "disabled"
            ) 
        )

        self.root.after(
            0,
            lambda: self.bt_selecionar.config(
                state="normal" if habilitado else "disabled"
            )
        )

    def limpar_log(self):

        self.log.configure(state="normal")
        self.log.delete("1.0", "end")
        self.log.configure(state="disabled")

    # ==========================================================
    # ESCOLHER PASTA
    # ==========================================================

    def selecionar_pasta(self):

        pasta = filedialog.askdirectory()

        if pasta:
            self.pasta.set(pasta)

    # ==========================================================
    # INICIAR
    # ==========================================================

    def iniciar(self):
        self.limpar_log()

        if not self.pasta.get():

            messagebox.showwarning(
                "Aviso",
                "Selecione uma pasta."
            )

            return

        self.habilitar_botao(False)
        self.alterar_status("Processando...")

        thread = threading.Thread(
            target=self.executar,
            daemon=True
        )

        thread.start()

    # ==========================================================
    # PROCESSAMENTO
    # ==========================================================

    def executar(self):

       try:

           renomeador.executar(
               pasta=self.pasta.get(),
               callback=self.escrever_log
           )

           self.alterar_status("Concluído.")

       except Exception as e:
  
           self.escrever_log(f"ERRO: {e}")
           self.alterar_status("Erro.")

       finally:

           self.habilitar_botao(True)


# ==========================================================
# MAIN
# ==========================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = RenomeadorApp(root)

    root.mainloop()
