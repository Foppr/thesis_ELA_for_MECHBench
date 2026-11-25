import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Iterated sine fractal construction
        result = 0.0
        for i in range(self.dim):
            # Apply multiple sine transformations with different frequencies
            term1 = np.sin(2 * np.pi * x_norm[i])
            term2 = np.sin(4 * np.pi * x_norm[i])
            term3 = np.sin(8 * np.pi * x_norm[i])
            
            # Combine with fractal-like scaling
            scaled_term = (term1 + 0.5 * term2 + 0.25 * term3) / (1.0 + 0.1 * np.abs(x_norm[i]))
            
            # Add cross-dimensional coupling with self-similarity
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling += np.sin(3 * np.pi * (x_norm[i] - x_norm[j])) * \
                               np.cos(2 * np.pi * (x_norm[i] + x_norm[j]))
            
            result += scaled_term + 0.3 * coupling
        
        # Add harmonic modulation with varying amplitudes
        harmonic_mod = 0.0
        for i in range(self.dim):
            harmonic_mod += np.sin(10 * x_norm[i]) * np.cos(15 * x_norm[i]) + \
                           0.5 * np.sin(20 * x_norm[i]) * np.cos(25 * x_norm[i])
        
        # Add noise-like perturbations for increased complexity
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(50 * x_norm[i]) + 0.05 * np.cos(75 * x_norm[i])
        
        return result + 0.2 * harmonic_mod + 0.1 * noise