import urllib2
import csv
import os.path

urlBase = 'https://localhost/strutture?'


with open('PROFILING_PROVINCIA.csv') as csv_file:
 csv_reader = csv.reader(csv_file, delimiter=',')
 line_count = 0
 for row in csv_reader:
    my_file = os.path.isfile('dirRis/' + row[0] + '.json')
    if my_file:
        print('File della provincia gia scaricato: ' + row[0] + '.json')
        continue

    urlParam = 'codiceProvincia=' + row[0]
    url = urlBase + urlParam
    req = urllib2.Request(url)

    req.add_header('User-agent', 'Mozilla/5.0 (Linux i686)')
    req.add_header('Content-Type', 'application/json')
    req.add_header('x-ibm-client-id', 'XXXX-XXXX-XXX')
    req.add_header('x-ibm-client-secret', 'Ddaskjjdsaoij231mokda')
    
    
    try:
        print('--- Scarico file della provincia ' + row[0] + ' -------')
        res = urllib2.urlopen(req, None, 30)
        html = res.read()
        with open('dirRis/' + row[0] + '.json', 'w') as file:
            file.write(html)
            print('--- Fine scarico file della provincia ' + row[0] + ' -------')
    except urllib2.URLError as e:
        print("Provincia non scaricata: " + row[0])
        print("There was an error: %r" % e)

print('Game over')

