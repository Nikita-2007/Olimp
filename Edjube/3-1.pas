program prog01;
var
  b, x, i: integer;
  arr: array[1..4] of integer;
begin
  read(x);
  for i := 1 to 4 do
  begin
    arr[i] := x mod 10;
    x := x div 10;
  end;
for i := 1 to 4 do arr[i] := (arr[i]+ 7) mod 10;
  x := arr[1];
  arr[1] := arr[2];
  arr[2] := x;
  x := arr[3];
  arr[3] := arr[4];
  arr[4] := x;
for i := 1 to 4 do write(arr[i]);
end.