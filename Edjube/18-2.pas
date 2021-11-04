program prog01;
var i,x:integer;
  z:real;
begin
  read(x);
  for i := 0 to x*3 do
    begin
      z := sqrt((x+i));
      if z = trunc(z) then break;
    end;
  write(z*z);
end.