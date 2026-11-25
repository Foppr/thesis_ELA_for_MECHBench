import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial landscape with varying exponents
        result = np.sum(x**4) + 0.5 * np.sum(x**6)
        
        # Add multiple sinusoidal modulations with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 2.0 * np.sin(3 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Introduce chaotic behavior through nested trigonometric functions
        for i in range(self.dim):
            result += 1.5 * np.sin(np.sin(x[i])) * np.cos(np.cos(x[i]))
            
        # Add fractal-like interactions between dimensions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited cross-dimension coupling
                result += 0.8 * np.sin(x[i] * x[j]) * np.cos(x[i]**2 + x[j]**2) * np.exp(-0.05 * (i+j))
                
        # Include adaptive scaling based on dimensionality
        adaptive_scale = 1.0 + 0.05 * self.dim
        
        # Add high-frequency oscillations with exponential decay
        for i in range(self.dim):
            result += 2.5 * np.sin(15 * x[i]) * np.exp(-0.2 * x[i]**2) * adaptive_scale
            
        # Add saddle point structure with mixed polynomial and exponential terms
        for i in range(self.dim):
            result += 0.3 * x[i]**3 - 0.1 * x[i]**5 + 0.05 * np.exp(-x[i]**2)
            
        # Add multi-scale penalty terms with varying norms
        result += 0.1 * np.sum(np.abs(x)**3.2) + 0.08 * np.sum(np.abs(x)**4.1)
        
        # Include cross-dimensional coupling with non-linear interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.6 * np.sin(0.5 * (x[i] + x[j])) * np.cos(2 * x[i] * x[j]) * np.exp(-0.02 * (i-j)**2)
                
        # Add a global transformation that increases complexity with dimensionality
        result *= (1.0 + 0.2 * np.log(self.dim + 1))
        
        return result