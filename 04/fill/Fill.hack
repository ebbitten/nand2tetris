// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
				
(LOOP)
	//Re-initialize spot in screen
	@screenSpot
	M=16384
	@wordSize
	M=16
	@screenEnd
	M=24575

	//Set the data to the keyboard input
	@KBD
	D=M
	//If it's 0 then send it to white
	@WHITE
	D;JEQ
	//else send it to black
	@BLACK
	0;JMP

(WHITE)
	@screenSpot
	D=M
	@screenEnd
	D=D-M
	@LOOP
	D;JEQ //Jump back to loop if we're done
	@screenSpot
	A=M
	M=0
	@wordSize
	D=M
	@screenSpot
	M=M+D
	@WHITE
	0;JMP



(BLACK)
	@screenSpot
	D=M
	@screenEnd
	D=D-M
	@LOOP
	D;JEQ //Jump back to loop if we're done
	@screenSpot
	A=M
	M=-1
	@wordSize
	D=M
	@screenSpot
	M=M+D
	@BLACK
	0;JMP

