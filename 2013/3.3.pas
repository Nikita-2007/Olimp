program prog01;
var
  x, i, z: integer;
  p: real;
begin
  read(x);
  p := 0;
  z := 1;
  
  for i := 0 to x-1 do
    begin
      p := p + z *(4/(i*2+1));
      z := z * -1;
    end;
  
  write(p:0:9);
end.