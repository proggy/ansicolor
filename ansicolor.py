#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Add ANSI escape codes to a given string to print colored text in consoles
and terminal emulators.

The main function with which you can do about anything is "colored()". There 
you can define almost any combination of text color, background color and 
different styles (bold, underlined, etc.) using keyword arguments.

For convenience, there exist some functions with an even shorter syntax:
"red()", "green()", etc. just to color text, "bred()", "bgreen()", etc. to get 
bold colored text (highlighted text), "ured()", "ugreen()", etc. to get 
underlined colored text. To just change the style of the text, not the color, 
the functions "bold()", "underline()", "invert()", "conceal()", "blink()", 
and "normal()" can be used.

List of colors: gray, red, green, yellow, blue, purple, cyan, lightgray
List of styles: normal, bold, underline, blink, invert, conceal

Note 1: The blinking style probably won't work in most terminal emulators.

Note 2: The "light" ANSI colors are called "bold" here, because most terminal
emulators are displaying them not only in a lighter color, but also in bold
style.

Note 3: As far as I know, on Windows it won't work.

Courtesy goes to:
http://www.tldp.org/HOWTO/Bash-Prompt-HOWTO/x329.html"""
__created__ = '2012-11-28'
__modified__ = '2012-11-28'




#=========================#
# Escape code definitions #
#=========================#

# styles
ANSI_NORMAL    = '\033[0m'
ANSI_BOLD      = '\033[1m'
ANSI_UNDERLINE = '\033[4m'
ANSI_BLINK     = '\033[5m'
ANSI_INVERT    = '\033[7m'
ANSI_CONCEAL   = '\033[8m'

# text colors
ANSI_GRAY      = '\033[30m'
ANSI_RED       = '\033[31m'
ANSI_GREEN     = '\033[32m'
ANSI_YELLOW    = '\033[33m'
ANSI_BLUE      = '\033[34m'
ANSI_PURPLE    = '\033[35m'
ANSI_CYAN      = '\033[36m'
ANSI_LIGHTGRAY = '\033[37m'

# background colors
ANSI_BG_GRAY      = '\033[40m'
ANSI_BG_RED       = '\033[41m'
ANSI_BG_GREEN     = '\033[42m'
ANSI_BG_YELLOW    = '\033[43m'
ANSI_BG_BLUE      = '\033[44m'
ANSI_BG_PURPLE    = '\033[45m'
ANSI_BG_CYAN      = '\033[46m'
ANSI_BG_LIGHTGRAY = '\033[47m'




#==================#
# General function #
#==================#


def colored(string, color=None, bg=None, style=None, revert=True):
  """Return string with ANSI escape sequences added to display a certain color
  and text style in a console or terminal emulator. If "revert" is True,
  return to normal style at the end of the string. In "style", multiple
  comma-separated styles can be specified."""
  __created__ = '2012-11-28'
  __modified__ = '2012-11-28'
  if not isinstance(string, basestring):
    raise TypeError, 'string expected'
  
  # set style
  preamble = ''
  if style:
    styles = str(style).replace('[', '').replace(']', '').replace('(', '')
    styles = styles.replace(')', '').replace(' ', '').replace('"', '')
    styles = styles.replace("'", '')
    for style in styles.split(','):
      style = style.strip()
      if style == '0' or 'normal'.startswith(style.lower()) \
      or 'standard'.startswith(style.lower()) \
      or 'default'.startswith(style.lower()):
        preamble += ANSI_NORMAL
      elif style == '1' or 'light'.startswith(style.lower()) \
      or 'bold'.startswith(style.lower()) \
      or 'highlighted'.startswith(style.lower()):
        preamble += ANSI_BOLD
      elif style == '4' or 'underlined'.startswith(style.lower()):
        preamble += ANSI_UNDERLINE
      elif style == '5' or 'blinking'.startswith(style.lower()):
        preamble += ANSI_BLINK
      elif style == '7' or 'inverted'.startswith(style.lower()) \
      or 'inverse'.startswith(style.lower()):
        preamble += ANSI_INVERT
      elif style == '8' or 'concealed'.startswith(style.lower()):
        preamble += ANSI_CONCEAL
      else:
        raise ValueError, 'unknown style: %s' % style
  
  # set background color
  if bg:
    bg = str(bg)
    if bg in ('0', '40') or 'gray'.startswith(bg.lower()) \
    or 'black'.startswith(bg.lower()):
      preamble += ANSI_BG_GRAY
    elif bg in ('1', '41') or 'red'.startswith(bg.lower()):
      preamble += ANSI_BG_RED
    elif bg in ('2', '42') or 'green'.startswith(bg.lower()):
      preamble += ANSI_BG_GREEN
    elif bg in ('3', '43') or 'yellow'.startswith(bg.lower()):
      preamble += ANSI_BG_YELLOW
    elif bg in ('4', '44') or 'blue'.startswith(bg.lower()):
      preamble += ANSI_BG_BLUE
    elif bg in ('5', '45') or 'purple'.startswith(bg.lower()):
      preamble += ANSI_BG_PURPLE
    elif bg in ('6', '46') or 'cyan'.startswith(bg.lower()):
      preamble += ANSI_BG_CYAN
    elif bg in ('7', '47') or 'lightgray'.startswith(bg.lower()) \
    or 'white'.startswith(bg.lower()):
      preamble += ANSI_BG_LIGHTGRAY
    else:
      raise ValueError, 'unknown background color: %s' % bg
  
  # set text color
  if color:
    color = str(color)
    if color in ('0', '30') or 'gray'.startswith(color.lower()) \
    or 'black'.startswith(color.lower()):
      preamble += ANSI_GRAY
    elif color in ('1', '31') or 'red'.startswith(color.lower()):
      preamble += ANSI_RED
    elif color in ('2', '32') or 'green'.startswith(color.lower()):
      preamble += ANSI_GREEN
    elif color in ('3', '33') or 'yellow'.startswith(color.lower()):
      preamble += ANSI_YELLOW
    elif color in ('4', '34') or 'blue'.startswith(color.lower()):
      preamble += ANSI_BLUE
    elif color in ('5', '35') or 'purple'.startswith(color.lower()):
      preamble += ANSI_PURPLE
    elif color in ('6', '36') or 'cyan'.startswith(color.lower()):
      preamble += ANSI_CYAN
    elif color in ('7', '37') or 'lightgray'.startswith(color.lower()) \
    or 'white'.startswith(color.lower()):
      preamble += ANSI_LIGHTGRAY
    else:
      raise ValueError, 'unknown background color: %s' % color
  
  # remove any existing ANSI escape codes in the string
  while True:
    try: start = string.index('\033[')
    except ValueError: break
    try: end = string.index('m', start)
    except ValueError: break
    string = string[:start]+string[(end+1):]
  
  # return colored string
  string = preamble+string
  if revert:
    string += ANSI_NORMAL
  return string
  

  

#=================#
# Short functions #
#=================#


# just change style, not color
def normal(string):
  return string
def underline(string):
  return colored(string, style='underline')
def bold(string):
  return colored(string, style='bold')
def invert(string):
  return colored(string, style='invert')
def blink(string):
  return colored(string, style='blink')
def conceal(string):
  return colored(string, style='conceal')

# define normal style text color functions
def gray(string):
  return colored(string, color='gray')
def red(string):
  return colored(string, color='red')
def green(string):
  return colored(string, color='green')
def yellow(string):
  return colored(string, color='yellow')
def blue(string):
  return colored(string, color='blue')
def purple(string):
  return colored(string, color='purple')
def cyan(string):
  return colored(string, color='cyan')
def lightgray(string):
  return colored(string, color='lightgray')

# define bold style text color functions
def bgray(string):
  return colored(string, style='bold', color='gray')
def bred(string):
  return colored(string, style='bold', color='red')
def bgreen(string):
  return colored(string, style='bold', color='green')
def byellow(string):
  return colored(string, style='bold', color='yellow')
def bblue(string):
  return colored(string, style='bold', color='blue')
def bpurple(string):
  return colored(string, style='bold', color='purple')
def bcyan(string):
  return colored(string, style='bold', color='cyan')
def blightgray(string):
  return colored(string, style='bold', color='lightgray')

# define underlined style text color functions
def ugray(string):
  return colored(string, style='underline', color='gray')
def ured(string):
  return colored(string, style='underline', color='red')
def ugreen(string):
  return colored(string, style='underline', color='green')
def uyellow(string):
  return colored(string, style='underline', color='yellow')
def ublue(string):
  return colored(string, style='underline', color='blue')
def upurple(string):
  return colored(string, style='underline', color='purple')
def ucyan(string):
  return colored(string, style='underline', color='cyan')
def ulightgray(string):
  return colored(string, style='underline', color='lightgray')
    

    
    
#==============#    
# Test program #
#==============#    

def test():
  """Test program for the ansicolor module."""
  __created__ = '2012-11-28'
  __modified__ = '2012-11-28'
  
  print bold('Welcome to the ansicolor module')
  print bold('-------------------------------')
  print
  print red('This is some red text.')
  print ublue('And this is blue and underlined. Awesome!')
  print
  print bgray('Finished.')

if __name__ == '__main__':
  test()
  
