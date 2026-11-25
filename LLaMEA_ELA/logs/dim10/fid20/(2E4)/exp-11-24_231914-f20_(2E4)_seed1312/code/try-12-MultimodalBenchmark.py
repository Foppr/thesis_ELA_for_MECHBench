import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with shifted global minimum
        f_val = np.sum((x - 1.5)**2)
        
        # Add multiple local minima using higher frequency cosine terms
        for i in range(self.dim):
            f_val += 0.3 * np.cos(12 * x[i]) * np.exp(-0.03 * (x[i] - 1.5)**2)
            
        # Add interaction terms between dimensions with higher order polynomial terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.03 * np.sin(7 * x[i]) * np.cos(4 * x[j]) * (x[i] * x[j])**4
        
        # Add a more complex noise term to increase landscape irregularity
        f_val += 0.002 * np.sum(x**5)
        
        # Add a periodic component to increase multimodality
        f_val += 0.1 * np.sin(20 * np.sum(x**2))
        
        return f_val