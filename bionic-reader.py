import http.client
import urllib.parse
import sys


#print("Enter API Key: ")
api_key = input("Enter API Key: ")

#### 300 line limit per api request
# Pro account  = 20,000 requests a day


# Convert file from pdf to txt via pdftotxt



# Open file that as converted from PDF
with open('bionic-emacs.txt') as f:
    lines = f.readlines()

# Convert list of strings to string
text = " ".join(lines)

# Encode string into bytes, utf-8
encoded_txt = str.encode(text)

# URL encode string
url_txt = urllib.parse.quote(encoded_txt)

# Create and add parameters for API call
params = {'response_type': 'html', 'request_type': 'html', 'fixation': '1', 'saccade': '10'}

# Fixup url
url_txt = 'content=' + url_txt + '&' + urllib.parse.urlencode(params)

#print(url_txt)

conn = http.client.HTTPSConnection("bionic-reading1.p.rapidapi.com")

# Example api call
#payload = "content=Lorem%20ipsum%20dolor%20sit%20amet%2C%20consetetur%20sadipscing%20elitr%2C%20sed%20diam%20nonumy%20eirmod%20tempor%20invidunt%20ut%20labore%20et%20dolore%20magna%20aliquyam%20erat%2C%20sed%20diam%20voluptua.%20At%20vero%20eos%20et%20accusam%20et%20justo%20duo%20dolores%20et%20ea%20rebum.%20Stet%20clita%20kasd%20gubergren%2C%20no%20sea%20takimata%20sanctus%20est%20Lorem%20ipsum%20dolor%20sit%20amet.%20Lorem%20ipsum%20dolor%20sit%20amet%2C%20consetetur%20sadipscing%20elitr%2C%20sed%20diam%20nonumy%20eirmod%20tempor%20invidunt%20ut%20labore%20et%20dolore%20magna%20aliquyam%20erat%2C%20sed%20diam%20voluptua.%20At%20vero%20eos%20et%20accusam%20et%20justo%20duo%20dolores%20et%20ea%20rebum.%20Stet%20clita%20kasd%20gubergren%2C%20no%20sea%20takimata%20sanctus%20est%20Lorem%20ipsum%20dolor%20sit%20amet.&response_type=html&request_type=html&fixation=1&saccade=10"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'X-RapidAPI-Host': "bionic-reading1.p.rapidapi.com",
    'X-RapidAPI-Key': api_key
    }

#conn.request("POST", "/convert", payload, headers)
conn.request("POST", "/convert", url_txt, headers)

res = conn.getresponse()
data = res.read()

#print(data.decode("utf-8"))

outfile = open("bionic-emacs.html", "w")
outfile.write("<html>\n<head></head>\n<body>\n")
outfile.write(data.decode("utf-8"))
outfile.write("</body>\n</html>\n")
outfile.close()


# Convert html to PDF ?



