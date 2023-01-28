program prog01;
var
  b, x, i, y, a: integer;
begin
read(x);
a := (x-1) div 2;
y := 0;
for i := 0 to x-1 do
  begin
    if a-i > -1 then
    begin
      for b := 0 to a-i-1 do write(' ');
      for b := 0 to i+i do write('*');
      writeln();
    end
    else
      begin
        for b := 0 to i-a-1 do write(' ');
        for b := 0 to x-3 do write('*');
        x := x-2;
        writeln();
      end;
  end;
end.