import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with conditioning
        f_val = np.sum(x**2)
        
        # Add multiple interacting local minima using high-frequency sinusoidal terms with exponential scaling
        for i in range(self.dim):
            f_val += 2.0 * np.exp(-0.1 * np.abs(x[i])) * np.sin(15 * x[i]) * np.cos(10 * x[i]) * np.sin(5 * x[i])
            
        # Add polynomial penalty terms with varying exponents for increased complexity
        f_val += 0.2 * np.sum(np.abs(x)**5)
        
        # Add cross-dimensional interactions with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.1 * np.exp(-0.05 * (x[i]**2 + x[j]**2)) * np.sin(5 * x[i]) * np.cos(5 * x[j])
        
        # Add a global minimum at origin with additional penalty terms including saddle points
        f_val += 0.05 * np.sum(np.abs(x)**1.7)
        
        # Add a secondary global minimum structure with multiple peaks
        f_val += 0.15 * np.sum(np.sin(3 * x)**2 + np.cos(3 * x)**2)
        
        # Add a complex interaction term that creates numerous local minima
        f_val += 0.08 * np.sum(np.sin(2 * x) * np.cos(2 * x) * np.sin(4 * x))
        
        # Add a term that creates saddle points and plateaus
        f_val += 0.03 * np.sum(np.sin(x)**4 + np.cos(x)**4)
        
        return f_val