import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Main quadratic term
        f_val = np.sum(x**2)
        
        # Add multiple local minima using sinusoidal terms with different frequencies and phase shifts
        for i in range(self.dim):
            f_val += 0.2 * np.sin(8 * x[i]) * np.cos(5 * x[i]) + 0.1 * np.sin(3 * x[i] + 1.0) * np.cos(2 * x[i] - 0.5)
            
        # Add more complex local optima with shifted interactions and higher-order terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.1 * np.sin(4 * x[i] + 3 * x[j]) * np.cos(3 * x[i] - 4 * x[j]) + 0.05 * (x[i]**3) * (x[j]**2) * np.sin(x[i] + x[j])
        
        # Add higher-order polynomial interactions for increased complexity
        for i in range(self.dim):
            f_val += 0.05 * (x[i]**5) * np.sin(x[i]) + 0.03 * (x[i]**4) * np.cos(x[i])
            
        # Add shifted sinusoidal terms to create more scattered local minima with varying amplitudes
        for i in range(self.dim):
            f_val += 0.15 * np.sin(7 * (x[i] - 1.5)) * np.cos(6 * (x[i] + 1.2)) + 0.1 * np.sin(5 * (x[i] - 0.8)) * np.cos(4 * (x[i] + 0.7))
        
        # Add a global structure component with multiple peaks and valleys
        f_val += 0.3 * np.prod(np.sin(0.5 * x + 1.0)) + 0.2 * np.prod(np.cos(0.3 * x - 0.5))
        
        return f_val