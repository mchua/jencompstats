class Respondent(object):
    """Jeden Respondent Objekt stellt Eine Person in die 2011-2012 Personalpronomen Daten. Ich habe mein Fachvokabular aus http://ada.rg16.asn-wien.ac.at/~python/how2think/ genommen. Ich weiss nicht wie man ä ö ü ß schreibt."""
    def __init__(self, geschlecht=0, alter = 0, aktueller_wohnort = 0, jahre_an_ort = 0, davor_gewohnt = 0, lange_davor_gewohnt = 0, familienstand = 0, muttersprache = 0, polyglotter = 0, schulabschluss = 0, q44 = 0):
	"""Ein neues Respondent Objekt machen."""
        """BEACHT: Ich weiss, dass man musst Substantive grossschrieben, aber auf Python man grossschriebt nicht Attribute, sondern Objekte."""
	"""BEACHT: Wir konnen 0 == 'keine Antwort' benutzen, weil Qualtrics mit 1 Zahlen beginnt. Praktisch."""
	# Q1
        self.geschlect = geschlecht
		# 0 bedeutet keine Antwort
		# 1 bedeutet Mann
		# 2 beduetet Frau
	# Q2
        self.alter = alter
		# 0 bedeutet keine Antwort
		# 1 bedeutet 18-24 Jahre alt
		# 2 bedeutet 25-29 Jahre alt
		# 3 bedeutet 30-34 Jahre alt
		# 4 bedeutet 35-39 Jahre alt
		# 5 bedeutet 40-44 Jahre alt
		# 6 bedeutet 45-49 Jahre alt
		# 7 bedeutet 50-54 Jahre alt
		# 8 bedeutet 55-59 Jahre alt
		# 9 bedeutet 60-64 Jahre alt
		# 10 bedeutet 65-69 Jahre alt
		# 11 bedeutet 70+ Jahre alt
		"""FRAGEN: mochtest du die aktuelle Nummern benutzen? Z.B. nicht '8', sondern '55'?"""
	# Q3
	self.aktueller_wohnort = aktueller_wohnort
		# 0 bedeutet keine Antwort
		# Anders dies Attribute sind eine String
	# Q4
	self.jahre_an_ort = jahre_an_ort # Q4
		"""Jahre an diesem Ort"""
		# 0 bedeutet keine Antwort
		# 1 bedeutet 0-5 Jahre
		# 2 bedeutet 6-10 Jahre
		# 3 bedeutet 11-15 Jahre
		# 4 bedeutet 16-20 Jahre
		# 5 bedeutet 21+ Jahre
	# Q4a
	self.davor_gewohnt = davor_gewohnt # Q4a
		"""Wo haben Sie davor gewohnt?"""
		# 0 bedeutet keine Antwort
		# Anders dies Attribute sind eine String
		"""BEACHT: Keine Personen geantwortet (2011-2012 Daten)."""
	# Q4b
	self.lange_davor_gewohnt = lange_davor_gewohnt # Q4b
		"""Wie lange haben Sie dort gewohnt?"""
		# 0 bedeutet keine Antwort
		# 1 bedeutet 0-5 Jahre
		# 2 bedeutet 6-10 Jahre
		# 3 bedeutet 11-15 Jahre
		# 4 bedeutet 16-20 Jahre
		# 5 bedeutet 21+ Jahre
		"""BEACHT: Keine Personen geantwortet (2011-2012 Daten)."""
	# Q5
	self.familienstand = familienstand
		# 0 bedeutet keine Antwort
		# 1 bedeutet ledig
		# 2 bedeutet verheiratet (Lebensgefahrte/-partner inklusive)
		# 3 bedeutet getrennt lebend
		# 4 bedeutet geschieden
		# 5 bedeutet verwitwet
	# Q6
	self.muttersprache = muttersprache
		# 0 bedeutet keine Antwort
		# Anders dies Attribute sind eine String
		"""FRAGEN: Einige Personen 'Englisch' sagen, und andere 'English' oder 'english' usw. sagen. Mochten wir dieses Antworten gleich benutzen? Wie kann man hier Python schreibt, um zu dass machen?"""
	# Q7
	"""Haben Sie mehr als eine Muttersprache?"""
	if polyglotter == 1: 
		self.polyglotter = True
	else:
		self.polyglotter = False
	"""BEACHT: Wenn man keine Antwort gibt, wir sagen auch dass er/sie ist nicht ein(e) Polyglotte(r)."""
	# Q8
	self.schulabschluss = schulabschluss
	"""Was fur einen Schulabschluss haben Sie gemacht?"""
		# 0 bedeutet keine Antwort
		# 1 bedeutet Abitur
		# 2 bedeutet Fachabitur
		# 3 bedeutet Realschule
		# 4 bedeutet Hauptschule
	"""BEACHT: Ich habe Nummern vom Q9 bis Q44, und vom Q45 bis Ende noch nicht realisert."""
	# Q44
	self.q44 = q44
		# 0 bedeutet keine Antwort
		# 1 bedeutet "du"
		# 2 bedeutet "ihr"
		# 3 bedeutet "Sie"
