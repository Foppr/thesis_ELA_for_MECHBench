import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic basin term to guide optimization towards origin
        quadratic = np.sum(x_scaled**2)
        
        # Enhanced periodic terms with multiple frequencies and amplitudes
        periodic = np.sum(0.8 * np.sin(15 * np.pi * x_scaled)**2 + 
                         0.3 * np.sin(30 * np.pi * x_scaled)**2 +
                         0.2 * np.sin(45 * np.pi * x_scaled)**2)
        
        # Modified exponential interaction term with stronger curvature
        exponential = np.exp(-np.sum(x_scaled**2) / 3.0) * np.sum(np.cos(5 * x_scaled)**3)
        
        # Novel penalty mechanism with steeper gradient near boundaries
        penalty = 1.0 / (1.0 + np.exp(-2.0 * (np.sum(x_scaled**2) - 1.5)))
        
        # Additional harmonic term to increase landscape complexity
        harmonic = 0.1 * np.sum(np.sin(8 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled))
        
        # Combine all terms with optimized weights
        result = 0.3 * quadratic + 0.4 * periodic + 0.2 * exponential + 0.05 * penalty + 0.05 * harmonic
        
        return result