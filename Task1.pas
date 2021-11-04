program Task1;

var a,b,c,x:integer;

begin
  read(x);
  a := x div 100;
  b := (x - a*100) div 10;
  c := x - b*10 - a*100;
  if (x < 100) or (x > 999) then write('FALSE')
  else if a+b+c = 13 then write('ENTER')
  else write('LOCK');
end.