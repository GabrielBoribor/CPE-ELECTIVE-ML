module Full_Decoder_dt;
reg a1,a2,a3,a4;
wire b1,b2,b3;

initial
begin 
$dumpfile("Decoder.vcd");
$dumpvars;

	a1 = 0;
	a2 = 0;
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

assign b1 = (~a1&a2|~a2&a1);
assign b2 = (~a1);
assign b3 = (a2&b2);
assign b4 = (~a3&b1|~a3&b1);
assign b5 = (~b1);
assign b6 = (b5&a3);
assign b7 = (b3|b6);

initial $monitor($time,"a1=%b a2=%b a3=%b b4=%b b7=%b", a1, a2, a3, b4, b7);
initial #100 $finish;
endmodule