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
            f_val += 1.0 * np.sin(10 * x[i]) * np.cos(4 * x[i]) + 0.5 * np.sin(6 * x[i]) + 0.3 * np.sin(12 * x[i])
            
        # Add a global minimum at origin with additional penalty terms
        f_val += 0.05 * np.sum(np.abs(x)) + 0.02 * np.sum(x**4) + 0.01 * np.sum(x**6) + 0.002 * np.sum(x**8)
        
        # Introduce additional complexity with higher frequency components and modified amplitudes
        for i in range(self.dim):
            f_val += 0.3 * np.sin(15 * x[i]) + 0.2 * np.cos(11 * x[i]) + 0.15 * np.sin(18 * x[i])
            
        # Add interaction terms between dimensions to increase complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.1 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) + 0.05 * np.sin(3*x[i]) * np.cos(3*x[j])
                
        # Add cross-dimensional polynomial interactions
        for i in range(self.dim):
            f_val += 0.08 * (x[i]**3) * np.sum(x[:i] if i > 0 else [0]) + 0.05 * x[i]**5
                
        # Add a large number of local minima using a sum of high-frequency sinusoids
        for i in range(self.dim):
            for k in range(1, 8):
                f_val += 0.05 * np.sin(k * 15 * x[i]) * np.cos(k * 9 * x[i])
                
        # Add even more complex interactions with non-linear combinations
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.03 * np.sin(x[i]**2 + x[j]**2) * np.cos(x[i] * x[j]) + 0.02 * np.sin(x[i] * x[j]**2)
                
        # Add a final layer of high-frequency noise
        for i in range(self.dim):
            f_val += 0.1 * np.sin(20 * x[i]) + 0.08 * np.cos(17 * x[i])
            
        return f_val