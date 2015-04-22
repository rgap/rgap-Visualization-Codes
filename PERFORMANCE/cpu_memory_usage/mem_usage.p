#!/usr/bin/gnuplot

set terminal postscript enhanced color "Helvetica" 20
set output 'memory_usage.ps'
set title "memory usage"
set xlabel "time"
set ylabel "size(M Bytes)"
set xdata time
set timefmt "%d-%m %H:%M:%S"
set format x "%H:%M"
plot "stat.dat" using 1:9 title "used" with lines, "stat.dat" using 1:10 title "buff" with lines, "stat.dat" using 1:11 title "cach" with lines, "stat.dat" using 1:12 title "free" with lines