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
            result += 2.3 * np.sin(2.2 * x[i]) * np.cos(1.3 * x[i]) + 0.65 * x[i]**2 + 0.16 * x[i]**3 + 0.025 * x[i]**5
            
        # Add interaction terms between dimensions with different coefficients and additional coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.22 * np.sin(2.7 * x[i]) * np.sin(2.2 * x[j]) + 0.055 * x[i] * x[j] + 0.035 * np.sin(3.2 * x[i] + 1.1 * x[j])
                
        # Add a global scaling factor with additional quadratic, quartic and sextic terms
        result = result * (1.0 + 0.65 * np.sum(x**2) + 0.27 * np.sum(x**4) + 0.11 * np.sum(x**6) + 0.022 * np.sum(x**8))
        
        # Add logarithmic scaling term to increase conditioning difficulty
        log_term = 1.0 + 0.05 * np.sum(np.log(np.abs(x) + 1.0))
        result = result * log_term
        
        # Add fractal-like perturbations to increase complexity
        fractal_factor = 1.0
        for i in range(self.dim):
            fractal_factor += 0.09 * np.sin(27.0 * x[i]) * np.cos(22.0 * x[i]) + 0.045 * np.sin(42.0 * x[i]) + 0.025 * np.sin(52.0 * x[i])
            
        result = result * fractal_factor
        
        # Add chaotic structures for increased complexity
        chaotic_factor = 1.0
        for i in range(self.dim):
            chaotic_factor += 0.035 * np.sin(105.0 * x[i]) * np.cos(85.0 * x[i]) + 0.017 * np.sin(125.0 * x[i])
            
        result = result * chaotic_factor
        
        return result