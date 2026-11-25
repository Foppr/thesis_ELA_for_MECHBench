import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add multiple sinusoidal oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 3.0 * np.sin(4.0 * x[i]) * np.cos(6.0 * x[i]) + 2.0 * np.sin(8.0 * x[i])
            
        # Add radial basis function components with adaptive widths
        for i in range(self.dim):
            result += 1.2 * np.exp(-0.5 * (x[i] - 2.5)**2) + 1.0 * np.exp(-0.3 * (x[i] + 3.5)**2)
            
        # Add a multi-modal component with enhanced polynomial interactions
        for i in range(self.dim):
            result += 0.6 * x[i]**5 - 1.2 * x[i]**4 + 0.8 * x[i]**3 - 0.4 * x[i]**2
            
        # Add cross-dimensional coupling with stronger trigonometric functions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.5 * np.sin(x[i] * x[j]) * np.cos(0.7 * (x[i]**2 + x[j]**2))
                
        # Add a conditioning component that scales with dimensionality
        condition_factor = 1.0 + 0.3 * self.dim
        result *= condition_factor
        
        # Add chaotic behavior through nested trigonometric functions
        for i in range(self.dim):
            result += 0.8 * np.sin(np.pi * np.sin(3.0 * x[i])) * np.cos(np.pi * np.cos(2.0 * x[i]))
            
        # Add a fractal-like component with more recursive sine terms
        for i in range(self.dim):
            recursive_term = 0.0
            for k in range(1, 6):
                recursive_term += 0.3**k * np.sin(2**(k) * x[i])
            result += recursive_term
            
        # Add penalty for large values with exponential scaling
        result += 0.2 * np.sum(np.exp(np.abs(x)) - 1)
        
        # Add a new component: hyperbolic tangent oscillations
        for i in range(self.dim):
            result += 0.4 * np.tanh(2.0 * x[i]) * np.sin(3.0 * x[i])
            
        # Add a multi-modal component with cross-dimensional polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * (x[i]**2 + x[j]**2) * np.sin(0.5 * x[i] * x[j])
                
        # Add enhanced chaotic component with fractional powers - mutated version
        for i in range(self.dim):
            result += 0.5 * np.sin(np.pi * np.sqrt(np.abs(x[i])) * np.cos(5.0 * x[i]))
            
        # Add a new cross-dimensional coupling term with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * np.exp(-0.3 * (x[i] - x[j])**2) * np.sin(3.0 * (x[i] + x[j]))
                
        # Add a new polynomial interaction term with higher degree
        for i in range(self.dim):
            result += 0.2 * x[i]**6 - 0.4 * x[i]**5 + 0.25 * x[i]**4
            
        # Add a new hyperbolic sine polynomial interaction term
        for i in range(self.dim):
            result += 0.3 * np.sinh(1.5 * x[i]) * x[i]**3
            
        return result