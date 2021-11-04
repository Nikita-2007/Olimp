program prog01;
var
  x, y, i, j, z: integer;
begin
  read(x);
  for i := 5 to 10 do
    for j := 1 to 10 do
    begin
    if ((x+1)*i) = ((x+2)*j) then
      begin
        y := (x+1)*(i+1)+1;
        z := j;
        break;
      end;
      if ((x+1)*i) = ((x+2)*z) then break;
    end;
    write(y);
end.