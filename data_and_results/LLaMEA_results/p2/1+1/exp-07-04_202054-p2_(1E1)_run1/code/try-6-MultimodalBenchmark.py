import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin with quadratic base
        f_value = np.sum(x**2)
        
        # Add multiple local minima using combined trigonometric perturbations with higher frequencies
        for i in range(self.dim):
            f_value += 0.3 * np.sin(7 * x[i]) * np.cos(5 * x[i]) * np.sin(9 * x[i])
            
        # Add higher-order polynomial local minima
        for i in range(self.dim):
            f_value += 0.15 * x[i]**6
            
        # Add cross-term interactions with stronger coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.1 * np.sin(2 * x[i]) * np.cos(3 * x[j]) * np.sin(5 * x[i] + 2 * x[j])
                
        # Add a secondary sinusoidal component with varying frequencies
        f_value += 0.2 * np.sum(np.sin(5 * x)**2)
        
        # Add a tertiary sinusoidal component with different frequency and amplitude
        f_value += 0.12 * np.sum(np.cos(8 * x)**2)
        
        # Add interaction terms between all variables with increased complexity
        f_value += 0.05 * np.sum(np.sin(x) * np.cos(x)**3)
        
        # Add a fourth-order polynomial interaction term
        for i in range(self.dim):
            f_value += 0.08 * x[i]**4 * np.sin(x[i])
            
        # Add a multi-scale sinusoidal component
        f_value += 0.1 * np.sum(np.sin(3 * x) * np.cos(4 * x))
        
        return f_value