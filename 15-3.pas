﻿program prog3;

var T, N, i, j, x:longint;
    arr:array of integer;
    m:string;

begin
readln(T);
setlength(arr, T);
for i := 0 to T-1 do
  readln(arr[i]);


for i := 0 to T-1 do
begin
  m := 'NO';
  for j := 1 to trunc(sqrt(arr[i])) do
  begin
    x := arr[i] - j*j;
    if (x > 0) and (frac(sqrt(x)) = 0) then
      begin
        m := 'YES';
        break;
      end;
  end;
  writeln(m);
end;
end.