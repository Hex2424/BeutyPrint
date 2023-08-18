
from colorama import Fore, Back, Style
from copy import deepcopy

LEFT = 0
RIGHT = 1
CENTER = 2
LEFT_AUTO = 3
RIGHT_AUTO = 4
CENTER_AUTO = 5

class BeutySpan():
    def __init__(self, color = Fore.WHITE, padding : int= 0, padStyle : int = RIGHT, bgColor= '', style :str = '', l_sep : str= '[ ', r_sep: str = ' ]', sepColor:str = Fore.WHITE, postProccessor = None):
        self.textColor = color
        self.textPadding = padding
        self.textPaddingDirection = padStyle
        self.textBackgroundColor = bgColor
        self.textStyle = style
        self.l_sep = l_sep
        self.r_sep = r_sep
        self.seperatorColor = sepColor
        self.postProcessor = postProccessor

class BeutyPrint():

    def __init__(self, format: list[BeutySpan] = [BeutySpan()], defaultSpan:BeutySpan = BeutySpan()):

        self.formatRules = format
        self.defaultSpan = defaultSpan

    def getFormatted(self, format: list[BeutySpan], messagesList : list):
        formattedString = ''
        formatIdx = 0

        for msg in messagesList:
            if formatIdx >= len(format):
                formatIdx = 0

            selectedSpan = deepcopy(format[formatIdx])

            if selectedSpan.postProcessor != None:
                (msg, span) = selectedSpan.postProcessor(msg, selectedSpan)
            else:
                span = selectedSpan

            formattedString += f"{span.seperatorColor}{span.l_sep}{span.textColor}{span.textBackgroundColor}{span.textStyle}"
            
            if span.textPaddingDirection == RIGHT:
                formattedString += f"{str(msg) :<{span.textPadding}}"
            elif span.textPaddingDirection == LEFT:
                formattedString += f"{str(msg) :>{span.textPadding}}"
            else:
                formattedString += f"{str(msg).center(span.textPadding)}"
            
            formattedString += f"{Style.RESET_ALL}{span.seperatorColor}{span.r_sep}"
            formatIdx += 1

        return formattedString

    def printUsingFormat(self, format: list[BeutySpan], messagesList : list, end = '\n'):
        print(self.getFormatted(format, messagesList), end=end)
    

    def print(self, messagesList : list, end='\n'):
        if type(messagesList) == str:
            self.printUsingFormat(self.formatRules, [messagesList], end)
        else:
            self.printUsingFormat(self.formatRules, messagesList, end)

    