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
        
        # Main sinusoidal contribution with increased complexity and added quintic term
        for i in range(self.dim):
            result += 1.5 * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i]) + 0.4 * x[i]**2 + 0.08 * x[i]**3 + 0.01 * x[i]**5
            
        # Add interaction terms between dimensions with enhanced coupling and additional fractal-like perturbations
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.sin(2.5 * x[i]) * np.sin(1.8 * x[j]) + 0.03 * x[i] * x[j] + 0.02 * np.sin(3.0 * x[i] + 0.8 * x[j]) + 0.005 * np.sin(10.0 * x[i] * x[j])
                
        # Add a global scaling factor with enhanced polynomial terms and modified logarithmic component
        log_term = np.log(1.0 + 0.2 * np.sum(x**2))
        result = result * (1.0 + 0.5 * np.sum(x**2) + 0.2 * np.sum(x**4) + 0.08 * np.sum(x**6) + 0.02 * np.sum(x**8) + 0.05 * log_term)
        
        # Add enhanced chaotic perturbations using a more complex fractal-like structure
        chaotic_factor = 1.0
        for i in range(self.dim):
            chaotic_factor += 0.05 * np.sin(20.0 * x[i]) * np.cos(15.0 * x[i]) + 0.02 * np.sin(30.0 * x[i]) + 0.01 * np.sin(35.0 * x[i]**2) + 0.005 * np.sin(50.0 * x[i]**3)
            
        result = result * chaotic_factor
        
        return result