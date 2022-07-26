class Storage:
    pass


class OfficeEquip(Storage):
    name = "Плотва!"  # переменная для всех классов. значение неважно. просто непустое строковое значение))

    def __init__(self, d_model, d_year, amount):
        self.d_model = d_model
        self.d_year = d_year
        self.amount = amount
        self.num_office = {'office_1': 0, 'office_2': 0}

    def __str__(self):
        return f"на складе {self.amount} {self.name}"

    def sended(self, send, office):
        if str(send).isdigit() and self.amount >= send:
            self.amount -= send
            self.num_office[office] += send
            return f'на складе {self.amount} принтеров в офисе {office} {self.num_office[office]} {self.name}'
        else:
            return f'we cant'


class Printers(OfficeEquip):
    name = "принтеров"

    def __init__(self, cartridge, wireless, d_model, d_year, amount):
        super().__init__(d_model, d_year, amount)
        self.cartridge = cartridge
        self.wireless = wireless


class Netbooks(OfficeEquip):
    name = "нетбуков"

    def __init__(self, bat_mah, screen_inches, d_model, d_year, amount):
        super().__init__(d_model, d_year, amount)
        self.bat_mah = bat_mah
        self.screen_inches = screen_inches


class Scanners(OfficeEquip):
    name = "сканеров"

    def __init__(self, doc_format, d_model, d_year, amount):
        super().__init__(d_model, d_year, amount)
        self.doc_format = doc_format


printer_1 = Printers('laser', 'yes', 1100, 2022, 10)
print(printer_1)
print(printer_1.sended(10, 'office_1'))
netbook_1 = Netbooks(5000, 15, '1500super', 2022, 20)
print(netbook_1)
print(netbook_1.sended(2, 'office_2'))
scanner_1 = Scanners('A3', 'max15', 2022, 7)
print(scanner_1)
print(scanner_1.sended(3, 'office_1'))
print(printer_1.num_office)
print(netbook_1.num_office)
print(scanner_1.num_office)
