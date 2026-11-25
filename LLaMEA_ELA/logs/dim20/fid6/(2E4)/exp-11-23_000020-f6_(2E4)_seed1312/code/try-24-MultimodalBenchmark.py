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
            result += 0.6 * np.sin(17 * x_norm[i]) * np.cos(11 * x_norm[(i+1) % self.dim])
            
            # Secondary interaction terms with more complex nesting
            if i > 0:
                result += 0.35 * np.sin(14 * x_norm[i-1]) * np.sin(10 * x_norm[i]) * np.cos(8 * x_norm[(i+2) % self.dim])
                
        # Add high-frequency oscillations for increased complexity
        for i in range(self.dim):
            result += 0.3 * np.sin(33 * x_norm[i]) * np.cos(27 * x_norm[(i+3) % self.dim]) * np.sin(20 * x_norm[(i+1) % self.dim])
        
        # Add a global minimum with penalty terms for convergence testing
        result += 0.05 * np.sum(np.abs(x_norm)**4) + 0.025 * np.sum(np.abs(x_norm)**5)
        
        # Add a complex interaction term between all dimensions with improved structure
        interaction_term = 0.4 * np.prod(np.sin(2.7 * x_norm)) + 0.18 * np.prod(np.cos(2.2 * x_norm))
        result += interaction_term
        
        # Add cross-dimensional coupling for better conditioning
        cross_term = 0.25 * np.sum(np.sin(x_norm) * np.cos(x_norm))
        result += cross_term
        
        return result