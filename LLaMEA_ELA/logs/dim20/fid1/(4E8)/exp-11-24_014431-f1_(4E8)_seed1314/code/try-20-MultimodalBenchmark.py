import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Main quadratic term with varying coefficients
        f_val = np.sum((0.5 + 0.5 * np.sin(np.arange(self.dim))) * x**2)
        
        # Add exponentially decaying correlations between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                correlation = np.exp(-0.1 * (i - j)**2)
                f_val += 0.3 * correlation * np.sin(x[i]) * np.cos(x[j])
        
        # Add multiple sinusoidal terms with different frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.2 * np.sin(10 * x[i]) * np.cos(3 * x[i]) + \
                     0.15 * np.sin(5 * x[i])**2 * np.cos(2 * x[i])
        
        # Add a complex polynomial penalty term
        f_val += 0.05 * np.sum(x**8) + 0.03 * np.sum(x**6) + 0.01 * np.sum(x**4)
        
        # Add a global sinusoidal modulation to increase landscape complexity
        f_val += 0.2 * np.sin(np.sum(x**2) / (self.dim * 25.0))
        
        # Add cross-dimensional interaction terms with varying strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range interactions
                strength = 0.1 / (1 + (j - i)**2)
                f_val += strength * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        return f_val