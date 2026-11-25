import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic logarithmic modulation with periodic components
        log_modulation = np.sum(np.log(np.abs(x) + 1.0) * np.sin(3.0 * x) * np.cos(2.0 * x))
        
        # Improved saddle-point structure with higher-order polynomial interactions
        saddle = np.sum(x**2 - 0.5 * x**4 + 0.1 * x**6 - 0.01 * x**8)
        
        # Stronger non-uniform scaling with mixed conditioning
        scaling = np.sum((x**2 + 0.3) * (x**3 + 0.1 * x**5))
        
        # Enhanced exponential cross-terms with adaptive weights
        exp_cross = np.sum(np.exp(0.3 * x[:-1]) * x[1:]**3) + np.sum(np.exp(-0.2 * x[:-2]) * x[2:]**4)
        
        # Increased fractal-like self-similarity through multi-scale polynomial terms
        fractal = 0.1 * np.sum(x**4 * np.sin(3.0 * x) * np.cos(x))
        
        # Additional asymmetric coupling and sharp ridge structures
        coupling = np.sum(x[:-1]**2 * x[1:] * np.sin(x[:-1] + x[1:]))
        
        return log_modulation + saddle + scaling + exp_cross + fractal + coupling