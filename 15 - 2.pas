program prog2;

var a, b, c, N, S:int64;

begin
read(a, b, N);
if a > b then c := a - (a - b)*(N-1)
else c := a + (b-a) * (N-1);
writeln(c);
end.