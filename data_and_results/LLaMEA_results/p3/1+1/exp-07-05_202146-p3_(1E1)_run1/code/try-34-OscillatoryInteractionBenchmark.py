import numpy as np

class OscillatoryInteractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term
        result = np.sum(x**2)
        
        # Enhanced periodic sinusoidal components with higher frequency variations and amplitude modulation
        for i in range(self.dim):
            freq = 3 ** (i % 5 + 2)
            amp = 1.0 + 0.3 * np.sin(i * 0.7)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
            
        # Stronger interaction terms with multi-scale trigonometric coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = (x[i] * x[j])**3 + (x[i] + x[j])**3
                result += 0.3 * interaction * np.sin(x[i] * x[j] * 0.7) * np.cos(x[i] + x[j])
                
        # Higher-order polynomial chaos with mixed exponents and additional nonlinearity
        for i in range(self.dim):
            result += 0.05 * x[i]**4 + 0.025 * x[i]**5 + 0.012 * x[i]**6 + 0.005 * x[i]**7
            
        # Global minimum enforcing term with stronger penalty and exponential scaling
        result += 0.005 * np.sum(np.abs(x)**8) * np.exp(-0.05 * np.sum(x**2))
        
        # Complex oscillatory component with multi-dimensional coupling and dynamic phase
        sum_x = np.sum(x)
        result += 0.6 * np.sin(3 * np.pi * sum_x) * np.cos(4 * np.pi * sum_x) * np.exp(-0.15 * sum_x**2)
        
        # Additional non-separable cross-term interactions with varying coupling strengths
        cross_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_sum += np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        result += 0.25 * cross_sum
        
        # Introduce a secondary global minimum landscape with additional periodic modulation
        secondary_term = 0
        for i in range(self.dim):
            secondary_term += np.sin(0.5 * x[i]) * np.cos(0.3 * x[i]) * np.exp(-0.02 * x[i]**2)
        result += 0.1 * secondary_term**2
        
        return result