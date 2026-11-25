import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Logistic map chaos component with varying r values
        logistic_chaos = np.sum(4.0 * x_scaled * (1.0 - x_scaled))
        
        # Trigonometric chaos with nested frequencies
        trig_chaos = np.sum(np.sin(20.0 * np.sin(15.0 * x_scaled)) + 
                           0.5 * np.cos(25.0 * np.cos(10.0 * x_scaled)) + 
                           0.3 * np.sin(30.0 * np.tan(5.0 * x_scaled)))
        
        # Fractal-like self-similarity with multi-scale interactions
        fractal_terms = np.sum((x_scaled**2 + 0.1) * np.sin(10.0 / (x_scaled**2 + 0.01)) + 
                              (x_scaled**3 + 0.05) * np.cos(8.0 / (x_scaled**3 + 0.001)))
        
        # Nested harmonic interference with exponential decay
        nested_harmonics = np.sum(np.exp(-2.0 * np.abs(x_scaled)) * 
                                (np.sin(12.0 * x_scaled) * np.cos(8.0 * x_scaled) + 
                                 0.7 * np.sin(18.0 * x_scaled**2) * np.cos(14.0 * x_scaled**2)))
        
        # Cross-dimensional coupling with chaotic phase shifts
        cross_coupling = np.sum(np.sin(5.0 * (x_scaled[:-1] + x_scaled[1:])) * 
                               np.cos(3.0 * (x_scaled[:-1] - x_scaled[1:])) * 
                               np.exp(-0.5 * (x_scaled[:-1]**2 + x_scaled[1:]**2)))
        
        # Asymmetric chaotic landscape with weighted components
        return 0.4 * logistic_chaos + 0.3 * trig_chaos + 0.15 * fractal_terms + \
               0.1 * nested_harmonics + 0.05 * cross_coupling + 2.1