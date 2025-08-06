from pymeasure.instruments import Instrument
from pymeasure.instruments.validators import truncated_range

class Fluke5522A(Instrument):
    def __init__(self, adapter, **kwargs):
        super().__init__(
            adapter,
            "Fluke 5522A Multifunction Calibrator",
            includeSCPI=False,
            **kwargs
        )

    @property
    def id(self):
        """ Zwraca identyfikator urządzenia """
        return self.ask("*IDN?")

    def standby(self):
        """ Przechodzi w tryb STANDBY """
        self.write("STBY")

    def operate(self):
        """ Przechodzi w tryb OPERATE (włącza wyjście) """
        self.write("OPER")

    def output_current(self, value_A, frequency_Hz=0):
        self.write("*RST")
        """ Ustawia prąd DC lub AC w amperach """
        value = truncated_range(value_A, (0, 20.5))
        if frequency_Hz and frequency_Hz > 0:
            freq = truncated_range(frequency_Hz, (10, 30000))
            self.write(f"OUT {value:.6f} A, {freq:.1f} HZ")
            self.write("*WAI")  # upewnia się, że poprzednie polecenia się wykonały
        else:
            self.write(f"OUT {value:.6f} A, 0 HZ")
            self.write("*WAI")  # upewnia się, że poprzednie polecenia się wykonały

    def output_voltage(self, value_V, frequency_Hz=0):
        """ Ustawia napięcie DC lub AC w woltach """
        value = truncated_range(value_V, (0, 1020))

        if frequency_Hz and frequency_Hz > 0:
            freq = truncated_range(frequency_Hz, (10, 300000))
            self.write(f"OUT {value:.6f} V, {freq:.1f} HZ")
            self.write("*WAI")  # upewnia się, że poprzednie polecenia się wykonały
        else:
            # jawne nadpisanie poprzedniej częstotliwości i trybu
            #self.write("DCV")
            self.write(f"OUT {value:.6f} V, 0 HZ")
            self.write("*WAI")  # upewnia się, że poprzednie polecenia się wykonały



