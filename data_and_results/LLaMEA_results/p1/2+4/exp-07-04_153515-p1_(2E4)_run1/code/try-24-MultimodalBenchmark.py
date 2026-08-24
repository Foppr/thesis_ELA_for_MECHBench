import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add multi-frequency sinusoidal components
        for i in range(self.dim):
            f_val += 0.5 * np.sin(2 * x[i]) + 0.3 * np.sin(5 * x[i]) + 0.2 * np.sin(8 * x[i])
        
        # Add polynomial interactions with sinusoidal modulation
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interactions
                f_val += 0.1 * (x[i]**2) * (x[j]**2) * np.cos(3 * (x[i] + x[j]))
        
        # Introduce Gaussian peaks to create multiple local minima
        peaks = np.array([[-2.0, 2.0], [2.0, -2.0], [0.0, 0.0], [-3.0, 3.0], [3.0, -3.0]])
        if self.dim >= 2:
            for peak in peaks:
                if len(peak) <= self.dim:
                    peak_vals = peak[:self.dim]
                    f_val += 0.3 * np.exp(-0.5 * np.sum((x - peak_vals)**2)) * np.cos(2 * np.sum(x - peak_vals))
        
        # Add higher-order polynomial terms with sinusoidal modulation
        for i in range(self.dim):
            f_val += 0.05 * (x[i]**4) * np.sin(3 * x[i]) + 0.03 * (x[i]**6) * np.cos(2 * x[i])
        
        # Introduce asymmetric saddle points
        for i in range(self.dim):
            f_val += 0.1 * x[i] * np.sin(4 * x[i]) * np.cos(2 * x[i])
        
        return f_val