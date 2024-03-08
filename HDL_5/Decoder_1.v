module Decoder_1;
reg a1,a2,a3,a4;
wire b1,b2,b3;

initial
begin 
$dumpfile("HalfDecoder.vcd");
$dumpvars;

	a1 = 0;
	a2 = 0;
#1 	a2 = 1;
#2 	a1 = 1;
	a2 = 0;
#3 	a2 = 1;

end	

xor G1 (b1,a1,a2) ;
not G2 (b2,a1);
and G3 (b3,a2,b2);

initial $monitor($time,"a1=%b a2=%b b1=%b b3=%b", a1, a2, b1, b3);
initial #100 $finish;
endmodule