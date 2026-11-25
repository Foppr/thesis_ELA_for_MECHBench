import numpy as np

class CorrelatedRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add quadratic term for conditioning
        f_val += 0.5 * np.sum(x**2)
        
        # Add exponentially decaying correlation structure
        # Correlation decreases with distance between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Exponentially decaying correlation coefficient
                corr = np.exp(-0.1 * (j - i))
                f_val += 0.3 * corr * x[i] * x[j]
        
        # Add ruggedness through high-frequency sinusoidal terms
        for i in range(self.dim):
            f_val += 0.2 * np.sin(10 * x[i]) * np.cos(5 * x[i])
            
        # Add polynomial penalty to encourage convergence to origin
        f_val += 0.01 * np.sum(x**4) + 0.005 * np.sum(x**6)
        
        # Add interaction terms with varying strengths based on dimension indices
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.02 / (1.0 + np.exp(-0.5*(i+j)))
                f_val += strength * np.sin(x[i]) * np.cos(x[j])
                
        return f_val