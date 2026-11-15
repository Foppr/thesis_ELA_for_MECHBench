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
            f_val += 0.3 * np.sin(12 * x[i]) * np.cos(8 * x[i]) * np.sin(5 * x[i])
            
        # Add polynomial penalty terms for increased complexity
        f_val += 0.15 * np.sum(x**4)
        
        # Add cross-dimensional interactions with varying strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.08 * np.sin(2 * x[i] + 3 * x[j]) * np.cos(3 * x[i] - 2 * x[j])
        
        # Add a global minimum at origin with additional penalty terms
        f_val += 0.03 * np.sum(np.abs(x)**1.7)
        
        # Add a secondary global minimum structure with variable amplitude
        f_val += 0.04 * np.sum(np.sin(3 * x)**2)
        
        # Add correlated variable interactions to increase landscape complexity
        for i in range(self.dim - 1):
            f_val += 0.06 * np.sin(x[i] * x[i+1]) * np.cos(x[i] + x[i+1])
            
        # Add adaptive penalty based on distance from origin
        dist_from_origin = np.sqrt(np.sum(x**2))
        f_val += 0.02 * dist_from_origin * np.sin(dist_from_origin)
        
        return f_val