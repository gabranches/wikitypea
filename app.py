from _Getch import getch
import time
import WikipediaAPI
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', phrase=pick_phrase())



def start_test(phrase):
    
    start = time.time()
    print(phrase)

    while len(phrase) > 0:
        key = getch()
        if key == phrase[0]:
            phrase = phrase[1:]
            print('\n\n' + phrase)

    end = time.time()
    print('WPM: ' + str((end - start) / 60 * 100))
    return (end - start) / 60 * 100

        

def countdown(seconds):
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1



def pick_phrase():

    return WikipediaAPI.get_random_summary()



def main():
    phrase = pick_phrase()
    words = len(phrase.split(' '))
    countdown(3)
    start_test(phrase)

if __name__ == '__main__':
    app.run()

