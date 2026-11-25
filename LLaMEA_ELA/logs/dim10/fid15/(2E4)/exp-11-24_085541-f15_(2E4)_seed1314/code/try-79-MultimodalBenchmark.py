import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add polynomial chaos expansion with mixed monomials
        for i in range(self.dim):
            result += 0.5 * x[i]**6 + 0.3 * x[i]**5 - 0.4 * x[i]**4 + 0.2 * x[i]**3
            
        # Add fractal-like trigonometric components with varying frequencies
        for i in range(self.dim):
            result += 1.2 * np.sin(3.0 * x[i]) * np.cos(7.0 * x[i]) * np.tan(2.5 * x[i])
            
        # Add adaptive radial basis functions with dimension-dependent widths
        for i in range(self.dim):
            width = 0.5 + 0.1 * self.dim
            result += 2.0 * np.exp(-0.5 * ((x[i] - 1.0) / width)**2) + 1.5 * np.exp(-0.3 * ((x[i] + 2.0) / (width * 0.7))**2)
            
        # Add cross-dimensional coupling with polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.8 * (x[i]**2 + x[j]**2) * np.sin(0.5 * x[i] * x[j])
                
        # Add chaotic sine-polynomial interactions with varying exponents
        for i in range(self.dim):
            result += 0.9 * np.sin(x[i]**3) * np.cos(2.0 * x[i]) + 0.6 * np.sin(np.sqrt(np.abs(x[i])) * np.cos(4.0 * x[i]))
            
        # Add fractal-like recursive components
        for i in range(self.dim):
            recursive_sum = 0.0
            for k in range(1, 8):
                recursive_sum += 0.3**k * np.sin(2**(k) * x[i])
            result += recursive_sum
            
        # Add multi-modal component with hyperbolic tangent and polynomial interactions
        for i in range(self.dim):
            result += 0.7 * np.tanh(x[i]) * (x[i]**4 - 2.0 * x[i]**3 + x[i]**2)
            
        # Add cross-dimensional exponential coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.4 * np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(3.0 * (x[i] + x[j]))
                
        # Add conditioning factor based on dimensionality
        condition_factor = 1.0 + 0.3 * self.dim
        result *= condition_factor
        
        # Add penalty for large values with logarithmic scaling
        result += 0.25 * np.sum(np.log(1.0 + np.abs(x)))
        
        return result