class Storage:
    pass


class OfficeEquip(Storage):
    def __init__(self, d_model, d_year, amount):
        self.d_model = d_model
        self.d_year = d_year
        self.amount = amount
        self.p_office = {'office_1': 0, 'office_2': 0}
        self.s_office = {'office_1': 0, 'office_2': 0}
        self.n_office = {'office_1': 0, 'office_2': 0}


class Printers(OfficeEquip):
    def __init__(self, cartridge, wireless, d_model, d_year, amount):
        super().__init__(d_model, d_year, amount)
        self.cartridge = cartridge
        self.wireless = wireless

    def __str__(self):
        return f"на складе {self.amount} принтеров"

    def sended(self, send, office):
        if str(send).isdigit() and self.amount >= send:
            self.amount -= send
            self.p_office[office] += send
            return f'на складе {self.amount} принтеров в офисе {office} {self.p_office[office]} принтеров'
        else:
            return f'we cant'


class Netbooks(OfficeEquip):
    def __init__(self, bat_mah, screen_inches, d_model, d_year, amount):
        super().__init__(d_model, d_year, amount)
        self.bat_mah = bat_mah
        self.screen_inches = screen_inches

    def __str__(self):
        return f"на складе {self.amount} нетбуков"

    def sended(self, send, office):
        if str(send).isdigit() and self.amount >= send:
            self.amount -= send
            self.n_office[office] += send
            return f'на складе {self.amount} нетбуков в офисе {office} {self.n_office[office]} нетбуков'
        else:
            return f'we cant'


class Scanners(OfficeEquip):
    def __init__(self, doc_format, d_model, d_year, amount):
        super().__init__(d_model, d_year, amount)
        self.doc_format = doc_format

    def __str__(self):
        return f"на складе {self.amount} сканеров"

    def sended(self, send, office):
        if str(send).isdigit() and self.amount >= send:
            self.amount -= send
            self.s_office[office] += send
            return f'на складе {self.amount} сканеров в офисе {office} {self.s_office[office]} сканеров'
        else:
            return f'we cant'


printer_1 = Printers('laser', 'yes', 1100, 2022, 10)
print(printer_1)
print(printer_1.sended(10, 'office_1'))
netbook_1 = Netbooks(5000, 15, '1500super', 2022, 20)
print(netbook_1)
print(netbook_1.sended(2, 'office_2'))

