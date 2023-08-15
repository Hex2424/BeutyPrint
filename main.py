from beutyprint import *

# printer = BeutyPrint([BeutySpan(
#     textColor=Fore.CYAN
# )])
def proc(msg, span):
    if msg == 3:
        span.textColor = Fore.RED
    return (msg, span)

printer = BeutyPrint([
     BeutySpan(
    textColor = Fore.BLUE,
    textPadding = 10,
    textPaddingDirection = CENTER,
    textStyle = Style.BRIGHT,
    l_sep = '[[-> ',
    r_sep = ' <-]]',
  ),
  BeutySpan(
    textColor = Fore.GREEN,
    textPadding = 10,
    textPaddingDirection = CENTER,
    textStyle = Style.BRIGHT,
    l_sep = '[[-> ',
    r_sep = ' <-]]',
  ),
  BeutySpan(
    textColor = Fore.RED,
    textPadding = 10,
    textPaddingDirection = CENTER,
    textStyle = Style.BRIGHT,
    l_sep = '[[-> ',
    r_sep = ' <-]]',
  )
])
print('')
printer.print(["Hello"])
printer.print(["Test1", "Test2", "Test3"])
print('')