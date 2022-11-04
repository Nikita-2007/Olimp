program Task2;

var x, i, s, y:integer;

begin
  writeln('Введите длину массива');
  readln(x);
  
  s := 0;
  for i := 1 to x do
    begin
    read(y);
    if y > i then
      s := s + y;
    end;
  
  writeln('Сумма: ', s);
end.