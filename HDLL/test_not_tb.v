module test_not_tb;	
reg a1;
wire b;

initial
begin
$dumpfile("test_not.vcd");
$dumpvars;


   a1=0;
#3 a1=1;
#1 a1=0;
#4 a1=1;
 

	
end

not g1(b,a1);

initial $monitor ($time, "a1=%b; b=%b", a1,,b);

initial #100 $finish;
endmodule