import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-modulated oscillation with adaptive frequency
        chaotic_osc = np.sum(np.sin(np.pi * x) * np.exp(-0.1 * x**2) * np.cos(3.0 * x))
        
        # Adaptive conditioning with polynomial scaling and exponential modulation
        adaptive_cond = np.sum((x**2 + 0.5 * x**4) * np.exp(-0.05 * x**2))
        
        # Saddle-point enhanced cross-terms with asymmetric coupling
        saddle_cross = np.sum(x[:-1]**2 * x[1:]**3 + 0.3 * x[:-2]**3 * x[2:]**2)
        
        # Hybrid fractal-like structure with multi-scale logarithmic modulation
        fractal_mod = np.sum(np.log(np.abs(x) + 1.0) * np.sin(2.0 * x) * np.cos(x))
        
        # Enhanced non-linear coupling with directional asymmetry
        asymmetry = np.sum((x[:-1]**3 + 0.5 * x[1:]**3) * np.exp(-0.2 * x[:-1]**2) * np.sin(x[1:]))
        
        # High-frequency chaotic modulation to increase gradient complexity
        high_freq = np.sum(np.sin(15.0 * x) * np.cos(7.0 * x) * np.exp(-0.1 * x**2))
        
        return chaotic_osc + adaptive_cond + saddle_cross + fractal_mod + asymmetry + high_freq