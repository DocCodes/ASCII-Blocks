import sublime, sublime_plugin
from string import ascii_lowercase as lowerletters

valid = "{} &,".format(lowerletters)
letters = [
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
 "███████"],
[" ",
 " ",
 " ",
 " ",
 " "],
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
 "██"]
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
   for i in lett:
      while len(i) < leng:
         i += " "
      padd.append(i)
   return padd
def padVert(li):
   """Vertically pads big letters
   
   Arguments:
      li {list} -- A list of big letters

   Returns:
      list -- Big letters with space padding below
   """
   for i in range(len(li)):
      leng = max([len(line) for line in li[i]])
      li[i].append(" "*leng)
   return li
def assemble(st):
   """Compiles a raw string to a list of big letters
   
   Arguments:
      st {str} -- A string of characters to be bigified
   
   Returns:
      [type] -- [description]
   """
   st = st.lower()
   li = [padHorz(letters[valid.index(c)]) for c in st[:-1]]
   li.append(letters[valid.index(st[-1])])
   return li
def printLi(li):
   out = []
   for i in range(6):
      out.append([c[i] for c in li])
      out[i] = "".join(out[i])
   return "\n".join(out)


class AsciiBlockCommand(sublime_plugin.TextCommand):
   def run(self, edit):
      sel = self.view.sel()[0]
      txt = self.view.substr(sel)

      self.view.replace(edit, sel, printLi(assemble(txt)))
      print(txt)