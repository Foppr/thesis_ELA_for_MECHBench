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
            freq = 2 ** (i % 3 + 2)  # Slightly different frequency pattern
            amp = 0.7 + 0.3 * np.sin(i * 0.5)  # Modified amplitude modulation
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Stronger interaction terms with trigonometric scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = (x[i] * x[j])**2 + (x[i] + x[j])**2
                result += 0.3 * interaction * np.sin(x[i] * x[j] * 0.3)  # Increased weight and modified scale
                
        # Higher-order polynomial chaos with mixed exponents
        for i in range(self.dim):
            result += 0.04 * x[i]**4 + 0.02 * x[i]**5 + 0.01 * x[i]**6  # Increased polynomial weights
            
        # Global minimum enforcing term with stronger penalty
        result += 0.003 * np.sum(np.abs(x)**7)  # Increased penalty strength
        
        # Complex oscillatory component with multi-dimensional coupling
        sum_x = np.sum(x)
        result += 0.5 * np.sin(2 * np.pi * sum_x) * np.cos(3 * np.pi * sum_x) * np.exp(-0.15 * sum_x**2)  # Adjusted scaling
        
        # Additional non-separable cross-term interactions
        cross_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_sum += np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        result += 0.2 * cross_sum  # Increased interaction strength
        
        return result