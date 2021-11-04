program Task2;

var a, b, c:integer;

begin
  read(a, b, c);
  if (a < b) and (a < c) then write(b+c);
  if (b < a) and (b < c) then write(a+c);
  if (c < a) and (c < b) then write(a+b);
end.