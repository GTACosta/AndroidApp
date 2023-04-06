from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
import webbrowser
from kivy.core.clipboard import Clipboard


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class DrawerList(ThemableBehavior, MDList):
    pass


class MediaApp(MDApp):

    def po_media(self):
        lista_notas = [str(self.root.ids.notaP1.text).replace(',', '.'), str(self.root.ids.notaP2.text).replace(',', '.'), str(self.root.ids.notaP3.text).replace(',', '.'),
                       str(self.root.ids.notaP4.text).replace(',', '.')]
        lista_pesos = [str(self.root.ids.peso1.text).replace(',', '.'), str(self.root.ids.peso2.text).replace(',', '.'), str(self.root.ids.peso3.text).replace(',', '.'),
                       str(self.root.ids.peso4.text).replace(',', '.')]
        lista_notas2 = []
        lista_pesos2 = []
        for i in lista_notas:
            if i != '':
                lista_notas2.append(float(i))
            else:
                pass
        for item in lista_pesos:
            if item != '':
                lista_pesos2.append(float(item))
            else:
                pass
        mult = [x * y for x, y in zip(lista_notas2, lista_pesos2)]
        try:
            media_ponderada = sum(mult) / sum(lista_pesos2)
        except ZeroDivisionError:
            return 'Esqueceu os pesos!'
        else:
            return f'{media_ponderada:.1f}'.replace('.', ',')

    def ar_media(self):
        tam = 0
        lista_notas = [str(self.root.ids.prin.text).replace(',', '.'), str(self.root.ids.segn.text).replace(',', '.'),
                       str(self.root.ids.tercn.text).replace(',', '.'), str(self.root.ids.quarn.text).replace(',', '.')]
        lista_notas2 = []
        for i in lista_notas:
            if i != '':
                lista_notas2.append(float(i))
                tam += 1
            else:
                pass
        try:
            media_aritmetica = (sum(lista_notas2) / tam)
        except ZeroDivisionError:
            return 'Esqueceu as notas!'
        else:
            return f'{media_aritmetica:.1f}'.replace('.', ',')

    def aritmetica_mostrar(self):
        self.root.ids.show_ma.text = f'{self.ar_media()}'

    def ponderada_mostrar(self):
        self.root.ids.mostrar_mp.text = f'{self.po_media()}'

    def limpar_a(self):
        self.root.ids.prin.text = ''
        self.root.ids.segn.text = ''
        self.root.ids.tercn.text = ''
        self.root.ids.quarn.text = ''
        self.root.ids.show_ma.text = ''

    def apagar_p(self):
        self.root.ids.notaP1.text = ''
        self.root.ids.notaP2.text = ''
        self.root.ids.notaP3.text = ''
        self.root.ids.notaP4.text = ''
        self.root.ids.peso1.text = ''
        self.root.ids.peso2.text = ''
        self.root.ids.peso3.text = ''
        self.root.ids.peso4.text = ''
        self.root.ids.mostrar_mp.text = ''

    def copy(self):
        try:
            Clipboard.copy('gabrieltorres570@gmail.com')
        except:
            pass

    def face(instance):
        webbrowser.open('https://www.facebook.com/gabriel.newton.900?mibextid=ZbWKwL')

    def twit(instance):
        webbrowser.open('https://twitter.com/Josoyeltorres?t=PXWbHisfhNiN9DUvI6wUWQ&s=08')

    def git(instance):
        webbrowser.open('https://github.com/GTACosta')

    def linke(instance):
        webbrowser.open('https://www.linkedin.com/in/gabriel-torres-4b77a9113')

    def build(self):
        root = Builder.load_file('/home/wyche/PycharmProjects/AppProject/App/media.kv')
        return root


MediaApp().run()
