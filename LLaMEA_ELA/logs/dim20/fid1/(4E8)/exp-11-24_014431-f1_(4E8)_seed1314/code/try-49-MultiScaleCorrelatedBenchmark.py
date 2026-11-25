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
        f_val += 0.2 * np.sum(x**2)
        
        # Add enhanced multi-scale periodic correlation structure
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced correlation with varying frequencies and amplitudes
                freq1 = 2 * (i + 1) / (j + 1)
                freq2 = 3 * (j + 1) / (i + 1)
                amp1 = 0.3 * np.exp(-0.1 * (j - i))
                amp2 = 0.2 * np.exp(-0.15 * (j - i))
                f_val += amp1 * np.sin(freq1 * x[i]) * np.cos(freq2 * x[j]) + \
                         amp2 * np.cos(freq1 * x[i]) * np.sin(freq2 * x[j])
        
        # Add multi-scale sinusoidal modulations with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.15 * (np.sin(8 * x[i]) + 0.4 * np.sin(16 * x[i]) + 
                            0.2 * np.sin(24 * x[i]) + 0.1 * np.sin(32 * x[i]))
        
        # Add polynomial penalties with adaptive weights
        f_val += 0.02 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Add interaction terms with enhanced adaptive coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced coupling based on dimension indices and sinusoidal modulation
                coupling = 0.08 * (1 + np.sin(0.3 * (i + j)) + 0.2 * np.cos(0.4 * (i - j)))
                f_val += coupling * np.sin(x[i] * x[j]) * np.cos(0.3 * (x[i] + x[j]))
                
        # Add a global sinusoidal modulation with enhanced complexity
        f_val += 0.15 * np.sin(np.sum(x) * 3)
        
        # Add a new cross-dimensional interaction term to increase landscape complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.05 * np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(5 * (x[i] + x[j]))
        
        return f_val