# -*- coding: utf-8 -*-

import Tkinter
from Tkinter import Text, Tk 
import tkMessageBox
from note_api import NoteAPI

#~ Creamos nuestro propio widget de texto derivado del Tkinter. Al crear una instancia, esperará una referencia de la API
#~ El constructor Tk () crea una nueva ventana de UI y el widget de texto se coloca dentro de ella
class NoteText(Text):
    def __init__(self, api, text='', id=None):
        self.master = Tk()
        self.id = id
        self.api = api
        Text.__init__(self, self.master, bg='#f9f3a9',
                      wrap='word', undo=True)
        self.bind('<Control-n>', self.create)
        self.bind('<Control-s>', self.save)
        if id:
            self.master.title('Nota #%d' % id)
            self.delete('1.0', 'end')
            self.insert('1.0', text)
            self.master.geometry('220x235')
            self.pack(fill='both',  expand=1)
 
#~ La acción de crear abre una nueva ventana vacía
    def create(self, event=None):
        NoteText(self.api, '')

#~ La acción de guardar se puede realizar en tareas existentes o nuevas
    def save(self,  event=None):
        text = self.get('1.0', 'end')
        self.id = self.api.set(text,  self.id)
        tkMessageBox.showinfo('Info', 'Note %d Saved.' % self.id)

#~ Finalmente, agregaremos el código que recupera y crea todas las ventanas de notas cuando se inicia el programa
if  __name__    ==  '__main__': 
    srv, db  = 'http://192.168.1.106:8069', 'odoo'
    user, pwd = 'admin', 'admin'
    api = NoteAPI(srv, db, user, pwd)
    for note in api.get():
        x = NoteText(api, note['name'], note['id'])
        x.master.mainloop()
