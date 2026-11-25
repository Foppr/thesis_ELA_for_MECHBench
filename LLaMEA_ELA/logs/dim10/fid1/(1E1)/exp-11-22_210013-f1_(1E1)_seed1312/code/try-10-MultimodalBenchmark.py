import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term
        quadratic = 0.1 * np.sum(x**2)
        
        # Sinusoidal oscillations with multiple local minima
        sinusoidal = 0.0
        for i in range(self.dim):
            sinusoidal += np.sin(8 * x[i]) * np.exp(-0.1 * (x[i] - 1)**2)
        
        # Additional multimodal term with stronger cross-interactions
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.6 * np.sin(4 * x[i]) * np.cos(3 * x[(i + 1) % self.dim])
            multimodal += 0.25 * x[i] * x[(i + 1) % self.dim]
            multimodal += 0.12 * np.sin(2 * x[i]) * np.sin(2 * x[(i + 2) % self.dim])
        
        # Add a non-separable global structure component
        global_structure = 0.0
        for i in range(self.dim):
            global_structure += (x[i] - 2)**4
            global_structure += 0.6 * np.sin(6 * x[i]) * np.cos(5 * x[(i + 1) % self.dim])
        
        # Improved fitness with better scaling and additional complexity
        return 0.85 * quadratic + 1.3 * sinusoidal + 1.6 * multimodal + 1.1 * global_structure