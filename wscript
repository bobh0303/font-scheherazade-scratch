#!/usr/bin/python
# Smith configuration file for Scheherazade

# override the default folders
DOCDIR = ["documentation", "web"]  # add "web" to default
genout = "generated/"

# set package name
APPNAME = "ScheherazadeNew"

# set the font family name
FAMILY = APPNAME

##DESC_NAME = "Scheherazade New"
DESC_SHORT = "Arabic-script font designed in the traditional Naskh style"

#DEBPKG = 'fonts-sil-scheherazade'

# Get version info from Regular UFO; must be first function call:
getufoinfo('source/masters/' + FAMILY + '-Regular' + '.ufo')
# BUILDLABEL = 'beta'

ftmlTest('tools/ftml-smith.xsl')

# APs to omit:
OMITAPS = '--omitaps "_above,_below,_center,_ring,_through,_aboveLeft,_H,_L,_O,_U,_R,above,below,center,ring,through,aboveLeft,H,L,O,U,R"'

# iterate over designspace
designspace('source/ScheherazadeNew.designspace',
    instanceparams='-l ' + genout + '${DS:FILENAME_BASE}_createintance.log',
    target = process('${DS:FILENAME_BASE}.ttf'
###       , cmd('${PSFCHANGETTFGLYPHNAMES} ${SRC} ${DEP} ${TGT}', ['source/${DS:FILENAME_BASE}.ufo']),
#        Note: ttfautohint-generated hints don't maintain stroke thickness at joins, so we're not hinting these fonts
#        cmd('${TTFAUTOHINT} -n -c  -D arab -W ${DEP} ${TGT}')
    ),
    ap = genout + '${DS:FILENAME_BASE}.xml',
    version=VERSION,  # Needed to ensure dev information on version string

    graphite=gdl(genout + '${DS:FILENAME_BASE}.gdl',
        depends=['source/graphite/cp1252.gdl', 'source/graphite/SchFeatures.gdh', 'source/graphite/SchGlyphs.gdh', 'source/graphite/stddef.gdh'],
        master = 'source/graphite/master.gdl',
        make_params = OMITAPS + ' --cursive "exit=entry,rtl" --cursive "_digit=digit"',
        params = '-d -q -e ${DS:FILENAME_BASE}_gdlerr.txt',
        ),
    opentype = fea(genout + '${DS:FILENAME_BASE}.fea',
        mapfile = genout + "${DS:FILENAME_BASE}.map",
        master = 'source/opentype/master.feax',
        make_params = OMITAPS,
        ),
    typetuner = typetuner("source/typetuner/feat_all.xml"),
    classes = 'source/classes.xml',
    script='arab',
    pdf=fret(genout + '${DS:FILENAME_BASE}-fret.pdf', params='-r -o i -m 48'),
    woff=woff('web/${DS:FILENAME_BASE}.woff', params='-v ' + VERSION + ' -m ../source/${FAMILY}-WOFF-metadata.xml'),
    )

def configure(ctx):
    ctx.find_program('psfchangettfglyphnames')
#    ctx.find_program('ttfautohint')

