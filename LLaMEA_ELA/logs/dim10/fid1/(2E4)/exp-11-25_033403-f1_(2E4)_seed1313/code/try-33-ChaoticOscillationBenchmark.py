import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Base chaotic oscillation term with enhanced complexity
        chaos_term = 0.0
        for i in range(self.dim):
            # Multi-frequency sinusoidal combinations with chaotic interference
            chaos_term += (np.sin(x[i]) * np.cos(2 * x[i]) * np.sin(3 * x[i]) * 
                          np.cos(4 * x[i]) + 0.5 * np.sin(0.5 * x[i]) * np.cos(1.5 * x[i]) * 
                          np.sin(2.5 * x[i]))
            # Stronger exponential barrier terms for increased ruggedness
            chaos_term += 2.0 * (np.exp(-0.5 * (x[i] - 1.0)**2) + np.exp(-0.5 * (x[i] + 1.0)**2))
            # Complex cross-dimensional coupling with higher-order interactions
            if i > 0:
                chaos_term += 0.6 * np.sin(x[i-1]) * np.cos(x[i]) * np.sin(0.7 * x[i-1]) * np.cos(0.3 * x[i]) * np.sin(1.2 * x[i-1] + 0.5 * x[i])
        
        # Enhanced basin term with higher-order polynomial components
        basin = 0.1 * np.sum(x**4) + 0.05 * np.sum(x**6) + 0.02 * np.sum(np.abs(x)**3)
        
        # Multi-scale noise perturbations with fractal-like characteristics
        noise = 0.05 * np.sum(np.sin(20 * x) + np.cos(20 * x) + np.sin(10 * x) * np.cos(10 * x) + 
                             np.sin(5 * x)**2 * np.cos(5 * x)**2)
        
        # New conditioning term with non-uniform scaling for increased ill-conditioning
        conditioning_term = 0.03 * np.sum(np.abs(x)**2.5) + 0.01 * np.sum(x**8)
        
        # Add a new term to create multiple overlapping basins with varying depths
        basin_overlap = 0.04 * np.sum(np.sin(3 * x)**2 + np.cos(3 * x)**2)
        
        return chaos_term + basin + noise + conditioning_term + basin_overlap