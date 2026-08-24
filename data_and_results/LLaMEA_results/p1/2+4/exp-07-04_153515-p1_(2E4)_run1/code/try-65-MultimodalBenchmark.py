import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Enhanced trigonometric components with higher frequencies
        for i in range(self.dim):
            f_val += 0.3 * np.sin(7 * x[i]) * np.cos(4 * x[i]) + 0.15 * np.sin(3 * x[i])**2
        
        # Stronger exponential interactions with modified decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.12 * np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(7 * (x[i] + x[j]))
        
        # Modified higher-order polynomial terms with sinusoidal modulation
        for i in range(self.dim):
            f_val += 0.05 * (x[i]**5) * np.cos(3 * x[i]) + 0.06 * (x[i]**4) * np.sin(1.5 * x[i])
        
        # Additional shifted sinusoidal components with increased density
        for i in range(self.dim):
            f_val += 0.25 * np.exp(-0.2 * (x[i] - 1.5)**2) * np.sin(10 * (x[i] + 0.5))
        
        # Global scaling with enhanced interaction
        f_val += 0.02 * np.sum(np.abs(x)) * np.sin(0.8 * np.sum(x**2))
        
        # Add cross-term interactions with varying amplitudes
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.05 * np.sin(4 * x[i]) * np.cos(3 * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        return f_val