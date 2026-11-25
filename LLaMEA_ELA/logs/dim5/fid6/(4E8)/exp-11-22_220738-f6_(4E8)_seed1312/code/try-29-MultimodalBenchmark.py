import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with chaotic modulation
        f_val = np.sum(x**2) * (1.0 + 0.3 * np.sin(3.0 * np.sum(x**2)))
        
        # Chaotic oscillatory components with asymmetric behavior
        for i in range(self.dim):
            f_val += 0.5 * np.sin(5.0 * x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.2 * x[i]**2)
            
        # Asymmetric saddle structure with cross-dimensional coupling
        if self.dim >= 2:
            saddle_term = 0
            for i in range(self.dim - 1):
                diff = x[i] - x[i+1]
                saddle_term += diff**2 * (1.0 + 0.1 * np.sin(x[i] * x[i+1]) * np.cos(0.5 * x[i]))
            f_val += 0.2 * saddle_term
            
        # Cross-dimensional coupling with Gaussian-like peaks
        for i in range(0, self.dim, 3):
            if i + 2 < self.dim:
                peak_x = x[i] - 1.5
                peak_y = x[i+1] + 1.0
                peak_z = x[i+2] - 0.5
                f_val += 0.3 * np.exp(-0.5 * (peak_x**2 + peak_y**2 + peak_z**2))
                
        # Additional chaotic interference from higher-order terms
        for i in range(self.dim):
            f_val += 0.1 * np.sin(10.0 * x[i]) * np.cos(7.0 * x[i]) * (1.0 + 0.2 * np.sin(x[i]**3))
            
        return f_val