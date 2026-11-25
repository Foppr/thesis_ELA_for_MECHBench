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
            result += 5.0 * np.sin(5.0 * x[i]) * np.cos(7.0 * x[i]) + 3.0 * np.sin(9.0 * x[i])
            
        # Add radial basis function components with adaptive widths
        for i in range(self.dim):
            result += 1.5 * np.exp(-0.4 * (x[i] - 2.0)**2) + 1.3 * np.exp(-0.2 * (x[i] + 4.0)**2)
            
        # Add a multi-modal component with enhanced polynomial interactions
        for i in range(self.dim):
            result += 0.8 * x[i]**6 - 1.5 * x[i]**5 + 1.0 * x[i]**4 - 0.6 * x[i]**3
            
        # Add cross-dimensional coupling with stronger trigonometric functions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.7 * np.sin(x[i] * x[j]) * np.cos(0.9 * (x[i]**2 + x[j]**2))
                
        # Add a conditioning component that scales with dimensionality
        condition_factor = 1.0 + 0.5 * self.dim
        result *= condition_factor
        
        # Add chaotic behavior through nested trigonometric functions
        for i in range(self.dim):
            result += 1.0 * np.sin(np.pi * np.sin(4.0 * x[i])) * np.cos(np.pi * np.cos(3.0 * x[i]))
            
        # Add a fractal-like component with more recursive sine terms
        for i in range(self.dim):
            recursive_term = 0.0
            for k in range(1, 8):
                recursive_term += 0.4**k * np.sin(2**(k) * x[i])
            result += recursive_term
            
        # Add penalty for large values with exponential scaling
        result += 0.3 * np.sum(np.exp(np.abs(x)) - 1)
        
        # Add a new component: hyperbolic tangent oscillations
        for i in range(self.dim):
            result += 0.6 * np.tanh(3.0 * x[i]) * np.sin(4.0 * x[i])
            
        # Add a multi-modal component with cross-dimensional polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * (x[i]**2 + x[j]**2) * np.sin(0.7 * x[i] * x[j])
                
        # Add a new component: higher-order chaotic sine waves
        for i in range(self.dim):
            result += 0.5 * np.sin(10.0 * x[i]) * np.cos(8.0 * x[i]) + 0.4 * np.sin(6.0 * x[i])
            
        # Add a new component: multi-scale radial basis functions
        for i in range(self.dim):
            result += 0.9 * np.exp(-0.6 * (x[i] - 1.5)**2) + 0.7 * np.exp(-0.4 * (x[i] + 2.5)**2)
            
        return result