import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#import customtkinter
import eel
from datetime import datetime, timedelta
from threading import Thread

############# FLIGHT INFORMATION #############
# Pour les tests seulement!
fromAirportTEST = "Paris"
toAirportTEST = "Prague"
fromDateTEST = "02/12/2024" #Format DD/MM/YYYY
toDateTEST = "" #Keep blank if one-way
directFlightTEST = True
favoriteAirlinesTEST = []

##############################################


##############################################

foundflights = [] #NE PAS TOUCHER
#De la forme [[Date, From, To, TakeOffAt, LandingAt, Airline, Price, Duration, Stopover], [...]...]

eel.init('web', allowed_extensions=['.js', '.html'])

def daysDistance(date1, date2):

    # Conversion des chaînes en objets datetime
    date_format = "%d/%m/%Y"
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    # Calcul de la différence en jours
    return abs((d2 - d1).days)

def incrementOneDay(date):
    print(f"BEFORE : {date}")
    # Conversion de la chaîne en objet datetime
    date_format = "%d/%m/%Y"
    date_obj = datetime.strptime(date, date_format)

    # Incrémenter d'un jour
    new_date_obj = date_obj + timedelta(days=1)

    # Conversion de l'objet datetime en chaîne de caractères
    print(f"AFTER : {new_date_obj.strftime(date_format)}")
    return new_date_obj.strftime(date_format)

def parse_duration(duration):
    # Initialiser heures et minutes
    hours = 0
    minutes = 0
    
    # Découper la chaîne de caractères
    parts = duration.split()
    if "h" in parts:
        hours = int(parts[parts.index("h") - 1])  # Récupère la valeur avant "h"
    if "min" in parts:
        minutes = int(parts[parts.index("min") - 1])  # Récupère la valeur avant "min"
    
    return hours * 60 + minutes  # Convertit tout en minutes

def add_durations(durations):
    total_minutes = sum(parse_duration(d) for d in durations)  # Additionne toutes les durées en minutes
    
    # Convertir le total en heures et minutes
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return f"{hours} h {minutes} min"

def naturalTyping(input, str):
    for letter in str:
        input.send_keys(letter)
        time.sleep(0.2)

def waitclick(target, by=By.XPATH, timeout=20):
    time.sleep(0.1)
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, target)))
    element.click()
    return element

def waitget(target, by=By.XPATH, timeout=20):
    time.sleep(0.1)
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, target)))

def searchFlight(fromAirport, toAirport, date, isDirect=False):
    print("0% | Started flight search...")
    #Put From destination
    waitclick('//*[@id="i23"]/div[1]/div/div/div[1]/div/div/input')
    try:
        combofrominput = waitget('//*[@id="i23"]/div[6]/div[2]/div[2]/div[1]/div/input')
        combofrominput.send_keys(fromAirport)
        combofrominput.send_keys(Keys.ENTER)
    except Exception as e:
        print('Input was not found.')
        driver.close()

    print("10% | Filled From destination...")

    #Put To destination
    waitclick('//*[@id="i23"]/div[4]/div/div/div[1]/div/div/input')
    try:
        combotoinput = waitget('//*[@id="i23"]/div[6]/div[2]/div[2]/div[1]/div/input')
        combotoinput.send_keys(toAirport)
        combotoinput.send_keys(Keys.ENTER)
    except Exception as e:
        print('Input was not found.')
        driver.close()

    print("20% | Filled To destination...")

    #Set Type
    """ if (toDate==None or toDate==""):
        print("NO DATE --> ONE-WAY")
        waitclick('/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[1]')
        waitclick('/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[2]/ul/li[2]')
        time.sleep(0.2) """

    time.sleep(0.2)

    #Put Dates
    fromDateInput = waitget('/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input')
    #print("NO DATE --> ONE-WAY")
    #waitclick('/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[1]')
    #waitclick('/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[2]/ul/li[2]')
    #time.sleep(1)
    fromDateInput.send_keys(date)
    fromDateInput.send_keys(Keys.ENTER)
    """ if not (toDate==None or toDate==""):
        print("RETURN")
        fromDateInput.send_keys(fromDate)
        fromDateInput.send_keys(Keys.ENTER)
        
        toDateInput = waitget('/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/div/input')
        toDateInput.send_keys(toDate)
        toDateInput.send_keys(Keys.ENTER) """
        
    print("30% | Filled Dates...")

    time.sleep(0.5)
    
    #Search
    waitclick('/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/button')
    print("50% | Launched search...")

    time.sleep(2)


    waitget('/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[2]/div/div[2]')
    print("60% | Got results...")

    if (isDirect):
        waitclick('/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[4]/div/div/div[2]/div[1]/div/div[1]/span/button')
        waitclick('/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[4]/div/div[2]/div[3]/div/div[1]/section/div[2]/div[1]/div/div/div[2]/div')
        print("70% | Filtered with direct flights...")
    
    try:
        waitclick('/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div/button')
        #                                                                                               ^^^ CHANGES?
        waitclick('/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/ul/li[2]')
        print("80% | Ordered by cheapest flights...")
    except:
        print("Failed to order by cheapest flights! Trying again...")
        time.sleep(1)
        try:
            waitclick('/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div/button')
            #                                                                                               ^^^ CHANGES?
            waitclick('/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/ul/li[2]')
            print("80% | Ordered by cheapest flights...")
        except:
            print("80% | Failed once again. Step ignored")
    

def scrapePage(date, maxPrice=None, foundflights=[], wait=0.5):
    flightslist = driver.find_elements(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[2]/div/div[2]/div[3]/ul/li')
    
    flightscount = len(flightslist)
    print(f"{flightscount} found flights.")

    if flightscount==0 and wait<=10:
        print("Retrying getting flights...")
        time.sleep(wait)
        scrapePage(date, maxPrice, foundflights, wait*2)
    elif wait>10:
        print("Failed to get flights. Maybe there's no flights availiable for this date?")

    prefix = '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[2]/div/div[2]/div[3]/ul/li['

    for i in range(flightscount):
        try:
            count = i+1

            timeStartXPATH = f"{prefix}{count}]/div/div[2]/div/div[2]/div/div[2]/div[1]/span/span[1]/span/span/span"
            timeEndXPATH = f"{prefix}{count}]/div/div[2]/div/div[2]/div/div[2]/div[1]/span/span[2]/span/span/span"
            airlineXPATH = f"{prefix}{count}]/div/div[2]/div/div[2]/div/div[2]/div[2]/span"
            durationXPATH = f"{prefix}{count}]/div/div[2]/div/div[2]/div/div[3]/div"
            fromAirportXPATH = f"{prefix}{count}]/div/div[2]/div/div[2]/div/div[3]/span/div[1]/span/span/span"
            toAirportXPATH = f"{prefix}{count}]/div/div[2]/div/div[2]/div/div[3]/span/div[2]/span/span/span"
            stopoversXPATH = f"{prefix}{count}]/div/div[2]/div/div[2]/div/div[4]/div[1]/span"
            priceXPATH = f"{prefix}{count}]/div/div[2]/div/div[2]/div/div[6]/div[1]/div[2]/span"

            timeStart = driver.find_element(By.XPATH, timeStartXPATH).text
            timeEnd = driver.find_element(By.XPATH, timeEndXPATH).text
            airline = driver.find_element(By.XPATH, airlineXPATH).text
            duration = driver.find_element(By.XPATH, durationXPATH).text
            fromAirport = driver.find_element(By.XPATH, fromAirportXPATH).text
            toAirport = driver.find_element(By.XPATH, toAirportXPATH).text
            stopovers = driver.find_element(By.XPATH, stopoversXPATH).text
            price = driver.find_element(By.XPATH, priceXPATH).text.replace("\u202f", " ")

            fromCity = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/div/div/input').get_attribute("value")
            toCity = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[2]/div[1]/div[4]/div/div/div[1]/div/div/input').get_attribute("value")

            if maxPrice!=None and int(price[:-1]) > maxPrice:
                break

            foundflights.append([date, fromCity, toCity, fromAirport, toAirport, timeStart, timeEnd, airline, price, duration, stopovers])

            """print(f"########## FLIGHT N°{count} ##########")
            print (f"{airline} : {timeStart} - {timeEnd}")
            print(f"{price}")
            print(" ")
            print(f"{fromAirport} - {toAirport} | {stopovers} : {duration}")
            print(" ") """
        except:
            pass
    
    return foundflights

def nextDay():
    waitclick('/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[3]/button')


    #Attendre le chargement des vols
    barxpath = '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[1]/div[1]/div[2]'
    progressbar = driver.find_element(By.XPATH, barxpath).get_attribute("class")
    
    """ input_xpath = waitget('/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input')
    showed_xpath = waitget('/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/label/span[1]/div') """
    time.sleep(1)
    timeout=10
    while (progressbar == driver.find_element(By.XPATH, barxpath).get_attribute("class")):
        print(progressbar)
        print(driver.find_element(By.XPATH, barxpath).get_attribute("class"))
        print("=====WAITING======")
        time.sleep(0.2)
        timeout-=0.2
        if (timeout==0):
            raise TimeoutError ("Timeout for comparing progress bars classes")

    """ wait = WebDriverWait(driver, 20)
    wait.until(lambda driver: progressbar.get_attribute("class")!=driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[1]/div[1]/div[2]').get_attribute("class")) """

def compare_dates(driver, input_xpath, div_xpath):
    try:
        # Attendre que les deux éléments soient présents
        input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, input_xpath))
        )
        div_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, div_xpath))
        )
        
        # Récupérer les valeurs des éléments
        input_value = input_element.get_attribute("value")
        div_text = div_element.text

        # Debugging : afficher les valeurs
        print(f"Input value: {input_value}, Div text: {div_text}")

        # Vérifier que les deux valeurs ne sont pas None et comparer
        if input_value and div_text:
            return input_value.endswith(div_text)
        else:
            print("Une des valeurs est None ou vide.")
            return False
    except Exception as e:
        print(f"Erreur lors de la comparaison des dates : {e}")
        return False

def manageFlights(flights, fromAirport, toAirport, maxPrice):
    #[date, fromCity, toCity, fromAirport, toAirport, timeStart, timeEnd, airline, price, duration, stopovers]
    print("MANAGE FLIGHTS...")
    for flight in flights:
        flight[8] = int(flight[8].replace("€", "").replace(" ", ""))
    sortedFlights = sorted(flights, key=lambda flight: flight[8])

    finalFlights = [] # [[Flight1, Flight2], [Flight], ...]

    for flight in sortedFlights:
        if flight[1].lower() == fromAirport.lower() and flight[2].lower() == toAirport.lower():
            finalFlights.append([flight])
        elif flight[1].lower() == fromAirport.lower():
            #Search second flight
            ddmmyyyy = flight[0].split('/')
            daysplus = 0
            if "+" in flight[6]:
                daysplus = int(flight[6][-1])
            print(f"{ddmmyyyy[2]}{ddmmyyyy[1]}{ddmmyyyy[0]}")
            firstFlightDate = datetime(int(ddmmyyyy[2]), int(ddmmyyyy[1]), (int(ddmmyyyy[0])+daysplus), int(flight[5][0:2]), int(flight[5][3:5]))
            flightPrice = flight[8]

            for secondFlight in sortedFlights:
                if flightPrice+secondFlight[8] > maxPrice:
                    continue
                if secondFlight[1] == flight[2]:
                    sFlightDate = datetime.strptime(secondFlight[0], "%d/%m/%Y")
                    secondFlightDate = sFlightDate.replace(hour=int(secondFlight[5][0:2]), minute=int(secondFlight[5][3:5]))   

                    if firstFlightDate < secondFlightDate:
                        finalFlights.append([flight, secondFlight])
                        #todo max price handle

        elif flight[2].lower() == toAirport.lower():
            #Search first flight
            sFlightDate = datetime.strptime(flight[0], "%d/%m/%Y")
            secondFlightDate = sFlightDate.replace(hour=int(flight[5][0:2]), minute=int(flight[5][3:5]))

            flightPrice = flight[8]
            for firstFlight in sortedFlights:
                if flightPrice + firstFlight[8] > maxPrice:
                    continue
                if firstFlight[2] == flight[1]:
                    ddmmyyyy = flight[0].split('/')
                    daysplus = 0
                    if "+" in flight[6]:
                        daysplus = int(flight[6][-1])
                    firstFlightDate = datetime(int(ddmmyyyy[2]), int(ddmmyyyy[1]), (int(ddmmyyyy[0])+daysplus), int(flight[5][0:2]), int(flight[5][3:5]))

                    if firstFlightDate < secondFlightDate:
                        finalFlights.append([firstFlight, flight])
                        #todo max price handle

    withoutDoublons = []
    for itinerary in finalFlights:
        if itinerary not in withoutDoublons:
            withoutDoublons.append(itinerary)

    for i in range(0,len(withoutDoublons)):
        itinerary = withoutDoublons[i]

        price = 0
        for flight in itinerary:
            price+=flight[8]
        
        itinerary.insert(0, price)

    sortedFinal = sorted(withoutDoublons, key=lambda x: x[0])

    print("here's the result:")
    for i in sortedFinal:
        addItinerary(i)

    with open('flights.txt', 'w') as file:
        for itinerary in sortedFinal:
            file.write(f"{itinerary}\n")

    eel.revertToSearchButton()




#Chrome options
o = Options()
#o.add_experimental_option("detach", True) #Not closing chrome after finishing all tasks
#o.add_argument("--headless")
o.add_argument("--disable-gpu")

#Open google flights and accept cookies
driver = webdriver.Chrome(options=o)
driver.get("https://www.google.com/travel/flights?tfs=CBwQARoOagwIAhIIL20vMG1fMXNAAUgBcAGCAQsI____________AZgBAg&tfu=KgIIAw")

waitclick('button[aria-label="Tout accepter"]', By.CSS_SELECTOR)

@eel.expose
def addItinerary(itinerary):
    print(itinerary)
    flights = ''
    totalDuration = itinerary[1][9]
    if len(itinerary)>2:
        date1 = datetime.strptime(itinerary[1][0] + " " + itinerary[1][5], "%d/%m/%Y %H:%M")
        print(f"NUMERO UNO : {itinerary[-1][0]}")
        print(f"NUMERO DOS : {itinerary[-1][6]}")
        date2 = datetime.strptime(itinerary[-1][0] + " " + itinerary[-1][6][0:5], "%d/%m/%Y %H:%M")
        if "+" in itinerary[-1][6]:
            for i in range(int(itinerary[-1][6][-1])):
                date2 = date2 + timedelta(days=1)
        # Calculer la différence
        difference = date2 - date1

        # Obtenir les heures et minutes de la différence
        hours, remainder = divmod(difference.total_seconds(), 3600)
        minutes = remainder // 60
        totalDuration = f"{round(hours)} h {round(minutes)} min"
    for i in range(1,len(itinerary)):
        airline = itinerary[i][7]
        if airline=="Correspondance autonome":
            airline = str(int(itinerary[i][10][0])+1) + " Compagnies"
        elif len(airline) > 15:
            airline = airline[0:14] + ".."
        
        flights = flights + '<div class="flight"><div class="fromAirport"><p>'+ itinerary[i][3] +'</p><h3>'+ itinerary[i][5] +'</h3></div> <svg class="plane-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 510 510"> <path fill="#0" d="M497.25 357v-51l-204-127.5V38.25C293.25 17.85 275.4 0 255 0s-38.25 17.85-38.25 38.25V178.5L12.75 306v51l204-63.75V433.5l-51 38.25V510L255 484.5l89.25 25.5v-38.25l-51-38.25V293.25l204 63.75z"/> </svg> <div class="toAirport"><p>'+ itinerary[i][4] +'</p><h3>'+ itinerary[i][6] +'</h3></div><div class="separator"></div><div class="info"><h3>'+ str(itinerary[i][8]) + ' €</h3><h3>'+ itinerary[i][10] +'</h3><h3>'+ itinerary[i][9] +'</h3><h3>'+ itinerary[i][0] +'</h3><h3>'+ airline +'</h3></div></div>'
    
    html = '<div class="itinerary"><div class="flights">' + flights + '</div><div class="sep"></div><div class="summary"><h2>'+ str(itinerary[0]) + ' €</h2><h2>'+ totalDuration +'</h2></div></div>'
    
    eel.addItinerary(html)

#manageFlights(TESTFLIGHTS, "Paris", "Erevan")

@eel.expose
def searchfromgui(from_airport, to_airport, from_date, to_date, direct_flight, stopovers, max_price):
    print(from_date)
    print(to_date)
    currentdate = from_date
    
    if max_price !="":
        max_price = int(max_price)
    else:
        max_price = None

    #First search without any entered stopover
    searchFlight(from_airport, to_airport, from_date, direct_flight)
    time.sleep(1)
    foundflights = scrapePage(currentdate, max_price)

    #Search next flights if date range > 1
    if not (to_date=="" or to_date==None):
        days = daysDistance(from_date, to_date)
        for i in range (days):
            currentdate = incrementOneDay(currentdate)
            nextDay()
            foundflights = scrapePage(currentdate, max_price, foundflights)

    #Finish search if no stopovers entered
    if stopovers == None or stopovers == "":
        manageFlights(foundflights, from_airport, to_airport, max_price)
        return

    #Continue with stopovers
    stopovers = stopovers.split(',')
    for stopover in stopovers:
        currentdate = from_date
        driver.get("https://www.google.com/travel/flights?tfs=CBwQARoOagwIAhIIL20vMG1fMXNAAUgBcAGCAQsI____________AZgBAg&tfu=KgIIAw")
        searchFlight(from_airport, stopover, from_date, direct_flight)
        time.sleep(1)
        foundflights = scrapePage(currentdate, max_price, foundflights)
        days = daysDistance(from_date, to_date)
        time.sleep(0.5)
        for i in range (days):
            currentdate = incrementOneDay(currentdate)
            nextDay()
            foundflights = scrapePage(currentdate, max_price, foundflights)

        time.sleep(0.5)

        currentdate = from_date
        driver.get("https://www.google.com/travel/flights?tfs=CBwQARoOagwIAhIIL20vMG1fMXNAAUgBcAGCAQsI____________AZgBAg&tfu=KgIIAw")
        searchFlight(stopover, to_airport, from_date, direct_flight)
        time.sleep(1)
        foundflights = scrapePage(currentdate, max_price, foundflights)
        days = daysDistance(from_date, to_date)
        time.sleep(0.5)
        for i in range (days):
            currentdate = incrementOneDay(currentdate)
            nextDay()
            foundflights = scrapePage(currentdate, max_price, foundflights)
    
    for flight in foundflights:
        print(flight)

    manageFlights(foundflights, from_airport, to_airport, max_price)

@eel.expose
def getnextday():
    nextDay()
    time.sleep(1)
    scrapePage()

@eel.expose
def getTransferDetails():
    print(driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[2]/div/div[2]/div[2]/ul/li[1]/div/div[4]/div/div[1]/div[14]').text)

    
eel.start('index.html')
