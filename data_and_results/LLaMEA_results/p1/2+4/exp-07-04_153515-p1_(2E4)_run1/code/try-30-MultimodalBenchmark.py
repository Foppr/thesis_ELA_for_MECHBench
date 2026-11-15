import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Main quadratic term
        f_val = np.sum(x**2)
        
        # Add multiple local minima using sinusoidal terms with different frequencies
        for i in range(self.dim):
            f_val += 0.2 * np.sin(8 * x[i]) * np.cos(5 * x[i])
            
        # Add more complex local optima with shifted interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.1 * np.sin(4 * x[i] + 3 * x[j]) * np.cos(3 * x[i] - 4 * x[j])
        
        # Add higher-order polynomial interactions for increased complexity
        for i in range(self.dim):
            f_val += 0.05 * (x[i]**5) * np.sin(x[i])
            
        # Add shifted sinusoidal terms to create more scattered local minima
        for i in range(self.dim):
            f_val += 0.15 * np.sin(7 * (x[i] - 1.5)) * np.cos(6 * (x[i] + 1.5))
        
        # Add cross-terms with exponential decay to create rugged landscape
        for i in range(self.dim):
            f_val += 0.08 * np.exp(-0.5 * x[i]**2) * np.sin(9 * x[i])
        
        # Add a global shaping term to balance the landscape
        f_val += 0.02 * np.sum(x**6)
        
        return f_val