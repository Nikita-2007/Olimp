program Task3;

var N, s, i:integer;

begin
  writeln('Введите количество сказок:');
  readln(N);
  
  while N > 0 do
    begin
    if (N mod 3) = 0 then
      begin
        s := s + (N div 3);
        break
      end;
    N := N - 5;
    s := s + 1;
    end;
   
  writeln('Количество дней: ', s);
end.