from experta import *
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi
import webbrowser
from PyQt5.uic.uiparser import QtCore
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtGui import QCursor, QWindow
import requests
import json

diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

disease_content = []

id_disease = ''
disease_details = '''
'''
treatments = '''

'''



hd = 'yes'
bp = 'yes'
cp = 'yes'
c = 'yes'
f = 'yes'
ft = 'yes'
se = 'yes'
lbt = 'yes'
r = 'yes'
st = 'yes'
fe = 'yes'
n = 'yes'
bv = 'yes'


def preprocess():
	global diseases_list,diseases_symptoms,symptom_map,d_desc_map,d_treatment_map
	diseases = open("diseases.txt")
	diseases_t = diseases.read()
	diseases_list = diseases_t.split("\n")
	diseases.close()
	for disease in diseases_list:
		disease_s_file = open("Disease symptoms/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		s_list = disease_s_data.split("\n")
		diseases_symptoms.append(s_list)
		symptom_map[str(s_list)] = disease
		disease_s_file.close()
		disease_s_file = open("Disease descriptions/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_desc_map[disease] = disease_s_data
		disease_s_file.close()
		disease_s_file = open("Disease treatments/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_treatment_map[disease] = disease_s_data
		disease_s_file.close()


def identify_disease(*arguments):
	symptom_list = []
	for symptom in arguments:
		symptom_list.append(symptom)
	# Handle key error
	return symptom_map[str(symptom_list)]

def get_details(disease):
	return d_desc_map[disease]

def get_treatments(disease):
	return d_treatment_map[disease]

def if_not_matched(disease):
	global disease_content, id_disease, disease_details, treatments
	print("")
	id_disease = disease
	disease_details = get_details(id_disease)
	treatments = get_treatments(id_disease)
	print("")
	print("The most probable disease that you have is %s\n" %(id_disease))
	id_disease = id_disease
	disease_details = disease_details
	treatments = treatments
	print("A short description of the disease is given below :\n")
	print(disease_details+"\n")
	print("The common medications and procedures suggested by other real doctors are: \n")
	print(treatments+"\n")

	

	# disease_content.append(id_disease)
	# disease_content.append(disease_details)
	# disease_content.append(treatments)


class Greetings(KnowledgeEngine):

	@DefFacts()
	def _initial_action(self):
		print("")
		print("")
		yield Fact(action="find_disease")


	@Rule(Fact(action='find_disease'), NOT(Fact(headache=W())),salience = 1)
	def symptom_0(self):
		self.declare(Fact(headache= hd)
		
		# input("headache: "))
		)
		

	@Rule(Fact(action='find_disease'), NOT(Fact(back_pain=W())),salience = 1)
	def symptom_1(self):
		self.declare(Fact(back_pain = bp
		# input("back pain: ")
		))
		

	@Rule(Fact(action='find_disease'), NOT(Fact(chest_pain=W())),salience = 1)
	def symptom_2(self):
		self.declare(Fact(chest_pain= cp
		# input("chest pain: ")
		))

	@Rule(Fact(action='find_disease'), NOT(Fact(cough=W())),salience = 1)
	def symptom_3(self):
		self.declare(Fact(cough= c
		# input("cough: ")
		))

	@Rule(Fact(action='find_disease'), NOT(Fact(fainting=W())),salience = 1)
	def symptom_4(self):
		self.declare(Fact(fainting= f
		# input("fainting: ")
		))

		print(f)

	@Rule(Fact(action='find_disease'), NOT(Fact(fatigue=W())),salience = 1)
	def symptom_5(self):
		self.declare(Fact(fatigue=ft
		# input("fatigue: ")
		))

	@Rule(Fact(action='find_disease'), NOT(Fact(sunken_eyes=W())),salience = 1)
	def symptom_6(self):
		self.declare(Fact(sunken_eyes=se
		# input("sunken eyes: ")
		))

	@Rule(Fact(action='find_disease'), NOT(Fact(low_body_temp=W())),salience = 1)
	def symptom_7(self):
		self.declare(Fact(low_body_temp=lbt
		# input("low body temperature: ")
		))

	@Rule(Fact(action='find_disease'), NOT(Fact(restlessness=W())),salience = 1)
	def symptom_8(self):
		self.declare(Fact(restlessness=r
		# input("restlessness: ")
		))

	@Rule(Fact(action='find_disease'), NOT(Fact(sore_throat=W())),salience = 1)
	def symptom_9(self):
		self.declare(Fact(sore_throat=st
		# input("sore throat: ")
		))

	@Rule(Fact(action='find_disease'), NOT(Fact(fever=W())),salience = 1)
	def symptom_10(self):
		self.declare(Fact(fever=fe
		# input("fever: ")
		))

	@Rule(Fact(action='find_disease'), NOT(Fact(nausea=W())),salience = 1)
	def symptom_11(self):
		self.declare(Fact(nausea=n
		# input("Nausea: ")
		))

	@Rule(Fact(action='find_disease'), NOT(Fact(blurred_vision=W())),salience = 1)
	def symptom_12(self):
		self.declare(Fact(blurred_vision=bv
		# input("blurred_vision: ")
		))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Jaundice"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_1(self):
		self.declare(Fact(disease="Alzheimers"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="yes"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_2(self):
		self.declare(Fact(disease="Arthritis"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_3(self):
		self.declare(Fact(disease="Tuberculosis"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_4(self):
		self.declare(Fact(disease="Asthma"))

	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_5(self):
		self.declare(Fact(disease="Sinusitis"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_6(self):
		self.declare(Fact(disease="Epilepsy"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_7(self):
		self.declare(Fact(disease="Heart Disease"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="yes"))
	def disease_8(self):
		self.declare(Fact(disease="Diabetes"))

	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="yes"))
	def disease_9(self):
		self.declare(Fact(disease="Glaucoma"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_10(self):
		self.declare(Fact(disease="Hyperthyroidism"))

	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_11(self):
		self.declare(Fact(disease="Heat Stroke"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="yes"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="yes"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_12(self):
		self.declare(Fact(disease="Hypothermia"))

	@Rule(Fact(action='find_disease'),Fact(disease=MATCH.disease),salience = -998)
	def disease(self, disease):
		global disease_content,id_disease,disease_details,treatments
		print("")
		id_disease = disease
		disease_details = get_details(id_disease)
		treatments = get_treatments(id_disease)
		id_disease = id_disease
		disease_details = disease_details
		treatments = treatments
		print("")
		print("The most probable disease that you have is %s\n" %(id_disease))
		print("A short description of the disease is given below :\n")
		print(disease_details+"\n")
		print("The common medications and procedures suggested by other real doctors are: \n")
		print(treatments+"\n")

		

		# disease_content.append(id_disease)
		# disease_content.append(disease_details)
		# disease_content.append(treatments)

	@Rule(Fact(action='find_disease'),
		  Fact(headache=MATCH.headache),
		  Fact(back_pain=MATCH.back_pain),
		  Fact(chest_pain=MATCH.chest_pain),
		  Fact(cough=MATCH.cough),
		  Fact(fainting=MATCH.fainting),
		  Fact(sore_throat=MATCH.sore_throat),
		  Fact(fatigue=MATCH.fatigue),
		  Fact(low_body_temp=MATCH.low_body_temp),
		  Fact(restlessness=MATCH.restlessness),
		  Fact(fever=MATCH.fever),
		  Fact(sunken_eyes=MATCH.sunken_eyes),
		  Fact(nausea=MATCH.nausea),
		  Fact(blurred_vision=MATCH.blurred_vision),NOT(Fact(disease=MATCH.disease)),salience = -999)

	def not_matched(self,headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever ,sunken_eyes ,nausea ,blurred_vision):
		print("\nDid not find any disease that matches your exact symptoms")
		lis = [headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever ,sunken_eyes ,nausea ,blurred_vision]
		max_count = 0
		max_disease = ""
		for key,val in symptom_map.items():
			count = 0
			temp_list = eval(key)
			for j in range(0,len(lis)):
				if(temp_list[j] == lis[j] and lis[j] == "yes"):
					count = count + 1
			if count > max_count:
				max_count = count
				max_disease = val
		if_not_matched(max_disease)

class HomeWindow(QMainWindow):

    def __init__(self):
        super(HomeWindow, self).__init__()
        loadUi('UI/home.ui', self)

        self.setWindowTitle("Medic")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.drop_widget.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))

        self.d_button.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=12, xOffset=3, yOffset=3))


        self.cls_button.clicked.connect(self.close)
        # self.register_button.clicked.connect(self.go_to_register_page)
        self.d_button.clicked.connect(self.start_expert)
        self.min_butto.clicked.connect(self.showMinimized)

        self.popup = QMessageBox()
        self.popup.setWindowTitle("Failed")



        self.show()

    def start_expert(self):

	    # print("Getting GUI data")

        object1 = Set_data(
		self.hd.text(),
		self.bp.text(),
		self.cp.text(),
		self.c.text(),
		self.f.text(),
		self.ft.text(),
		self.se.text(),
		self.lbt.text(),
		self.r.text(),
		self.st.text(),
		self.fe.text(),
		self.n.text(),
		self.bv.text()
		)
        object1.data_transform()

        preprocess()

		
        engine = Greetings()
        engine.reset()
        engine.run()
        self.shortWind = ShortWindow()
        self.close()
        print(engine.facts)

        # self.shortWind.set_info()

		# print("Getting GUI data")
	

# class Set_data()


class Set_data():

	

	def __init__(self,hd,bp,cp,c,f,ft,se,lbt,r,st,fe,n,bv):

		

		self.hd = hd
		self.bp = bp
		self.cp = cp
		self.c = c
		self.f = f
		self.ft = ft
		self.se = se
		self.lbt = lbt
		self.r = r
		self.st = st
		self.fe = fe
		self.n = n
		self.bv = bv;

		
	def data_transform(self):
		global hd,bp,cp,c,f,ft,se,lbt,r,st,fe,n,bv

		hd = self.hd
		bp = self.bp
		cp = self.cp
		c = self.c
		f = self.f
		ft = self.ft
		se = self.se
		lbt = self.lbt
		r = self.r
		st = self.st
		fe = self.fe
		n = self.n
		bv = self.bv

        # print("Already Set the attributes")

class ShortWindow(QMainWindow):

    def __init__(self):
        super(ShortWindow, self).__init__()
        loadUi('UI/shorty.ui', self)

        self.setWindowTitle("Medic")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.drop_widget.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))

        self.more.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=12, xOffset=3, yOffset=3))


        self.cls_button_2.clicked.connect(self.close)
     
        self.more.clicked.connect(self.start_treat)
        self.min_butto_2.clicked.connect(self.showMinimized)


        self.show()
        self.disease_id.setText(id_disease)
        self.desc.setText(disease_details)

    def start_treat(self):
        self.treaty = TreatWindow()
        self.close()

		# # disease_content.append(id_disease)
		# # disease_content.append(disease_details)
		# # disease_content.append(treatments)
        #     self.disease_id.setText(disease_content[0])
        #     self.desc.setText(disease_content[0])

class TreatWindow(QMainWindow):

    def __init__(self):
        super(TreatWindow, self).__init__()
        loadUi('UI/treat.ui', self)

        self.setWindowTitle("Medic")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.drop_widget.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))

        self.end.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=12, xOffset=3, yOffset=3))


        self.cls_button_2.clicked.connect(self.close)

        self.min_butto_2.clicked.connect(self.showMinimized)

        self.end.clicked.connect(self.close)

        self.popup = QMessageBox()
        self.popup.setWindowTitle("Failed")

        self.show()

    
        # global disease_content,id_disease,disease_details,treatments
       
        self.treat.setText(treatments)
		




def run():
    preprocess()
    engine = Greetings()
    while(1):
        engine.reset()  # Prepare the engine for the execution.
        engine.run()  # Run it!
        print("Would you like to diagnose some other symptoms?")
        ff = engine.facts
        print(ff)
        if input() == "no":
        	exit()




if __name__ == "__main__":
    run()
	# preprocess()
	# engine = Greetings()
	# while(1):
	# 	engine.reset()  # Prepare the engine for the execution.
	# 	engine.run()  # Run it!
	# 	print("Would you like to diagnose some other symptoms?")
	# 	if input() == "no":
	# 		exit()
	# 	print(engine.facts)
