import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add chaotic sinusoidal components with exponential decay
        for i in range(self.dim):
            result += 2.0 * np.sin(np.exp(0.5 * x[i])) * np.cos(np.exp(0.3 * x[i]))
            
        # Add polynomial chaos with fractional exponents
        for i in range(self.dim):
            result += 0.5 * (x[i]**3.5 + x[i]**2.7 + x[i]**1.3)
            
        # Add fractal-like recursive sine components
        for i in range(self.dim):
            recursive_sum = 0.0
            for k in range(1, 8):
                recursive_sum += (0.4 / k) * np.sin(k**2 * x[i])
            result += recursive_sum
            
        # Add cross-dimensional exponential coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                result += 0.3 * np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(x[i] * x[j])
                
        # Add dimensionally adaptive conditioning
        condition_factor = 1.0 + 0.2 * self.dim + 0.05 * np.sum(np.abs(x))
        result *= condition_factor
        
        # Add hyperbolic tangent and logarithmic oscillations
        for i in range(self.dim):
            result += 0.7 * np.tanh(x[i]) * np.sin(np.log(np.abs(x[i]) + 1))
            
        # Add multi-modal polynomial with varying coefficients
        for i in range(self.dim):
            result += 0.2 * x[i]**6 - 0.4 * x[i]**5 + 0.3 * x[i]**4 - 0.1 * x[i]**3
            
        # Add chaotic oscillations with irrational frequencies
        for i in range(self.dim):
            result += 0.6 * np.sin(np.pi * np.sqrt(2) * x[i]) * np.cos(np.e * x[i])
            
        # Add penalty term for extreme values
        result += 0.1 * np.sum(np.exp(2 * np.abs(x)) - 2)
        
        return result