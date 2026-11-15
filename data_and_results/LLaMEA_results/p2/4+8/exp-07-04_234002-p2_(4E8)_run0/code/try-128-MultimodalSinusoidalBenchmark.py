import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function with enhanced sinusoidal components
        result = 0.0
        
        # Main sinusoidal contribution with nested frequencies, cubic, quintic and septic terms
        for i in range(self.dim):
            result += 1.5 * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i]) * np.sin(0.7 * x[i]) + \
                      0.4 * x[i]**2 + 0.08 * x[i]**3 + 0.01 * x[i]**5 + 0.002 * x[i]**7
            
        # Add complex interaction terms between dimensions with nested coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.sin(2.5 * x[i]) * np.sin(1.8 * x[j]) * np.cos(0.9 * x[i] + 0.6 * x[j]) + \
                          0.03 * x[i]**2 * x[j] + 0.02 * x[i] * x[j]**2 + \
                          0.015 * np.sin(3.0 * x[i] + 1.2 * x[j]) * np.cos(1.4 * x[i] - 0.8 * x[j])
                
        # Add a dynamic scaling factor with polynomial and logarithmic components
        poly_term = 1.0 + 0.5 * np.sum(x**2) + 0.2 * np.sum(x**4) + 0.08 * np.sum(x**6) + 0.02 * np.sum(x**8)
        log_term = np.log(1.0 + 0.2 * np.sum(x**2))
        adaptive_scale = poly_term * (1.0 + 0.1 * log_term)
        
        # Add fractal-like chaotic perturbations with multiple frequency components
        chaotic_factor = 1.0
        for i in range(self.dim):
            chaotic_factor += 0.05 * np.sin(20.0 * x[i]) * np.cos(17.0 * x[i]) + \
                              0.025 * np.sin(35.0 * x[i]) + \
                              0.015 * np.sin(40.0 * x[i]**2) + \
                              0.01 * np.cos(25.0 * x[i]) * np.sin(12.0 * x[i]**3)
            
        result = result * adaptive_scale * chaotic_factor
        
        # Add a final high-order polynomial correction term
        result += 0.005 * np.sum(x**10) + 0.001 * np.sum(x**12)
        
        return result