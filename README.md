This is the codebase for the bachelor thesis "Evaluating Exploratory Landscape Analysis for Replacing Real-World Optimization Problems with LLM-generated Proxy Functions", containing all necessary files to replicate the study. The codebase consists of three main folders, each allowing replication of a main part of the study.


<p align="center">

&#x20; <picture>

&#x20;   <source media="(prefers-color-scheme: light)" srcset="pipeline.svg">

&#x20;   <img alt="Shows the thesis pipeline." src="pipeline.svg" width="700px">

&#x20; </picture>

</p>


## 0. Install requirements
```bash
  pip install -r requirements.txt
```


## 1. MECHBench Data Collection (MECHBench)

* Sample ND points X with `sampler.py`
* Min-max normalize X
* Run simulations and compute objective values y with (`parallel.slurm` and) `main.py`
* Min-max normalize y
* Compute ELA feature vector



## 2. LLaMEA Loop (LLaMEA_ELA)

* Run LLaMEA loop with (`ela.slurm` and) `ELA_for_MECHBench.py`
* Extract proxies with `process_results.py`



## 3. Algorithm Runs (algorithm_runs)

* Run algorithms on MECHBench problems with (`optimize_on_mechbench.slurm` and) `optimize_on_mechbench.py`
* Run algorithms on proxies with (`optimize_on_proxies.slurm` and) `optimize_on_proxies.py`



## 4. Analysis (LLaMEA_ELA > `process_results.py`)

* Compute AOCCs on min-max normalized, best-seen objective values
* Rank AOCCs and compute Kendall's Tau on MB-proxy ranking pairs
* Compare Tau and Fitness scores

