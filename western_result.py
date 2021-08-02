#!/usr/bin/python
print ("Content-type: text/html\n")

import cgi
data = cgi.FieldStorage()

def get_template(choice):
    if choice=='chinese':
        f = open('ctemplate.html')
    else:
        f = open('wtemplate.html')
    template = f.read()
    f.close()
    return template

def fill_tag(html, tag, content):
    index = html.find('</'+tag+'>')
    ans = html[:index] + content + html[index:]
    return ans

def bday_sign():
    month = int(data.getvalue('month'))
    day = str(data.getvalue('day'))
    year = str(data.getvalue('year'))
    for n in str(year):
        if ord(n)<48 or ord(n)>57:
            return 'Please input numbers for the year'
    for n in str(day):
        if ord(n)<48 or ord(n)>57:
            return 'Please input numbers for the date'
    year = int(year)
    day = int(day)
    if year<1900 or year>2020:
        return 'Please fill in a proper year'
    elif day<=0 or (month==2 and day>29) or (month in {4,6,9,11} and day>30) or (month in {1,3,5,7,8,10,12} and day>31):
        return 'Please fill in a proper date'
    else:
        cutoffs = [22, 20, 19, 21, 20, 20, 21, 23, 23, 23, 23, 22]
        signs = ['CAPRICORN', 'AQUARIUS', 'PISCES', 'ARIES', 'TAURUS', 'GEMINI', 'CANCER', 'LEO', 'VIRGO', 'LIBRA', 'SCORPIO', 'SAGITTARIUS']
        if month==12:
            month = 0
        if day < cutoffs[month]:
            month -= 1
        return signs[month]

template = get_template('western')
html = fill_tag(template, 'title', 'Results!')
if ('month' in data):
    user_sign = bday_sign()
    if user_sign[:6]=='Please':
        html = fill_tag(html, 'h1', user_sign)
    else:
        html = fill_tag(html, 'h1', 'Your birth sign is ' + user_sign + '!')
        html = fill_tag(html, 'body', '<a href="western_zodiac.py?sign='+user_sign+'" style="color:azure">Tell me more about my zodiac >></a>')
else:
    traits = ["adventurous","independent","brave","honest","passionate","stubborn","reckless","aggressive","short-tempered","dependable","hardworking","dedicated","smart","patient","lazy","possessive","uncompromising","adaptable","outgoing","curious","gentle","loves to learn","indecisive","unreliable","nosy","nervous","protective","intuitive","caring","persuasive","sensitive","moody","pessimistic","insecure","generous","confident","cheerful","leader","arrogant","self-centered","kind","creative","shy","worrying","critical","uptight","fair","idealistic","diplomatic","clever","cooperative","self-pitying","non-confrontational","resourceful","jealous","secretive","violent","distrustful","compassionate","impatient","tactless","unrealistic","disciplined","responsible","ambitious","good self-control","condescending","unforgiving","workaholic","visionary","unbiased","aloof","unpredictable","artistic","wise","overly trusting","closed off"]
    f = open("zodiacs_info.csv")
    info = f.read()
    info = info.split('\n')[12:]
    i = 0
    while i<12:
        info[i] = info[i].split(',')[2:11]
        i+=1
    scores = [0,0,0,0,0,0,0,0,0,0,0,0]
    for trait in traits:
        if trait in data:
            i=0
            while i<12:
                if trait in info[i]:
                    scores[i]+=1
                i+=1
    html = fill_tag(html, 'h1', "Here's how much you match each zodiac")
    table = '''<table style="color:azure; font-size:30px; margin:auto">
<tr"><th>Sign</th><th>Score</th></tr>'''
    signs = ['ARIES', 'TAURUS', 'GEMINI', 'CANCER', 'LEO', 'VIRGO', 'LIBRA', 'SCORPIO', 'SAGITTARIUS', 'CAPRICORN', 'AQUARIUS', 'PISCES']
    i=0
    while i<12:
        table += '<tr><td><a href=western_zodiac.py?sign=' + signs[i] + ' style="color:skyblue">' + signs[i] + '</a></td><td>' + str(scores[i]) + '<td></tr>\n'
        i+=1
    table += '</table>'
    html = fill_tag(html, 'body', table)
        


if ('consent' in data) and ('month' in data) and (user_sign[:6]!="Please"):
    f = open('user_data.csv')
    past = f.read();
    f.close();
    past = past.split('\n')
    i=0
    while i<24:
        past[i] = past[i].split(',')
        if past[i][0]==user_sign:
            index = i
        i+=1
    f = open('user_data.csv', 'w')
    i=0
    while i<24:
        if i==index:
            f.write(past[i][0])
            f.write(',')
            f.write(str(int(past[i][1])+1))
            f.write('\n')
        else:
            f.write(past[i][0])
            f.write(',')
            f.write(past[i][1])
            f.write('\n')
        i+=1
    f.close()
    
    
print(html)
