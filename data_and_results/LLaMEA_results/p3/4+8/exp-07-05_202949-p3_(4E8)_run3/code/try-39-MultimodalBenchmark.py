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
            f_val += 1.5 * np.exp(-0.15 * np.abs(x[i])) * np.sin(20 * x[i]) * np.cos(12 * x[i]) * np.sin(8 * x[i])
            
        # Add polynomial penalty terms with varying exponents for increased complexity
        f_val += 0.15 * np.sum(np.abs(x)**4.5)
        
        # Add cross-dimensional interactions with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.08 * np.exp(-0.03 * (x[i]**2 + x[j]**2)) * np.sin(7 * x[i]) * np.cos(7 * x[j])
        
        # Add a global minimum at origin with additional penalty terms including saddle points
        f_val += 0.03 * np.sum(np.abs(x)**1.5)
        
        # Add a secondary global minimum structure with multiple peaks
        f_val += 0.12 * np.sum(np.sin(4 * x)**2 + np.cos(4 * x)**2)
        
        # Add a complex interaction term that creates numerous local minima
        f_val += 0.06 * np.sum(np.sin(3 * x) * np.cos(3 * x) * np.sin(6 * x))
        
        # Add a term that creates saddle points and plateaus
        f_val += 0.02 * np.sum(np.sin(x)**3 + np.cos(x)**3)
        
        # Add a shifted global minimum to increase challenge
        f_val += 0.05 * np.sum((x - 0.5)**2)
        
        return f_val