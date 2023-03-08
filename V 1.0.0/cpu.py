import mainSettings as setting
import ram
import id

def terminalUserPath():
    if ram.currentDirectory == setting.null:
        terminalPrompt = str(ram.user) + "@Cali ~$: "
    elif ram.currentDirectory != setting.null:
        terminalPrompt = str(ram.user) + "@Cali/" + str(ram.currentDirectory) + "/ " + "~$: "