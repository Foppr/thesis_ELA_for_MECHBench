import numpy as np

class MultiScaleCorrelatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add quadratic term for conditioning
        f_val += 0.3 * np.sum(x**2)
        
        # Add multi-scale periodic correlation structure
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Multi-scale correlation with different frequencies
                corr1 = np.exp(-0.05 * (j - i))
                corr2 = 0.5 * np.exp(-0.2 * (j - i))
                f_val += 0.2 * (corr1 * np.sin(2 * np.pi * x[i]) * np.cos(2 * np.pi * x[j]) + 
                               corr2 * np.cos(4 * np.pi * x[i]) * np.sin(4 * np.pi * x[j]))
        
        # Add multi-scale sinusoidal modulations with varying amplitudes
        for i in range(self.dim):
            f_val += 0.1 * (np.sin(10 * x[i]) + 0.5 * np.sin(20 * x[i]) + 
                           0.3 * np.sin(30 * x[i]) + 0.2 * np.sin(40 * x[i]))
        
        # Add polynomial penalties with adaptive weights
        f_val += 0.01 * np.sum(x**4) + 0.005 * np.sum(x**6)
        
        # Add interaction terms with adaptive coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive coupling based on dimension indices and sinusoidal modulation
                coupling = 0.05 * (1 + np.sin(0.5 * (i + j)))
                f_val += coupling * np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i] + x[j]))
                
        # Add a global sinusoidal modulation to create complex landscape
        f_val += 0.1 * np.sin(np.sum(x) * 2)
        
        return f_val