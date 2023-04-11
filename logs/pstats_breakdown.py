import pstats

p = pstats.Stats('logec-perf.prof')
p.sort_stats('cumulative').print_stats(10)
