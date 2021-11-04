program prog01;
var x, y, a, m, n: int64;
begin
    read(x, y);
    m := 0;
    while x>0 do
    begin
        a := x mod 10;
        x := x div 10;
        m := m*10 + a;
    end;
    while y>0 do
    begin
        a := y mod 10;
        y := y div 10;
        n := n*10 + a;
     end;
     x := n + m;
     m := 0;
         while x>0 do
    begin
        a := x mod 10;
        x := x div 10;
        m := m*10 + a;
    end;
    write(m);
end.