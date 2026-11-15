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
            result += 1.5 * np.sin(1.7 * x[i]) * np.cos(1.1 * x[i]) + 0.4 * x[i]**2 + 0.08 * x[i]**3 + 0.01 * x[i]**5
            
        # Add interaction terms between dimensions with different coefficients and additional coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.sin(2.1 * x[i]) * np.sin(1.5 * x[j]) + 0.03 * x[i] * x[j] + 0.015 * np.sin(2.5 * x[i] + 0.8 * x[j])
                
        # Add a global scaling factor with additional quadratic, quartic and sextic terms
        result = result * (1.0 + 0.4 * np.sum(x**2) + 0.15 * np.sum(x**4) + 0.05 * np.sum(x**6) + 0.008 * np.sum(x**8))
        
        # Add fractal-like perturbations to increase complexity
        fractal_factor = 1.0
        for i in range(self.dim):
            fractal_factor += 0.05 * np.sin(15.0 * x[i]) * np.cos(10.0 * x[i]) + 0.02 * np.sin(18.0 * x[i]) + 0.01 * np.sin(20.0 * x[i])**2
            
        result = result * fractal_factor
        
        # Add chaotic structures for further complexity
        chaotic_factor = 1.0
        for i in range(self.dim):
            chaotic_factor += 0.02 * np.sin(25.0 * x[i] + 0.5 * np.sin(30.0 * x[i])) + 0.01 * np.cos(35.0 * x[i])
            
        result = result * chaotic_factor
        
        return result