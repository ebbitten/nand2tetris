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
	@16384
	D=A
	@screenspot
	M=D
	@1
	D=A
	@wordsize
	M=D
	@24575
	D=A
	@screenend
	M=D

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
	@screenend
	D=M
	@screenspot
	D=D-M
	@LOOP
	D;JLT //Jump back to loop if we're done
	@screenspot
	A=M
	M=0
	@wordsize
	D=M
	@screenspot
	M=D+M
	@WHITE
	0;JMP

(BLACK)
	@screenend
	D=M
	@screenspot
	D=D-M
	@LOOP
	D;JLT //Jump back to loop if we're done
	@screenspot
	A=M
	M=-1
	@wordsize
	D=M
	@screenspot
	M=D+M
	@BLACK
	0;JMP

