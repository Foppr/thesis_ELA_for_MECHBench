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
            f_val += 0.5 * np.sin(7 * x[i]) * np.cos(3 * x[i]) + 0.2 * np.sin(5 * x[i])
            
        # Add a global minimum at origin with additional penalty terms
        f_val += 0.02 * np.sum(np.abs(x)) + 0.01 * np.sum(x**4) + 0.003 * np.sum(x**6)
        
        # Introduce additional complexity with higher frequency components and modified amplitudes
        for i in range(self.dim):
            f_val += 0.25 * np.sin(15 * x[i]) + 0.12 * np.cos(9 * x[i])
            
        # Add interaction terms between dimensions to increase complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.03 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) + 0.01 * np.sin(2*x[i]) * np.sin(2*x[j])
                
        # Add a complex high-order polynomial term for increased difficulty
        f_val += 0.005 * np.sum((x**8) + (x**10))
        
        # Add a multi-modal component with exponentially increasing frequencies
        for i in range(self.dim):
            f_val += 0.18 * np.sin(20 * x[i]) * np.cos(13 * x[i]) + 0.09 * np.sin(17 * x[i])
            
        return f_val