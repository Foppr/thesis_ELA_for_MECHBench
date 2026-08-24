import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        f_value = np.sum(x**2)
        
        # Add multiple local minima using combined trigonometric perturbations
        for i in range(self.dim):
            f_value += 0.2 * np.sin(5 * x[i]) * np.cos(3 * x[i]) * np.sin(7 * x[i])
            
        # Add polynomial local minima
        for i in range(self.dim):
            f_value += 0.1 * x[i]**4
            
        # Add cross-term interactions for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.05 * np.sin(x[i]) * np.cos(x[j]) * np.sin(2 * x[i] + x[j])
                
        # Add a secondary sinusoidal component
        f_value += 0.15 * np.sum(np.sin(4 * x)**2)
        
        # Add a tertiary sinusoidal component with different frequency
        f_value += 0.08 * np.sum(np.cos(6 * x)**2)
        
        # Add interaction terms between all variables
        f_value += 0.03 * np.sum(np.sin(x) * np.cos(x)**2)
        
        return f_value