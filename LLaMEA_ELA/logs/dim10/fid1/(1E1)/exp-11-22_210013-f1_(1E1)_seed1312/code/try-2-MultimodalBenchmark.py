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
            sinusoidal += np.sin(5 * x[i]) * np.exp(-0.1 * (x[i] - 1)**2)
        
        # Additional multimodal term with cross-interactions
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.5 * np.sin(3 * x[i]) * np.cos(2 * x[(i + 1) % self.dim])
            multimodal += 0.1 * x[i] * x[(i + 1) % self.dim]  # Cross-term interaction
        
        return quadratic + sinusoidal + multimodal