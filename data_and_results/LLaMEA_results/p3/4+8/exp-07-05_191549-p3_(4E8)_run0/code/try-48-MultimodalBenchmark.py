import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial term with multiple minima
        r = np.sqrt(np.sum(x_scaled**2, axis=0))
        radial_term = r**2 * np.sin(5 * np.pi * r)**2
        
        # Logarithmic barrier to prevent escape from center
        log_barrier = np.sum(np.log(1 + 0.1 * x_scaled**2))
        
        # Coupled sine-wave interference creating complex terrain
        sine_interference = np.sum(np.sin(3 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled))
        
        # Combine all terms
        return 0.4 * radial_term + 0.3 * log_barrier + 0.3 * sine_interference