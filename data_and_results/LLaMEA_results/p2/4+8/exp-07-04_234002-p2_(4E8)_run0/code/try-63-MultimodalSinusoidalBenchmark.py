import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function with sinusoidal components
        result = 0.0
        
        # Main sinusoidal contribution with modified frequencies and added quintic term
        for i in range(self.dim):
            result += 0.8 * np.sin(1.5 * x[i]) * np.cos(0.7 * x[i]) + 0.15 * x[i]**3 + 0.02 * x[i]**5
            
        # Add interaction terms between dimensions with different coefficients and higher-order terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * np.sin(1.8 * x[i]) * np.sin(1.1 * x[j]) + 0.02 * x[i]**2 * x[j] + 0.01 * x[i] * x[j]**2
                
        # Add chaotic perturbations for increased complexity
        chaotic_factor = 0.0
        for i in range(self.dim):
            chaotic_factor += 0.03 * np.sin(3.0 * x[i] + 0.5 * np.sin(7.0 * x[i]))
            
        # Add fractal-like perturbations
        fractal_factor = 0.0
        for i in range(self.dim):
            fractal_factor += 0.02 * np.sin(2.0 * x[i]) * np.cos(4.0 * x[i]) * np.sin(0.5 * x[i]**2)
            
        # Add a global scaling factor with additional quadratic, quartic, and sextic terms for better conditioning
        scaling = 1.0 + 0.15 * np.sum(x**2) + 0.05 * np.sum(x**4) + 0.015 * np.sum(x**6)
        
        result = result * scaling + chaotic_factor + fractal_factor
        
        return result