program prog01;
var L, T, M:integer;
  X:real;
begin
  read(L, T, M);
  X := (T/L)*M+T;
  write(X : 0 : 3);
end.