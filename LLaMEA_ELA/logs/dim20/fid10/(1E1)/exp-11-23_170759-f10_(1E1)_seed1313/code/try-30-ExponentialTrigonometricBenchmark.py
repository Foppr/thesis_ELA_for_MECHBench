import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Base exponential decay term with varying coefficients
        for i in range(self.dim):
            result += 0.2 * np.exp(-0.5 * (x[i] ** 2)) * (1.0 + 0.1 * i)
        
        # Add multi-frequency trigonometric components with radial interaction
        for i in range(self.dim):
            freq = 2.0 * (i + 1)
            result += 0.3 * np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.1 * abs(x[i]))
        
        # Add radial symmetry component with varying scale
        if self.dim >= 2:
            r = np.sqrt(x[0]**2 + x[1]**2)
            result += 0.4 * np.sin(5.0 * r) * np.exp(-0.2 * r)
        
        # Add cross-dimensional interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * (1.0 + 0.05 * (i + j))
        
        # Add asymmetric exponential terms with coordinate-dependent scaling
        for i in range(self.dim):
            if x[i] > 0:
                result += 0.25 * np.exp(-0.3 * x[i]) * (1.0 + 0.2 * x[i]**2)
            else:
                result += 0.2 * np.exp(-0.4 * abs(x[i])) * (1.0 + 0.15 * x[i]**2)
        
        # Add high-frequency oscillatory component
        for i in range(self.dim):
            result += 0.15 * np.sin(20.0 * x[i]) * np.cos(15.0 * x[i])
        
        # Add polynomial interaction terms with increasing degree
        for i in range(min(self.dim, 3)):
            result += 0.1 * (x[i] ** 3) * np.sin(x[i])
            
        # Add global modulation based on sum of squares
        sum_squares = np.sum(x**2)
        result += 0.3 * np.exp(-0.1 * sum_squares) * np.sin(2.0 * sum_squares)
        
        # Add boundary attraction term to encourage exploration near boundaries
        for i in range(self.dim):
            result += 0.1 * (5.0 - abs(x[i]))**2
        
        return result