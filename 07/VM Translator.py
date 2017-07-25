from pathlib import Path
class Parser(object):
    # Handles the parsing of a single .vm file, encapsulates access to the input code
    def __init__(self, inFile):
        # Opens the input file/stream and gets ready ot parse it
        self.inFile = open(inFile, 'r')

    def hasMoreCommands(self):
        # Return a Boolean for if there are more commands in the input
        pass

    def advance(self):
        # Reads the next command from the input and makes it the current command.
        # Should only be called if hasMoreCommands() is true. Initially there is
        # no current command
        pass

    def commandType(self):
        '''Returns C_ARITHMETIC, C_PUSH, C_POP, C_LABEL, C_GOTO, C_IF, C_FUNCTION,
        C_RETURN, C_CALL.
        Returns the type of the current VM Command. C_ARITHMETIC is returned for all
        the arithemtic commands'''
        pass

    def arg1(self):
        '''Returns String
        Returns the first argument of the current command. In the case of C_ARITHMETIC
        the command itself (add, sub, etc.) is returned. Should not be called if the 
        current command is C_RETURN'''
        pass

    def arg2(self):
        '''Returns int
        Returns the second argument of the current command, should be called 
        only if the current command is C_PUSH, C_POP, C_FUNCTION, or C_CALL'''
        pass


class CodeWriter(object):
    def __init__(self, outFile):
        # Opens the output file and gets ready to write into it
        self.outFile = open(outFile, 'w')

    def setFileName(self, fileName):
        '''Sets the file name, not actually sure that I'll need this outside of the 
        __init__'''
        pass

    def writeArithmetic(self, command):
        ''' command as string
        writes the assembly that is the trnaslation of the given arithmetic
        command'''
        pass

    def writePushPop(self, command, segment, index):
        '''command as C_PUSH or C_POP, segment as string, index as int
        writes the assembly that is the translation of the given command. where 
        command is either C_PUSH or C_POP'''

    def close(self):
        self.outFile.close()







def mainLoop(inFilexDir, outFile):
    # Make our input parameter into a path, check if its a file or a dir
    filePath = Path(inFilexDir)
    isInputFile = filePath.is_file()
    isInputDir = filePath.is_dir()
    assert isInputFile or isInputDir, "Input parameter is neither a file\
    nor a directory"
    # handle if its a file or a directory
    if isInputDir:
        files = filePath.iterdir()
    else:
        files = [].append(filePath)
    assert files, "Files didn't get defined"
    # open our codeWriter
    CodeWriter = Parser(outFile)
    # Iterate over our input files
    for file in files:
        print(file)


mainLoop('MemoryAccess', 'testOut')
