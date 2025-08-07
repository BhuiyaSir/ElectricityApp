from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# Tariff constants
RATE_1 = 4.63
RATE_2 = 5.26
RATE_3 = 7.20
RATE_4 = 7.59
RATE_5 = 8.02
RATE_6 = 12.67
RATE_7 = 14.61
DemandCharge = 168
MeterRent = 40
VAT = 0.047
Rebate = 0.0047

def calculate_cost_per_unit(unit):
    unit = float(unit)
    if unit <= 50:
        charge = unit * RATE_1
    elif unit <= 75:
        charge = unit * RATE_2
    elif unit <= 200:
        charge = 75 * RATE_2 + (unit - 75) * RATE_3
    elif unit <= 300:
        charge = 75 * RATE_2 + 125 * RATE_3 + (unit - 200) * RATE_4
    elif unit <= 400:
        charge = 75 * RATE_2 + 125 * RATE_3 + 100 * RATE_4 + (unit - 300) * RATE_5
    elif unit <= 600:
        charge = 75 * RATE_2 + 125 * RATE_3 + 100 * RATE_4 + 100 * RATE_5 + (unit - 400) * RATE_6
    else:
        charge = 75 * RATE_2 + 125 * RATE_3 + 100 * RATE_4 + 100 * RATE_5 + 200 * RATE_6 + (unit - 600) * RATE_7

    NetCharge = charge + DemandCharge + MeterRent + (charge * VAT) - (charge * Rebate)
    return charge, NetCharge

class ElectricityCalculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.input = TextInput(hint_text='Enter unit', multiline=False, input_filter='int')
        self.add_widget(self.input)

        self.button = Button(text='Calculate')
        self.button.bind(on_press=self.calculate)
        self.add_widget(self.button)

        self.output = Label(text='')
        self.add_widget(self.output)

    def calculate(self, instance):
        try:
            unit = self.input.text
            charge, net = calculate_cost_per_unit(unit)
            self.output.text = f"Base Charge: {charge:.2f}\nTotal Cost: {net:.2f}"
        except:
            self.output.text = "Invalid input"

class CalculatorApp(App):
    def build(self):
        return ElectricityCalculator()

if __name__ == '__main__':
    CalculatorApp().run()
