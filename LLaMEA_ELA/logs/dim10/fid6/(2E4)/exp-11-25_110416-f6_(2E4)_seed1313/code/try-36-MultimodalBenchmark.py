import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add exponentially decaying sinusoidal components with varying frequencies
        for i in range(self.dim):
            freq = 3 ** (i % 4 + 1)
            decay = np.exp(-0.15 * np.abs(x[i]))
            result += decay * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.2)
            
        # Add adaptive polynomial penalties with modified exponents and coefficients
        for i in range(self.dim):
            power = 3 + (i % 3)
            result += 0.35 * (x[i] - 1.5)**power + 0.25 * (x[i] + 1.5)**(power + 1)
            
        # Add a complex global minimum structure with multiple peaks
        for i in range(self.dim):
            result += 0.08 * np.exp(-0.5 * ((x[i] - 1.5) / 0.4)**2) * np.sin(20 * x[i])
            
        # Add cross-dimensional coupling with stronger interaction strength and different pattern
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                interaction = (x[i]**2 * x[j] + x[i] * x[j]**2) * np.sin(x[i] + x[j])
                result += 0.04 * interaction
                
        # Add a chaotic component with nested sinusoidal patterns and altered scaling
        chaotic_term = 0.06 * np.sum(np.sin(17 * x) * np.cos(9 * x))
        result += chaotic_term
        
        return result