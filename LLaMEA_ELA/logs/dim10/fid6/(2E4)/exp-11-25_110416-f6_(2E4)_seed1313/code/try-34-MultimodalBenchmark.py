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
            freq = 2 ** (i % 5 + 1)
            decay = np.exp(-0.2 * np.abs(x[i]))
            result += decay * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
            
        # Add adaptive polynomial penalties with altered exponents and coefficients
        for i in range(self.dim):
            power = 4 + (i % 4)
            result += 0.25 * (x[i] - 1.2)**power + 0.22 * (x[i] + 1.6)**(power + 1)
            
        # Add a complex global minimum structure with multiple peaks
        for i in range(self.dim):
            result += 0.08 * np.exp(-0.5 * ((x[i] - 1.2) / 0.35)**2) * np.sin(25 * x[i])
            
        # Add cross-dimensional coupling with stronger interaction strength and wider range
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                interaction = (x[i]**2 + x[j]**2) * np.cos(0.4 * (x[i] - x[j]))
                result += 0.04 * interaction
                
        # Add a more chaotic component with nested sinusoidal patterns and different scaling
        chaotic_term = 0.05 * np.sum(np.sin(18 * x) * np.cos(9 * x))
        result += chaotic_term
        
        return result