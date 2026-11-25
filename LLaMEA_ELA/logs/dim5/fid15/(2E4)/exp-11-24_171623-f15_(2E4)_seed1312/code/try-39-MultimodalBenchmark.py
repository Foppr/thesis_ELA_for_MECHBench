import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial periodic component with amplitude modulation
        r = np.sqrt(np.sum(x_norm**2, axis=0))
        radial_term = np.sin(5 * r) * np.cos(3 * r) * np.exp(-0.5 * r**2)
        
        # Asymmetric oscillatory terms in each dimension
        asym_term = 0
        for i in range(self.dim):
            asym_term += (x_norm[i]**3) * np.sin(4 * x_norm[i]) * np.cos(2 * x_norm[i])
            
        # Cross-dimensional polynomial coupling with mixed powers
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim):
                for j in range(i+1, self.dim):
                    cross_term += (x_norm[i]**2) * (x_norm[j]**3) * np.sin(2 * (x_norm[i] + x_norm[j]))
                    
        # Additional harmonic interaction with varying frequencies
        freq_term = 0
        if self.dim > 1:
            for i in range(self.dim):
                for j in range(i+1, self.dim):
                    freq_term += np.cos(3 * x_norm[i]) * np.sin(5 * x_norm[j]) * np.exp(-0.2 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Final combined function with weighted components
        result = 0.3 * radial_term + 0.4 * asym_term + 0.2 * cross_term + 0.1 * freq_term
        
        return result