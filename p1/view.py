import requests
import gi
import qrcode
import os
from datetime import datetime

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Atk



class View:
    def start(cls):
        Gtk.main()
    def quit(cls, widget=None, event=None):
        Gtk.main_quit()

    def __init__(self):
        self.window = Gtk.Window()
        self.window.set_title('Rastreo Covid')
        self.window.set_default_size(750, 700)
        self.window.connect('destroy', Gtk.main_quit)
        self.vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.vbox.set_homogeneous(True)
        self.window.add(self.vbox)
        self.grid = Gtk.Grid()
        self.grid.set_row_spacing(25)
        self.grid.set_column_spacing(25)
        self.vbox.pack_start(self.grid, expand=True, fill=False, padding=50)
        self.searchentry = Gtk.SearchEntry()
        self.grid.insert_row(0)
        self.grid.attach(self.searchentry, 0, 0, 1, 1)
        hgrid = Gtk.Grid()
        hgrid.set_border_width(5)
        hgrid.set_row_spacing(5)
        hgrid.set_column_spacing(300)
        self.label1 = Gtk.Label(label = "Nombre:")
        hgrid.attach(self.label1, 0, 0, 1, 1)
        self.label2 = Gtk.Label(label = "Apellidos:")
        hgrid.attach(self.label2, 0, 1, 1, 1)
        self.label3 = Gtk.Label(label = "¿Está vacunado?:")
        hgrid.attach(self.label3, 0, 2, 1, 1)
        self.label4 = Gtk.Label(label = "Nombre de usuario:")
        hgrid.attach(self.label4, 1, 0, 1, 1)
        self.label5 = Gtk.Label(label = "Teléfono:")
        hgrid.attach(self.label5, 1, 1, 1, 1)
        self.label6 = Gtk.Label(label = "Email:")
        hgrid.attach(self.label6, 1, 2, 1, 1)
        self.label7 = Gtk.Label(label = "uuid:")
        hgrid.attach(self.label7, 0, 3, 1, 1)
        self.grid.insert_row(2)
        self.grid.attach(hgrid, 0, 2, 1, 1)
        self.notebook = Gtk.Notebook()
        self.grid.insert_row(3) #delete_row la elimina asi podemos actualizar la info
        self.grid.attach(self.notebook, 0, 3, 1, 1)
        self.notebook.insert_page(Gtk.Label(label = "Rastreo"), Gtk.Label(label = "Rastreo contactos"), 0)
        self.notebook.insert_page(Gtk.Label(label = "Sitios"), Gtk.Label(label = "Ultimos Sitios"), 1)
        self.notebook.insert_page(Gtk.Label(label = "QR"), Gtk.Label(label = "QR"), 2)
        self.start_date = Gtk.Entry(text= "")
        self.end_date = Gtk.Entry(text= "")
        entry1 = self.start_date.get_accessible()
        entry1.set_name("start date")
        entry2 = self.end_date.get_accessible()
        entry2.set_name("end date")
        self.rastrear = Gtk.Button(label=("Rastrear"))
        self.agrid = Gtk.Grid()
        self.agrid.set_border_width(20)
        self.agrid.set_row_spacing(20)
        self.agrid.set_column_spacing(10)
        label = Gtk.Label(label = "Seleccione el rango de fechas para iniciar el rastreo de contactos.")
        self.agrid.insert_row(0)
        self.agrid.attach(label, 0, 0, 1, 1)
        date = datetime.now()
        date_sample= datetime.strftime(date, "%x %H:%M ")
        label_start_date = Gtk.Label(label=("Desde:"), xalign=1)
        self.start_date.set_placeholder_text(("Ex. {}").format(date_sample))
        self.start_date.get_accessible().add_relationship(Atk.RelationType.LABELLED_BY, label_start_date.get_accessible())
        label_end_date = Gtk.Label(label= ("Hasta:"), xalign=0)
        self.end_date.set_placeholder_text(("Ex. {}").format(date_sample))
        self.end_date.get_accessible().add_relationship(Atk.RelationType.LABELLED_BY, label_end_date.get_accessible())
        entry1 = self.start_date.get_accessible()
        entry1.set_name("start date")
        entry2 = self.end_date.get_accessible()
        entry2.set_name("end date")
        self.agrid.insert_row(1)
        self.agrid.attach(label_start_date, 0, 1, 1, 1)
        self.agrid.attach(self.start_date, 1, 1, 1, 1)
        self.agrid.attach(label_end_date, 2, 1, 1, 1)
        self.agrid.attach(self.end_date, 3, 1, 1, 1)
        self.agrid.attach(self.rastrear, 4, 1, 1, 1)
        
        

    def new_error(self, text):
        if hasattr(self, "infobar"):
            self.infobar.hide()
            del self.infobar
        self.infobar = Gtk.InfoBar()
        self.infobar.connect("response", self.on_infobar_response)
        self.infobar.set_show_close_button(True)
        self.infobar.set_message_type(Gtk.MessageType.ERROR)
        self.infobar.show() 
        self.grid.insert_row(1)
        self.grid.attach(self.infobar, 0, 1, 1, 1)
        texto = Gtk.Label(text)
        texto.show()
        content = self.infobar.get_content_area()
        content.add(texto)
        self.infobar.set_message_type(Gtk.MessageType.ERROR)
        


        

    def on_infobar_response(self, infobar, respose_id):
        self.infobar.hide()

    def set_rastreocalendar(self) :
        
        if hasattr(self, "scrolledwindow"):
            self.agrid.remove_row(2)
            self.agrid.remove(self.scrolledwindow)
        self.notebook.remove_page(0)
        self.agrid.show_all()
        self.notebook.insert_page(self.agrid, Gtk.Label(label ="Rastreo Contactos"),0)


    def update_info(self, r) :        
        for d in r :
            self.label1.set_markup(("<b>Nombre:</b>" + " "+d['name']))
            self.label2.set_markup(("<b>Apellidos:</b>" + " "+d['surname']))
            if (d['is_vaccinated']):
                self.label3.set_markup(("<b>¿Está vacunado?:</b>" + " "+"Si"))
            else:
                self.label3.set_markup(("<b>¿Está vacunado?:</b>" + " "+"No"))
            self.label4.set_markup(("<b>Nombre de usuario:</b>" + " "+d['username']))
            self.label5.set_markup(("<b>Teléfono:</b>" + " "+d['phone']))
            self.label6.set_markup(("<b>Email:</b>" + " "+d['email']))
            self.label7.set_markup(("<b>Uuid:</b>" + " "+d['uuid']))
            if hasattr(self, 'uuid') :
                delattr(self, 'uuid')
            self.uuid = d['uuid']
            qrname = d['name']+","+d['surname']+","+d['uuid']
            qr = qrcode.make(qrname)
            qr.save(qrname+".png")
            img = Gtk.Image.new_from_file(qrname+".png")
            img.show()
            self.notebook.remove_page(2)
            self.notebook.insert_page(img, Gtk.Label(label = "QR"), 2)
            os.remove(qrname+".png")
            self.set_rastreocalendar()
        
    def set_usersitios(self, r):
        scrolledwindow = Gtk.ScrolledWindow()
        sgrid = Gtk.Grid()
        sgrid.set_border_width(10)
        sgrid.set_row_spacing(10)
        sgrid.set_column_spacing(40)
        label = Gtk.Label(label = "")
        label.set_markup("<b><big>Lugar:</big></b>")
        sgrid.attach(label, 0, 0, 1, 1)
        label = Gtk.Label(label = "")
        label.set_markup("<b><big>Direccióm:</big></b>")
        sgrid.attach(label, 1, 0, 1, 1)
        label = Gtk.Label(label = "")
        label.set_markup("<b><big>Fecha:</big></b>")
        sgrid.attach(label, 2, 0, 1, 1)
        label = Gtk.Label(label = "")
        label.set_markup("<b><big>Temperatura:</big></b>")
        sgrid.attach(label, 3, 0, 1, 1)
        count = 1
        sitios = [""]
        for d in r :
            if d['facility']['name'] != sitios[-1]:
                sitios.append(d['facility']['name'])
                label = Gtk.Label(label = d['facility']['name'])
                if(count == 1):
                    label_acc = label.get_accessible()
                    label_acc.set_name("NOMBREINICIO")
                if(count == len(r)/2 - 1):
                    label_acc = label.get_accessible()
                    label_acc.set_name("NOMBREFINAL")
                sgrid.attach(label, 0, count, 1, 1)
                label = Gtk.Label(label = d['facility']['address'])
                if(count == 1):
                    label_acc = label.get_accessible()
                    label_acc.set_name("DIRECCIONINICIO")
                if(count == len(r)/2-1):
                    label_acc = label.get_accessible()
                    label_acc.set_name("DIRECCIONFINAL")
                sgrid.attach(label, 1, count, 1, 1)
                timestamp = d['timestamp']
                date = datetime.fromisoformat(timestamp)
                dateparsed = datetime.strftime(date, "%d/%m/%Y %H:%M:%S")
                label = Gtk.Label(label = dateparsed)
                if(count == 1):
                    label_acc = label.get_accessible()
                    label_acc.set_name("FECHAINICIO")
                if(count == len(r)/2 - 1):
                    label_acc = label.get_accessible()
                    label_acc.set_name("FECHAFINAL")
                sgrid.attach(label, 2, count, 1, 1)
                label = Gtk.Label(label = d['temperature'])
                if(count == 1):
                    label_acc = label.get_accessible()
                    label_acc.set_name("TEMPERATURAINICIO")
                if(count == len(r)/2 - 1):
                    label_acc = label.get_accessible()
                    label_acc.set_name("TEMPERATURAFINAL")
                sgrid.attach(label, 3, count, 1, 1)
                count += 1

        scrolledwindow.add(sgrid)
        scrolledwindow.show_all()
        self.notebook.remove_page(1)
        self.notebook.insert_page(scrolledwindow, Gtk.Label(label = "Ultimos Sitios"), 1)
    

    
    def set_ultimoscontactos(self, lista) :
        if hasattr(self, "scrolledwindow"):
            self.agrid.remove_row(2)
            self.agrid.remove(self.scrolledwindow)
        self.scrolledwindow = Gtk.ScrolledWindow()
        cgrid = Gtk.Grid()
        cgrid.set_border_width(20)
        cgrid.set_row_spacing(10)
        cgrid.set_column_spacing(70)
        countrow = 0
        countlist = 0
        if len(lista) == 0 :
            label = Gtk.Label(label = "", xalign = 1)
            label.set_markup("<big><b>No se han encontrado contactos cercanos en las \nfechas introducidas, pruebe con otras.</b></big>")
            self.agrid.insert_row(2)
            self.agrid.attach(label, 0, 2, 1, 1)
            self.agrid.show_all()
            self.notebook.remove_page(0)
            self.notebook.insert_page(self.agrid, Gtk.Label(label ="Rastreo Contactos"),0)
        else :
            for d in range(len(lista)) :
                auxgrid = Gtk.Grid()
                auxgrid.set_border_width(10)
                auxgrid.set_row_spacing(10)
                auxgrid.set_column_spacing(100)
                label = Gtk.Label(label = "")
                label.set_markup("<big><span style=\"normal\"><b>Lugar: "+lista[countlist][0]+"</b></span></big>")
                auxgrid.attach(label, 1, 0, 1, 1)
                timestamp = lista[countlist][2]
                date = datetime.fromisoformat(timestamp)
                dateparsed = datetime.strftime(date, "%d/%m/%Y")
                label = Gtk.Label(label = "")
                label.set_markup("<big><span style=\"normal\"><b>Fecha: "+dateparsed+"</b></span></big>")

                auxgrid.attach(label, 1, 1, 1, 1)
                label = Gtk.Label(label = "")
                label.set_markup("<big><span style=\"normal\"><b>Lista de personas a rastrear: </b></span></big>")
                auxgrid.attach(label, 1, 2, 1, 1)
                label = Gtk.Label(label = "")
                label.set_markup("<big><span style=\"normal\"><b>Nombre contacto: </b></span></big>")
                auxgrid.attach(label, 0, 3, 1, 1)
                label = Gtk.Label(label = "")
                label.set_markup("<big><span style=\"normal\"><b>Uuid: </b></span></big>")    
                auxgrid.attach(label, 1, 3, 1, 1) 
                label = Gtk.Label(label = "")
                label.set_markup("<big><span style=\"normal\"><b>¿Está vacunado? </b></span></big>")            
                auxgrid.attach(label, 2, 3, 1, 1)
                countaux = 4
                userlist = lista[countlist][1]
                listainsertados = [[""]]
                for d in range(len(userlist)) :
                    
                    if userlist[d][2] != self.uuid and userlist[d][2] not in listainsertados:
                        listainsertados.append(userlist[d][2])
                        label = Gtk.Label(label = userlist[d][0])
                        label = Gtk.Label(label = "")
                        label.set_markup("<big><span style=\"normal\">"+userlist[d][0]+"</span></big>")
                        label.set_selectable(True)
                        auxgrid.attach(label, 0, countaux, 1, 1)
                        label = Gtk.Label(label = "")
                        label.set_markup("<big><span style=\"normal\">"+userlist[d][2]+"</span></big>")                    
                        label.set_selectable(True)
                        auxgrid.attach(label, 1, countaux, 1, 1)
                        label = Gtk.Label(label = "")
                        label.set_markup("<big><span style=\"normal\">"+userlist[d][1]+"</span></big>")                    
                        auxgrid.attach(label, 2, countaux, 1, 1)
                        countaux += 1
                if len(listainsertados) > 1 :
                    cgrid.insert_row(countrow)
                    cgrid.attach(auxgrid, 0, countrow, 10, 1)
                    countrow += 1                
                countlist += 1
                
            self.scrolledwindow.add(cgrid)
            self.agrid.insert_row(2)
            self.scrolledwindow.show_all()
            self.agrid.attach(self.scrolledwindow, 0, 2, 5, 20)
            self.notebook.remove_page(0)
            self.notebook.insert_page(self.agrid, Gtk.Label(label ="Rastreo Contactos"),0)

        

    def connect_start_date_changed(self, fun):
        self.start_date.connect('changed', fun)

    def connect_end_date_changed(self, fun):
        self.end_date.connect('changed', fun)

    def connect_rastrear_clicked(self, handler):
        self.rastrear.connect('clicked', handler)
    
    def on_search_activated(self, searchentry):
        self.searchentry.connect('activate', searchentry)
        
    
    def show_all(self):
        self.window.show_all()
    
    def hide(self):
        self.window.hide()
    
    def destroy(self):
        self.window.destroy()


