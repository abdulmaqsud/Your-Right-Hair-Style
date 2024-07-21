import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

#Hello dear, in order to find your right Hairstyle, you just need to click the run botton and answer some questions.

def greeding():
    #It Starts from here by greeding and telling what we are going to do.
    print("Hello")
    print("Good to see you here.")
    print("let's find out what is the Best Hairstyle for you!")
    return askingTheyKnowFaceShape()


def askingTheyKnowFaceShape():
    #It asks whether they know their face shape or not and based on their answer it takes further actions and if user enters something else than what is asked it recalls itselfe.
    KnowingFaceShape = input("Do you know what is your face shape(Yes/No): ")
    if KnowingFaceShape.lower() == "yes":
        return askingHairStyleYesNo()
    elif KnowingFaceShape.lower() == "no":
        return toStarMeasuringFace()
    else:
        printToWriteCorrectly()
        return askingTheyKnowFaceShape()
    

def printToWriteCorrectly():
    #It is called to just print out that there is some incorrect spelling.
    print("I want you to spell it correctly, Please.")


def askingHairStyleYesNo():
    #It asks whether they want to see some hairstyle or not and based on their answer it takes further actions and if user enters something else than what is asked it recalls itselfe.
    WantingHairstyle = input("Do you want to see some Hairstyle based on your Face Shape(Yes/No): ")
    if WantingHairstyle.lower() == "yes":
        return askingfacseShape()
    elif WantingHairstyle.lower() == "no":
        print("Sure, Have a good time, See you back!")
    else:
        printToWriteCorrectly()
        return askingHairStyleYesNo()
    
    
def askingfacseShape():
    #It asks their face shape
    faceShape = input("Enter your Face Shape then(Oval|Square|Rectangle|Round|Diamond|Heart|Triangle): ")
    return hairStyleOptions(faceShape)


def hairStyleOptions(faceShape):
    #It sees what is the entered face shape and base on that offers some hairstyle to choose from and if user enters something else than what is asked it recalls itselfe.
    faceShape = faceShape.lower()
    if faceShape == "oval":
        hairStyle = input("Choose a Hairstyle to see (Quiff|Slick Back|Buzz Cut): ")
    elif faceShape == "triangle":
        hairStyle = input("Choose a Hairstyle to see (Longer Crew Cut|Textured Spikes|Quiff): ")
    elif faceShape == "rectangle":
        hairStyle = input("Choose a Hairstyle to see (Fringes|Swept Back Quiff|Messy Natural Look): ")
    elif faceShape == "round":
        hairStyle = input("Choose a Hairstyle to see (Spiky Hair|Messy Waves|Side part): ")
    elif faceShape == "diamond":
        hairStyle = input("Choose a Hairstyle to see (Long Sweeping Fringe|Textured Crop|Long Bob): ")
    elif faceShape == "heart":
        hairStyle = input("Choose a Hairstyle to see (Shoulder Lenght|Fringes Sideswept|Slick Back): ")
    elif faceShape == "square":
        hairStyle = input("Choose a Hairstyle to see (Buzz Cut|Modern Flat Top|Quiff): ")
    else:
        printToWriteCorrectly()
        return askingfacseShape()
    return showHairStyle(hairStyle, faceShape)


def showHairStyle(hairstyleName, faceShape):
    #It sees if the passed hairstyle exist in the "images" folder, if it does exist it shows it and if it does not exist it asks to type it correctly!
    directoryOfImagesName = "images"
    hairStyleFound = False
    for i in os.listdir(directoryOfImagesName):
        if i.lower().startswith(hairstyleName.lower()) and i.lower().endswith(".png"):
            hairStyleFound = True
            hairstyleNamePNG = os.path.join(directoryOfImagesName, i)
            break

    if not hairStyleFound:
        printToWriteCorrectly()
        return hairStyleOptions(faceShape)
    
    plt.ion()
    image = mpimg.imread(hairstyleNamePNG)
    changeTitle = plt.figure()
    changeTitle.canvas.manager.set_window_title("The Chosen Hair Style")
    plt.imshow(image)
    plt.axis("off")
    plt.show()

    return ifContinue1(faceShape)

    
def ifContinue1(faceShape):
    #It asks if the user wants to continue for choosing another hairstyle and if user enters something else than what is asked it recalls itselfe.
    Continue = input("Do you want to see another Hairstyle(Yes/No): ")
    if Continue.lower() == "yes":
        return hairStyleOptions(faceShape)
    elif Continue.lower() == "no":
        return ifContinue2()
    else:
        printToWriteCorrectly()
        return ifContinue1(faceShape)
    

def ifContinue2():
    #It asks if the user wants to continue for choosing another face shape and if user enters something else than what is asked it recalls itselfe.
    Continue = input("Do you want to see Hairstyle for another Face Shape(Yes/No): ")
    if Continue.lower() == "yes":
        return askingfacseShape()
    elif Continue.lower() == "no":
        print("Sure, Have a good time, See you back!")
    else:
        printToWriteCorrectly()
        return ifContinue2()
    

def toStarMeasuringFace():
    #It prints the introduction part of "how to measure"
    print("Let's figure it out then!")
    print("Get a flexible Tape Measure!")
    return measuringFace()


def measuringFace():
    #It asks the forehead, cheek bones, face length, and jawline sizes with giving the instruction in how to do it.
    forehead = input("Measure from the peak of one Eyebrow Arch to the other(write it here): ")
    cheekBones = input("Measure from the pointiest part below the corner of each Eye(write it here): ")
    jawline = input("Measure from below the Ear to the top of your Chin(write it here): ")
    faceLength = input("Measure from the center of your Hairline to the tip of your Chain(write it here): ")
    print('Forehead: {} | Cheek Bones: {} | Jawline: {} | Face lenght: {}'.format(forehead, cheekBones, jawline, faceLength))
    isItCorrect()
    return askingInchOrCentimeter(forehead, cheekBones, jawline, faceLength)


def isItCorrect():
    #It aaks if the input which user passed in is correct or not and if user enters something else than what is asked it recalls itselfe.
    beingCorrect = input("Are they correct(Yes/No): ")
    if beingCorrect.lower() == "yes":
        pass
    elif beingCorrect.lower() == "no":
        print("let's try again")
        measuringFace()
    else: 
        printToWriteCorrectly()
        return isItCorrect()
    

def askingInchOrCentimeter(forehead, cheekBones, jawline, faceLength):
    #It takes the entered sizes and turn them to a list, and it goes through each of them and turns them into float and asks if the measurements were in crntimeter or in inch and if user enters something else than what is asked it recalls itselfe.
    listMeasures = [forehead, cheekBones, jawline, faceLength]
    listMeasuresFloat = []
    for i in listMeasures:
        #It catches errors that is caused by entering something else than numbers.
        try:
            i = float(i)
        except:
            print("You should have entered numbers, please try again!")
            return measuringFace()
        listMeasuresFloat.append(i)
    inOrCm = input('For more accuracy i want you to tell me which measuement did you used inch or centimeter(in/cm): ')
    if inOrCm.lower() == "in":
        return inchToCentimeter(listMeasuresFloat) 
    elif inOrCm.lower() == "cm":
        return checkPoint(listMeasuresFloat), figuringFaceShape(listMeasuresFloat)
    else:
        printToWriteCorrectly()
        return askingInchOrCentimeter(forehead, cheekBones, jawline, faceLength)
    

def inchToCentimeter(listMeasuresFloat):
    #It takes measurements in inches and turn them into centimeters.
    measuresInCentimeter = []
    for i in listMeasuresFloat:
        i = i * 2.54
        measuresInCentimeter.append(i)
        checkPoint(measuresInCentimeter)
    return figuringFaceShape(measuresInCentimeter)


def checkPoint(theList): 
    #It checks if the given sizes are between 8-28 because less or more than this might be a mistake in entering the sizes.
    for i in theList:
        if i <= 8 or i >= 30:
            print("The Entered Measures are out of limit, please try again with logical measures!")
            return measuringFace()


def almostEqual(a, b, tolerance = 1):
    #It sees if the two passed sizes are almost equal by maximum of 1 tolerance. 
    return abs(a - b) <= tolerance


def figuringFaceShape(listMeasures):
    #It sees which condition is true for the given sizes in order to find out what is the fcae shape of the user and if the given sizes do not match the conditions it apologizes and gives them another turn to try.
    forehead, cheekBones, jawline, faceLength = listMeasures
    isForeheadCheekBonesJawlineAlmostEqual = (almostEqual(forehead, cheekBones) and 
                                            almostEqual(jawline, cheekBones) and 
                                            almostEqual(forehead, jawline))
    if isForeheadCheekBonesJawlineAlmostEqual and almostEqual(forehead, faceLength):
        print("Your face shape is Square")
    elif isForeheadCheekBonesJawlineAlmostEqual and not almostEqual(faceLength, cheekBones):
        print("Your face shape is Recatngle")
    elif faceLength > cheekBones and forehead > jawline:
        print("Your face shape is Oval")
    elif cheekBones > forehead and almostEqual(faceLength, cheekBones):
        print("Your face shape is Round")
    elif faceLength > cheekBones > forehead > jawline:
        print("Your face shape is Diamond")
    elif forehead > cheekBones and almostEqual(cheekBones, jawline):
        print("Your face shape is Heart")
    elif jawline > cheekBones > forehead:
        print("Your face shape is Triangle")
    else:
        print("Unknown Shape, I apologize if it is my fault, but could you check your measurements once and Try again!")
        return ifContinue3()
    return askingHairStyleYesNo()

def ifContinue3():
    #It asks if you want to continue measuring or not after the fact that it could not find the face shape and if user enters something else than what is asked it recalls itselfe.
    Continue = input("Do you want to try again(Yes/No): ")
    if Continue.lower() == "yes":
        return measuringFace()
    elif Continue.lower() == "no":
        print("Sure, Have a good time, See you back!")
    else:
        printToWriteCorrectly()
        return ifContinue3()

greeding()