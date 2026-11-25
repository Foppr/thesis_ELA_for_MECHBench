import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basin component
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.5 * r**2 * np.exp(-0.1 * r**2)
        
        # Sinusoidal oscillations in each dimension
        sin_term = np.sum(np.sin(3 * x) * np.cos(2 * x))
        
        # Cross-terms creating non-separability
        cross_term = 0.3 * np.sum(x[:-1] * x[1:]) if self.dim > 1 else 0
        
        # Additional multimodal component with multiple local minima
        multimodal = 0
        for i in range(self.dim):
            multimodal += (x[i] - np.sin(x[i]))**2 + 0.5 * np.sin(4 * x[i])**2
        
        # Combine all terms
        result = radial_term + sin_term + cross_term + multimodal
        
        return result