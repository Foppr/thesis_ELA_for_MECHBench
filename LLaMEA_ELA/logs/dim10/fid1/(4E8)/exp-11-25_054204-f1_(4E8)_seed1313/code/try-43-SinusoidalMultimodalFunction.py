import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = np.sum(x**2)
        
        # Add sinusoidal oscillations with higher frequency and amplitude
        for i in range(self.dim):
            result += 0.3 * np.sin(10 * x[i]) * np.cos(7 * x[i])
            
        # Add interaction terms between dimensions with increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.15 * np.sin(4 * x[i] + 3 * x[j]) * np.cos(3 * x[i] - 4 * x[j])
                
        # Add cubic nonlinear terms with increased coefficient
        for i in range(self.dim):
            result += 0.08 * x[i]**3
            
        # Add Gaussian perturbations with multiple peaks and varied widths
        for i in range(self.dim):
            result += 0.1 * np.exp(-0.5 * ((x[i] - 2.5) / 1.2)**2) + \
                      0.1 * np.exp(-0.5 * ((x[i] + 2.5) / 1.2)**2) + \
                      0.05 * np.exp(-0.5 * ((x[i] - 1.0) / 0.8)**2) + \
                      0.05 * np.exp(-0.5 * ((x[i] + 1.0) / 0.8)**2)
            
        # Add higher-order polynomial interaction terms with increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.06 * (x[i]**3) * (x[j]**2) + 0.06 * (x[i]**2) * (x[j]**3)
                
        # Add quartic terms to increase landscape complexity
        for i in range(self.dim):
            result += 0.03 * x[i]**4
            
        # Add cross-dimensional sine-cosine interactions with varying frequencies
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction range for complexity control
                result += 0.05 * np.sin(2 * x[i] + 5 * x[j]) * np.cos(5 * x[i] - 2 * x[j])
                
        return result