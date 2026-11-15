import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function with chaotic modulation
        rbf = np.sum(np.exp(-np.sum((x[:, None] - x[None, :])**2, axis=0) / (2 * 0.5**2)) * 
                     np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * np.sin(5 * np.pi * x))
        
        # Adaptive frequency modulation with polynomial scaling
        freq_mod = np.sum((x**2 + 1) * np.sin(1.5 * np.pi * x) * np.cos(2.5 * np.pi * x) * 
                         np.sin(4 * np.pi * x) * np.cos(6 * np.pi * x))
        
        # Cross-dimensional dependency chain with exponential coupling
        chain_term = np.sum(np.exp(-0.5 * (x[:-1] - x[1:])**2) * np.sin(7 * np.pi * x[:-1]) * 
                           np.cos(8 * np.pi * x[1:]) * np.sin(9 * np.pi * x[:-1]) * 
                           np.cos(10 * np.pi * x[1:]))
        
        # Multi-scale chaotic oscillations with varying amplitudes
        chaos_osc = np.sum(np.sin(2 * np.pi * x) * np.cos(4 * np.pi * x) * 
                          np.sin(6 * np.pi * x) * np.cos(8 * np.pi * x) * 
                          np.sin(10 * np.pi * x) * np.cos(12 * np.pi * x))
        
        # Polynomial coupling with mixed degrees
        poly_coupling = np.sum(0.1 * x**10 - 0.5 * x**8 + 1.2 * x**6 - 1.8 * x**4 + 2.5 * x**2)
        
        # Fractional power chaotic interactions
        frac_interaction = np.sum(np.sin(np.pi * x**1.2) * np.cos(2 * np.pi * x**1.4) * 
                                np.sin(3 * np.pi * x**1.6) * np.cos(4 * np.pi * x**1.8))
        
        # Combine all terms with optimized weights
        return 0.3 * rbf + 0.25 * freq_mod + 0.15 * chain_term + 0.1 * chaos_osc + 0.08 * poly_coupling + 0.07 * frac_interaction + 3.0