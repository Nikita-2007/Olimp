program Task4;

var N, K, M, s:integer;

begin
  writeln('Введите количество пассажиров, вместительность первой и второй машины:');
  readln(N, K, M);
  
  s := trunc((N / (K+M))*2)+1;
   
  writeln('Количество автомобилей: ', s);
end.