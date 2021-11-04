program Task5;

var M, N, temp, r, i:integer;
                   s:string;

begin
  writeln('Введите деопозон:');
  readln(M, N);
  
  temp := 0;
  writeln('Автоморфные числа: ');
  for i := M to N do
  begin
    s := IntToStr(i*i);
    r := StrToInt(s.Substring(s.Length - Length(IntToStr(i))));
    if i = r then
      begin
      writeln(i);
      temp := 1
      end;
  end;
  if temp = 0 then
    write('0');
end.