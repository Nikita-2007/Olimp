program prog01;
var x, i, j, y: integer;
begin
  read(x);
  for i := 1 to round(sqrt(x)) do
        if (x mod i = 0) then y := y+1;
  write(y);
end.