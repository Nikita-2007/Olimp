program Task1;

var x1, y1, x2 ,y2, a, b: real;
z:char;

begin
  writeln('Введите координаты точек:');
  readln(x1, y1, x2, y2);
  
  a := (y1 - y2)/(x1 - x2);
  b := y2-x2*a;
  if (b >= 0) then z := '+'
  else z := '-';
  b := abs(b);
  
  writeln('Уровнение прямой: y=', a, 'x', z, b);
end.