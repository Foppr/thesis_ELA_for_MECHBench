import numpy as np

class AsymmetricMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with asymmetric scaling
        poly_term = np.sum((x * (1.0 + 0.1 * np.abs(x)))**4)
        
        # Radial sinusoidal modulation with varying frequency
        r = np.sqrt(np.sum(x**2))
        radial_mod = np.sin(3.0 * r) * np.cos(2.0 * r) * np.exp(-0.1 * r)
        
        # Directional bias with trigonometric components
        direction_bias = 0.0
        for i in range(self.dim):
            direction_bias += np.sin(x[i] * (i + 1)) * np.cos(x[i] * 0.5 * (i + 1))
        
        # Cross-dimensional interaction with asymmetric coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j] * 0.1)
        
        # Additional multimodal component with exponential decay
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += np.exp(-0.5 * (x[i] - 2.0)**2) + np.exp(-0.5 * (x[i] + 2.0)**2)
        
        # Final combination with weighted components
        result = 0.1 * poly_term + 0.3 * radial_mod + 0.2 * direction_bias + 0.2 * cross_term + 0.2 * multi_modal
        
        return result