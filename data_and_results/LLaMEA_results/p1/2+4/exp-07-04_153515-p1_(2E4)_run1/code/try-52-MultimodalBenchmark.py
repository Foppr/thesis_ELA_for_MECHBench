import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Enhanced trigonometric components with varied frequencies
        for i in range(self.dim):
            f_val += 0.3 * np.sin(6 * x[i]) * np.cos(4 * x[i]) + 0.15 * np.sin(3 * x[i])**2
        
        # Modified exponential interactions with stronger coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.1 * np.exp(-0.3 * (x[i] - x[j])**2) * np.sin(5 * (x[i] + x[j]))
        
        # Adjusted higher-order polynomial terms with different modulation
        for i in range(self.dim):
            f_val += 0.03 * (x[i]**5) * np.cos(3 * x[i]) + 0.04 * (x[i]**3) * np.sin(2 * x[i])
        
        # Modified shifted sinusoidal components with different scaling
        for i in range(self.dim):
            f_val += 0.2 * np.exp(-0.15 * (x[i] - 1.5)**2) * np.sin(8 * (x[i] + 0.5))
        
        # Revised global scaling factor with different sinusoidal influence
        f_val += 0.02 * np.sum(np.abs(x)) * np.sin(0.3 * np.sum(x**2))
        
        return f_val