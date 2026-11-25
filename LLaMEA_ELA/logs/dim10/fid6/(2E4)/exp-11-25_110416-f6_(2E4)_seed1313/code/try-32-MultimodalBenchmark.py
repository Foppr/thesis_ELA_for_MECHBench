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
            
        # Add adaptive polynomial penalties with altered exponents and coefficients
        for i in range(self.dim):
            power = 3 + (i % 3)
            result += 0.3 * (x[i] - 1.5)**power + 0.2 * (x[i] + 1.8)**(power + 1)
            
        # Add a complex global minimum structure with multiple peaks
        for i in range(self.dim):
            result += 0.07 * np.exp(-0.5 * ((x[i] - 1.5) / 0.4)**2) * np.sin(20 * x[i])
            
        # Add cross-dimensional coupling with stronger interaction strength and wider range
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                interaction = (x[i]**2 + x[j]**2) * np.cos(0.5 * (x[i] - x[j]))
                result += 0.03 * interaction
                
        # Add a more chaotic component with nested sinusoidal patterns and different scaling
        chaotic_term = 0.04 * np.sum(np.sin(15 * x) * np.cos(7 * x))
        result += chaotic_term
        
        return result