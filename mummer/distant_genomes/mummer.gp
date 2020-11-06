set terminal postscript color solid "Courier" 8
set output "mummer.ps"
set size 1,1
set grid
unset key
set border 0
set tics scale 0
set xlabel "REF"
set ylabel "NZ_CP024964.1"
set format "%.0f"
set mouse format "%.0f"
set mouse mouseformat "[%.0f, %.0f]"
if(GPVAL_VERSION < 5) set mouse clipboardformat "[%.0f, %.0f]"
set xrange [0:825824]
set yrange [0:85478]
set style line 1  lt 1 lw 2 pt 6 ps 0.5
set style line 2  lt 3 lw 2 pt 6 ps 0.5
set style line 3  lt 2 lw 2 pt 6 ps 0.5
plot \
 "mummer.fplot" title "FWD" w lp ls 1, \
 "mummer.rplot" title "REV" w lp ls 2
