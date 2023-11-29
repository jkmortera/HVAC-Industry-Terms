import pandas as pd

parts_dict = {
    'street_name': ['Supply motor', 'Fan motor', 'Indoor motor', 
                    'Furnace motor', 'condensing fan motor', 
                    'outdoor motor', 'squirrel cage', 'supply wheel', 
                    'blade', 'combustion motor', 'draft motor', 'orifice', 
                    'piston', 'pulley', 'timer', 'fan board', 'supply motor mount',
                    'cover plate', 'hot surface ignitor', 'starter', 
                    'a coil', 'torch kit', 'drier', 'compressor wires', 'cabinets',
                    'filter box', 'packaged unit', 'spark plug', 'outdoor coil',
                    'indoor coil', 'well sensor', 'electric point', 'electric ingnitor',
                    'mastic', 'sniffer', 'pookie', 'brazing rod', 'bubbles', 'coolant',
                    'pcb', 'blue filter', 'washable filter', ],
    
    
    
    'tech_name': ['Blower motor', 'Blower motor', 'Blower motor', 
                  'Blower motor', 'Outdoor motor', 'condensing fan motor', 
                  'blower wheel', 'blower wheel', 'fan propeller', 
                  'inducer motor', 'inducer', 'piston', 'orifice', 
                  'blower or motor pulley?', 'time delay relay', 'module', 'heat exchange panel',
                  'heat exchange panel', 'ignitor (hsi)', 'hard start kit', 
                  'standard coil', 'welder', 'filter drier', 'wiring harness', 'filter cabinets',
                  'filter cabinets', 'rooftop unit', 'ignitor', 'condenser coil',
                  'evaporator coil', 'thermistor', 'hall effect', 'hall effect',
                  'sealant', 'leak detector', 'sealant', 'solder', 'leak detector', 'refrigerant',
                  'printed circuit board', 'fiter media', 'filter media' ]
}

def street_name_lookup(dictionary, street_term):
    for index, term in enumerate(dictionary['street_name']):
        if street_term.lower() == term.lower():
            return dictionary['tech_name'][index]
    return None

street_input = input("Enter a part name: ")
result = street_name_lookup(parts_dict, street_input)

while True:
    street_input = input("Enter a street name: ")
    tech_name = street_input
    
    if tech_name:
        print(f"{street_input} is can be found under: {tech_name}.")
        break
    else:
        print(f"{street_input} not found.")