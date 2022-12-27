import openai
import tkinter as tk
from tkinter import ttk, Frame, PhotoImage
import pyperclip
import os

# Creamos los tooltips que expliquen cada opción
class CreateToolTip(object):

    def __init__(self, widget, text='widget info'):
        self.waittime = 500     # milisegundos
        self.wraplength = 180   # pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creamos una toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                       background="#ffffff", relief='solid', borderwidth=1,
                       wraplength = self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()


# Comprobamos si el archivo de texto tiene el código de OpenAI
if os.path.getsize('archivo.txt') == 0:
    # Creamos la ventana para escribir texto
    window = tk.Tk()
    window.title("Añadir OpenAI API Key")
    window['bg'] = "#ffffff"
    window.resizable(width=False, height=False)

    # Creamos una etiqueta
    lbl = tk.Label(window, text="Introduce tu API Key de OpenAI:", background="#ffffff")
    lbl.grid(row=0, column=0, pady=5, padx=10)

    # Creamos una caja de texto
    txt = tk.Entry(window, width=20, justify=tk.CENTER)
    txt.grid(row=1, column=0, pady=5, padx=5)

    # Creamos un botón para guardar
    btn = tk.Button(window, text="Guardar", command=lambda: guardar_texto(txt.get()))
    btn.grid(row=2, column=0, pady=5, padx=5)

    # Explicación de la contraseña
    lbl = tk.Label(window, text="Esta aplicación precisa de una API Key que proporciona OpenAI. Si se introduce una API Key errónea, la aplicación no funcionará. Una vez introducida la API Key deberá volver a iniciar la aplicación y no se volverá a mostrar de nuevo esta ventana.", background="#ffffff", wraplength=210)
    lbl.grid(row=3, column=0, pady=10, padx=5)

    # Función para guardar el texto en el archivo
    def guardar_texto(texto):
        file = open('archivo.txt', 'w')
        file.write(texto)
        file.close()
        window.destroy()

    window.mainloop()

else:
    # Creamos la ventana principal
    file = open('archivo.txt', 'r')
    openai.api_key = file.read()

    root = tk.Tk()
    root.title("Procesador de argumentos")
    root['bg'] = "#ffffff"
    root.resizable(width=True, height=True)

    # Título de la ventana
    label_titulo = tk.Label(root, text="Procesador de Argumentos", background="#ffffff", font=45)
    label_titulo.grid(row=0, column=0, pady=10, columnspan=4)

    # Creamos una lista vacia donde se almacenara los elementos seleccionados
    seleccionados = []
    resultado = ""
    seleccionados_nuevo = []
    resultado_nuevo = ""

    # Creamos funciones para preparar el texto
    def eliminar_salto_inicial(texto):
        while texto[0] == "\n":
            texto = texto[1:]
        return texto


    def borrar_saltos_linea_vacios(texto):
        return texto.replace("\n\n", "\n")


    def tabular_parrafos(texto):
        parrafos = texto.split("\n")
        parrafos_tabular = []
        for parrafo in parrafos:
            parrafos_tabular.append("\t" + parrafo)
        return "\n".join(parrafos_tabular)


    def texto_preparado_para_procesador(texto):
        preparado1 = eliminar_salto_inicial(texto)
        preparado2 = borrar_saltos_linea_vacios(preparado1)
        preparado3 = tabular_parrafos(preparado2)
        return preparado3


    def escribir_frase(tupla):
        # inicializamos una lista vacía
        lista = []
        # recorremos la tupla
        for elem in tupla:
            # agregamos cada elemento a la lista
            lista.append(elem)
        # si la lista tiene más de un elemento
        if len(lista) > 1:
            # quitamos el último elemento
            ultimo_elem = lista.pop()
            # unimos todos los elementos con comas
            frase = ', '.join(lista)
            # agregamos el último elemento con 'y'
            frase += ' y ' + ultimo_elem
        # si la lista sólo tiene un elemento
        else:
            # la frase es el elemento
            frase = lista[0]
        # devolvemos la frase
        return frase


    def check_state():
        if var.get() == 2:
            coh.configure(state=tk.DISABLED)
            coherencia.set(0)
            incoh.configure(state=tk.NORMAL)
            seri.configure(state=tk.DISABLED)
            seriedad.set(0)
            rehus.configure(state=tk.NORMAL)
            clari.configure(state=tk.DISABLED)
            claridad.set(0)
            ambi.configure(state=tk.NORMAL)
            conci.configure(state=tk.DISABLED)
            concision.set(0)
            confu.configure(state=tk.NORMAL)
            concre.configure(state=tk.DISABLED)
            concreto.set(0)
            inconcre.configure(state=tk.NORMAL)
            espont.configure(state=tk.DISABLED)
            espontaneidad.set(0)
            prepa.configure(state=tk.NORMAL)
            persis.configure(state=tk.DISABLED)
            persistencia.set(0)
            motivos.configure(state=tk.NORMAL)
            cointest.configure(state=tk.DISABLED)
            coincidenciatest_var.set(0)
            coincidenciatest.delete(0, tk.END)
            coincidenciatest.grid_forget()
            coindoc.configure(state=tk.DISABLED)
            coincidenciadoc_var.set(0)
            coincidenciadoc.delete(0, tk.END)
            coincidenciadoc.grid_forget()
            ami.configure(state=tk.NORMAL)
            fami.configure(state=tk.NORMAL)
        elif var.get() == 1:
            coh.configure(state=tk.NORMAL)
            incoh.configure(state=tk.DISABLED)
            incoherencia.set(0)
            seri.configure(state=tk.NORMAL)
            rehus.configure(state=tk.DISABLED)
            rehusion.set(0)
            clari.configure(state=tk.NORMAL)
            ambi.configure(state=tk.DISABLED)
            ambiguo.set(0)
            conci.configure(state=tk.NORMAL)
            confu.configure(state=tk.DISABLED)
            confuso.set(0)
            concre.configure(state=tk.NORMAL)
            inconcre.configure(state=tk.DISABLED)
            inconcreto.set(0)
            espont.configure(state=tk.NORMAL)
            persis.configure(state=tk.NORMAL)
            prepa.configure(state=tk.DISABLED)
            preparacion.set(0)
            motivos.configure(state=tk.DISABLED)
            motivosespurios.set(0)
            cointest.configure(state=tk.NORMAL)
            coindoc.configure(state=tk.NORMAL)
            ami.configure(state=tk.DISABLED)
            amigo_var.set(0)
            amigo.delete(0, tk.END)
            amigo.grid_forget()
            fami.configure(state=tk.DISABLED)
            familiar_var.set(0)
            familiar.delete(0, tk.END)
            familiar.grid_forget()

    def limpiar():
        var1.set(0)
        var.set(0)
        incoh.configure(state=tk.NORMAL)
        rehus.configure(state=tk.NORMAL)
        ambi.configure(state=tk.NORMAL)
        confu.configure(state=tk.NORMAL)
        inconcre.configure(state=tk.NORMAL)
        ami.configure(state=tk.NORMAL)
        fami.configure(state=tk.NORMAL)
        coh.configure(state=tk.NORMAL)
        seri.configure(state=tk.NORMAL)
        clari.configure(state=tk.NORMAL)
        conci.configure(state=tk.NORMAL)
        concre.configure(state=tk.NORMAL)
        espont.configure(state=tk.NORMAL)
        prepa.configure(state=tk.NORMAL)
        motivos.configure(state=tk.NORMAL)
        persis.configure(state=tk.NORMAL)
        cointest.configure(state=tk.NORMAL)
        coindoc.configure(state=tk.NORMAL)
        coherencia.set(0)
        seriedad.set(0)
        claridad.set(0)
        concision.set(0)
        concreto.set(0)
        espontaneidad.set(0)
        preparacion.set(0)
        motivosespurios.set(0)
        persistencia.set(0)
        coincidenciatest_var.set(0)
        coincidenciatest.delete(0, tk.END)
        coincidenciatest.grid_forget()
        coincidenciadoc_var.set(0)
        coincidenciadoc.delete(0, tk.END)
        coincidenciadoc.grid_forget()
        incoherencia.set(0)
        rehusion.set(0)
        ambiguo.set(0)
        confuso.set(0)
        inconcreto.set(0)
        amigo_var.set(0)
        amigo.delete(0, tk.END)
        amigo.grid_forget()
        familiar_var.set(0)
        familiar.delete(0, tk.END)
        familiar.grid_forget()
        entry_nombre.delete(0, tk.END)
        entry_texto_libre.delete(0, tk.END)
        imagen_label.grid(column=3, row=0, rowspan=19)
        texto_escrito.grid_forget()

    # Tipo de testimonio
    var1 = tk.IntVar()
    interrog = tk.Radiobutton(root, text="Interrogatorio", variable=var1, value=1, background="#ffffff")
    interrog.grid(row=2, column=0, pady=2, padx=2, sticky='W')
    testif = tk.Radiobutton(root, text="Testifical", variable=var1, value=2, background="#ffffff")
    testif.grid(row=2, column=1, pady=2, padx=2, sticky='W')

    # Nombre del que presta testimonio
    entry_var_nombre = tk.StringVar()
    label_nombre = tk.Label(root, text="Nombre del declarante", background="#ffffff")
    entry_nombre = tk.Entry(root, textvariable=entry_var_nombre, justify=tk.CENTER)
    label_nombre.grid(row=1, column=0, pady=2, padx=4, sticky='W')
    entry_nombre.grid(row=1, column=1, pady=2, padx=4)

    # Me creo el testimonio
    var = tk.IntVar()
    si = tk.Radiobutton(root, text="Credibilidad", variable=var, value=1, background="#ffffff", command=check_state)
    si.grid(row=3, column=0, pady=2, padx=2, sticky='W')
    si_ttp = CreateToolTip(si, 'Es creible el testimonio prestado')
    no = tk.Radiobutton(root, text="Incredibilidad", variable=var, value=2, background="#ffffff", command=check_state)
    no.grid(row=3, column=1, pady=2, padx=2, sticky='W')
    no_ttp = CreateToolTip(no, 'No es creible el testimonio prestado')

    # linea primera
    horizontal1 = Frame(root, bg='gray', height=1, width=200)
    horizontal1.grid(row=4, column=0, pady=10, columnspan=2)

    # Coherencia
    coherencia = tk.IntVar()
    coh = tk.Checkbutton(root, text='Coherencia', variable=coherencia, background="#ffffff", justify=tk.CENTER)
    coh.grid(row=5, column=0, pady=2, padx=2, sticky='W')
    coh_ttp = CreateToolTip(coh, 'El testimonio es coherente')

    # Incoherencia
    incoherencia = tk.IntVar()
    incoh = tk.Checkbutton(root, text='Incoherencia', variable=incoherencia, background="#ffffff", justify=tk.CENTER)
    incoh.grid(row=5, column=1, pady=2, padx=2, sticky='W')
    incoh_ttp = CreateToolTip(incoh, 'El testimonio es incoherente')

    # Seriedad
    seriedad = tk.IntVar()
    seri = tk.Checkbutton(root, text='Seriedad', variable=seriedad, background="#ffffff", justify=tk.CENTER)
    seri.grid(row=6, column=0, pady=2, padx=2, sticky='W')
    seri_ttp = CreateToolTip(seri, 'Se aprecia seriedad en sus respuestas')

    # Rehusión
    rehusion = tk.IntVar()
    rehus = tk.Checkbutton(root, text='Rehusión', variable=rehusion, background="#ffffff", justify=tk.CENTER)
    rehus.grid(row=6, column=1, pady=2, padx=2, sticky='W')
    rehus_ttp = CreateToolTip(rehus, 'El declarante rehusa a contestar')

    # Claridad
    claridad = tk.IntVar()
    clari = tk.Checkbutton(root, text='Claridad', variable=claridad, background="#ffffff", justify=tk.CENTER)
    clari.grid(row=7, column=0, pady=2, padx=2, sticky='W')
    clari_ttp = CreateToolTip(clari, 'Se aprecia claridad en el testimonio')

    # Ambiguo
    ambiguo = tk.IntVar()
    ambi = tk.Checkbutton(root, text='Ambiguo', variable=ambiguo, background="#ffffff", justify=tk.CENTER)
    ambi.grid(row=7, column=1, pady=2, padx=2, sticky='W')
    ambi_ttp = CreateToolTip(ambi, 'El testimonio es ambiguo')

    # Concisión
    concision = tk.IntVar()
    conci = tk.Checkbutton(root, text='Concisión', variable=concision, background="#ffffff", justify=tk.CENTER)
    conci.grid(row=8, column=0, pady=2, padx=2, sticky='W')
    conci_ttp = CreateToolTip(conci, 'El declarante es conciso en sus respuestas')

    # Confuso
    confuso = tk.IntVar()
    confu = tk.Checkbutton(root, text='Confuso', variable=confuso, background="#ffffff", justify=tk.CENTER)
    confu.grid(row=8, column=1, pady=2, padx=2, sticky='W')
    confu_ttp = CreateToolTip(confu, 'El relato del declarante es confuso')

    # Concreto
    concreto = tk.IntVar()
    concre = tk.Checkbutton(root, text='Concreto', variable=concreto, background="#ffffff", justify=tk.CENTER)
    concre.grid(row=9, column=0, pady=2, padx=2, sticky='W')
    concre_ttp = CreateToolTip(concre, 'El declarante es concreto en sus respuestas')

    # Inconcreto
    inconcreto = tk.IntVar()
    inconcre = tk.Checkbutton(root, text='Inconcreto', variable=inconcreto, background="#ffffff", justify=tk.CENTER)
    inconcre.grid(row=9, column=1, pady=2, padx=2, sticky='W')
    inconcre_ttp = CreateToolTip(inconcre, 'El declarante no es concreto en sus respuestas')

    # Espontaneidad
    espontaneidad = tk.IntVar()
    espont = tk.Checkbutton(root, text='Espontaneidad', variable=espontaneidad, background="#ffffff", justify=tk.CENTER)
    espont.grid(row=10, column=0, pady=2, padx=2, sticky='W')
    espont_ttp = CreateToolTip(espont, 'El testimonio prestado es espontáneo')

    # Preparación
    preparacion = tk.IntVar()
    prepa = tk.Checkbutton(root, text='Aprendido', variable=preparacion, background="#ffffff", justify=tk.CENTER)
    prepa.grid(row=10, column=1, pady=2, padx=2, sticky='W')
    prepa_ttp = CreateToolTip(prepa, 'El testimonio aparenta ser un discurso aprendido')

    # Motivos espurios
    motivosespurios = tk.IntVar()
    motivos = tk.Checkbutton(root, text='Motivos espurios', variable=motivosespurios, background="#ffffff", justify=tk.CENTER)
    motivos.grid(row=11, column=1, pady=2, padx=2, sticky='W')
    motivos_ttp = CreateToolTip(motivos, 'El declarante tiene motivos espurios')

    # Persistencia
    persistencia = tk.IntVar()
    persis = tk.Checkbutton(root, text='Persistencia', variable=persistencia, background="#ffffff", justify=tk.CENTER)
    persis.grid(row=11, column=0, pady=2, padx=2, sticky='W')
    persis_ttp = CreateToolTip(persis, 'El declarante ha sido persitente en su versión de los hechos a lo largo del proceso')

    # linea segunda
    horizontal2 = Frame(root, bg='gray', height=1, width=100)
    horizontal2.grid(row=12, column=0, pady=10, columnspan=2)

    # coincidencia con documentos
    def show_concidenciadoc():
        if coincidenciadoc_var.get() == 1:
            coincidenciadoc.grid(row=13, column=1)
        else:
            coincidenciadoc.grid_forget()


    coincidenciadoc_var = tk.IntVar()
    coindoc = tk.Checkbutton(root, text="Coincidencia con documentos", variable=coincidenciadoc_var, command=show_concidenciadoc, background="#ffffff")
    coindoc.grid(row=13, column=0, pady=2, padx=2, sticky='W')
    coincidenciadoc_entry = tk.StringVar()
    coincidenciadoc = ttk.Entry(root, textvariable=coincidenciadoc_entry, justify=tk.CENTER)

    # coincidencia con otros testigos
    def show_concidenciatest():
        if coincidenciatest_var.get() == 1:
            coincidenciatest.grid(row=14, column=1)
        else:
            coincidenciatest.grid_forget()

    coincidenciatest_var = tk.IntVar()
    cointest = tk.Checkbutton(root, text="Coincidencia con testigos", variable=coincidenciatest_var, command=show_concidenciatest, background="#ffffff")
    cointest.grid(row=14, column=0, pady=2, padx=2, sticky='W')
    coincidenciatest_entry = tk.StringVar()
    coincidenciatest = ttk.Entry(root, textvariable=coincidenciatest_entry, justify=tk.CENTER)

    # amigo de la parte
    def show_amigo():
        if amigo_var.get() == 1:
            amigo.grid(row=15, column=1)
        else:
            amigo.grid_forget()


    amigo_var = tk.IntVar()
    ami = tk.Checkbutton(root, text="Amistad con", variable=amigo_var, command=show_amigo, background="#ffffff")
    ami.grid(row=15, column=0, pady=2, padx=2, sticky='W')
    amigo_entry = tk.StringVar()
    amigo = ttk.Entry(root, textvariable=amigo_entry, justify=tk.CENTER)

    # familiar de la parte
    def show_familiar():
        if familiar_var.get() == 1:
            familiar.grid(row=16, column=1)
        else:
            familiar.grid_forget()

    familiar_var = tk.IntVar()
    fami = tk.Checkbutton(root, text="Familiar de", variable=familiar_var, command=show_familiar, background="#ffffff")
    fami.grid(row=16, column=0, pady=2, padx=2, sticky='W')
    familiar_entry = tk.StringVar()
    familiar = ttk.Entry(root, textvariable=familiar_entry, justify=tk.CENTER)

    # Linea tercera
    horizontal3 = Frame(root, bg='gray', height=1, width=200)
    horizontal3.grid(row=17, column=0, pady=10, columnspan=2)

    # Texto libre
    entry_var_texto_libre = tk.StringVar()
    label_texto_libre = tk.Label(root, text="Texto Libre", background="#ffffff")
    entry_texto_libre = ttk.Entry(root, textvariable=entry_var_texto_libre, justify=tk.CENTER, width=50)
    label_texto_libre.grid(row=18, column=0, pady=2, padx=4, columnspan=2)
    entry_texto_libre.grid(row=19, column=0, pady=2, padx=4, columnspan=2)
    entry_texto_libre_ttp = CreateToolTip(entry_texto_libre, 'Añadir cualquier otro motivo de credibilidad o incredibilidad')

    # Posicionar imagen

    imagen = PhotoImage(file="pantallainicio.png")
    imagen_label = tk.Label(root, image=imagen, borderwidth="0")
    imagen_label.grid(column=3, row=0, rowspan=21)


    # Función para escribir la frase entera
    def boton_crear():
        resultado = "Escribe, como si fueras un Juez en una Sentencia, varios razonamientos jurídicos largos, sobre porqué este Juzgador "
        if var.get() == 1:
            resultado = "Escribe, como si fueras un Juez en una Sentencia, varios razonamientos jurídicos largos, sobre porqué 'este Juzgador' sí se cree el testimonio prestado "
            if var1.get() == 1:
                resultado = "Escribe, como si fueras un Juez en una Sentencia, varios razonamientos jurídicos largos, sobre porqué 'este Juzgador' sí se cree el testimonio prestado en el interrogatorio de "
            if var1.get() == 2:
                resultado = "Escribe, como si fueras un Juez en una Sentencia, varios razonamientos jurídicos largos, sobre porqué 'este Juzgador' sí se cree el testimonio prestado en la testifical de "
        if var.get() == 2:
            resultado = "Escribe, como si fueras un Juez en una Sentencia, varios razonamiento jurídicos largos, sobre porqué 'este Juzgador' no se cree el testimonio prestado "
            if var1.get() == 1:
                resultado = "Escribe, como si fueras un Juez en una Sentencia, varios razonamiento jurídicos largos, sobre porqué 'este Juzgador' no se cree el testimonio prestado en el interrogatorio de "
            if var1.get() == 2:
                resultado = "Escribe, como si fueras un Juez en una Sentencia, varios razonamiento jurídicos largos, sobre porqué 'este Juzgador' no se cree el testimonio prestado en la testifical de "
        if entry_var_nombre.get():
            resultado += entry_var_nombre.get() + ", basado en los siguientes argumentos: "
        if coherencia.get():
            seleccionados.append('coherencia')
        if incoherencia.get():
            seleccionados.append('incoherencia')
        if seriedad.get():
            seleccionados.append('seriedad en su discurso')
        if rehusion.get():
            seleccionados.append('rehusa a contestar las preguntas que se le formulan')
        if claridad.get():
            seleccionados.append('claridad en su relato')
        if ambiguo.get():
            seleccionados.append('ambiguedad en su discurso')
        if concision.get():
            seleccionados.append('conciso en sus respuestas')
        if confuso.get():
            seleccionados.append('relato confuso')
        if concreto.get():
            seleccionados.append('concreción en su testimonio')
        if inconcreto.get():
            seleccionados.append('falta de concreción en sus respuestas')
        if espontaneidad.get():
            seleccionados.append('espontaneidad en el testimonio prestado')
        if preparacion.get():
            seleccionados.append('el testimonio aparenta ser un discurso aprendido')
        if motivosespurios.get():
            seleccionados.append('el declarante tiene motivos espurios que pueden afectar a su testimonio')
        if persistencia.get():
            seleccionados.append('el declarante ha sido persistente en su versión de los hechos a lo largo del proceso')
        if coincidenciatest_var.get() == 1:
            coincidenciatestdef = "coincidencia del testimonio con otros testigos como " + coincidenciatest_entry.get()
            seleccionados.append(coincidenciatestdef)
        if coincidenciadoc_var.get() == 1:
            coincidenciadocdef = "coincidencia del testimonio con otros documentos como " + coincidenciadoc_entry.get()
            seleccionados.append(coincidenciadocdef)
        if amigo_var.get() == 1:
            amigodef = "amistad del declarante con " + amigo_entry.get()
            seleccionados.append(amigodef)
        if familiar_var.get() == 1:
            familiardef = "familiar de " + familiar_entry.get()
            seleccionados.append(familiardef)
        if entry_var_texto_libre.get():
            seleccionados.append(entry_var_texto_libre.get())
        resultado += escribir_frase(seleccionados) + "."
        imagen_label.grid_forget()
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=resultado,
            temperature=0.7,
            max_tokens=2800,
            top_p=1,
            best_of=2,
            frequency_penalty=0.2,
            presence_penalty=0.2
        )
        seleccionados.clear()
        texto_escrito["text"] = (eliminar_salto_inicial(response['choices'][0]['text']))
        texto_escrito.grid(row=0, column=3, pady=15, padx=11, rowspan=21)
        pyperclip.copy(texto_preparado_para_procesador(response['choices'][0]['text']))


    # Posicionar el texto
    texto_escrito = tk.Label(root, text="", background="#ffffff", wraplength=390, justify=tk.LEFT)
    texto_escrito_ttp = CreateToolTip(texto_escrito, 'El texto está en el portapapeles')

    # Posicionar boton de crear texto

    button = ttk.Button(root, text="Crear texto", command=boton_crear)
    button.grid(row=20, column=1, pady=15, columnspan=1)
    button_ttp = CreateToolTip(button, 'Espere unos segundos hasta que aparezca el texto a la derecha')

    # Crear atajo de teclado para crear texto

    root.bind('<Control-Return>', lambda event: button.invoke())

    # Posicionar boton de limpiar

    button2 = ttk.Button(root, text="Limpiar", command=limpiar)
    button2.grid(row=20, column=0, pady=15, columnspan=1)
    button2_ttp = CreateToolTip(button2, 'Limpiar todos los campos')

    # Crear atajo de teclado para limpiar

    root.bind('<Control-BackSpace>', lambda event: button2.invoke())

    root.mainloop()
