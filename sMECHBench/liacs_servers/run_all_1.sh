mkdir -p logs
seq 1 20 | parallel \
  -j 20 \
  --memfree 4G \
  --joblog logs/joblog.txt \
  './run_opt_1.sh {} > logs/run_optimizers_{}.out 2> logs/run_optimizers_{}.err'
