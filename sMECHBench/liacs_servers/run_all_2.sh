mkdir -p logs
seq 21 40 | parallel \
  -j 20 \
  --memfree 4G \
  --joblog logs/joblog.txt \
  './run_opt_2.sh {} > logs/run_optimizers_{}.out 2> logs/run_optimizers_{}.err'
