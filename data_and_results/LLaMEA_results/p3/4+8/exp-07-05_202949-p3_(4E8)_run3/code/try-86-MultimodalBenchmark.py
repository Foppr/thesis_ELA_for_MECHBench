import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Dynamic shift based on dimensionality for global minimum
        self.shift = np.array([0.5 * np.sin(i / (self.dim + 1)) for i in range(self.dim)])
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base with asymmetric coefficients
        result = 0.0
        for i in range(self.dim):
            result += 0.5 * (x[i] - self.shift[i])**2 + 0.3 * (x[i] + self.shift[i])**4
        
        # Coupled trigonometric interaction terms with varying frequencies
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 2.0 + 0.5 * i
                freq_j = 1.5 + 0.3 * j
                result += 0.2 * np.sin(freq_i * x[i]) * np.cos(freq_j * x[j])
        
        # Asymmetric saddle point structure with exponential scaling
        for i in range(self.dim):
            result += 0.4 * np.sin(2.0 * x[i]) * np.cos(3.0 * x[i]) + 0.1 * np.sin(5.0 * x[i])**3
        
        # Dynamic global minimum adjustment based on dimension
        result += 0.01 * np.sum((x - self.shift)**2) + 0.005 * np.sum((x - self.shift)**4)
        
        # Additional high-frequency noise component
        noise = 0.0
        for i in range(self.dim):
            noise += 0.03 * np.sin(15.0 * x[i]) * np.cos(12.0 * x[i])
        result += noise
        
        # Add a complex multimodal component with multiple local minima
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.6 * np.sin(4.0 * x[i]) * np.cos(7.0 * x[i]) + 0.2 * np.sin(9.0 * x[i])
        result += 0.1 * multimodal
        
        return result