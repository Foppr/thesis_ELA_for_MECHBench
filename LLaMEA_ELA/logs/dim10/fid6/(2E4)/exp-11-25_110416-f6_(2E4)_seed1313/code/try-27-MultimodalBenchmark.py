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
            decay = np.exp(-0.1 * np.abs(x[i]))
            result += decay * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
            
        # Add adaptive polynomial penalties that change based on dimension
        for i in range(self.dim):
            power = 2 + (i % 4)
            result += 0.2 * (x[i] - 1)**power + 0.15 * (x[i] + 2)**(power + 1)
            
        # Add a complex global minimum structure with multiple peaks
        for i in range(self.dim):
            result += 0.05 * np.exp(-0.5 * ((x[i] - 2.0) / 0.3)**2) * np.sin(15 * x[i])
            
        # Add cross-dimensional coupling with variable interaction strength
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                interaction = (x[i]**2 + x[j]**2) * np.cos(x[i] - x[j])
                result += 0.02 * interaction
                
        # Add a chaotic component with nested sinusoidal patterns
        chaotic_term = 0.03 * np.sum(np.sin(10 * x) * np.cos(5 * x))
        result += chaotic_term
        
        return result