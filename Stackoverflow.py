import requests

class Stackoverflow:


    def get_questions_python(self):
          url = 'https://stackoverflow.com/questions/tagged/python/'
          headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
          response = requests.get(url, headers=headers)
          print(response.e.doc())

if __name__ == '__main__':
    stackoverflow = Stackoverflow()
    stackoverflow.get_questions_python()