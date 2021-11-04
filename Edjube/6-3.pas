program prog01;
var
  x, i:int64;
  arr:array of int64;
begin
  read(x);
  setlength(arr, x+3);
  for i := 0 to x+2 do
  begin
    if i < 3 then arr[i] := 1
    else arr[i] := arr[i-1] + arr[i-2] + arr[i-3];
  end;
  write(arr[x-1]);
end.