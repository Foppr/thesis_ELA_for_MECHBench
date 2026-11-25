import numpy as np

class MultiModalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add quadratic term for conditioning
        f_val += 0.35 * np.sum(x**2)
        
        # Add periodic correlation structure with varying frequencies
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Correlation based on periodic function with different wavelengths
                corr = np.sin(0.6 * (i - j)) * np.cos(0.4 * (i + j))
                f_val += 0.25 * corr * x[i] * x[j]
        
        # Add multi-modal sinusoidal terms with varying amplitudes and frequencies
        for i in range(self.dim):
            f_val += 0.6 * np.sin(3.5 * x[i]) * np.cos(2.5 * x[i]) + 0.35 * np.sin(7.5 * x[i])
            
        # Add polynomial penalties with different degrees to create varied curvature
        f_val += 0.025 * np.sum(x**4) + 0.015 * np.sum(x**5) + 0.008 * np.sum(x**6)
        
        # Add interaction terms that create interference patterns
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Interaction with sinusoidal modulation based on dimension indices
                mod = np.sin(0.25 * (i + j)) + 1.6
                f_val += 0.12 * mod * np.sin(x[i]) * np.sin(x[j])
                
        # Add a global sinusoidal modulation to increase complexity
        f_val += 0.45 * np.sin(np.sum(x) * 0.55)
        
        return f_val