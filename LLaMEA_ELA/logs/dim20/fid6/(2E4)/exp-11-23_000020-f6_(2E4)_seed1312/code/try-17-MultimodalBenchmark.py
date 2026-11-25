import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with conditioning
        result = np.sum(x_norm**2)
        
        # Multiple nested sinusoidal components creating complex landscape
        for i in range(self.dim):
            # Primary oscillatory pattern with varying frequencies
            result += 0.4 * np.sin(13 * x_norm[i]) * np.cos(10 * x_norm[(i+1) % self.dim])
            
            # Secondary interaction terms with more complex nesting
            if i > 0:
                result += 0.25 * np.sin(11 * x_norm[i-1]) * np.sin(9 * x_norm[i]) * np.cos(7 * x_norm[(i+2) % self.dim])
                
        # Add high-frequency oscillations for increased complexity
        for i in range(self.dim):
            result += 0.2 * np.sin(27 * x_norm[i]) * np.cos(22 * x_norm[(i+3) % self.dim]) * np.sin(16 * x_norm[(i+1) % self.dim])
        
        # Add cubic and higher-order polynomial terms for increased complexity
        result += 0.04 * np.sum(x_norm**3) + 0.02 * np.sum(np.abs(x_norm)**4) + 0.015 * np.sum(np.abs(x_norm)**5)
        
        # Add a complex interaction term between all dimensions with improved structure
        interaction_term = 0.35 * np.prod(np.sin(2.5 * x_norm)) + 0.15 * np.prod(np.cos(1.8 * x_norm))
        result += interaction_term
        
        # Add cross-dimensional coupling for better conditioning
        cross_term = 0.18 * np.sum(np.sin(x_norm) * np.cos(x_norm))
        result += cross_term
        
        return result