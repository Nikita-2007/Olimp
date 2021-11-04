program Task3;

var a1, a2, a3, a4, x, y, z:integer;

begin
  read(a1, a2, a3, a4);
  x := a1+a2+a3+a4;
  write(x);
  y := x div 10;
  z := x - y*10;
  if(z = 1) and (y <> 1) then write(' птица')
  else if (z > 1) and (z < 5) and (z > 15) and (z < 10 ) then write(' птицы')
  else write(' птиц')
end.