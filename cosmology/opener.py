cosmology_txt = open ("cosmology.txt", 'r')
planets_tab = open ("planets.tab", 'r')
planets_csv = open ("planets.csv", 'r')
planets_fixedwidth_txt = open ("planets-fixedwidth.txt", 'r')

# COSMOLOGY.TXT
print ("~~~~~~~~~ COSMOLOGY.TXT ~~~~~~~~~~")
cosmology_whole = cosmology_txt.read()

print (cosmology_whole)
cosmology_txt.seek(0)

print ("~~~~~~~ END COSMOLOGY.TXT ~~~~~~~~")



# COSMOLOGY.TXT as chars
#print ("~~ COSMOLOGY.TXT (char-by-char) ~~")
#while True:
#    c = cosmology_txt.read(1)
#    if c=='': break
#    print (c, ord(c))
#cosmology_txt.seek(0)

#print ("~~~~~~~ END COSMOLOGY.TXT ~~~~~~~~")

# COSMOLOGY.TXT as lines
#print ("~~ COSMOLOGY.TXT (line-by-line) ~~")
#n = 0
#while True:
#    c = cosmology_txt.readline()
#    if c=='': break
#    print (n, ":", c.strip())
#    n+=1
#cosmology_txt.seek(0)

#print ("~~~~~~~ END COSMOLOGY.TXT ~~~~~~~~")




# PLANETS-FIXEDWIDTH.TXT
print ("~~~~~ PLANETS-FIXEDWIDTH.TXT ~~~~~")
records = []

for line in planets_fixedwidth_txt:
    rec = []
    rec.append (line[0:8].strip())
    rec.append (line[8:15].strip())
    rec.append (line[15:29].strip())
    records.append (rec)

print (records)

print ("~~~ END PLANETS-FIXEDWIDTH.TXT ~~~")

# PLANETS.CSV

print ("~~~~~ PLANETS.CSV ~~~~~")
records = []

for line in planets_csv:
    rec = []
    rec.append ('')
    isInsideQuotes = False
    for char in line.strip():
        if char == ',' and not isInsideQuotes:
            rec.append('')
            continue
        if char == '"':
            isInsideQuotes = not isInsideQuotes
            continue
        rec[-1] += char
    records.append (rec)

print (records)

print ("~~~ END PLANETS.CSV ~~~")

cosmology_txt.close()
planets_tab.close()
planets_csv.close()
planets_fixedwidth_txt.close()
