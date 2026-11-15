import numpy as np

class OscillatoryInteractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term
        result = np.sum(x**2)
        
        # Enhanced periodic sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 2 ** (i % 4 + 1)
            amp = 0.8 + 0.2 * np.sin(i)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Stronger interaction terms with trigonometric scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = (x[i] * x[j])**2 + (x[i] + x[j])**2
                result += 0.2 * interaction * np.sin(x[i] * x[j] * 0.5)
                
        # Higher-order polynomial chaos with mixed exponents
        for i in range(self.dim):
            result += 0.03 * x[i]**4 + 0.015 * x[i]**5 + 0.008 * x[i]**6
            
        # Global minimum enforcing term with stronger penalty
        result += 0.002 * np.sum(np.abs(x)**7)
        
        # Complex oscillatory component with multi-dimensional coupling
        sum_x = np.sum(x)
        result += 0.4 * np.sin(2 * np.pi * sum_x) * np.cos(3 * np.pi * sum_x) * np.exp(-0.1 * sum_x**2)
        
        # Additional non-separable cross-term interactions
        cross_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_sum += np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        result += 0.15 * cross_sum
        
        return result