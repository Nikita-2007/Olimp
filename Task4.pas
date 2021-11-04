program Task4;

var x, y:integer;

begin
  x := 1;
  while(y < 8) do
    begin
    x := x * 2;
    y := y + 1;
    end;
    write(x);
end.