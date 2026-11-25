import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Polynomial basin term
        basin_term = np.sum(x_norm**4, axis=1)
        
        # Sinusoidal oscillation component with chaotic behavior
        oscillation_term = np.zeros(x.shape[0])
        
        # Use chaotic sequence for frequency modulation
        for i in range(1, self.dim + 1):
            freq = 2.0 * np.pi * (i + np.sin(i))
            oscillation_term += np.sin(freq * x_norm[:, i-1]) * np.cos(freq * x_norm[:, i-1])
        
        # Radial component with varying intensity
        radial = np.sum(x_norm**2, axis=1)
        radial_term = 0.5 * np.sin(3.0 * radial) * np.exp(-0.1 * radial)
        
        # Combine all terms with adaptive weights
        return basin_term + 0.3 * oscillation_term + 0.2 * radial_term