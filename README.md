##Zmijica
```Igrica po uzoru na igru Snake gde igrac kontrolise zmijicu koja se krece i poraste
svaki put kada pojede hranu. Ako zmija kretanjem udari u zid ili zagrize sama sebe
igra se završava i ispisuju se poeni. Igrica će biti napravljena u jeziku Python 
sa grafičkim korisničkim interfejsom. Od dodatnih biblioteka bice koriscena Tkinder
i PIL biblioteka. Tkinter se koristi za kreiranje grafickog intrfejsa a PIL za ubacivanje 
slika, iz Tkinter-a smo koristili canvas za kreiranje tela zmije, hrane i za dobijanje moci.
Postoji zelena hrana koja povecava brzinu zmije i crvena koja omogucuje kretanje kroz zidove,
te moci traju po 5 sekudi i za to vreme zmija dobija boju hrane (crvena/zelena). Komande za 
upravljanje zmijom su:
    w-skrece ka gornjem delu polja
    s-skrece ka donjem delu polja
    a-skrece ka levom delu polja
    d-skrece ka desnom delu polja
Na kraju igre korisniku se ispisuje njegov rezultat (svaka pojedena hrana nosi 5 bodova),
i moze da bira da ponovo igra ili da ugasi program.
Namenjena je Linux operativnom sistemu i pokrece se lokalno.
Članovi tima:
Anja Drašković 19/2016 
Ilija Katić 379/2016
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