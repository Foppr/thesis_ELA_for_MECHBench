import numpy as np

class ExponentialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Add exponentially decaying harmonic terms with radial symmetry
        for i in range(1, min(self.dim + 1, 20)):
            # Radial distance from origin
            r = np.sqrt(np.sum(x**2))
            
            # Exponentially decaying amplitude with harmonic modulation
            amplitude = np.exp(-i * 0.3) * (1.0 + 0.5 * np.sin(i * r))
            
            # Harmonic component with dimensionally adaptive frequency
            freq = i * 2.0 + 0.5 * np.sin(r * 0.2)
            harmonic = np.sin(freq * x[i-1]) * np.cos(freq * x[i-1] * 0.7)
            
            result += amplitude * harmonic
        
        # Add radial multi-modal component with exponentially increasing frequencies
        radial_term = 0.0
        for i in range(1, min(self.dim + 1, 15)):
            r = np.sqrt(np.sum(x**2))
            freq = 3.0 * np.exp(i * 0.4)
            radial_term += np.sin(freq * r) * np.cos(freq * r * 0.3)
        
        # Add dimensionally adaptive ruggedness
        ruggedness = 0.0
        for i in range(self.dim):
            ruggedness += np.sin(10 * x[i]) * np.cos(8 * x[i]) * np.sin(6 * x[i])
        
        # Combine all terms with dimensionality scaling
        dim_scaling = 1.0 + 0.5 * np.log(self.dim + 1)
        
        return result * dim_scaling + 0.3 * radial_term + 0.2 * ruggedness