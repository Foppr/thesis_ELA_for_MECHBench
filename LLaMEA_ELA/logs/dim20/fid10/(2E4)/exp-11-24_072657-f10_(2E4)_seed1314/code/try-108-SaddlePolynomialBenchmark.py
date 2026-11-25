import numpy as np

class SaddlePolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial terms with mixed degrees to create varied curvature
        poly_terms = np.sum(x_norm**4 + 0.5 * x_norm**3 - 0.3 * x_norm**2 + 0.1 * x_norm)
        
        # Saddle point structure with hyperbolic tangent interactions
        saddle_terms = np.sum(np.tanh(x_norm[:-1] * x_norm[1:]) * 
                             (x_norm[:-1]**2 - x_norm[1:]**2))
        
        # Adaptive noise based on dimensionality and position
        noise_amp = 0.01 * (1 + 0.5 * np.log(self.dim + 1))
        adaptive_noise = noise_amp * np.random.random() * np.cos(np.sum(x_norm**2))
        
        # Cross-dimensional coupling with exponential decay
        coupling = np.sum(np.exp(-0.5 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                         (x_norm[:-1] + x_norm[1:]) * 
                         np.sin(3.0 * (x_norm[:-1] - x_norm[1:])))
        
        # High-frequency oscillatory component for fine structure
        oscillatory = np.sum(np.sin(10.0 * x_norm) * np.cos(7.0 * x_norm) * 
                           np.exp(-0.3 * np.abs(x_norm)))
        
        # Combined function with weighted components
        result = 0.8 * poly_terms + 0.6 * saddle_terms + 0.4 * coupling + 0.3 * oscillatory
        
        return result + adaptive_noise