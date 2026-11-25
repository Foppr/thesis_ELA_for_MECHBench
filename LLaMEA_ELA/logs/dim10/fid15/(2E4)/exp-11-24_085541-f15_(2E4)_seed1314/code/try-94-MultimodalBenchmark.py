import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Tent map chaotic component with varying parameter
        for i in range(self.dim):
            tent = 0.0
            a = 1.8
            xi = x[i]
            for _ in range(10):
                if xi < 0.5:
                    xi = a * xi
                else:
                    xi = a * (1 - xi)
            result += 2.0 * xi**2 - 1.0
            
        # Fractional polynomial interactions with adaptive exponents
        for i in range(self.dim):
            alpha = 1.0 + 0.3 * np.sin(i)
            result += 1.5 * np.abs(x[i])**alpha + 0.8 * x[i]**(alpha + 0.5)
            
        # Adaptive sinusoidal modulations with frequency scaling
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.cos(i)
            result += 3.0 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) + 1.2 * np.sin(freq * x[i]**2)
            
        # Cross-dimensional coupling with fractional powers
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.5 * (x[i]**1.3 + x[j]**1.7) * np.sin(0.8 * x[i] * x[j])
                
        # Multi-modal polynomial with varying coefficients
        for i in range(self.dim):
            result += 0.4 * x[i]**6 - 0.8 * x[i]**5 + 0.3 * x[i]**4 - 0.2 * x[i]**3
            
        # Complex cross-dimensional interactions with hyperbolic functions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.7 * np.sinh(x[i] + x[j]) * np.cos(1.5 * (x[i]**2 - x[j]**2))
                
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.5 * self.dim
        result *= condition_factor
        
        # Recursive chaotic component with sine and cosine combinations
        for i in range(self.dim):
            recursive_term = 0.0
            for k in range(1, 12):
                recursive_term += 0.3**k * np.sin(3**k * x[i])
            result += recursive_term
            
        # Penalty term with logarithmic scaling
        result += 0.8 * np.sum(np.log(np.abs(x) + 1.5))
        
        # Multi-scale sinusoidal oscillations
        for i in range(self.dim):
            result += 2.5 * np.sin(4.0 * x[i]) * np.cos(3.0 * x[i]) * np.tan(2.0 * x[i])
            
        # Modified fractional chaotic component with tent-like behavior
        for i in range(self.dim):
            result += 1.2 * np.sin(np.pi * np.power(np.abs(x[i]), 1.4)) * np.cos(5.0 * x[i])
            
        return result