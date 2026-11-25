import numpy as np

class RadialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Center basin term
        basin = 0.1 * np.sum(x**2)
        
        # Radial sinusoidal wells
        wells = 0.0
        radius = np.sqrt(np.sum(x**2))
        
        # Create multiple radial wells with different frequencies
        for i in range(1, 6):
            freq = i * 2 * np.pi
            # Add exponentially decaying sinusoidal wells
            well_contribution = np.exp(-radius / (2.0 * i)) * np.sin(freq * radius)
            wells += well_contribution
        
        # Add a small noise term to make it non-trivial
        noise = 0.01 * np.sum(np.sin(x))
        
        return basin - wells + noise