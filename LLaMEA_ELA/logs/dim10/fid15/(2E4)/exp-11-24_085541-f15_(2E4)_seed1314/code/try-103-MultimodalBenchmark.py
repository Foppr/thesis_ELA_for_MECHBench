import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Exponential decay with sinusoidal modulation
        for i in range(self.dim):
            result += 3.0 * np.exp(-0.5 * x[i]**2) * np.sin(10.0 * x[i])
            
        # Chaotic component using nested exponentials and trigonometric functions
        for i in range(self.dim):
            result += 2.0 * np.exp(-np.abs(x[i])) * np.cos(np.pi * np.exp(x[i]))
            
        # Polynomial cross-terms with dynamic exponents
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 1.5 * (x[i]**3 + x[j]**3) * np.sin(2.0 * x[i] * x[j])
                
        # Hyperbolic tangent with dynamic scaling
        for i in range(self.dim):
            result += 1.8 * np.tanh(x[i]) * np.cos(5.0 * x[i])
            
        # Multi-modal component with exponential peaks
        for i in range(self.dim):
            result += 2.5 * np.exp(-0.5 * (x[i] - 1.0)**2) + 1.5 * np.exp(-0.3 * (x[i] + 2.0)**2)
            
        # Dynamic conditioning based on dimensionality
        condition_factor = 1.0 + 0.8 * self.dim
        result *= condition_factor
        
        # Cross-dimensional coupling with fractional powers
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.7 * (x[i]**1.5 + x[j]**1.5) * np.cos(3.0 * (x[i] + x[j]))
                
        # Fractional chaotic sine component
        for i in range(self.dim):
            result += 1.2 * np.sin(np.pi * np.power(np.abs(x[i]), 0.7)) * np.cos(7.0 * x[i])
            
        # Logarithmic chaotic modulation
        for i in range(self.dim):
            if np.abs(x[i]) > 0.1:
                result += 0.8 * np.log(np.abs(x[i])) * np.sin(9.0 * x[i])
                
        # Polynomial interaction with exponential decay
        for i in range(self.dim):
            result += 0.6 * x[i]**4 * np.exp(-0.2 * x[i]**2)
            
        # Sine-cosine cross-dimension coupling with varying frequency
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 1.0 * np.sin(1.5 * x[i]) * np.cos(2.0 * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
                
        # Penalty for large values with logarithmic scaling
        result += 0.5 * np.sum(np.log(np.abs(x) + 1.5))
        
        return result