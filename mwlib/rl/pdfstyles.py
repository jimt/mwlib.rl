#! /usr/bin/env python
#! -*- coding:utf-8 -*-

# Copyright (c) 2007, PediaPress GmbH
# See README.txt for additional licensing information.

#################################################################
#
# PLEASE DO NOT EDIT THIS FILE UNLESS YOU KNOW WHAT YOU ARE DOING
#
# If you want to customize the layout of the pdf, do this in
# a separate file customconfig.py
#
#################################################################


import os

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.lib.units import cm

from reportlab.lib.fonts import addMapping
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4


# used to mark translateable strings:
if '_' not in globals():
    _ = lambda x: x


########## REGISTER FONTS

import mwlib.fonts
default_fontpath = os.path.dirname(mwlib.fonts.__file__)

fonts = [
    {'name': 'DejaVuSerif',
     'code_points': ['Latin Extended-B', 'Latin-1 Supplement', 'Latin Extended-A', 'Basic Latin'] ,
     'file_names': ['DejaVuSerif.ttf', 'DejaVuSerif-Bold.ttf', 'DejaVuSerif-Italic.ttf', 'DejaVuSerif-BoldItalic.ttf'],
     'type': 'ttf',
     },
    {'name': 'DejaVuSans',
     'code_points': [(593, 11904)] ,
     'file_names': ['DejaVuSans.ttf', 'DejaVuSans-Bold.ttf', 'DejaVuSans-Oblique.ttf', 'DejaVuSans-BoldOblique.ttf'],
     'type': 'ttf',
     },
    {'name': 'DejaVuSansMono',
     'code_points': [] , # not used for particular scripts/code-point-blocks. only used when explicitly requested (code/source/etc.)
     'file_names': ['DejaVuSansMono.ttf', 'DejaVuSansMono-Bold.ttf', 'DejaVuSansMono-Oblique.ttf', 'DejaVuSansMono-BoldOblique.ttf'],
     'type': 'ttf',
     },
    {'name': 'STSong-Light',
     'code_points': [(11904, 12591), (12704, 12735), (13312, 19903), (19968, 40895), (65104, 65135) ] ,
     'type': 'cid',
     },
    {'name': 'HYSMyeongJo-Medium',
     'code_points': [(63744, 64255), (12592, 12687), (44032, 55215)],
     'type': 'cid',
     },
    ]

def sys_fonts(filename):
    return os.path.join('/usr/share/fonts/truetype/', filename)

serif_font =  "DejaVuSerif"
sans_font = "DejaVuSans"
mono_font = "DejaVuSansMono"
default_font = 'DejaVuSans'

## fonts = [
##     {'name': 'DejaVuSerif',
##      'code_points': ['Latin Extended-B', 'Latin-1 Supplement', 'Latin Extended-A', 'Basic Latin'] ,
##      'file_names': ['DejaVuSerif.ttf', 'DejaVuSerif-Bold.ttf', 'DejaVuSerif-Italic.ttf', 'DejaVuSerif-BoldItalic.ttf'],
##      'type': 'ttf',
##      },
##     {'name': 'DejaVuSans',
##      'code_points': [] ,
##      'file_names': ['DejaVuSans.ttf', 'DejaVuSans-Bold.ttf', 'DejaVuSans-Oblique.ttf', 'DejaVuSans-BoldOblique.ttf'],
##      'type': 'ttf',
##      },
##     {'name': 'DejaVuSansMono',
##      'code_points': ['Box Drawing'] , # also used for code/source/etc.
##      'file_names': ['DejaVuSansMono.ttf', 'DejaVuSansMono-Bold.ttf', 'DejaVuSansMono-Oblique.ttf', 'DejaVuSansMono-BoldOblique.ttf'],
##      'type': 'ttf',
##      },
##     {'name': 'AR PL UMing HK',
##      'code_points': ['CJK Unified Ideographs', 'CJK Strokes', 'CJK Unified Ideographs Extension A', 'Halfwidth and Fullwidth Forms', 'CJK Compatibility Ideographs', 'Small Form Variants', 'Low Surrogates', 'CJK Radicals Supplement'] ,
##      'file_names': [sys_fonts('arphic/uming.ttc')],
##      'type': 'ttf',
##      },   
##     {'name': 'Ezra SIL',
##      'code_points': ['Alphabetic Presentation Forms', 'Hebrew'] ,
##      'file_names': [sys_fonts('ttf-sil-ezra/SILEOT.ttf')],
##      'type': 'ttf',
##      },
## ##     {'name': 'GFS Artemisia',
## ##      'code_points': ['Greek Extended', 'Greek and Coptic'] ,
## ##      'file_names': [sys_fonts('ttf-gfs-artemisia/GFSArtemisia.otf'), sys_fonts('ttf-gfs-artemisia/GFSArtemisiaBold.otf'), sys_fonts('ttf-gfs-artemisia/GFSArtemisiaIt.otf'), sys_fonts('ttf-gfs-artemisia/GFSArtemisiaBoldIt.otf')],
## ##      'type': 'ttf',
## ##      },
##     {'name': 'Nazli',
##      'code_points': ['Arabic Presentation Forms-A', 'Arabic', 'Arabic Presentation Forms-B', 'Arabic Supplement'] ,
##      'file_names': [sys_fonts('ttf-farsiweb/nazli.ttf')],
##      'type': 'ttf',
##      },
##     {'name': 'UnBatang',
##      'code_points': ['Hangul Syllables', 'Hangul Jamo', 'Hangul Compatibility Jamo'] ,
##      'file_names': [sys_fonts('unfonts/UnBatang.ttf')],
##      'type': 'ttf',
##      },
##     {'name': 'Garuda',
##      'code_points': ['Thai'] ,
##      'file_names': [sys_fonts('thai/Garuda.ttf'), sys_fonts('thai/Garuda-Bold.ttf'), sys_fonts('thai/Garuda-Oblique.ttf'), sys_fonts('thai/Garuda-BoldOblique.ttf')],
##      'type': 'ttf',
##      },
##     {'name': 'Lohit Telugu',
##      'code_points': ['Telugu'] ,
##      'file_names': [sys_fonts('ttf-telugu-fonts/lohit_te.ttf')],
##      'type': 'ttf',
##      },
##     {'name': 'Samyak-Gujarati',
##      'code_points': ['Gujarati'] ,
##      'file_names': [sys_fonts('ttf-gujarati-fonts/Samyak-Gujarati.ttf')],
##      'type': 'ttf',
##      },
##     {'name': 'Samyak-Devanagari',
##      'code_points': ['Devanagari'] ,
##      'file_names': [sys_fonts('ttf-devanagari-fonts/Samyak-Devanagari.ttf')],
##      'type': 'ttf',
##      },    
##     {'name': 'Lohit Punjabi',
##      'code_points': ['Gurmukhi'] ,
##      'file_names': [sys_fonts('ttf-indic-fonts-core/lohit_pa.ttf')],
##      'type': 'ttf',
##      },
##     {'name': 'Lohit Oriya',
##      'code_points': ['Oriya'] ,
##      'file_names': [sys_fonts('ttf-oriya-fonts/lohit_or.ttf')],
##      'type': 'ttf',
##      },
##     {'name': 'AnjaliOldLipi',
##      'code_points': ['Malayalam'] ,
##      'file_names': [sys_fonts('ttf-malayalam-fonts/AnjaliOldLipi.ttf')],
##      'type': 'ttf',
##      },
##     {'name': 'Kedage',
##      'code_points': ['Kannada'] ,
##      'file_names': [sys_fonts('ttf-kannada-fonts/Kedage-n.ttf'), sys_fonts('ttf-kannada-fonts/Kedage-b.ttf'), sys_fonts('ttf-kannada-fonts/Kedage-i.ttf'), sys_fonts('ttf-kannada-fonts/Kedage-t.ttf')],
##      'type': 'ttf',
##      },
##     {'name': 'LikhanNormal',
##      'code_points': ['Bengali'] ,
##      'file_names': [sys_fonts('ttf-bengali-fonts/LikhanNormal.ttf')],
##      'type': 'ttf',
##      },
##     {'name': 'Lohit Tamil',
##      'code_points': ['Tamil'] ,
##      'file_names': [sys_fonts('ttf-indic-fonts-core/lohit_ta.ttf')],
##      'type': 'ttf',
##      },
##     ]


########## / REGISTER FONTS

### TABLE CONFIG

tableOverflowTolerance = 20  # max width overflow for tables    unit: pt 


######### PAGE CONFIGURATION

pageWidth, pageHeight = A4   # roughly: pW= 21*cm pH=29*cm

pageMarginHor = 2 * cm
pageMarginVert= 2 * cm

headerMarginHor = 1.5 * cm
headerMarginVert= 1.5 * cm

printWidth = pageWidth - 2*pageMarginHor
printHeight = pageHeight - 2*pageMarginVert

footerMarginHor = 1.5 * cm
footerMarginVert= 1.5 * cm

showTitlePage = True
showPageHeader = True 
showPageFooter = True
showTitlePageFooter = True
pageBreakAfterArticle = False

showArticleSource = True        # Set to False in customConfig.py to exclude article source URL from the output.
showArticleAuthors = True       # Set to False in customConfig.py to exclude principal author information from the output.

# NOTE: strings can contain reportlab styling tags the text needs to be xml excaped.
# more information is available in the reportlab user documentation (http://www.reportlab.com/docs/userguide.pdf)
# check the section 6.2 "Paragraph XML Markup Tags"
# since the documenatition is not guaranteed to be up to date, you might also want to check the docsting of the
# Paragraph class (reportlab/platypus/paragraph.py --> class Paragraph())
# e.g. the use of inline images is not included in the official documenation of reportlab
pagefooter = u''
titlepagefooter = _(u'PDF generated using the open source mwlib toolkit<br/>see http://code.pediapress.com/ for more information')


######### IMAGE CONFIGURATION

max_img_width = 9 # max size in cm 
max_img_height = 12 
min_img_dpi = 75 # scaling factor in respect to the thumbnail-size in the wikimarkup which limits image-size
inline_img_dpi = 100 # scaling factor for inline images. 100 dpi should be the ideal size in relation to 10pt text size 

# margins for floated images - margins like in html/css: (top, right, bottom, left)
img_margins_float_left = (0, 0.4*cm, 0.7*cm, 0) # img that is left aligned
img_margins_float_right = (0, 0, 0.7*cm, 0.4*cm) # ...
img_margins_float = (0.2*cm,0.2*cm,0.2*cm,0.2*cm) # any other alignment

######### TEXT CONFIGURATION
fontsize = 10
leading = 15
text_align = TA_JUSTIFY # default alignment of text outside of tables TA_LEFT, TA_JUSTIFY, TA_RIGHT, TA_CENTER are valid
table_text_align = TA_LEFT # ... inside of tables

smallfontsize = 8
smallleading = 12

bigfontsize = 12
bigleading = 17

LEFTINDENT = 25 # indentation of paragraphs...
RIGHTINDENT = 25 # indentation of paragraphs...
LISTINDENT = 12 # indentation of lists per level

tabsize = 6

maxCharsInSourceLine = 72 # if printing a source node, the maximum number of chars in one line

class BaseStyle(ParagraphStyle):

    def __init__(self, name, parent=None, **kw):
        ParagraphStyle.__init__(self, name=name, parent=parent, **kw)
        self.fontName = sans_font
        self.fontSize = fontsize
        self.leading = leading
        self.autoLeading = 'max'
        self.leftIndent = 0
        self.rightIndent = 0
        self.firstLineIndent = 0
        self.alignment = text_align
        self.spaceBefore = 3
        self.spaceAfter = 0
        self.bulletFontName = sans_font
        self.bulletFontSize = fontsize
        self.bulletIndent = 0
        self.textColor = colors.black
        self.backColor = None
        self.wordWrap = None
        self.textTransform = None
        
        
def text_style(mode='p', indent_lvl=0, in_table=0, relsize='normal', text_align='left'):
    """
    mode: p (normal paragraph), blockquote, center (centered paragraph), footer, figure (figure caption text),
          preformatted, list, license, licenselist, box
    relsize: relative text size: small, normal, big  (currently only used for preformatted nodes
    indent_lvl: level of indentation in lists or indented paragraphs
    in_table: 0 - outside table
              1 or above - inside table (nesting level of table)
    """

    style = BaseStyle(name='text_style_%s_indent_%d_table_%d_size_%s' % (mode, indent_lvl, in_table, relsize))
    style.flowable = True # needed for "flowing" paragraphs around figures

    if in_table > 0:
        style.alignment = table_text_align
    if text_align == 'right':
        style.alignment = TA_RIGHT
    elif text_align == 'center':
        style.alignment = TA_CENTER

    if in_table or mode in ['footer', 'figure'] or (mode=='preformatted' and relsize=='small'):
        style.fontSize=smallfontsize
        style.bulletFontSize = smallfontsize
        style.leading = smallleading
        if relsize == 'small':
            style.fontSize -= 1
        elif relsize == 'big':
            style.fontSize += 1

    if mode == 'blockquote':
        style.rightIndent = RIGHTINDENT
        indent_lvl += 1

    if mode in ['footer', 'figure', 'center']:
        style.alignment = TA_CENTER

    if mode == 'box' or mode == 'source' or mode == 'preformatted':
        style.backColor = '#eeeeee'
        style.borderPadding = 3 # borderPadding is not calculated onto the box dimensions.
        style.spaceBefore = 6 # therefore spaceBefore = 3 + borderPadding
        style.spaceAfter = 9 # add an extra 3 to spaceAfter, b/c spacing seems to small otherwise
    
    if mode == 'source' or mode == 'preformatted':
        style.fontName = mono_font   
        
    if mode == 'list':
        style.spaceBefore = 0
        style.bulletIndent = LISTINDENT * max(0, indent_lvl-1)
        style.leftIndent = LISTINDENT * indent_lvl
    else:
        style.leftIndent = indent_lvl*LEFTINDENT

    if mode == 'booktitle':
        style.fontSize = 36
        style.leading = 40
        style.spaceBefore = 16
        style.fontName= sans_font

    if mode == 'booksubtitle':
        style.fontSize = 24
        style.leading = 30
        style.fontName= sans_font

    if mode == 'license':
        style.fontSize = 6
        style.leading = 1
        style.spaceBefore = 0

    if mode == 'licenselist':
        style.fontSize = 6
        style.leading = 1
        style.spaceBefore = 0
        style.bulletIndent = LISTINDENT * max(0, indent_lvl-1)
        style.leftIndent = LISTINDENT * indent_lvl
        style.bulletFontSize = 6
        
    return style

table_style = {'spaceBefore': 0.25*cm,
               'spaceAfter': 0.25*cm}


class BaseHeadingStyle(ParagraphStyle):

    def __init__(self, name, parent=None, **kw):
        ParagraphStyle.__init__(self, name=name, parent=parent, **kw)
        self.fontName = sans_font
        self.fontSize = bigfontsize
        self.leading = leading
        self.autoLeading = 'max'
        self.leftIndent = 0
        self.rightIndent = 0
        self.firstLineIndent = 0
        self.alignment = TA_LEFT        
        self.spaceBefore = 12
        self.spaceAfter = 6
        self.bulletFontName = sans_font
        self.bulletFontSize = bigfontsize
        self.bulletIndent = 0
        self.textColor = colors.black
        self.backcolor = None
        self.wordWrap = None
        self.textTransform = None
        #self.allowWidows = 0
        #self.allowOrphans = 0
        
def heading_style(mode='chapter', lvl=1):

    style = BaseHeadingStyle(name='heading_style_%s_%d' % (mode, lvl))

    if mode == 'chapter':
        style.fontSize = 26
        style.leading = 30
        style.alignment = TA_CENTER
    elif mode == 'article':
        style.fontSize = 22
        style.leading = 26
        style.spaceBefore = 20
        style.spaceAfter = 2
    elif mode == 'section':
        lvl = max(min(5,lvl), 1)  
        style.fontSize = 18 - (lvl - 1) * 2
        style.leading = style.fontSize + max(2, min(int(style.fontSize / 5), 3)) # magic: increase in leading is between 2 and 3 depending on fontsize...
        style.spaceBefore = min(style.leading, 20)
        if lvl > 1: # needed for "flowing" paragraphs around figures
            style.flowable = True
    elif mode == 'tablecaption':
        style.fontsize = 12
        style.leading = 16
        style.alignment = TA_CENTER
        style.flowable = False
        style.spaceAfter = 0
    elif mode == "license":
        style.fontSize = 8
        style.leading = 5
        style.spaceAfter = 0
        style.spaceBefore = 5

    elif mode == "licensearticle":
        style.fontSize = 10
        style.leading = 5
        style.spaceAfter = 0
        style.spaceBefore = 5
            
    return style
    

# import custom configuration to override configuration values
# if doing so, you need to be careful not to break things...
try:
    from customconfig import *
except ImportError:
    pass


