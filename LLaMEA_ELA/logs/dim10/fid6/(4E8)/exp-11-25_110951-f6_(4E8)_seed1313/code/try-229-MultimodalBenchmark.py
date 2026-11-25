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
            term1 = np.sin(2.5 * np.pi * x_norm[i])
            term2 = np.sin(5.0 * np.pi * x_norm[i])
            term3 = np.sin(10.0 * np.pi * x_norm[i])
            
            # Combine with fractal-like scaling and added nonlinearity
            scaled_term = (term1 + 0.3 * term2 + 0.05 * term3) / (1.0 + 0.15 * np.abs(x_norm[i]) + 0.03 * x_norm[i]**2)
            
            # Add enhanced cross-dimensional coupling with chaotic interactions
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling += np.sin(3.5 * np.pi * (x_norm[i] - x_norm[j])) * \
                               np.cos(2.5 * np.pi * (x_norm[i] + x_norm[j])) * \
                               np.exp(-0.3 * (x_norm[i] - x_norm[j])**2)
            
            result += scaled_term + 0.35 * coupling
        
        # Add enhanced harmonic modulation with varying amplitudes and phases
        harmonic_mod = 0.0
        for i in range(self.dim):
            harmonic_mod += np.sin(12 * x_norm[i]) * np.cos(18 * x_norm[i]) + \
                           0.25 * np.sin(25 * x_norm[i]) * np.cos(30 * x_norm[i]) + \
                           0.08 * np.sin(35 * x_norm[i])
        
        # Add more complex noise-like perturbations
        noise = 0.0
        for i in range(self.dim):
            noise += 0.12 * np.sin(50 * x_norm[i]) + 0.06 * np.cos(70 * x_norm[i]) + \
                    0.04 * np.sin(90 * x_norm[i]) * np.cos(110 * x_norm[i])
        
        return result + 0.25 * harmonic_mod + 0.12 * noise