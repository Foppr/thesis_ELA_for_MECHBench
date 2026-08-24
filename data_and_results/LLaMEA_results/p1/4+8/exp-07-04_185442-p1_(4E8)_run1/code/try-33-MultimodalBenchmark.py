import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic = np.sum(x_norm**2)
        
        # Enhanced sinusoidal terms with modified frequencies and interactions
        sinusoidal = np.sum(np.sin(4 * np.pi * x_norm) ** 2) + 0.7 * np.sum(np.sin(6 * np.pi * x_norm) ** 2)
        
        # Add cross-terms to increase landscape complexity
        cross_terms = 0.4 * np.sum(np.sin(3 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Add cubic nonlinear terms for sharper local minima
        cubic = 0.2 * np.sum(x_norm**3)
        
        # Slight shift in global minimum to increase complexity
        shift = 0.1 * np.sum((x_norm - 0.2)**2)
        
        # Combine all terms to create enhanced multimodal landscape
        return quadratic + sinusoidal + cross_terms + cubic + shift