import sublime, sublime_plugin

from string import ascii_lowercase as lower, digits

valid = " !&,{}?{}".format(digits, lower)
letters = [
[" ",
 " ",
 " ",
 " ",
 " "],
["██",
 "██",
 "██",
 "",
 "██"],
[" ███",
 "██ ██",
 " ███  █",
 "██ ███",
 " ███ █"],
["",
 "",
 "",
 "",
 " ███",
 "██"],
[" █████",
 "██   ██",
 "██ █ ██",
 "██   ██",
 " █████"],
["███",
 " ██",
 " ██",
 " ██",
 "████"],
[" ████",
 "██  ██",
 "   ██",
 "  ██ ",
 " █████"],
["██████",
 "    ██",
 " █████",
 "    ██",
 "██████"],
["██  ██",
 "██  ██",
 "██████",
 "    ██",
 "    ██"],
["██████",
 "██",
 "█████",
 "    ██",
 "██████"],
["██████",
 "██",
 "█████",
 "██  ██",
 " ████"],
["██████",
 "    ██",
 "   ██",
 "  ██",
 " ██"],
[" ████ ",
 "██  ██",
 " ████ ",
 "██  ██",
 " ████ "],
[" ████ ",
 "██  ██",
 " █████",
 "    ██",
 "    ██"],
[" ████",
 "██  ██",
 "   ██",
 "      ",
 "  ██"],
[" █████",
 "██   ██",
 "███████",
 "██   ██",
 "██   ██"],
["██████",
 "██   ██",
 "██████",
 "██   ██",
 "██████"],
[" ██████",
 "██",
 "██",
 "██",
 " ██████"],
["██████",
 "██   ██",
 "██   ██",
 "██   ██",
 "██████"],
["███████",
 "██",
 "█████",
 "██",
 "███████"],
["███████",
 "██",
 "█████",
 "██",
 "██"],
[" ██████",
 "██",
 "██   ███",
 "██    ██",
 "██████"],
["██   ██",
 "██   ██",
 "███████",
 "██   ██",
 "██   ██"],
["██",
 "██",
 "██",
 "██",
 "██"],
["     ██",
 "     ██",
 "     ██",
 "██   ██",
 " █████"],
["██   ██",
 "██  ██",
 "█████",
 "██  ██",
 "██   ██"],
["██",
 "██",
 "██",
 "██",
 "███████"],
["███    ███",
 "████  ████",
 "██ ████ ██",
 "██  ██  ██",
 "██      ██"],
["███    ██",
 "████   ██",
 "██ ██  ██",
 "██  ██ ██",
 "██   ████"],
[" ██████",
 "██    ██",
 "██    ██",
 "██    ██",
 " ██████"],
["██████",
 "██   ██",
 "██████",
 "██",
 "██"],
[" ██████",
 "██    ██",
 "██    ██",
 "██ ▄▄ ██",
 " ██████",
 "    ▀▀"],
["██████",
 "██   ██",
 "██████",
 "██   ██",
 "██   ██"],
["███████",
 "██",
 "███████",
 "     ██",
 "███████"],
["████████",
 "   ██",
 "   ██",
 "   ██",
 "   ██"],
["██    ██",
 "██    ██",
 "██    ██",
 "██    ██",
 " ██████"],
["██    ██",
 "██    ██",
 "██    ██",
 " ██  ██",
 "  ████"],
["██     ██",
 "██     ██",
 "██  █  ██",
 "██ ███ ██",
 " ███ ███"],
["██   ██",
 " ██ ██",
 "  ███",
 " ██ ██",
 "██   ██"],
["██    ██",
 " ██  ██",
 "  ████",
 "   ██",
 "   ██"],
["███████",
 "   ███",
 "  ███",
 " ███",
 "███████"]
]


def padHorz(lett):
   """Horizontally pads a big letter

   Arguments:
      lett {list} -- The big letter in terms of an array
   
   Returns:
      list -- A big letter with space padding at the end
   """
   leng = max([len(line) for line in lett])+1
   padd = []
   for line in lett:
      while len(line) < leng:
         line += " "
      padd.append(line)
   return padd
def padVert(li):
   """Vertically pads big letters
   
   Arguments:
      li {list} -- A list of big letters

   Returns:
      list -- Big letters with space padding below
   """
   maxh = max([len(lett) for lett in li])

   for i in range(len(li)):
      h = len(li[i])
      while(len(li[i]) < maxh):
         li[i].append(" ")
   return li

def assemble(st):
   """Compiles a raw string to a list of big letters
   
   Arguments:
      st {str} -- A string of characters to be bigified
   
   Returns:
      [type] -- [description]
   """
   st = st.lower()

   li = [letters[valid.index(c)] for c in st]
   li = padVert(li)
   li = [padHorz(lett) for lett in li[:-1]]
   li.append(letters[valid.index(st[-1])])

   return li

def printLi(li):
   out = []
   maxh = max([len(lett) for lett in li])
   
   for i in range(maxh):
      out.append([c[i] for c in li])
      out[i] = "".join(out[i])
   return "\n".join(out)


class AsciiBlockCommand(sublime_plugin.TextCommand):
   def run(self, edit):
      sel = self.view.sel()[0]
      txt = self.view.substr(sel)

      self.view.replace(edit, sel, printLi(assemble(txt)))

class AsciiBlockCommand(sublime_plugin.TextCommand):
   def run(self, edit):
      sel = self.view.sel()[0]
      txt = self.view.substr(sel)

      self.view.replace(edit, sel, printLi(assemble(txt)))
      print(txt)