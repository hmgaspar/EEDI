#! /usr/bin/env python
from pylab import *

class Ship:
	def __init__(self):
#		self.Name = raw_input('Vessel Name: ')
		self.Name = 'Princess'
		self.Mission = Mission()

class Mission:
	def __init__(self):
		_mission = []
#		_mission.append(raw_input('Mission Name: '))
		_mission.append('Statoil')
		_mission.append(raw_input('Number of Operational Profiles: '))
#		_mission.append('2')
		self.Name = _mission[0]
		self.N_OP = _mission[1]
		print ' '
		print ' '
		print '   Selecting Operational Profiles'
		print ' '
		_op = []
		for i in range(int(self.N_OP)):
			global n_op
			n_op = i
			_op.append(self.OperProf())
		self.OP = _op
		print 'po', _op
#		self.OP = []

	def OperProf(self):
		_ope_pro = []
		print 'Operational Profile - ', n_op
		_oper_pro_types = ['Supply', 'Towing', 'Anchor Handling', 'Delivery']
		print '   Select a type of Operational Profile:'
		for j in range(len(_oper_pro_types)):
			print '   ', j, ' - ', _oper_pro_types[j]
		_sel_type = _oper_pro_types[int(raw_input('    :'))]
#		_sel_type = _oper_pro_types[0]
		_ope_pro.append(_sel_type)
		print _sel_type, ' - Percentage of Mission Time'
		_ope_pro.append(float(raw_input(' : '))/100)
#		_ope_pro.append(float(50)/100)
		print ' - Number of Operational States'
		_ope_pro.append(raw_input(' : '))
#		_ope_pro.append(1)
		_os = []
		for i in range(int(_ope_pro[2])):
			global n_os
			n_os = i
			_os.append(self.OperStates())
		_ope_pro.append(_os)
		return _ope_pro

	def OperStates(self):
		_op_sta = []
		print 'Operational State - ', n_os
		_oper_sta_types = ['Stand By', 'Towing (150ton force, 4knots)', 'Anchor Handling (100ton force)', 'Discharge', 'Loading', 'Sailing (100% DWT, 12knots)', 'Sailing(20% DWT, 12knots)', 'Waiting']
		print '   Select a type of Operational State:'
		for j in range(len(_oper_sta_types)):
			print '   ', j, ' - ', _oper_sta_types[j]
		_sel_type = _oper_sta_types[int(raw_input('    :'))]
#		_sel_type = _oper_sta_types[0]
		_op_sta.append(_sel_type)
		print _sel_type, ' - Percentage of Oper. Profile Time'
		_op_sta.append(float(raw_input(' : '))/100)
#		_op_sta.append(float(100)/100)
		print ' - Fuel Consumption (ton/hour)'
		_op_sta.append(raw_input(' : '))
#		_op_sta.append(0.65)
		return _op_sta
	
	def EEDI(self):
		_op_value = []
		for i in range(int(self.N_OP)):
			_os_value = [] 
			for j in range(int(self.OP[i][2])):
				_tmp = 	float(self.OP[i][3][j][1]) * float(self.OP[i][3][j][2])	
				_os_value.append(_tmp)
			_op_value.append(sum(_os_value)*float(self.OP[i][1])*3.114)
			
		return sum(_op_value)

a = Ship()
print ' '
print ' '
print ' '
print 'Name :', a.Name
print 'Mission :', a.Mission.Name
print 'Number of Operational Profiles: ', a.Mission.N_OP
print 'Operational Profile:'
print a.Mission.OP
print 'EEDI: ', a.Mission.EEDI(), 'tonsCO2 / Mission'

figure(1,figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

labels = []
fracs = []
explode = []
for i in range(int(a.Mission.N_OP)):
	labels.append(a.Mission.OP[i][0])
	fracs.append(a.Mission.OP[i][1])
	explode.append(0.05)

pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
title('Mission "' + a.Mission.Name + '" - Operational Profiles', bbox={'facecolor':'0.8', 'pad':10})

for i in range(int(a.Mission.N_OP)):
	labels = []
	fracs = []
	explode = []
	for j in range(int(a.Mission.OP[i][2])):
		labels.append(a.Mission.OP[i][3][j][0])
		fracs.append(a.Mission.OP[i][3][j][1])
		explode.append(0.05)
	figure(i+2, figsize=(6,6))
	pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
	title('States of "'+ a.Mission.OP[i][0]+'"', bbox={'facecolor':'0.8', 'pad':10})

show()



