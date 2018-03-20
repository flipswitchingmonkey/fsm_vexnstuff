# shelf tool to save the currently open scene with an incremented version counter
# if there is no versioning, a three digit counter will be attached to the original file name

# attention: probably does not catch all edge-cases...

# author: Michael Auerswald <michael@flipswitchingmonkey.com>

import os
import string

output = False

def IncreaseVersion(fullPath, originalVersion=None):
    fn, ext = os.path.splitext(fullPath)
    fnreverse = fn[::-1]  # reverse string

    versionString = ""
    versionNumber = 0
    beginVersionString = False
    for letter in fnreverse:
        if letter.isdigit() is True:
            beginVersionString = True
            versionString += letter
            if output: print("Digit: {0}").format(letter)
        else:
            if output: print("Non-Digit: {0}").format(letter)
            if beginVersionString is True:
                versionString = versionString[::-1]  # reverse string
                versionNumber = int(versionString)
                break  # first non-digit ends version string
    if originalVersion is None:
        if versionString == '':
            originalVersion = "No Version"
        else:
            originalVersion = versionString

    versionNumber += 1
    fill_length = len(versionString)
    divider = ''
    if fill_length == 0:
        if fn[-1] != '_' or fn[-1] != '-' :
            divider = '_'
        fill_length = 3
    versionStringNew = divider + str(versionNumber).zfill(fill_length)

    fnreverse = fnreverse.replace(versionString[::-1], versionStringNew[::-1], 1)
    fullPathNew = fnreverse[::-1] + ext

    if os.path.exists(fullPathNew):
        if output: print("{0} already exists, increasing further...").format(fullPathNew, originalVersion)
        fullPathNew = IncreaseVersion(fullPathNew, originalVersion)
    else:
        if output: print("Increased version {0} to {1}").format(originalVersion, versionStringNew)
        if output: print("Changed path {0} to {1}").format(fullPath, fullPathNew)
    return fullPathNew
    
def main():
    currentPath = hou.hipFile.name()
    fullPathNew = IncreaseVersion(currentPath)
    
    hou.hipFile.setName(fullPathNew)
    hou.hipFile.save()
    print("Saved as {0}").format(fullPathNew)

main()
