#-----------------------------------------------------------------------------#
# BALTZ ALGORITHMIC GENERATOR OF SPECTRA (BAGS)
#
# Written during an all-night one-person hackathon on February 23 during mission
# Silver Seas 2018
#
# Change the proportions in the section below
#-----------------------------------------------------------------------------#

from PIL import Image as image
from PIL import ImageDraw as draw


#-----------------------------------------------------------------------------#
# User-selected settings: specify your compound in this section
#-----------------------------------------------------------------------------#
# Here the simulators should input exactly what proportions of each element the
#   compound they have in mind contains. Each number enetered must be an integer
#   and for practical reasons the maximum proportion is (unfortunately) capped
#   at 10, although this can be changed by altering the maxThickness value.
#So, for example, if I want to simulate pure hydrogen, I will put 1 for hydrogen
#   and 0 for every other value in the proportions list. If I want to simulate
#   CH4, I will put a 4 in the index corresponding to hydrogen, a 1 in the 
#   index corresponding to carbon, and a 0 everywhere else

changedElems = ["hydrogen", "helium", "carbon", "oxygen"]
proportions = [1, 1, 1, 1]

maxThickness = 10


#-----------------------------------------------------------------------------#
#Invariant parameters
#-----------------------------------------------------------------------------#
#Please don't change these numbers because everything will certainly explode
maxColor = 255
stretchFactor = 1
wavelengths = maxColor
#Extreme magic numbers are unfortunately necessary (at this time of night)
#   to make the spectrum look right while maintaining a unique mapping of
#   values to lines in the image
imWidth = int(maxColor*float(5)/float(3)*3)
blueLoc = float(1)/float(5)*imWidth
greenBlueLoc = float(2)/float(5)*imWidth
greenLoc = float(3)/float(5)*imWidth
redGreenLoc = float(4)/float(5)*imWidth
imHeight = 100

#First we need to construct a massive dictionary which sets 
#    every element's value, so that we can easily set values for any element
elements =                                                                     \
    {"hydrogen": 0, "helium": 0, "lithium": 0, "beryllium": 0, "boron": 0,     \
    "carbon": 0, "nitrogen": 0, "oxygen": 0, "fluorine": 0, "neon": 0,         \
    "sodium": 0, "magnesium": 0, "aluminum": 0, "silicon": 0,                  \
    "phosphorus": 0, "sulfur": 0, "chlorine": 0, "argon": 0, "potassium": 0,   \
    "calcium": 0, "scandium": 0, "titanium": 0, "vanadium": 0, "chromium": 0,  \
    "manganese": 0, "iron": 0, "cobalt": 0, "nickel": 0, "copper": 0,          \
    "zinc": 0, "gallium": 0, "germanium": 0, "arsenic": 0, "selenium": 0,      \
    "bromine": 0, "krypton": 0, "rubidium": 0, "strontium": 0, "yttrium": 0,   \
    "zirconium": 0, "niobium": 0, "molybdenum": 0, "technetium": 0,            \
    "ruthenium": 0, "rhodium": 0, "palladium": 0, "silver": 0, "cadmium": 0,   \
    "indium": 0, "tin": 0, "antimony": 0, "tellurium": 0, "iodine": 0,         \
    "xenon": 0, "cesium": 0, "barium": 0, "lanthanum": 0, "cerium": 0,         \
    "praseodymium": 0, "neodymium": 0, "promethium": 0, "samarium": 0,         \
    "europium": 0, "gadolinium": 0, "terbium": 0, "dysprosium": 0,             \
    "holmium": 0, "erbium": 0, "thulium": 0, "ytterbium": 0, "lutetium": 0,    \
    "hafnium": 0, "tantalum": 0, "tungsten": 0, "rhenium": 0, "osmium": 0,     \
    "iridium": 0, "platinum": 0, "gold": 0, "mercury": 0, "thallium": 0,       \
    "lead": 0, "bismuth": 0, "polonium": 0, "astatine": 0, "radon": 0,         \
    "francium": 0, "radium": 0, "actinium": 0, "thorium": 0, "protactinium": 0 \
    ,"uranium": 0, "neptunium": 0, "plutonium": 0, "americium": 0, "curium": 0 \
    ,"berkelium": 0, "californium": 0, "einsteinium": 0, "fermium": 0,         \
    "mendelevium": 0, "nobelium": 0, "lawrencium": 0, "rutherfordium": 0,      \
    "dubnium": 0, "seaborgium": 0, "bohrium": 0, "hassium": 0, "meitnerium": 0 \
    ,"darmstadtium": 0, "roentgenium": 0, "copernicium": 0, "nihonium": 0,     \
    "flerovium": 0, "moscovium": 0, "livermorium": 0, "tennessine": 0,         \
    "oganesson": 0}


#Construct the spectrum mapping dictionary so that each line in the image has a
#   unique colour associated with it
spectrum = image.new("RGB", (imWidth, imHeight), "black")
lineMaps = {}

spectDraw = draw.Draw(spectrum)

#Start the spectrum out at purple, as is conventional
blue = int(maxColor)
red = int(maxColor)
green = 0

for inc in range(0,imWidth):
    spectDraw.line([(inc,0),(inc,imHeight)],fill=(red,green,blue),width=1)
    if inc < blueLoc:
        if red > 0:
            red -= stretchFactor
    if inc > blueLoc and inc < greenBlueLoc:
        if green < maxColor:
            green += stretchFactor
    if inc > greenBlueLoc and inc < greenLoc:
        if blue > 0:
            blue -= stretchFactor
    if inc > greenLoc and inc < redGreenLoc:
        if red < maxColor:
            red += stretchFactor
    if inc > redGreenLoc:
        if green > 0:
            green -= stretchFactor
    lineMaps[inc] = [(red,green,blue)]


#Draw the default black background image on which we will draw and print the
#   Spectrograph output
compound = image.new("RGB", (imWidth, imHeight), "black")
drawComp = draw.Draw(compound)

for elemIndex in range(0,len(changedElems)):
    elements[changedElems[elemIndex]] = proportions[elemIndex]


#ALL OF THESE ARE MAGIC NUMBERS BECAUSE THIS IS MY PRIVATE HACKATHON PROJECT AND
#   I'LL HOLD IT TOGETHER WITH DUCT TAPE IF I WANT TO (Also how else would you do it)
if elements["hydrogen"] != 0:
    hydrogenPos1 = 1180
    thickness1 = 3*elements["hydrogen"]
    if thickness1 > maxThickness:
        thickness1 = maxThickness
    drawComp.line([(hydrogenPos1,0),(hydrogenPos1,imHeight)],fill=lineMaps[hydrogenPos1][0],width=thickness1)
    hydrogenPos2 = 450
    thickness2 = 5*elements["hydrogen"]
    if thickness2 > maxThickness:
        thickness2 = maxThickness
    drawComp.line([(hydrogenPos2,0),(hydrogenPos2,imHeight)],fill=lineMaps[hydrogenPos2][0],width=thickness2)
    hydrogenPos3 = 200
    thickness3 = 2*elements["hydrogen"]
    if thickness3 > maxThickness:
        thickness3 = maxThickness
    drawComp.line([(hydrogenPos3,0),(hydrogenPos3,imHeight)],fill=lineMaps[hydrogenPos3][0],width=thickness3)
    hydrogenPos4 = 130
    thickness4 = 2*elements["hydrogen"]
    if thickness4 > maxThickness:
        thickness4 = maxThickness
    drawComp.line([(hydrogenPos4,0),(hydrogenPos4,imHeight)],fill=lineMaps[hydrogenPos4][0],width=thickness4)

if elements["helium"] != 0:
    heliumPos1 = 1200
    thickness1 = 1*elements["helium"]
    if thickness1 > maxThickness:
        thickness1 = maxThickness
    drawComp.line([(heliumPos1,0),(heliumPos1,imHeight)],fill=lineMaps[heliumPos1][0],width=thickness1)
    heliumPos2 = 1025
    thickness2 = 5*elements["helium"]
    if thickness2 > maxThickness:
        thickness2 = maxThickness     
    drawComp.line([(heliumPos2,0),(heliumPos2,imHeight)],fill=lineMaps[heliumPos2][0],width=thickness2)
    heliumPos3 = 650
    thickness3 = 4*elements["helium"]
    if thickness3 > maxThickness:
        thickness3 = maxThickness    
    drawComp.line([(heliumPos3,0),(heliumPos3,imHeight)],fill=lineMaps[heliumPos3][0],width=thickness3)
    heliumPos4 = 600
    thickness4 = 1*elements["helium"]
    if thickness4 > maxThickness:
        thickness4 = maxThickness    
    drawComp.line([(heliumPos4,0),(heliumPos4,imHeight)],fill=lineMaps[heliumPos4][0],width=thickness4)
    heliumPos5 = 400
    thickness5 = 1*elements["helium"]
    if thickness5 > maxThickness:
        thickness5 = maxThickness    
    drawComp.line([(heliumPos5,0),(heliumPos5,imHeight)],fill=lineMaps[heliumPos5][0],width=thickness5)
    heliumPos6 = 380
    thickness6 = 1*elements["helium"]
    if thickness6 > maxThickness:
        thickness6 = maxThickness    
    drawComp.line([(heliumPos6,0),(heliumPos6,imHeight)],fill=lineMaps[heliumPos6][0],width=thickness6)
    heliumPos7 = 300
    thickness7 = 2*elements["helium"]
    if thickness7 > maxThickness:
        thickness7 = maxThickness    
    drawComp.line([(heliumPos7,0),(heliumPos7,imHeight)],fill=lineMaps[heliumPos7][0],width=thickness7)
    heliumPos8 = 45
    thickness8 = 2*elements["helium"]
    if thickness8 > maxThickness:
        thickness8 = maxThickness    
    drawComp.line([(heliumPos8,0),(heliumPos8,imHeight)],fill=lineMaps[heliumPos8][0],width=thickness8)


if elements["carbon"] != 0:
    carbonPos1 = 70
    thickness1 = 1*elements["carbon"]
    if thickness1 > maxThickness:
        thickness1 = maxThickness
    drawComp.line([(carbonPos1,0),(carbonPos1,imHeight)],fill=lineMaps[carbonPos1][0],width=thickness1)
    carbonPos2 = 100
    thickness2 = 1*elements["carbon"]
    if thickness2 > maxThickness:
        thickness2 = maxThickness
    drawComp.line([(carbonPos2,0),(carbonPos2,imHeight)],fill=lineMaps[carbonPos2][0],width=thickness2)
    carbonPos3 = 425
    thickness3 = 1*elements["carbon"]
    if thickness3 > maxThickness:
        thickness3 = maxThickness
    drawComp.line([(carbonPos3,0),(carbonPos3,imHeight)],fill=lineMaps[carbonPos3][0],width=thickness3)
    carbonPos4 = 602
    thickness4 = 1*elements["carbon"]
    if thickness4 > maxThickness:
        thickness4 = maxThickness    
    drawComp.line([(carbonPos4,0),(carbonPos4,imHeight)],fill=lineMaps[carbonPos4][0],width=thickness4)
    carbonPos5 = 660
    thickness5 = 1*elements["carbon"]
    if thickness5 > maxThickness:
        thickness5 = maxThickness    
    drawComp.line([(carbonPos5,0),(carbonPos5,imHeight)],fill=lineMaps[carbonPos5][0],width=thickness5)
    carbonPos6 = 685
    thickness6 = 4*elements["carbon"]
    if thickness6 > maxThickness:
        thickness6 = maxThickness    
    drawComp.line([(carbonPos6,0),(carbonPos6,imHeight)],fill=lineMaps[carbonPos6][0],width=thickness6)
    carbonPos7 = 840
    thickness7 = 1*elements["carbon"]
    if thickness7 > maxThickness:
        thickness7 = maxThickness    
    drawComp.line([(carbonPos7,0),(carbonPos7,imHeight)],fill=lineMaps[carbonPos7][0],width=thickness7)
    carbonPos8 = 940
    thickness8 = 4*elements["carbon"]
    if thickness8 > maxThickness:
        thickness8 = maxThickness    
    drawComp.line([(carbonPos8,0),(carbonPos8,imHeight)],fill=lineMaps[carbonPos8][0],width=thickness8)
    carbonPos9 = 1035
    thickness9 = 1*elements["carbon"]
    if thickness9 > maxThickness:
        thickness9 = maxThickness    
    drawComp.line([(carbonPos9,0),(carbonPos9,imHeight)],fill=lineMaps[carbonPos9][0],width=thickness9)
    carbonPos10 = 1090
    thickness10 = 3*elements["carbon"]
    if thickness10 > maxThickness:
        thickness10 = maxThickness
    drawComp.line([(carbonPos10,0),(carbonPos10,imHeight)],fill=lineMaps[carbonPos10][0],width=thickness10)
    carbonPos11 = 1190
    thickness11 = 3*elements["carbon"]
    if thickness11 > maxThickness:
        thickness11 = maxThickness
    drawComp.line([(carbonPos11,0),(carbonPos11,imHeight)],fill=lineMaps[carbonPos11][0],width=thickness11)
    carbonPos12 = 1230
    thickness12 = 1*elements["carbon"]
    if thickness12 > maxThickness:
        thickness12 = maxThickness
    drawComp.line([(carbonPos12,0),(carbonPos12,imHeight)],fill=lineMaps[carbonPos12][0],width=thickness12)

if elements["oxygen"] != 0:
    oxygenPos1 = 10
    thickness1 = 2*elements["oxygen"]
    if thickness1 > maxThickness:
        thickness1 = maxThickness
    drawComp.line([(oxygenPos1,0),(oxygenPos1,imHeight)],fill=lineMaps[oxygenPos1][0],width=thickness1)
    oxygenPos2 = 72
    thickness2 = 2*elements["oxygen"]
    if thickness2 > maxThickness:
        thickness2 = maxThickness
    drawComp.line([(oxygenPos2,0),(oxygenPos2,imHeight)],fill=lineMaps[oxygenPos2][0],width=thickness2)
    oxygenPos3 = 73
    thickness3 = 1*elements["oxygen"]
    if thickness3 > maxThickness:
        thickness3 = maxThickness
    drawComp.line([(oxygenPos3,0),(oxygenPos3,imHeight)],fill=lineMaps[oxygenPos3][0],width=thickness3)
    oxygenPos4 = 77
    thickness4 = 1*elements["oxygen"]
    if thickness4 > maxThickness:
        thickness4 = maxThickness
    drawComp.line([(oxygenPos4,0),(oxygenPos4,imHeight)],fill=lineMaps[oxygenPos4][0],width=thickness4)
    oxygenPos5 = 83
    thickness5 = 1*elements["oxygen"]
    if thickness5 > maxThickness:
        thickness5 = maxThickness
    drawComp.line([(oxygenPos5,0),(oxygenPos5,imHeight)],fill=lineMaps[oxygenPos5][0],width=thickness5)
    oxygenPos6 = 90
    thickness6 = 1*elements["oxygen"]
    if thickness6 > maxThickness:
        thickness6 = maxThickness
    drawComp.line([(oxygenPos6,0),(oxygenPos6,imHeight)],fill=lineMaps[oxygenPos6][0],width=thickness6)
    oxygenPos7 = 103
    thickness7 = 2*elements["oxygen"]
    if thickness7 > maxThickness:
        thickness7 = maxThickness
    drawComp.line([(oxygenPos7,0),(oxygenPos7,imHeight)],fill=lineMaps[oxygenPos7][0],width=thickness7)
    oxygenPos8 = 150
    thickness8 = 1*elements["oxygen"]
    if thickness8 > maxThickness:
        thickness8 = maxThickness
    drawComp.line([(oxygenPos8,0),(oxygenPos8,imHeight)],fill=lineMaps[oxygenPos8][0],width=thickness8)
    oxygenPos9 = 170
    thickness9 = 1*elements["oxygen"]
    if thickness9 > maxThickness:
        thickness9 = maxThickness
    drawComp.line([(oxygenPos9,0),(oxygenPos9,imHeight)],fill=lineMaps[oxygenPos9][0],width=thickness9)
    oxygenPos10 = 180
    thickness10 = 1*elements["oxygen"]
    if thickness10 > maxThickness:
        thickness10 = maxThickness
    drawComp.line([(oxygenPos10,0),(oxygenPos10,imHeight)],fill=lineMaps[oxygenPos10][0],width=thickness10)
    oxygenPos11 = 200
    thickness11 = 1*elements["oxygen"]
    if thickness11 > maxThickness:
        thickness11 = maxThickness
    drawComp.line([(oxygenPos11,0),(oxygenPos11,imHeight)],fill=lineMaps[oxygenPos11][0],width=thickness11)
    oxygenPos12 = 210
    thickness12 = 1*elements["oxygen"]
    if thickness12 > maxThickness:
        thickness12 = maxThickness
    drawComp.line([(oxygenPos12,0),(oxygenPos12,imHeight)],fill=lineMaps[oxygenPos12][0],width=thickness12)
    oxygenPos13 = 350
    thickness13 = 1*elements["oxygen"]
    if thickness13 > maxThickness:
        thickness13 = maxThickness    
    drawComp.line([(oxygenPos13,0),(oxygenPos13,imHeight)],fill=lineMaps[oxygenPos13][0],width=thickness13)
    oxygenPos14 = 355
    thickness14 = 1*elements["oxygen"]
    if thickness14 > maxThickness:
        thickness14 = maxThickness    
    drawComp.line([(oxygenPos14,0),(oxygenPos14,imHeight)],fill=lineMaps[oxygenPos14][0],width=thickness14)
    oxygenPos15 = 365
    thickness15 = 1*elements["oxygen"]
    if thickness15 > maxThickness:
        thickness15 = maxThickness
    drawComp.line([(oxygenPos15,0),(oxygenPos15,imHeight)],fill=lineMaps[oxygenPos15][0],width=thickness15)
    oxygenPos16 = 375
    thickness16 = 1*elements["oxygen"]
    if thickness16 > maxThickness:
        thickness16 = maxThickness
    drawComp.line([(oxygenPos16,0),(oxygenPos16,imHeight)],fill=lineMaps[oxygenPos16][0],width=thickness16)
    oxygenPos17 = 380
    thickness17 = 1*elements["oxygen"]
    if thickness17 > maxThickness:
        thickness17 = maxThickness
    drawComp.line([(oxygenPos17,0),(oxygenPos17,imHeight)],fill=lineMaps[oxygenPos17][0],width=thickness17)
    oxygenPos18 = 590
    thickness18 = 1*elements["oxygen"]
    if thickness18 > maxThickness:
        thickness18 = maxThickness
    drawComp.line([(oxygenPos18,0),(oxygenPos18,imHeight)],fill=lineMaps[oxygenPos18][0],width=thickness18)
    oxygenPos19 = 615
    thickness19 = 1*elements["oxygen"]
    if thickness19 > maxThickness:
        thickness19 = maxThickness
    drawComp.line([(oxygenPos19,0),(oxygenPos19,imHeight)],fill=lineMaps[oxygenPos19][0],width=thickness19)
    oxygenPos20 = 1060
    thickness20 = 1*elements["oxygen"]
    if thickness20 > maxThickness:
        thickness20 = maxThickness
    drawComp.line([(oxygenPos20,0),(oxygenPos20,imHeight)],fill=lineMaps[oxygenPos20][0],width=thickness20)
    oxygenPos21 = 1100
    thickness21 = 1*elements["oxygen"]
    if thickness21 > maxThickness:
        thickness21 = maxThickness
    drawComp.line([(oxygenPos21,0),(oxygenPos21,imHeight)],fill=lineMaps[oxygenPos21][0],width=thickness21)
    oxygenPos22 = 1130
    thickness22 = 1*elements["oxygen"]
    if thickness22 > maxThickness:
        thickness22 = maxThickness
    drawComp.line([(oxygenPos22,0),(oxygenPos22,imHeight)],fill=lineMaps[oxygenPos22][0],width=thickness22)
    oxygenPos23 = 1175
    thickness23 = 2*elements["oxygen"]
    if thickness23 > maxThickness:
        thickness23 = maxThickness
    drawComp.line([(oxygenPos23,0),(oxygenPos23,imHeight)],fill=lineMaps[oxygenPos23][0],width=thickness23)


#-----------------------------------------------------------------------------#
#Saving function: enter the names you'd like to save and uncomment
# If you are using an IDE you may also be able to view the image in console
#-----------------------------------------------------------------------------#
#spectrum.save("spectrum.PNG")
#compound.save("COMPOUNDNAME.PNG")
