##Zmijica
```Igrica po uzoru na igru Snake gde igrac kontrolise zmijicu koja se krece i poraste
svaki put kada pojede hranu. Ako zmija kretanjem udari u zid ili zagrize sama sebe
igra se završava i ispisuju se poeni. Igrica će biti napravljena u jeziku Python 
sa grafičkim korisničkim interfejsom. Od dodatnih biblioteka bice koriscena Tkinder
biblioteka. Namenjena je Linux operativnom sistemu i pokrece se lokalno. Članovi 
tima: Anja Drašković 19/2016 Ilija Katić 379/2016
```
### Install virtual environment:
```sh
$ virtualenv venv --python=python3
$ source venv/bin/activate (or . venv/bin/activate)
$ pip install -r requirements.txt
$ echo "$(pwd)" | sudo tee venv/lib/python3.6/site-packages/snakegame_app.pth > /dev/null
```
```
starting game python sankegame_app/run.py
```