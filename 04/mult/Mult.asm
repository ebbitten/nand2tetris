// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

@R2
M=0
@i
M=0
(LOOP)
	//check to see if loop is over, will loop R1 times
	@i
	D=M
	@R1
	D=D-M
	@END
	D;JEQ //If i=R1 goto END
	
	//add R0 to R2
	@R0
	D=M
	@R2
	M=D+M
	
	//Increment i
	@i
	M=M+1
	//Jump back to loop
	@LOOP
	0;JMP

(END)
	@END
	0;JMP