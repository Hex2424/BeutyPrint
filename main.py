from beutyprint.beutyprint import *

# printer = BeutyPrint([BeutySpan(
#     textColor=Fore.CYAN
# )])
def proc(msg, span):
    if msg == 3:
        span.textColor = Fore.RED
    return (msg, span)

printer = BeutyPrint([
    BeutySpan(
        textColor=Fore.CYAN,
        defaultColor = Fore.CYAN
    ),
    BeutySpan(
        textColor=Fore.BLUE,
        l_sep='( ',
        r_sep=' )',
        textPadding=0,
        textPaddingDirection=CENTER,
        postProccessor=proc
    ),
    BeutySpan(
        textColor=Fore.RED,
    )
], Fore.BLUE)


printer.print(["hello", 4, "555"])