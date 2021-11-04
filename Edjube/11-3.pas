program prog1;

var N, i, stup1, stup2, L, maxL:integer;
begin
  
read(N);
stup2 := 0;
L := 0;

for i := 0 to N-1 do
begin
  read(stup1);
  if stup1 >= stup2 then
  begin
    L := L + 1;
    if L > maxL then
      maxL := L;
  end
  
    else 
      L := 1;
  stup2 := stup1;
end;

write(maxL);
end.