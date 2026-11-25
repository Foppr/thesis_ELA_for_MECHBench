import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add multiple local minima using sine waves with different frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.5 * np.sin(7 * x[i]) * np.cos(3 * x[i]) + 0.2 * np.sin(5 * x[i]) + 0.1 * np.sin(8 * x[i])
            
        # Add a global minimum at origin with additional penalty terms
        f_val += 0.02 * np.sum(np.abs(x)) + 0.01 * np.sum(x**4) + 0.005 * np.sum(x**6) + 0.001 * np.sum(x**8)
        
        # Introduce additional complexity with higher frequency components and modified amplitudes
        for i in range(self.dim):
            f_val += 0.2 * np.sin(12 * x[i]) + 0.15 * np.cos(9 * x[i]) + 0.1 * np.sin(15 * x[i])
            
        # Add interaction terms between dimensions to increase complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.05 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) + 0.03 * np.sin(2*x[i]) * np.cos(2*x[j])
                
        # Add cross-dimensional polynomial interactions
        for i in range(self.dim):
            f_val += 0.04 * (x[i]**3) * np.sum(x[:i] if i > 0 else [0]) + 0.02 * x[i]**5
                
        # Add a large number of local minima using a sum of high-frequency sinusoids
        for i in range(self.dim):
            for k in range(1, 6):
                f_val += 0.03 * np.sin(k * 10 * x[i]) * np.cos(k * 7 * x[i])
                
        return f_val