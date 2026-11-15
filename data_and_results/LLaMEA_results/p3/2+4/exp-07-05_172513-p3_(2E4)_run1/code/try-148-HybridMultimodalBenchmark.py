import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Separable quadratic component for global structure
        quadratic = np.sum(x_scaled**2)
        
        # Non-separable sine-cosine interaction terms
        sine_cosine = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                sine_cosine += np.sin(10 * np.pi * x_scaled[i]) * np.cos(8 * np.pi * x_scaled[j])
        
        # Chaotic tent map component for local complexity
        tent = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            if xi < 0.5:
                tent += 2.0 * xi
            else:
                tent += 2.0 * (1.0 - xi)
        
        # High-frequency oscillation component
        oscillation = np.sum(np.sin(50 * x_scaled) * np.cos(40 * x_scaled))
        
        # Asymmetric barrier terms
        barriers = np.sum(2.0 * np.exp(-3.0 * np.abs(x_scaled)) * (1.0 + np.sin(15 * x_scaled)**2))
        
        # Coupling between adjacent dimensions with cubic interaction
        coupling = np.sum(x_scaled[:-1]**3 * x_scaled[1:]**2)
        
        # Combined fitness function with carefully balanced weights
        return 0.5 * quadratic + 2.5 * sine_cosine + 0.8 * tent + 1.5 * oscillation + 1.2 * barriers + 0.3 * coupling