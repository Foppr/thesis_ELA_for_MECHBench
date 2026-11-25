import numpy as np

class MultimodalInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Add multiple sinusoidal interference terms with varying frequencies and amplitudes
        for i in range(1, min(self.dim + 1, 6)):
            # Create interference pattern with radial component
            r = np.sqrt(np.sum(x**2))
            freq = i * 2.0
            amp = 2.0 / (i + 1)
            
            # Sinusoidal interference term
            interference = amp * np.sin(freq * r) * np.cos(freq * x[i-1] if i <= len(x) else 0)
            result += interference
            
        # Add radial basins with multiple local minima
        basin_term = 0.0
        for i in range(self.dim):
            # Create a series of radial basins with different depths
            basin_depth = 1.5 * (i + 1) / self.dim
            basin_width = 0.5 * (i + 1)
            basin_center = 2.0 * np.sin(i * 0.7)
            
            # Radial basin function
            dist_from_center = abs(x[i] - basin_center)
            basin_term += basin_depth * np.exp(-dist_from_center**2 / (2 * basin_width**2))
        
        # Add high-frequency noise to increase ruggedness
        noise = 0.3 * np.sum(np.sin(10 * x) * np.cos(7 * x))
        
        return result + basin_term + noise