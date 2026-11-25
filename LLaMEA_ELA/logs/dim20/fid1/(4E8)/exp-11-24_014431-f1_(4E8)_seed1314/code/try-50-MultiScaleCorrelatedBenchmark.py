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
        f_val += 0.35 * np.sum(x**2)
        
        # Add multi-scale periodic correlation structure with altered coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Modified correlation with different frequencies and weights
                corr1 = np.exp(-0.07 * (j - i))
                corr2 = 0.6 * np.exp(-0.25 * (j - i))
                f_val += 0.25 * (corr1 * np.sin(2.5 * np.pi * x[i]) * np.cos(2.5 * np.pi * x[j]) + 
                               corr2 * np.cos(4.5 * np.pi * x[i]) * np.sin(4.5 * np.pi * x[j]))
        
        # Add multi-scale sinusoidal modulations with altered amplitudes
        for i in range(self.dim):
            f_val += 0.15 * (np.sin(12 * x[i]) + 0.6 * np.sin(22 * x[i]) + 
                           0.4 * np.sin(32 * x[i]) + 0.3 * np.sin(42 * x[i]))
        
        # Add polynomial penalties with modified weights
        f_val += 0.015 * np.sum(x**4) + 0.008 * np.sum(x**6)
        
        # Add interaction terms with modified coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Modified adaptive coupling based on dimension indices and sinusoidal modulation
                coupling = 0.07 * (1 + np.sin(0.6 * (i + j)))
                f_val += coupling * np.sin(x[i] * x[j]) * np.cos(0.6 * (x[i] + x[j]))
                
        # Add a stronger global sinusoidal modulation
        f_val += 0.15 * np.sin(np.sum(x) * 2.5)
        
        return f_val