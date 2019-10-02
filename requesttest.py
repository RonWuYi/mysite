import requests

my_buck = 'bugs-246912.appspot.com'
r = requests.get('https://www.googleapis.com/storage/v1/b/bugs-246912.appspot.com')
print(r.status_code)