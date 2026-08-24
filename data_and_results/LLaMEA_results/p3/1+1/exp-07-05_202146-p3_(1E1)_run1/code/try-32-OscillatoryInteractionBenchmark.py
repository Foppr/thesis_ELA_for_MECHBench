import numpy as np

class OscillatoryInteractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term with conditioning
        result = np.sum(x**2) * (1.0 + 0.1 * np.sum(np.abs(x)))
        
        # Chaotic sinusoidal components with irrational frequencies
        for i in range(self.dim):
            freq = np.pi * (i + 1) * np.sqrt(2)
            amp = 1.0 + 0.3 * np.sin(i * np.pi / 3)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
            
        # Stronger interaction terms with exponential scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = (x[i] * x[j])**2 + (x[i] + x[j])**2
                result += 0.3 * interaction * np.exp(-0.5 * np.abs(x[i] - x[j]))
                
        # Higher-order polynomial chaos with mixed exponents and variable coefficients
        for i in range(self.dim):
            coeff = 0.05 + 0.02 * np.sin(i * np.pi / 4)
            result += coeff * (x[i]**4 + 0.5 * x[i]**5 + 0.2 * x[i]**6)
            
        # Global minimum enforcing term with multi-modal penalty
        result += 0.005 * np.sum(np.abs(x)**8) + 0.003 * np.sum(np.sin(0.5 * x)**2)
        
        # Complex multi-dimensional coupling with fractal-like behavior
        sum_x = np.sum(x)
        result += 0.5 * np.sin(3 * np.pi * sum_x) * np.cos(4 * np.pi * sum_x) * np.exp(-0.2 * sum_x**2)
        
        # Additional non-separable cross-term interactions with chaotic coupling
        cross_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_sum += np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * np.exp(-0.1 * np.abs(x[i] - x[j]))
        result += 0.2 * cross_sum
        
        # Add a highly oscillatory component with chaotic phase modulation
        phase = np.sum(np.sin(x) * np.cos(x * 0.5))
        result += 0.3 * np.sin(10 * phase) * np.cos(15 * phase) * np.exp(-0.05 * np.sum(x**2))
        
        return result