mkdir -p logs
seq 41 55 | parallel \
  -j 15 \
  --memfree 4G \
  --joblog logs/joblog.txt \
  './run_opt_3.sh {} > logs/run_optimizers_{}.out 2> logs/run_optimizers_{}.err'
