module test_xor_tb;	
reg a1,a2;
wire b;

initial
begin
$dumpfile("test_xor.vcd");
$dumpvars;

   a1=0;
 
   a2=0;
 
#3 a1=1;

#1 a1=0;
 
#2 a2=1;
 
#4 a1=1;
 
#3 a2=0;
 
#1 a2=1;
end

xor g1(b,a1,a2);

initial $monitor ($time, "a1=%b;a2=%b ;b=%b", a1,a2,b);

initial #100 $finish;
endmodule