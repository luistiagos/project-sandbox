
csv_file = open('./roms/PS1 Jogos (ISOS).csv', 'r')
data = csv_file.readlines()
html = "<html><body><table>"
for i in range(1, len(data)):
    row = data[i].split(";")
    html += '<tr><td><a href="' + row[1] + '" targe="blank">' + row[0] + '</a></td></tr>' 
html += "</table></body></html>"
f = open("JogosPS1.html", "a")
f.write(html)
f.close()