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
            result += 2.1 * np.sin(2.0 * x[i]) * np.cos(1.2 * x[i]) + 0.6 * x[i]**2 + 0.15 * x[i]**3 + 0.02 * x[i]**5
            
        # Add interaction terms between dimensions with different coefficients and additional coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * np.sin(2.5 * x[i]) * np.sin(2.0 * x[j]) + 0.05 * x[i] * x[j] + 0.03 * np.sin(3.0 * x[i] + 1.0 * x[j])
                
        # Add a global scaling factor with additional quadratic, quartic and sextic terms
        result = result * (1.0 + 0.6 * np.sum(x**2) + 0.25 * np.sum(x**4) + 0.1 * np.sum(x**6) + 0.02 * np.sum(x**8))
        
        # Add fractal-like perturbations to increase complexity
        fractal_factor = 1.0
        for i in range(self.dim):
            fractal_factor += 0.08 * np.sin(25.0 * x[i]) * np.cos(20.0 * x[i]) + 0.04 * np.sin(40.0 * x[i]) + 0.02 * np.sin(50.0 * x[i])
            
        result = result * fractal_factor
        
        # Add chaotic structures for increased complexity
        chaotic_factor = 1.0
        for i in range(self.dim):
            chaotic_factor += 0.03 * np.sin(100.0 * x[i]) * np.cos(80.0 * x[i]) + 0.015 * np.sin(120.0 * x[i])
            
        result = result * chaotic_factor
        
        # NEW: Hybrid chaotic-logarithmic perturbation mechanism
        log_perturbation = 0.0
        for i in range(self.dim):
            log_perturbation += 0.02 * np.log(1.0 + np.abs(x[i])) * np.sin(50.0 * x[i]) + 0.01 * np.log(1.0 + np.abs(x[i])) * np.cos(70.0 * x[i])
            
        result = result + log_perturbation
        
        # NEW: Enhanced cross-dimensional coupling with exponential interactions
        exp_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_coupling += 0.05 * np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(10.0 * (x[i] + x[j]))
                
        result = result + exp_coupling
        
        return result