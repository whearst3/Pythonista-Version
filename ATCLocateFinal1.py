import location
from math import radians, degrees, sqrt, sin, cos, atan2

# ready for pythonista test


db =[ [ "FJS", 41.4497, -122.806, 109.6, "FORT JONES" ],
 [ "RDD", 40.5046, -122.292, 108.4, "REDDING" ],
 [ "AHC", 40.2679, -120.152, 109.0, "AMEDEEHERLONG" ],
 [ "RBL", 40.0989, -122.236, 115.7, "RED BLUFF" ],
 [ "CIC", 39.7898, -121.847, 109.8, "CHICO" ],
 [ "MXW", 39.3176, -122.222, 110.0, "MAXWELL" ],
 [ "SWR", 39.1803, -120.27, 113.2, "SQUAW VALLEY SOUTH LAKE TAHOE" ],
 [ "MYV", 39.0986, -121.573, 110.8, "MARYSVILLE" ],
 [ "ILA", 39.0712, -122.027, 114.4, "WILLIAMS" ],
 [ "ENI", 39.0532, -123.274, 112.3, "MENDOCINO UKIAH" ],
 [ "HNW", 38.7247, -120.749, 115.5, "HANGTOWN PLACERVILLE" ],
 [ "MCC", 38.6674, -121.404, 109.2, "MC CLELLAN SACRAMENTO" ],
 [ "STS", 38.5082, -122.81, 113.0, "SANTA ROSA" ],
 [ "SAC", 38.4437, -121.552, 115.2, "SACRAMENTO" ],
 [ "TZZ", 38.3442, -121.811, 116.4, "TRAVIS FAIRFIELD" ],
 [ "SGD", 38.1794, -122.373, 112.1, "SCAGGS ISLAND NAPA" ],
 [ "PYE", 38.0798, -122.868, 113.7, "POINT REYES" ],
 [ "LIN", 38.0746, -121.004, 114.8, "LINDEN" ],
 [ "CCR", 38.0449, -122.045, 117.0, "CONCORD" ],
 [ "SAU", 37.8553, -122.523, 116.2, "SAUSALITO" ],
 [ "ECA", 37.8336, -121.171, 116.0, "MANTECA STOCKTON" ],
 [ "OAK", 37.7259, -122.224, 116.8, "OAKLAND" ],
 [ "MOD", 37.6274, -120.958, 114.6, "MODESTO" ],
 [ "SFO", 37.6195, -122.374, 115.8, "SAN FRANCISCO" ],
 [ "OSI", 37.3925, -122.281, 113.9, "WOODSIDE" ],
 [ "BIH", 37.377, -118.367, 109.6, "BISHOP" ],
 [ "SJC", 37.3747, -121.945, 114.1, "SAN JOSE" ],
 [ "HYP", 37.2194, -120.4, 114.2, "EL NIDO MERCED" ],
 [ "FRA", 37.1044, -119.595, 115.6, "FRIANT" ],
 [ "CZQ", 36.8843, -119.815, 112.9, "CLOVIS FRESNO" ],
 [ "PXN", 36.7155, -120.779, 112.6, "PANOCHE" ],
 [ "SNS", 36.6638, -121.603, 117.3, "SALINAS" ],
 [ "VIS", 36.3673, -119.482, 109.4, "VISALIA" ],
 [ "BSR", 36.1813, -121.642, 114.0, "BIG SUR" ],
 [ "ROM", 36.1404, -120.665, 110.0, "PRIEST" ],
 [ "TTE", 35.9131, -119.021, 109.2, "TULE ORTERVILLE" ],
 [ "PRB", 35.6725, -120.627, 114.3, "PASO ROBLES" ],
 [ "AVE", 35.647, -119.979, 117.1, "AVENAL" ],
 [ "EHF", 35.4846, -119.097, 115.4, "SHAFTER BAKERSFIELD" ],
 [ "MQO", 35.2522, -120.76, 112.4, "MORRO BAY SAN LUIS OBISPO" ],
 [ "GFS", 35.1311, -115.176, 114.4, "GOFFS" ],
 [ "FLW", 35.0931, -119.866, 117.5, "FELLOWS" ],
 [ "EDW", 34.9824, -117.733, 116.4, "EDWARDS" ],
 [ "DAG", 34.9625, -116.578, 113.2, "DAGGETT" ],
 [ "GLJ", 34.9524, -120.521, 111.0, "GUADALUPE SANTA MARIA" ],
 [ "GMN", 34.804, -118.861, 116.1, "GORMAN" ],
 [ "HEC", 34.797, -116.463, 112.7, "HECTOR" ],
 [ "EED", 34.766, -114.474, 115.2, "NEEDLES" ],
 [ "LHS", 34.683, -118.577, 108.4, "LAKE HUGHES" ],
 [ "PMD", 34.6314, -118.064, 114.5, "PALMDALE" ],
 [ "VCV", 34.5942, -117.39, 109.4, "VICTORVILLE" ],
 [ "GVO", 34.5313, -120.091, 113.8, "GAVIOTA" ],
 [ "RZS", 34.5095, -119.771, 114.9, "SAN MARCUS SANTA BARBARA" ],
 [ "FIM", 34.3567, -118.881, 112.5, "FILLMORE" ],
 [ "VNY", 34.2234, -118.492, 113.1, "VAN NUYS" ],
 [ "CMA", 34.2125, -119.094, 115.8, "CAMARILLO" ],
 [ "VTU", 34.1151, -119.049, 108.2, "VENTURA OXNARD" ],
 [ "TNP", 34.1122, -115.77, 114.2, "TWENTYNINE PALMS" ],
 [ "PKE", 34.102, -114.682, 117.9, "PARKER" ],
 [ "POM", 34.0784, -117.787, 110.4, "POMONA" ],
 [ "SMO", 34.0102, -118.457, 110.8, "SANTA MONICA" ],
 [ "RAL", 33.9552, -117.45, 112.4, "RIVERSIDE" ],
 [ "LAX", 33.9331, -118.432, 113.6, "LOS ANGELES" ],
 [ "PDZ", 33.9183, -117.53, 112.2, "PARADISE ONTARIO" ],
 [ "PSP", 33.87, -116.43, 115.5, "PALM SPRINGS" ],
 [ "SLI", 33.7833, -118.055, 115.7, "SEAL BEACH LOS ALAMITOS" ],
 [ "HDF", 33.7763, -117.185, 113.4, "HOMELAND RIVERSIDE" ],
 [ "ELB", 33.676, -117.731, 117.2, "EL TORO SANTA ANA" ],
 [ "TRM", 33.6281, -116.16, 116.2, "THERMAL PALM SPRINGS" ],
 [ "BLH", 33.5961, -114.761, 117.4, "BLYTHE" ],
 [ "SXC", 33.3751, -118.42, 111.4, "SANTA CATALINA" ],
 [ "OCN", 33.2406, -117.418, 115.3, "OCEANSIDE" ],
 [ "JLI", 33.1405, -116.586, 114.0, "JULIAN" ],
 [ "NSD", 32.8799, -118.441, 113.9, "BEAVER" ],
 [ "MZB", 32.7822, -117.225, 117.8, "MISSION BAY SAN DIEGO" ],
 [ "IPL", 32.7489, -115.509, 115.9, "IMPERIAL" ],
 [ "PGY", 32.6103, -116.979, 109.8, "POGGI SAN DIEGO" ] ]

def geocode(lat1, lon1, lat2, lon2):
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon1 - lon2
         
    EARTH_R = 3440.0695

    y = sqrt(
        (cos(lat2) * sin(dlon)) ** 2
        + (cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(dlon)) ** 2
        )
    x = sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(dlon)
    c = atan2(y, x)
    bearing =atan2(cos(lat1)*sin(lat2)-sin(lat1)*cos(lat2)*cos(lon2-lon1), sin(lon2-lon1)*cos(lat2))
    
    bd =  (90-degrees(bearing)) % 360 
    
    #  bdm = (bd - (5.6 + 0.2*lat1)) % 360 is approx. mag correction for CA
    
    nm = round(EARTH_R * c)

    return [nm,bd]

def dist(lat1, lon1, lat2, lon2):
	return geocode(lat1, lon1, lat2, lon2)[0]
	
def bear(lat1, lon1, lat2, lon2):
	return geocode(lat1, lon1, lat2, lon2)[1]
    		
def compdir(heading):
	compass = " "

	if (heading >= 0 and heading < 22.5) :
		compass = "N"
	elif (heading > 22.5 and heading < 67.5):
		compass = "NE"
	elif (heading > 67.5 and heading < 112.5):
		compass = "E"
	elif (heading > 112.5 and heading < 157.5):
		compass = "SE"
	elif (heading > 157.5 and heading < 202.5):
		compass = "S"
	elif (heading > 202.5 and heading < 247.5):
		compass = "SW"
	elif (heading > 247.5 and heading < 292.5):
		compass = "W"
	elif (heading > 292.5 and heading < 337.5):
		compass = "NW"
	elif (heading > 337.5 and heading <= 360):
		compass = "N"
	else:
		compass = "QQ"

	return compass

def findnear(a,b, db):
	dlow = 1000.
	i = 0
	for rec in db:
		newd = dist(a,b,rec[1],rec[2])
		if newd < dlow:
			dlow = newd
			lowest = i
		i +=1
	return [db[lowest],dlow]
	
def messages(lat,lon, dbase):
	refp = findnear(lat,lon, dbase)
	dnm = refp[1]
	ref = refp[0]
	comment = ref[4]
	freq = ref[3]
	name = ref[0]
	lola2 = [ref[1],ref[2]]
	comph = lola2 + [lat,lon]
	dir = compdir(bear(*comph))
	str1 = "{0} nm {1} of {2}".format(dnm, dir, name)
	str2 = comment + " - " + str(freq)
	return [str1,str2]
						

def getpos():
	location.start_updates()
	dict = location.get_location()
	location.stop_updates()
	lat,lon = dict['latitude'], dict['longitude]
	return [lat,lon]


	
def update(sender):
	toplabel = v['label3']
	botlabel = v['label1']
	
	latc, lonc = getpos()
	mess1, mess2 = messages(latc, lonc, db)
	
	toplabel.text = mess1
	botlabel.text = mess2
	

	
v = ui.load_view('testOne')
v.present('sheet')

