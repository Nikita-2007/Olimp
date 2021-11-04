program prog01;

var s, s2:string;
  c:char;
  i :integer;
begin
  readln(s);
  readln(s2);
  for c:= 'a' to 'z' do
    if (pos(c, s)>0) and (pos(c, s2)>0) then
      i := i+1;
  write(i);
end.