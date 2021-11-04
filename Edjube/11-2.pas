program prog1;
var x, y, i:integer;
arr:array of integer;
begin
read(x);
setlength(arr, x);
for i := 0 to x-1 do
  begin
    read(y);
    arr[i] := y;
  end;
  for i := 0 to x-1 do
  begin
    if arr[i] = 0 then writeln(2)
    else if arr[i] = 1 then writeln(0)
    else writeln(1);
  end;
end.