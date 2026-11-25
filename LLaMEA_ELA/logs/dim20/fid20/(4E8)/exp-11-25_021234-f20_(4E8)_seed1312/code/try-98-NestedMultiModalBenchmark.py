import numpy as np

class NestedMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial with varying degrees to create structured valleys
        f1 = np.sum(0.5 * x**6 + 0.3 * x**4 + 0.2 * x**2)
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        f2 = np.sum(np.sin(10.0 * x) * np.cos(5.0 * x) * np.exp(-0.1 * x**2))
        
        # Polynomial barriers with exponential damping to create local minima
        f3 = np.sum((x**2 + 0.5)**(-2.0) * np.exp(-0.2 * np.abs(x)))
        
        # Nested multi-scale structure with harmonic components
        f4 = np.sum(np.sin(20.0 * x) * np.cos(15.0 * x) * np.exp(-0.05 * x**2) + 
                    np.sin(35.0 * x) * np.cos(25.0 * x) * np.exp(-0.03 * x**2))
        
        # Chaotic sine modulation with varying phase shifts
        f5 = np.sum(np.sin(50.0 * x + np.sin(10.0 * x)) * np.exp(-0.1 * np.abs(x)))
        
        # Logarithmic-like structure with controlled ruggedness
        f6 = np.sum(np.log(np.abs(x) + 1.0) * np.sin(25.0 * x))
        
        # Fractional polynomial terms to introduce non-smooth behavior
        f7 = np.sum(x**3.2 + x**2.7 + x**1.8)
        
        # Multi-scale exponential damping with sinusoidal modulation
        f8 = np.sum(np.exp(-0.5 * x**2) * np.sin(40.0 * x) * np.cos(30.0 * x))
        
        # Combine all components with carefully tuned weights
        return 1.0 * f1 + 0.7 * f2 + 0.6 * f3 + 0.5 * f4 + 0.4 * f5 + 0.3 * f6 + 0.2 * f7 + 0.1 * f8