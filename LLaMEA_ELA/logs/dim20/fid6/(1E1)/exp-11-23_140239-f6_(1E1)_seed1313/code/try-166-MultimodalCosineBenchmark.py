import numpy as np

class MultimodalCosineBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin with quadratic basin
        result = 0.1 * np.sum(x**2)
        
        # Add multiple cosine-based harmonic terms with varying frequencies and amplitudes
        for i in range(1, min(self.dim + 1, 20)):
            freq = i * 2.0
            amp = 5.0 / (i * 1.5)
            result += amp * np.cos(freq * x[i-1]) * np.exp(-0.1 * x[i-1]**2)
        
        # Add radial symmetry component with multiple peaks
        r = np.sqrt(np.sum(x**2))
        radial_term = 3.0 * np.sin(5.0 * r) * np.cos(3.0 * r) * np.exp(-0.05 * r**2)
        result += radial_term
        
        # Add cross-dimensional coupling with sine-based interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        result += 2.0 * coupling
        
        # Add periodic modulation based on dimensionality
        dim_mod = 1.0 + 0.5 * np.sin(self.dim * 0.5)
        
        # Add noise component for increased ruggedness
        noise = 0.3 * np.sum(np.sin(10 * x) * np.cos(7 * x))
        
        return result * dim_mod + noise