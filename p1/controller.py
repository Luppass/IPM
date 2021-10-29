from requests import NullHandler
import model
import view

from datetime import datetime


class Controller:
	def __init__(self) :
		self.view = view.View()
		self.model = model.Model("http://localhost:8080/api/rest", {"x-hasura-admin-secret": "myadminsecretkey"})
		self.view.on_search_activated(self.on_search_activated)
		self.view.connect_start_date_changed(self.on_start_date_changed)
		self.view.connect_end_date_changed(self.on_end_date_changed)
		self.view.connect_rastrear_clicked(self.on_rastrear_clicked)
		
	def start(self):
		self.view.show_all()
		self.view.start()
	
	def on_search_activated(self, search) :
		[code, dictionary] = self.model.get_userinfo(search)
		if code == "404" :
			self.view.new_error("ERROR")
		if code == "200":
			self.view.update_info(dictionary)
			[code1, dict1] = self.model.get_usersitios(self.view.uuid)
			if code1 == "200" :
				self.view.set_usersitios(dict1)
	def on_start_date_changed(self, entry):
		s = entry.get_text().strip()
		if(len(s)==14):
			x = s.strip().split(" ")
			try:
				if len(x) == 2:
					self.model.start_date = x[0]
					aux = x[1].strip().split(":")
					if len(aux) == 2:
						self.model.hour_start = aux[0]
						self.model.minute_start = aux[1]
					else :
						raise ValueError
				else :
					raise ValueError
			except ValueError:
				self.view.new_error("ERROR")

	
	def on_end_date_changed(self, entry):
		s = entry.get_text().strip()
		if(len(s)==14):
			x = s.strip().split(" ")
			try:
				if len(x) == 2:
					self.model.end_date = x[0]
					aux = x[1].strip().split(":")
					if len(aux) == 2:
						self.model.hour_end = aux[0]
						self.model.minute_end = aux[1]
					else :
						raise ValueError
				else :
					raise ValueError
			except ValueError:
				self.view.new_error("ERROR")
	def on_rastrear_clicked(self, calendar) :
		[code, rultimos] = self.model.get_ultimossitios(self.view.uuid)
		count = 0
		a = [[0] * 3 for i in range(len(rultimos))]
		for d in rultimos :
			a[count][0] = d['facility']['id']
			a[count][1] = d['timestamp']
			a[count][2] = d['facility']['name']
			count+=1
		rcontactos = self.model.get_usuarioscerca(a)
		self.view.set_ultimoscontactos(rcontactos)

