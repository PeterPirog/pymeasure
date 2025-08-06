from pymeasure.instruments.fluke.fluke5522a import Fluke5522A

instr = Fluke5522A("GPIB::5")

print("ID:", instr.id)

instr.standby()
#instr.output_current(0.1)
instr.output_current(0.2, 20)
#instr.output_voltage(5,10)
#instr.output_voltage(4,10)
#instr.output_voltage(5)
instr.operate()
