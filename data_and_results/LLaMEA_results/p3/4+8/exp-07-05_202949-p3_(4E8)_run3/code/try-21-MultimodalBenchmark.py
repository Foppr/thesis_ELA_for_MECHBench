import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add multiple interacting local minima using high-frequency sinusoidal terms
        for i in range(self.dim):
            f_val += 0.7 * np.sin(12 * x[i]) * np.cos(8 * x[i]) * np.sin(5 * x[i])
            
        # Add adaptive polynomial penalty terms for increased complexity
        f_val += 0.15 * np.sum(x**4)
        
        # Add cross-dimensional interactions with variable coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.08 * np.sin(2 * x[i] + x[j]) * np.cos(x[i] - 2 * x[j])
        
        # Add a global minimum at origin with additional penalty terms
        f_val += 0.03 * np.sum(np.abs(x)**1.7)
        
        # Add a secondary global minimum structure with modified frequency
        f_val += 0.04 * np.sum(np.sin(3 * x)**2)
        
        # Add a structured noise component to increase landscape complexity
        noise = 0.02 * np.sum(np.sin(15 * x) * np.cos(10 * x))
        f_val += noise
        
        return f_val