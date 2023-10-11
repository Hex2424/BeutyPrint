from beutyprint import *

# printer = BeutyPrint([BeutySpan(
#     textColor=Fore.CYAN
# )])
def proc(msg, span):
    if msg == "ON":
        span.textColor = Fore.GREEN
    elif msg == "OFF":
        span.textColor = Fore.RED  
    return (msg, span)

# printer = BeutyPrint([
#     BeutySpan(
#     color = Fore.BLUE,
#     padding = 10,
#     padStyle = CENTER,
#     sepColor = Fore.GREEN,
#     l_sep = f' ',
#     r_sep = ' <-]]',
#   ),
#    BeutySpan(
#     color = Fore.YELLOW,
#     padding = 10,
#     padStyle = CENTER,
#     sepColor = Fore.BLACK,
#     # style= Style.BRIGHT,
#     l_sep = '[[-> ',
#     r_sep = ' <-]]',
#   ),
#    BeutySpan(
#     color = Fore.CYAN,
#     padStyle = CENTER,
#     style= Style.BRIGHT,
#     l_sep = '[[-> ',
#     r_sep = ' <-]]\n',
#     postProccessor=proc
#   )
# ])
printer = BeutyPrint([])
# print('')
# printer.print(["Hello"])
# printer.print(["Test1", "Test2", "ON", "Test1", "Test2", "ON", "Test1", "Test2", "OFF", "Test1", "Test2", "LOL"])

printer.printTable([["LOL","NOOB"], ["HAHAAHHAssss", "NOOB"]])
print('')