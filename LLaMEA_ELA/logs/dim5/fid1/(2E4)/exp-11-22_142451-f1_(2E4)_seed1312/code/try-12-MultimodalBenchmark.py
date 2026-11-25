import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = np.sum(x**2)
        
        # Add exponentially decaying sinusoidal terms with varying frequencies
        for i in range(self.dim):
            freq = 2 ** (i % 3)  # Frequencies 1, 2, 4
            decay = 0.5 ** (i // 3 + 1) if i >= 3 else 1.0
            result += decay * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Add cross-terms creating complex interactions between variables
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Interaction term with exponential decay based on index distance
                decay = 0.1 ** (abs(i - j) / max(1, self.dim))
                result += decay * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Add nested local minima using polynomial coupling
        for i in range(self.dim):
            result += 0.05 * (x[i]**4 - 2*x[i]**2)
            
        return result