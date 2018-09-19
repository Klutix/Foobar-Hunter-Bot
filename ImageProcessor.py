from PIL import Image
import webcolors

class ImageProcessor(object):

    def __init__(self,image):
        global pix
        im = Image.open(image) #Can be many different formats.
        self.pix = im.load()
        self.width, self.height = im.size
                 
        self.red    = "crimson"
        self.yellow = "darkorange"
        self.blue   = "lightseagreen"
        self.black  = "black"
        self.grey   = "darkslategrey"

        self.redBool   = False
        self.yellBool  = False
        self.blueBool  = False
        self.blackBool = False
        self.greyBool  = False
        
    def _closest_colour(self,requested_colour): #https://stackoverflow.com/questions/9694165/convert-rgb-color-to-english-color-name-like-green
        min_colours = {}
        for key, name in webcolors.css3_hex_to_names.items():
            r_c, g_c, b_c = webcolors.hex_to_rgb(key)
            rd = (r_c - requested_colour[0]) ** 2
            gd = (g_c - requested_colour[1]) ** 2
            bd = (b_c - requested_colour[2]) ** 2
            min_colours[(rd + gd + bd)] = name
        return min_colours[min(min_colours.keys())]

    
    def _CheckForPixels(self,Color):

        if Color == self.red and not self.redBool:
            self.redBool   = True
            print("..red")    #uncomment for debug
        elif Color == self.yellow and not self.yellBool:
            self.yellBool  = True
            print("..yellow") #uncomment for debug
        elif Color == self.blue and not self.blueBool:
            self.blueBool  = True
            print("..blue")   #uncomment for debug
        elif Color == self.black and not self.blackBool:
            print("..black")  #uncomment for debug
            self.blackBool = True
        elif Color == self.grey and not self.greyBool:
            print("..grey")   #uncomment for debug
            self.greyBool  = True
            
        
    def isMatch(self):
        if self.redBool and self.yellBool and self.blueBool and self.blackBool and self.greyBool:
            return True
        return False

    def process(self):            
        rgbAlreadyProcessed = []
        for h in range(1,self.height,10):
            if self.isMatch():
                        break
            for w in range(1,self.width,10):
                color = self.pix[w,h]
                if color not in rgbAlreadyProcessed:
                    rgbAlreadyProcessed.append(color)
                    color = self._closest_colour(color)
                    self._CheckForPixels(color)
                    if self.isMatch():
                        break

