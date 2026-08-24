import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic terms
        result = 0.0
        for i in range(self.dim):
            result += (x[i] - 1.0)**2 + (x[i] + 1.0)**2
        
        # Polynomial interaction terms with varying degrees
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * (x[i]**3 - x[j]**3) * (x[i] - x[j])
        
        # Trigonometric modulation to create multiple local minima
        for i in range(self.dim):
            result += 0.5 * np.sin(5.0 * x[i]) * np.cos(3.0 * x[i])
        
        # Add a global minimum at the origin with high curvature
        result += 0.01 * np.sum(x**4) + 0.001 * np.sum(x**6)
        
        # Add a periodic component to increase landscape complexity
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(4.0 * x[i]) * np.cos(2.0 * x[i])
        result += 0.2 * periodic_term
        
        # Add a saddle point structure with exponential scaling
        for i in range(self.dim):
            result += 0.3 * np.exp(-0.5 * x[i]**2) * np.sin(2.0 * x[i])
        
        return result