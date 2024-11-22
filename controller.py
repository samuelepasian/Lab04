import time
import flet as ft
import model as md
from view import View

class SpellChecker:

    def __init__(self, view:View):
        self._multiDic = md.MultiDictionary()
        self._view = view


    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None

    def handleSpellCheck(self,e):
        self._view._lvOut.controls.clear()
        self._view.update()
        errori=""
        tempo=0

        if self._view._menu.value=="":
            self._view._lvOut.controls.append(ft.Text("Non hai inserito la lingua"))
        elif self._view._ricerca.value == "":
            self._view._lvOut.controls.append(ft.Text("Non hai inserito modalità di ricerca"))
        else:

            errori,tempo=self.handleSentence(self._view._txtIn.value,self._view._menu.value,self._view._ricerca.value)
            self._view._lvOut.controls.append(ft.Text(errori))
            self._view._lvOut.controls.append(ft.Text(tempo))
            self._view.update()

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    def scegliLingua(self,e):
        lista=["italiano", "inglese", "spagnolo"]
        try:
            self._view._menu.value in lista
        except ValueError:
            self._view._lvOut.controls.append(ft.Text("Errore nella selezione della lingua"))
            self._view.update()
            return
        self._view._lvOut.controls.append(ft.Text("Lingua selezionata correttamente"))
        self._view.update()

    def scegliRicerca(self, e):
        lista = ["Default", "Lineare", "Dicotomica"]
        try:
            self._view._menu.value in lista
        except ValueError:
            self._view._lvOut.controls.append(ft.Text("Errore nella selezione della ricerca"))
            self._view.update()
            return
        self._view._lvOut.controls.append(ft.Text("Ricerca selezionata correttamente"))
        self._view.update()




def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text


    