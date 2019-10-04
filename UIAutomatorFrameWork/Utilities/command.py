import subprocess

def executeCommandOnDevice(command):
    try:
        output = None
        commandToExecute = __getPrefixCommand()
        commandToExecute += command
        output = subprocess.check_output(commandToExecute, shell=True)
        if output is not None:
            outputStr = output.decode('utf-8')
            return outputStr
    except Exception as e:
        print("Error: {}".format(e.__str__()))
        return None


def __getPrefixCommand():
    return "adb "