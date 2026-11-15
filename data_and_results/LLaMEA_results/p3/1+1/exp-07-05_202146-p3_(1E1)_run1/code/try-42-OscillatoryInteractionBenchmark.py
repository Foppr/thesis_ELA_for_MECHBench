import numpy as np

class OscillatoryInteractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term
        result = np.sum(x**2)
        
        # Enhanced periodic sinusoidal components with increased frequency diversity and amplitude modulation
        for i in range(self.dim):
            freq = 2 ** (i % 5 + 2)
            amp = 1.0 + 0.3 * np.sin(i * 0.7)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
            
        # Stronger interaction terms with multi-scale trigonometric coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = (x[i] * x[j])**2 + (x[i] + x[j])**2
                result += 0.3 * interaction * np.sin(x[i] * x[j] * 0.7) * np.cos(x[i] - x[j])
                
        # Higher-order polynomial chaos with mixed exponents and cross-terms
        for i in range(self.dim):
            result += 0.05 * x[i]**4 + 0.025 * x[i]**5 + 0.01 * x[i]**6
            
        # Global minimum enforcing term with exponential penalty
        result += 0.005 * np.sum(np.abs(x)**8)
        
        # Complex oscillatory component with multi-dimensional coupling and variable phase shifts
        sum_x = np.sum(x)
        result += 0.6 * np.sin(3 * np.pi * sum_x) * np.cos(4 * np.pi * sum_x) * np.exp(-0.15 * sum_x**2)
        
        # Additional non-separable cross-term interactions with enhanced complexity
        cross_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_sum += np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        result += 0.25 * cross_sum
        
        # Introduce additional multimodal components with sharp local optima
        multimodal = 0
        for i in range(self.dim):
            multimodal += 0.5 * np.sin(5 * x[i]) * np.cos(3 * x[i]) + 0.3 * np.sin(7 * x[i])
        result += multimodal
        
        return result