import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal component with self-similar structure using multiple sine waves at different scales
        fractal_term = 0.0
        for i in range(1, min(6, self.dim + 1)):
            scale = 2 ** i
            fractal_term += np.sum(np.sin(scale * np.pi * x_norm) * 
                                 np.cos(scale * np.pi * x_norm) * 
                                 np.exp(-0.1 * scale * np.abs(x_norm)))
        
        # Logarithmic scaling component that increases complexity with dimensionality
        log_term = np.sum(np.log(1 + np.abs(x_norm)) * np.sin(3 * np.pi * x_norm))
        
        # Adaptive ridge formation with dimension-dependent weights
        ridge_term = 0.0
        for i in range(self.dim - 1):
            weight = (i + 1) / self.dim
            ridge_term += weight * np.exp(-0.5 * (x_norm[i] - x_norm[i+1])**2) * \
                         np.sin(4 * np.pi * (x_norm[i] + x_norm[i+1]))
        
        # Multi-scale oscillatory component with varying frequencies and amplitudes
        oscillatory_term = 0.0
        for freq in [1, 2, 3, 5, 7]:
            oscillatory_term += np.sum(np.sin(freq * x_norm) * 
                                     np.cos(freq * x_norm) * 
                                     np.exp(-0.05 * freq**2 * np.abs(x_norm)))
        
        # Combined fitness with dynamic global scaling
        combined = fractal_term + log_term + ridge_term + oscillatory_term
        
        # Add dimensionality-dependent bias and noise
        dim_bias = 0.1 * self.dim * np.sum(np.sin(x_norm))
        noise = 0.01 * np.random.rand()
        
        return combined + dim_bias + noise