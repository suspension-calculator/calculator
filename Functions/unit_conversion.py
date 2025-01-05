def in2mm(value):
    # Conversion from inches to millimeters if global units is set to metric
    value=value*25.4
    return(value)

def mm2in(value):
    # Conversion from millimeters to inches if global units is set to metric
    value=value/25.4
    return(value)

def kg2lb(value):
    # Conversion from kilograms to pounds if global units is set to metric
    value=value*2.20462
    return(value)

def lb2kg(value):
    # Conversion from pounds to kilograms if global units is set to metric
    value=value/2.20462
    return(value)

def kmh2mph(value):
    # Conversion from kilometers per hour to miles per hour if global units is set to metric
    value=value*0.621371
    return(value)

def mph2kmh(value):
    # Conversion from miles per hour to kilometers per hour if global units is set to metric
    value=value/0.621371
    return(value)

def npmm2lbpin(value):
    # Conversion from newtons per millimeters to pounds per inch if global units is set to metric
    value=value*5.7101471627692
    return(value)

def lbpin2npmm(value):
    # Conversion from pounds per inch to newtons per millimeters if global units is set to metric
    value=value/5.7101471627692
    return(value)

def lb2N(value):
    # Conversion from pounds per inch to newtons per millimeters if global units is set to metric
    value=value*4.4482216
    return(value)