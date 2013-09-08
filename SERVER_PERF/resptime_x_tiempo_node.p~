#!/usr/bin/gnuplot

set terminal png
set output "resptime_tiempo_node.png"

set title "Benchmark testing"

set key left top   # Where to place the legend/key
set grid y   # Draw gridlines oriented on the y axis

set xdata time    # Specify that the x-series data is time data
set timefmt "%s"  # Specify the *input* format of the time data

set format x "%S" # Specify the *output* format for the x-axis tick labels

set xlabel 'seconds'
set ylabel "response time (ms)"

set datafile separator '\t'

#plot "serv_nodejs.tsv" every ::2 using 2:5 title 'response time' with points
plot "serv_nodejs.tsv" using 2:5 title 'response time' with points
