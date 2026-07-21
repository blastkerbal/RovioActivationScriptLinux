import uuid, os

print("Rovio Activation Script v1.0.1 (Linux Tweaked) by PRO100KatYT\n")

def getMacAddressesInString():
    # Use uuid.getnode() which is reliable and cross-platform on Linux/Windows
    mac_int = uuid.getnode()
    macAddress = "-".join("{:012X}".format(mac_int)[i:i+2] for i in range(0, 12, 2))
    return macAddress

def main():
    try:
        xmlContent = '''<?xml version="1.0" encoding="utf-8"?>
<data>
<Boolean key="BDPGS12FL" value="True" />
<String key="BDPGS12FL_hardwareID" value="{macAddress}" />
</data>'''.format(macAddress=getMacAddressesInString())

        # Save directly to the current directory since you're already in the game's AppData folder
        filePath = os.path.join(os.getcwd(), 'Settings.xml')

        with open(filePath, 'w', encoding='utf-8') as f:
            f.write(xmlContent)

        input("Settings.xml file has successfully been generated and saved in:\n{filePath}\n\nBad Piggies should now be activated!\n\nPress ENTER to close the program.".format(filePath=filePath))

    except Exception as e:
        print("Unexpected error: {}".format(e))

try:
    main()
except ValueError as e:
    input("Error: {}\nPress ENTER to close the program.".format(e))

