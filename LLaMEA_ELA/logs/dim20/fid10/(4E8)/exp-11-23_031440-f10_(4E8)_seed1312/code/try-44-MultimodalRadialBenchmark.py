import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Convert to numpy array and ensure correct shape
        x = np.array(x)
        
        # Radial term with adaptive conditioning
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.1 * r**2
        
        # Sinusoidal perturbations with varying frequencies
        sinusoidal_term = 0.0
        for i in range(self.dim):
            # Multiple frequency components to create complex landscape
            sinusoidal_term += np.sin(2 * np.pi * x[i]) + 0.5 * np.sin(4 * np.pi * x[i]) + 0.3 * np.sin(8 * np.pi * x[i])
            
        # Nested basins with varying depths
        basin_depths = 0.0
        for i in range(self.dim):
            # Create nested structure using exponential decay and polynomial terms
            basin_depths += np.exp(-0.1 * (x[i] - 1)**2) * np.exp(-0.05 * (x[i] + 1)**2) * (1 + 0.5 * np.sin(5 * x[i]))
            
        # Adaptive conditioning based on distance from origin
        condition_factor = 1.0 + 0.5 * np.tanh(2.0 - r)
        
        # Combine all terms with adaptive scaling
        result = condition_factor * (radial_term + sinusoidal_term + basin_depths)
        
        return result