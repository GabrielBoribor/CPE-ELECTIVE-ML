module Full_DecoderGL;
reg a1,a2,a3;
wire b1,b2,b3,b4,b5,b6,b7;

initial
begin 
$dumpfile("Decoder.vcd");
$dumpvars;

	a2 = 0;
	a1 = 0;
	a3 = 0;
#1 	a3 = 1;
#2 	a2 = 1;
	a3 = 0;
#3 	a3 = 1;
#4 	a1 = 1;
	a2 = 0;
	a3 = 0;
#5 	a3 = 1;
#6 	a2 = 1;
	a3 = 0;
#7	a3 = 1;

end	

xor G1 (b1,a1,a2) ;
not G2 (b2,a1);
and G3 (b3,a2,b2);
xor G4 (b4,a3,b1);
not G5 (b5,b1);
and G6 (b6,b5,a3);
or 	G7 (b7,b3,b6);

initial $monitor($time,"a1=%b a2=%b a3=%b b4=%b b7=%b", a1, a2, a3, b4, b7);
initial #100 $finish;
endmodule