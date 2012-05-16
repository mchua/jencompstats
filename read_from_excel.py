# Man braucht http://pypi.python.org/pypi/xlrd fur dieser Code.
import xlrd # "eXceL ReaD library"

# Man braucht auch Respondent.py.
# FRAGEN: Wie sagt man "put it in the same folder as this python file?"
from Respondent import Respondent

# Man muss 2011-2012 Daten in Anredepronomen-data.xls haben.
excelworkbook = xlrd.open_workbook("Anredepronomen-data.xls")

# Gibt es nur 1 Sheet, heisst Anredepronomen_im_Alltag. Alles Daten sind hier.
daten = excelworkbook.sheet_by_name("Anredepronomen_im_Alltag")

# Hier sind 283 Personen.
# FRAGEN: Wie kann man die richtig Nummer automatisch finden?
ganz_personen = 283

# Eine Liste, wohin die Personen gehen.
# Einige Personen ein Respondent Objekt werden.
Personen = []

# Eine Dictionary. Es habt die Fragen auf Anredepronomen-data.xls abgezahlt.
fragen = {'geschlecht':12,
		'alter':13,
		'aktueller_wohnort':14,
		'jahre_an_ort':15,
		'davor_gewohnt':16,
		'lange_davor_gewohnt':17,
		'familienstand':18,
		'muttersprache':19,
		'polyglotter':20,
		'schulabschluss':21,
        'q33_5':92,
		'q37_4':103,
		'q37_5':104,
		'q37_6':105,
		'q37_7':106,
		'q37_8':107,
		'q37_9':108,
		'q37_10':109,
		'q44':117}

# Respondent Objekte machen.
for index in range(ganz_personen):
	# BEACHTE: print daten.row_values(2)[12] == row 3, column M.
	row = 2+index
	neues_respondent = Respondent(ausweisnummer=index,
				geschlecht = daten.row_values(row)[fragen['geschlecht']],
				alter = daten.row_values(row)[fragen['alter']],
				aktueller_wohnort = daten.row_values(row)[fragen['aktueller_wohnort']],
				jahre_an_ort = daten.row_values(row)[fragen['jahre_an_ort']],
				davor_gewohnt = daten.row_values(row)[fragen['davor_gewohnt']],
				lange_davor_gewohnt = daten.row_values(row)[fragen['lange_davor_gewohnt']],
				familienstand = daten.row_values(row)[fragen['familienstand']],
				muttersprache = daten.row_values(row)[fragen['muttersprache']],
				polyglotter = daten.row_values(row)[fragen['polyglotter']],
				schulabschluss = daten.row_values(row)[fragen['schulabschluss']],
                q33_5 = daten.row_values(row)[fragen['q33_5']],
				q37_4 = daten.row_values(row)[fragen['q37_4']],
				q37_5 = daten.row_values(row)[fragen['q37_5']],
				q37_6 = daten.row_values(row)[fragen['q37_6']],
				q37_7 = daten.row_values(row)[fragen['q37_7']],
				q37_8 = daten.row_values(row)[fragen['q37_8']],
				q37_9 = daten.row_values(row)[fragen['q37_9']],
				q37_10 = daten.row_values(row)[fragen['q37_10']],
				q44 = daten.row_values(row)[fragen['q44']],
				)
	Personen += [neues_respondent]

# BEISPIEL: Antworten fur q44 ausgeben.
for person in Personen:
	print(str(person.ausweisnummer)+'-'+person.q44)

# BEISPIEL: Wie viele personen hat du/ihr/Sie fur q44 geantwortet?
du_count = 0
ihr_count = 0
sie_count = 0
keine_antwort_count = 0
for person in Personen:
	if person.q44 == "du":
		du_count += 1
	elif person.q44 == "ihr":
		ihr_count += 1
	elif person.q44 == "Sie":
		sie_count += 1
	else:
		keine_antwort_count += 1
print("du - " + str(du_count))
print("ihr - " + str(ihr_count))
print("Sie - " + str(sie_count))
print("Keine Antwort - " + str(keine_antwort_count))

# BEISPIEL: 3 Liste machen, Jede ein anders Pronomen benutzen.

du_list = []
ihr_list = []
sie_list = []
keine_antwort_list = []

# Wir konnen "list comprehension" benutzen hier, 
# aber du hast es noch nicht gesehen.
for person in Personen:
	if person.q44 == "du":
		du_list += [person]
	elif person.q44 == "ihr":
		ihr_list += [person]
	elif person.q44 == "Sie":
		sie_list += [person]
	else:
		keine_antwort_list += [person]

# BEISPIEL: wie alt sind die Personen, wer q44 'ihr' hat geantwortet?
for person in ihr_list:
	print person.alter

# BEISPIEL: was ist die Mittelwert von Alter fur die Personen,
# wer jede Antwort fur q44 hat gegeben?

# Hier sind "list comprehension." Wir konnen auch if/elif/else, wie oben.
du_ages = [person.alter for person in du_list if person.alter != 0]
ihr_ages = [person.alter for person in ihr_list if person.alter != 0]
sie_ages = [person.alter for person in sie_list if person.alter != 0]
keine_antwort_ages = [person.alter for person in keine_antwort_list if person.alter != 0]

print("Mittelwert von Alter, q44 'du' geantwortet - " + str(sum(du_ages)/len(du_ages)) + " (" + str(len(du_ages)) + " Personen)")
print("Mittelwert von Alter, q44 'ihr' geantwortet - " + str(sum(ihr_ages)/len(ihr_ages)) + " (" + str(len(ihr_ages)) + " Personen)")
print("Mittelwert von Alter, q44 'Sie' geantwortet - " + str(sum(sie_ages)/len(sie_ages)) + " (" + str(len(sie_ages)) + " Personen)")
print("Mittelwert von Alter, q44 'Keine Antwort' geantwortet - " + str(sum(keine_antwort_ages)/len(keine_antwort_ages)) + " (" + str(len(keine_antwort_ages)) + " Personen)")

# BEISPIEL: Antworten fur q44 anders zwischen Mann und Frau?
# Schrieb das Code. :)

# The people who responded 'ihr' to any of
# Q37_{4,5,6,7,8,9,10}...
# Note: ihr == 2.0 for Q37_{4,5,6,7,8,9,10}

q37_ihr_respondents = []

for person in Personen:
    # if they answered 'ihr' to any q37 subquestions
    if 2.0 in [person.q37_4, person.q37_5, person.q37_6, person.q37_7, person.q37_8, person.q37_9, person.q37_10]:
        # add them to our q37_ihr_respondents list
        q37_ihr_respondents += [person]

# What did they answer to q33_5?
for person in q37_ihr_respondents:
    print person.ausweisnummer,
    print ' - ',
    print person.q33_5
