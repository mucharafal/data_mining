# Eksploracja danych- DBLP
Repozytorium zawiera skrypty oraz notatniki jupytera używane do analizy zbioru DBLP.
## Dataset
### Źródłowy
Zbiór: https://www.aminer.cn/citation    
Wykorzystywaliśmy zbiór V11, najnowszy w chwili rozpoczęcia projetku.   
Większość notebooków wykorzystuje już przetworzony zbiór rozbity na części (slicer.py) oraz z odfiltrowanymi niepotrzebnymi polami czy zamienionymi na indeksy nazwami autorów czy słowami kluczowymi. Są to pliki author_index... dostarczone razem z plikami.
### Przetworzony
Przetworzone pliki: https://drive.google.com/file/d/1Th58VQ4lJTj-K__zcFVvNMP-wI_6FHh3/view?usp=sharing
Należy w notebookach zmienić katalog roboczy na katalog, gdzie zostaną rozpakowane powyższe pliki.
## Wymagane oprogramowanie
 - python 3
 - jupyter notebook
 - pandas
 - networkx    
 - Gephi    
 ## Analizy
Analizy wykonane są w notatnikach jupyter.
 ## Odtworzenie datasetów z pierwotnego zbioru
 - uruchomienie `slicer.py`
 - uruchomienie notebooka `fos_to_index.ipynb`
 - uruchomienie notebooka `authors_to_index.ipynb`
 ### Podział na grupy tematyczne w Gephi
 Niestety ze względu na element losowy w metodzie dzielącej na grupy (o czym zorientowaliśmy się po czasie, gdy próbowaliśmy dograć wyniki) w programie, podział na grupy tematyczne jest niejednoznaczny. Uzyskane przez nas wyniki mogą być nie do odtworzenia. Uzyskane grupy zapisane są w plikach `csv`
## Dokumentacja
https://trac.iisg.agh.edu.pl/ed/wiki/projects/2020/DBLP
## Prezentacja
https://drive.google.com/file/d/1fFTZHWXUjxmsoL2DZE4NoQR55ST2nxdO/view?usp=sharing
Jest to paczka źródłowa z overleafa.
