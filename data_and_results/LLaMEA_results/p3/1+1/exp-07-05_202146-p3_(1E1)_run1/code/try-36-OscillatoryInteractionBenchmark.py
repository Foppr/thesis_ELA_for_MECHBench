import numpy as np

class OscillatoryInteractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Fractional polynomial chaos with non-integer exponents
        for i in range(self.dim):
            result += 0.02 * np.abs(x[i])**1.7 + 0.01 * np.abs(x[i])**2.3
            
        # Chaotic oscillatory components with dynamic frequencies
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(i * 0.7)
            amp = 1.0 + 0.5 * np.cos(i * 0.3)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
            
        # Strong non-separable cross-interactions with exponential scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.exp(-0.5 * (x[i]**2 + x[j]**2)) * (x[i] * x[j])**3
                result += 0.3 * interaction * np.sin(x[i] + x[j])
                
        # Multi-scale periodic components with varying amplitudes
        for i in range(self.dim):
            for k in range(1, 5):
                result += 0.1 * np.sin(k * x[i]) * np.cos(k * x[i] * 0.3) * np.exp(-0.1 * k)
                
        # Hyperbolic and logarithmic interaction terms
        log_sum = 0.0
        for i in range(self.dim):
            log_sum += np.log(1.0 + np.abs(x[i]))
        result += 0.2 * log_sum**2
        
        # Global optimum enforcing with high-order penalties
        result += 0.005 * np.sum(np.abs(x)**8)
        
        # Complex coupling with multi-dimensional trigonometric products
        product_sum = 1.0
        for i in range(self.dim):
            product_sum *= (1.0 + 0.5 * np.sin(x[i]))
        result += 0.5 * np.cos(2 * np.pi * product_sum)
        
        # Additional non-smooth landscape with step-like transitions
        step_term = 0.0
        for i in range(self.dim):
            step_term += np.floor(np.abs(x[i]) * 10.0) * np.sin(x[i])
        result += 0.1 * step_term
        
        return result