import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced fractal component with modified sine/cosine interactions
        fractal_term = 0.0
        for i in range(1, min(7, self.dim + 1)):
            scale = 2 ** i
            fractal_term += np.sum(np.sin(scale * np.pi * x_norm) * 
                                 np.cos(scale * np.pi * x_norm) * 
                                 np.exp(-0.05 * scale * np.abs(x_norm)) * 
                                 np.log(1 + scale))
        
        # Improved logarithmic scaling with dimension-dependent adjustment
        log_term = np.sum(np.log(1 + np.abs(x_norm)) * 
                         np.sin(2 * np.pi * x_norm) * 
                         np.exp(-0.1 * np.abs(x_norm)))
        
        # Enhanced ridge formation with non-linear weight adjustments
        ridge_term = 0.0
        for i in range(self.dim - 1):
            weight = (i + 1) / self.dim
            ridge_term += weight * np.exp(-0.3 * (x_norm[i] - x_norm[i+1])**2) * \
                         np.sin(6 * np.pi * (x_norm[i] + x_norm[i+1])) * \
                         np.cos(2 * np.pi * (x_norm[i] - x_norm[i+1]))
        
        # Refined oscillatory component with adaptive frequency weights
        oscillatory_term = 0.0
        frequencies = [1, 2, 3, 4, 6, 8]
        for i, freq in enumerate(frequencies):
            weight = (i + 1) / len(frequencies)
            oscillatory_term += np.sum(weight * np.sin(freq * x_norm) * 
                                     np.cos(freq * x_norm) * 
                                     np.exp(-0.03 * freq**2 * np.abs(x_norm)))
        
        # Combined fitness with improved global scaling
        combined = fractal_term + log_term + ridge_term + oscillatory_term
        
        # Enhanced dimensionality-dependent bias and structured noise
        dim_bias = 0.15 * self.dim * np.sum(np.sin(2 * x_norm))
        noise = 0.005 * np.random.rand()
        
        return combined + dim_bias + noise