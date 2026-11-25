import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Iterated sine fractal construction with modified frequencies
        result = 0.0
        for i in range(self.dim):
            # Apply multiple sine transformations with different frequencies
            term1 = np.sin(3 * np.pi * x_norm[i])
            term2 = np.sin(6 * np.pi * x_norm[i])
            term3 = np.sin(12 * np.pi * x_norm[i])
            
            # Combine with fractal-like scaling and added nonlinearity
            scaled_term = (term1 + 0.4 * term2 + 0.1 * term3) / (1.0 + 0.2 * np.abs(x_norm[i]) + 0.05 * x_norm[i]**2)
            
            # Add enhanced cross-dimensional coupling with chaotic interactions
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling += np.sin(4 * np.pi * (x_norm[i] - x_norm[j])) * \
                               np.cos(3 * np.pi * (x_norm[i] + x_norm[j])) * \
                               np.exp(-0.5 * (x_norm[i] - x_norm[j])**2)
            
            result += scaled_term + 0.45 * coupling
        
        # Add enhanced harmonic modulation with varying amplitudes and phases
        harmonic_mod = 0.0
        for i in range(self.dim):
            harmonic_mod += np.sin(15 * x_norm[i]) * np.cos(20 * x_norm[i]) + \
                           0.3 * np.sin(30 * x_norm[i]) * np.cos(35 * x_norm[i]) + \
                           0.1 * np.sin(40 * x_norm[i])
        
        # Add more complex noise-like perturbations with modified weights
        noise = 0.0
        for i in range(self.dim):
            noise += 0.2 * np.sin(60 * x_norm[i]) + 0.1 * np.cos(80 * x_norm[i]) + \
                    0.08 * np.sin(100 * x_norm[i]) * np.cos(120 * x_norm[i])
        
        return result + 0.35 * harmonic_mod + 0.2 * noise