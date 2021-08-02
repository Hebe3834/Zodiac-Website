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

def bin_search(g, key, low, high):
    mid = (low+high+1)//2
    if(low>high):
        return -1
    elif(int(g[mid][7:11])==key):
        return mid
    elif(key>int(g[mid][7:11])):
        return bin_search(g, key, mid+1, high)
    else:
        return bin_search(g, key, low, mid-1)

def bday_sign():
    month = int(data.getvalue('month'))
    day = str(data.getvalue('day'))
    year = str(data.getvalue('year'))
    if len(day)>2:
        day = day[len(day)-2:len(day)]
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
        f = open('lunar_ny_dates.csv')
        dates = f.read()
        dates_list = dates.split('\n')
        index = bin_search(dates_list, year, 0, 120)
        lunar_year = dates_list[index]
        if lunar_year[:3]=='Jan':
            ny_code = '1'
        else:
            ny_code = '2'
        ny_code += lunar_year[4:6]
        if day<10:
            user_code = str(month) + '0' + str(day)
        else:
            user_code = str(month) + str(day)
        prev_sign = False
        if(int(user_code)<int(ny_code)):
            prev_sign = True
        signs = ['MONKEY', 'ROOSTER', 'DOG', 'BOAR', 'RAT', 'OX', 'TIGER', 'RABBIT', 'DRAGON', 'SNAKE', 'HORSE', 'GOAT']
        index = year%12
        if prev_sign:
            index-=1
        user_sign = signs[index]
        return user_sign

template = get_template('chinese')
html = fill_tag(template, 'title', 'Results!')
if ('month' in data):
    user_sign = bday_sign()
    if user_sign[:6]=='Please':
        html = fill_tag(html, 'h1', user_sign)
    else:
        html = fill_tag(html, 'h1', 'You were born on the year of the ' + user_sign + '!')
        html = fill_tag(html, 'body', '<a href="chinese_zodiac.py?sign='+user_sign+'" style="color:azure">Tell me more about my zodiac >></a>')
else:
    traits = ["optimistic","energetic","clever","resourceful","imaginative","hardworking","generous","just","stable","responsible","ambitious","courageous","smart","gentle","patient","elegant","considerate","dedicated","initiative","talented","inspiring","quick-witted","sympathetic","easy-going","calm","determined","endurance","warm-hearted","social","brave","independent","creative","competitive","enthusiastic","innovative","versatile","efficient","confident","loyal","honest","cheerful","trustful","timid","suspicious","short-sighted","not persistent","stubborn","hesitant","struggles to adapt","moody","impulsive","arrogant","aloof","hasty","conservative","peacockish","intolerant","tactless","unrealistic","sly","narrow-minded","jealous","pessimistic","lacks calm","indecisive","vain","emotional","undisciplined","selfish","cunning","critical","impatient","sensitive","reckless","sluggish","naive"]
    f = open("zodiacs_info.csv")
    info = f.read()
    info = info.split('\n')[:12]
    i = 0
    while i<12:
        info[i] = info[i].split(',')[1:10]
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
    table = '''<table style="color:gold; font-size:30px; margin:auto">
<tr"><th>Sign</th><th>Score</th></tr>'''
    signs = ['RAT', 'OX', 'TIGER', 'RABBIT', 'DRAGON', 'SNAKE', 'HORSE', 'GOAT', 'MONKEY', 'ROOSTER', 'DOG', 'BOAR']
    i=0
    while i<12:
        table += '<tr><td><a href=chinese_zodiac.py?sign=' + signs[i] + ' style="color:gold">' + signs[i] + '</a></td><td>' + str(scores[i]) + '<td></tr>\n'
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
