#!/usr/bin/python
print ("Content-type: text/html\n")

import matplotlib.pyplot as plt

f = open('user_data.csv')
data = f.read()
f.close()
data = data.split('\n')[:12]
signs = []
freq = []
for i in data:
    i = i.split(',')
    signs.append(i[0])
    freq.append(int(i[1]))

plt.pie(freq, labels=signs, shadow=True)
plt.savefig("cpie.png")
plt.close()

plt.bar(signs, freq)
plt.xticks(rotation=30)
plt.savefig("cbar.png")
plt.close()

f = open('user_data.csv')
data = f.read()
f.close()
data = data.split('\n')[12:24]
signs = []
freq = []
for i in data:
    i = i.split(',')
    signs.append(i[0])
    freq.append(int(i[1]))

plt.pie(freq, labels=signs, shadow=True)
plt.savefig("wpie.png")
plt.close()

plt.bar(signs, freq)
plt.xticks(rotation=20)
plt.savefig("wbar.png")
plt.close()

print('''<!DOCTYPE html>

<html>

  <head>
    <title>Data plots!</title>
    <link rel="icon" href="icon.jpg">
    <style>
      body {
      font-family: "Lucida Console";
      background-image: url("home_bkgd.jpg");
      background-size: cover;
      background-position: center;
      padding: 70px;
      text-align:center
      }
      h1 {
      text-align: center;
      font-size: 40px;
      color: white;
      }
      a {
      padding: 20px;
      color: skyblue;
      font-size: 20px
      }
      p {
      color: gold;
      font-size: 30px
      }
    </style>
    <body>
      <h1>Pick a chart</h1><br><br>
      <p style="color:azure">Data taken from submissions on this website</p>
      <p>Pie Charts</p>
      <a href="cpie.png">Chinese Sign Frequency</a><br><br><br><br><br>
      <a href="wpie.png">Western Sign Frequency</a><br><br><br><br><br>
      <p>Bar Plots</p>
      <a href="cbar.png">Chinese Sign Frequency</a><br><br><br><br><br>
      <a href="wbar.png">Western Sign Frequency</a>
    </body>
</html>''')
