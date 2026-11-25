import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Enhanced exponential decay terms with varying rates
        for i in range(self.dim):
            f_val += np.exp(-0.2 * x[i]**2) * np.sin(3 * np.pi * x[i]) * np.cos(2 * np.pi * x[i])
            
        # Modified trigonometric oscillations with higher frequency components
        for i in range(self.dim):
            f_val += 0.3 * np.sin(5 * x[i]) * np.cos(3 * x[i]) + 0.2 * np.sin(7 * x[i])
            
        # Improved polynomial penalty terms with higher degree and adaptive weights
        f_val += 0.15 * np.sum(x**8) + 0.05 * np.sum(x**4)
        
        # Enhanced cross-terms with non-linear coupling and varying strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.1 * x[i]**2 * x[j]**2 * np.sin(0.3 * (x[i]**2 + x[j]**2))
                
        # Additional interaction terms to increase conditioning difficulty
        for i in range(self.dim):
            f_val += 0.08 * x[i]**3 * np.sin(2 * x[i])
            
        return f_val