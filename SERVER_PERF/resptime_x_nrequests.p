#!/usr/bin/gnuplot

set terminal png
set output "resptime_nreq.png"

set title "Benchmark testing"

set key left top   # Where to place the legend/key
set grid y   # Draw gridlines oriented on the y axis

set xlabel 'requests'
set ylabel "response time (ms)"

set datafile separator '\t'

#plot "serv_apache.tsv" every ::2 using 5 title 'response time' with lines
plot "serv_apache.tsv" using 5 title 'response time' with lines
