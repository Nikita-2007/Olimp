program prog01;

var x:integer;
  
begin
  read(x);
  if x mod 4 = 0 then write(-x)
  else if (x + 1) mod 4 = 0 then write(0)
  else if (x + 2) mod 4 = 0 then write(x+1)
  else write(1);
end.