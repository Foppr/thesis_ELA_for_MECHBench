import numpy as np

class MultiModalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add quadratic term for conditioning with improved scaling
        f_val += 0.4 * np.sum(x**2)
        
        # Add periodic correlation structure with varying frequencies and amplitudes
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced correlation with exponential decay and sinusoidal modulation
                corr = np.sin(0.7 * (i - j)) * np.cos(0.4 * (i + j)) * np.exp(-0.1 * abs(i - j))
                f_val += 0.3 * corr * x[i] * x[j]
        
        # Add multi-modal sinusoidal terms with varying amplitudes, frequencies and phases
        for i in range(self.dim):
            f_val += 0.6 * np.sin(4 * x[i]) * np.cos(3 * x[i]) + 0.4 * np.sin(8 * x[i]) + 0.2 * np.sin(12 * x[i])
            
        # Add polynomial penalties with different degrees and improved conditioning
        f_val += 0.03 * np.sum(x**4) + 0.02 * np.sum(x**5) + 0.01 * np.sum(x**6)
        
        # Add interaction terms that create interference patterns with enhanced complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Interaction with sinusoidal modulation based on dimension indices and exponential decay
                mod = (np.sin(0.3 * (i + j)) + 1.2) * np.exp(-0.05 * abs(i - j))
                f_val += 0.15 * mod * np.sin(x[i]) * np.sin(x[j])
                
        # Add a global sinusoidal modulation with increased complexity and variable frequency
        f_val += 0.5 * np.sin(np.sum(x) * 0.7) * np.cos(np.sum(x) * 0.3)
        
        # Add cross-dimensional coupling with higher-order interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    f_val += 0.05 * np.sin(x[i] + x[j] + x[k]) * np.cos(0.5 * (i + j + k))
        
        return f_val