import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base quadratic term for global attraction
        quadratic = np.sum(x_scaled**2)
        
        # Fractal-like component with recursive sine terms
        fractal = np.sum(np.sin(20 * np.pi * x_scaled) * np.cos(15 * np.pi * x_scaled)**2)
        
        # Logarithmic barrier terms creating fine-scale structure
        barriers = np.sum(np.log(1 + 5 * np.abs(x_scaled)) * np.sin(5 * np.pi * x_scaled)**2)
        
        # Gradient mixing using higher-order polynomial terms
        gradient_mix = np.sum(x_scaled**6 - 3 * x_scaled**4 + 2 * x_scaled**2)
        
        # Combine all components with different weights
        return 0.3 * quadratic + 1.8 * fractal + 1.2 * barriers + 0.5 * gradient_mix