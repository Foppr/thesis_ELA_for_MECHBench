import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic logarithmic modulation with sinusoidal coupling
        log_modulation = np.sum(np.log(np.abs(x) + 1.0) * np.sin(2.0 * x) * np.cos(x))
        
        # Improved saddle-point structure with higher-order polynomial interactions
        saddle = np.sum(x**2 - 0.5 * x**4 + 0.1 * x**6)
        
        # Stronger non-uniform scaling with adaptive conditioning (modified coefficients)
        scaling = np.sum((x**2 + 0.7) * (x**3 + 0.4 * x**5))
        
        # Enhanced exponential cross-terms with directional asymmetry (modified factors)
        exp_cross = np.sum(np.exp(0.8 * x[:-1]) * x[1:]**2) + np.sum(np.exp(-0.6 * x[:-2]) * x[2:]**3)
        
        # Increased fractal-like self-similarity through multi-scale polynomial terms
        fractal = 0.15 * np.sum(x**4 * np.sin(3.0 * x))
        
        # Additional high-frequency oscillation term to increase gradient complexity (increased frequency)
        oscillation = np.sum(np.sin(12.0 * x) * np.cos(6.0 * x))
        
        return log_modulation + saddle + scaling + exp_cross + fractal + oscillation