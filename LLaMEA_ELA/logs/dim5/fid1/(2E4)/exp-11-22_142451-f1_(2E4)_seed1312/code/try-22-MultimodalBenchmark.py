import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global minimum at origin
        result = np.sum(x**2)
        
        # Add polynomial chaos with varying degrees and coefficients
        for i in range(self.dim):
            result += 0.3 * x[i]**3 * np.sin(10 * x[i]) + 0.2 * x[i]**5 * np.cos(8 * x[i])
            
        # Radial symmetry component with chaotic modulation
        r_squared = np.sum(x**2)
        result += 0.1 * np.exp(-0.05 * r_squared) * np.sin(5 * np.sqrt(r_squared))
        
        # Add trigonometric coupling between variables with varying frequencies
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.08 * np.cos(x[i] + x[j]) * np.sin(3 * x[i] - 2 * x[j])
                
        # Add a chaotic component using sine and cosine with exponential decay
        for i in range(self.dim):
            result += 0.25 * np.sin(12 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
            
        # Add cross-dimensional polynomial terms with chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.03 * (x[i]**2 + x[j]**2) * np.sin(4 * x[i] * x[j]) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
                
        # Add higher-order polynomial with sinusoidal modulation
        for i in range(self.dim):
            result += 0.15 * x[i]**6 * np.sin(6 * x[i]) * np.cos(3 * x[i])
            
        # Add radial basis function component for multiple local minima
        for i in range(self.dim):
            result += 0.1 * np.exp(-0.5 * (x[i] - 2)**2) + 0.1 * np.exp(-0.5 * (x[i] + 2)**2)
            
        # Add a final chaotic component with multiple frequencies
        for i in range(self.dim):
            result += 0.05 * np.sin(15 * x[i]) * np.cos(11 * x[i]) * np.tan(0.5 * x[i])
            
        return result