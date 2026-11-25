import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # High-frequency cosine terms with exponential growth
        for i in range(self.dim):
            freq = 2 ** (i + 1)
            result += 0.3 * np.cos(freq * x[i]) * np.exp(-0.15 * x[i]**2)
            
        # Complex interaction terms with varying coefficients and enhanced nonlinearity
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced interaction range
                coeff = 0.2 / (1 + abs(i - j)**1.5)
                result += coeff * np.sin(3 * x[i]) * np.cos(4 * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
                
        # Multi-modal global structure with multiple valleys and modified amplitude
        for i in range(self.dim):
            result += 0.2 * (np.cos(6 * x[i]) + 0.3 * np.sin(9 * x[i])) * np.exp(-0.15 * (x[i] - 1.8)**2)
            
        # Enhanced penalty term for being far from the global minimum with higher order polynomial
        result += 0.1 * np.sum((x - 1.2)**6)
        
        # Additional sinusoidal modulation to increase landscape complexity
        for i in range(self.dim):
            result += 0.05 * np.sin(7 * x[i]) * np.cos(2 * x[(i+1) % self.dim]) * np.exp(-0.08 * x[i]**2)
            
        return result