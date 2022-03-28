
from typing import List
import requests
import datetime



class Model:
    def __init__(self, url, headers):
        self.r = {}
        self.url = url  # parte de la url fija para todas las peticiones a la bd
        self.headers = headers  # headers, que en este caso seran los mismos para todas las peticiones
        self.start_date = None
        self.end_date = None
        self.hour_start = None
        self.minute_start = None
        self.hour_end = None
        self.minute_end = None
    
    def reset_dates(self) :
        self.start_date = None
        self.end_date = None
        self.hour_start = None
        self.minute_start = None
        self.hour_end = None
        self.minute_end = None
        
    def is_validdate(self):
        if self.start_date is None or self.end_date is None :
            return False
        else :
            startaux = self.start_date + " " + self.hour_start + ":" + self.minute_start
            start = datetime.datetime.strptime(startaux, "%d/%m/%y %H:%M")
            endaux = self.end_date + " " + self.hour_end + ":" + self.minute_end
            end = datetime.datetime.strptime(endaux, "%d/%m/%y %H:%M")
            error = start > end
            return not error
    
    def get_userinfo(self, search) :
        x = search.get_text().strip().split(" ")
        try:
            if len(x)==1 :
                r = requests.get(self.url + "users/"+search.get_text().strip(),
                headers=self.headers, timeout=10.0) 
            else :
                r = requests.get(self.url + "user?name="+x[0].capitalize()+"&surname="+x[1].capitalize(),
                headers=self.headers, timeout=10.0)
        except Exception: #esperamos el timeout, si no lanza excepción 
            return ["500", None]
        if r.status_code != 200:
            return ["500", None]
        elif len(r.json()['users']) == 0 :
            return ["404", r.json()['users']]
        elif r.status_code == 200:
            return ["200", r.json()['users']]
        
    def get_usersitios(self, uuid) :
        r = requests.get(self.url + "user_access_log/"+uuid,
            headers=self.headers)
        return ["200", r.json()['access_log']]
    
    def get_ultimossitios(self, uuid) :
        start = self.start_date.split("/")
        end = self.end_date.split("/")
        ystart = "20"+start[2]
        yend = "20"+end[2]
        mstart = start[1]
        mend = end[1]
        dstart = start[0]
        dend = end[0]
        r = requests.get( 
            self.url + "user_access_log/"+uuid+"/daterange", 
            headers=self.headers, 
            json={"startdate": ystart+"-"+mstart+"-"+dstart+"T"+self.hour_start+":"+self.minute_start+":00+00:000", "enddate": yend+"-"+mend+"-"+dend+"T"+self.hour_end+":"+self.minute_end+":00+00:000"})
        return ["200", r.json()['access_log']]

    def get_usuarioscerca(self, list) :
        try :
            countlist = 0
            rlist = [[0] * 3 for i in range(len(list)//2)]
            for count in range(len(list)) :
                if count != (len(list) - 1) and list[count][0] == list[count +1][0] :
                    r = requests.get( 
                        self.url + "facility_access_log/"+str(list[count][0])+"/daterange",
                        headers=self.headers, 
                        json={"startdate": list[count][1], "enddate": list[count+1][1]})
                    iter = 0
                    userlist =[[0]*3 for i in range(len(r.json()['access_log']))]
                    for d in r.json()['access_log'] : 
                        userlist[iter][0] = d['user']['name']+" "+d['user']['surname']
                        if d['user']['is_vaccinated'] :
                            userlist[iter][1] = "Si"
                        else :
                            userlist[iter][1] = "No"
                        userlist[iter][2]  = d['user']['uuid']
                        iter+=1
                    rlist[countlist][0] = list[count][2]
                    rlist[countlist][1] = userlist
                    rlist[countlist][2] = list[count][1]
                    countlist += 1
            return rlist
        except IndexError :
            return rlist
        