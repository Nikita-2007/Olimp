program Task5;

var
  x, y: integer;
  arr: array [1..20] of integer;

begin
  read(x);
  for var i := 1 to x do
  begin
    read(arr[i]);
    if(arr[i] > i) then y := y + arr[i]
  end;
  writeln(y);
end.