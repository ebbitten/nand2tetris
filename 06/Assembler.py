import re

class parseLine(object):
	def __init__(self, line):
		line = str(line)
		#stip out whitespace
		line = re.sub('\s',"",line)
		#strip out comments
		result = re.search('(([\=\;\&\|\+\-]*\w*\s*)*)(//)',line) #Todo need to make sure this line preserves = and ;
		if result:
			line = result.group(1)
		self.line = line
		self.type = ""
		self.dest = ""
		self.comp = ""
		self.jump = ""
	def findType(self):
		if len(self.line)<1:
			self.type = "White"
		elif self.line[0] == "(":
			self.type = "Label"
		elif self.line[0] == "@":
			self.type = "A"
		elif self.line[0] in [' ', '	', '/'] : 
			self.type = "White"
		else:
			self.type = "C"
	def translateA(self, symbolTable):
		outStr = "0"
		value = self.line[1:]
		#if we're not referencing a number
		if not self.line[1:].isdigit():
			value = symbolTable[value]
		binaryPart = str(bin(int(value)))[2:]
		while len(binaryPart)<15:
			binaryPart = '0' + binaryPart
		outStr += binaryPart
		outStr += '\n'
		return outStr
	def parsePartsC(self):
		if "=" in self.line:
			self.dest = self.line.split("=")[0]
			self.comp = self.line.split("=")[1].split(";")[0]
			if ";" in self.line:
				self.jump = self.line.split("=")[1].split(";")[1]
		elif ";" in self.line:
			self.jump = self.line.split(";")[1]
			self.comp = self.line.split(";")[0]
		else:
			self.comp = self.line
	def translateC(self):
		outStr = "111"
		#Computation
		compPart = ""
		compDict = {}
		compDict['0'] = '0101010'
		compDict['1'] = '0111111'
		compDict['-1'] = '0111010'
		compDict['D'] = '0001100'
		compDict['A'] = '0110000'
		compDict['!D'] = '0001100'
		compDict['!A'] = '0110001'
		compDict['-D'] = '0001111'
		compDict['-A'] = '0110011'
		compDict['D+1'] = '0011111'
		compDict['A+1'] = '0110111'
		compDict['D-1'] = '0001110'
		compDict['A-1'] = '0110010'
		compDict['D+A'] = '0000010'
		compDict['D-A'] = '0010011'
		compDict['A-D'] = '0000111'
		compDict['D&A'] = '0000000'
		compDict['D|A'] = '0010101'
		compDict['M'] = '1110000'
		compDict['!M'] = '1110001'
		compDict['M+1'] = '1110111'
		compDict['M-1'] = '1110010'
		compDict['D+M'] = '1000010'
		compDict['D-M'] = '1010011'
		compDict['M-D'] = '1000111'
		compDict['D&M'] = '1000000'
		compDict['D|M'] = '1010101'
		if not self.comp:
			compPart = '1111111'
		else:
			compPart = compDict[self.comp]
		#Destination
		destPart = ""
		for n, char in enumerate(['A', 'D', 'M']):
			if char in self.dest:
				destPart += "1"
			else:
				destPart += "0"
		#Jump
		jumpPart = ""
		jumpDict = {}
		jumpDict['JGT'] = '001'
		jumpDict['JEQ'] = '010'
		jumpDict['JGE'] = '011'
		jumpDict['JLT'] = '100'
		jumpDict['JNE'] = '101'
		jumpDict['JLE'] = '110'
		jumpDict['JMP'] = '111'
		if self.jump:
			jumpPart = jumpDict[self.jump]
		else:
			jumpPart = '000'
		#Concat
		return ("".join([outStr, compPart, destPart, jumpPart,'\n']))
class readFile(object):
	def __init__(self, inFile, outFile):
		self.inFile = inFile
		self.outFile = outFile
		self.currentLineNum = 0
		self.currentLine = ""
		self.symbolTable = {}
		self.nextSymbolSpace = 16
		self.firstRun = True
		self.outStr = ""
		self.mainLoop()
	def makeSymbolTable(self):
		#Makes and stores in decimal
		self.symbolTable['SP'] = 0
		self.symbolTable['LCL'] = 1
		self.symbolTable['ARG'] = 2
		self.symbolTable['THIS'] = 3
		self.symbolTable['THAT'] = 4
		self.symbolTable['SCREEN'] = 16384
		self.symbolTable['KBD'] = 24576
		for i in range(16):
			self.symbolTable['R' + str(i)] = i
	def checkAndAddSymbol(self, symbol, label = False):
		if symbol in self.symbolTable.keys():
			pass
		else:
			if label:
				self.symbolTable[symbol] = self.currentLineNum
			else:
				self.symbolTable[symbol] = self.nextSymbolSpace
				self.nextSymbolSpace += 1
	def mainLoop(self):
		self.makeSymbolTable()
		with open(self.inFile, 'r') as f:
			#First run of loop
			self.innerLoop(f)
			self.firstRun = False
		with open(self.inFile, 'r') as f:
			#Second run of loop
			self.innerLoop(f)
		with open(self.outFile, 'w') as g:
			g.write(self.outStr)
	def innerLoop(self,f):
		for line in f:
			self.currentLine = parseLine(line)
			self.currentLine.findType()
			if self.firstRun:
				if self.currentLine.type not in  ["White","Label"]:
					# print(self.currentLine.line)
					self.currentLineNum += 1
				if self.currentLine.type == "Label":
					result = re.search('(\()(\w*)(\))',self.currentLine.line)
					value = result.group(2)
					self.checkAndAddSymbol(value, label = True)
			else:
				if self.currentLine.type == "A":
					value = self.currentLine.line[1:]
					if not value.isdigit():
						self.checkAndAddSymbol(value)
					self.outStr += self.currentLine.translateA(self.symbolTable)
					self.currentLineNum += 1
				if self.currentLine.type == "C":
					self.currentLine.parsePartsC()
					self.outStr += self.currentLine.translateC()
					self.currentLineNum += 1

import io
nextRead = readFile('Rect.asm', 'Rect.HACK')








