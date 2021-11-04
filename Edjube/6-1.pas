program prog01;

var A1, B1, A2, B2, H:integer;

begin
read(A1, B1, A2, B2);
if A1 < B1 then
begin
    if A2 < B2 then H := B1 + B2
    else H := B1 + A2;
end
else
begin
    if A2 < B2 then H := A1 + B2
    else H := A1 + A2;
end;
write(H);
end.