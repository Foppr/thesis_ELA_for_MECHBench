import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add multiple global minima with exponential scaling and sine modulation
        for i in range(self.dim):
            result += 0.9 * np.exp(-0.03 * x[i]**2) * np.sin(12 * x[i])**3
            
        # Add chaotic oscillations with varying frequencies and damping factors
        for i in range(self.dim):
            result += 0.35 * np.sin(x[i] * np.exp(0.8 * i)) * np.cos(x[i] * np.exp(0.5 * i)) * np.exp(-0.12 * i)
            
        # Add saddle point structure with higher-order polynomial terms
        for i in range(self.dim):
            result += 0.25 * x[i]**5 - 0.18 * x[i]**4 + 0.07 * x[i]**3
            
        # Add a complex penalty term with mixed norms and adaptive scaling
        result += 0.09 * np.sum(np.abs(x)**3.7) + 0.02 * np.sum(np.abs(x)**5.5)
        
        # Add cross-dimensional interactions for increased complexity with trigonometric coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.18 * np.sin(x[i] * x[j]) * np.cos(0.4 * (x[i] + x[j])) * np.exp(-0.03 * (i+j))
                
        # Add a global scaling factor that increases with dimensionality
        result *= (1.0 + 0.12 * self.dim)
        
        # Add a novel fractal-like component with recursive sine and cosine interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.15 * np.sin(np.pi * x[i] * np.cos(x[j])) * np.cos(np.pi * x[j] * np.sin(x[i])) * np.exp(-0.02 * (i+j)**1.5)
                
        # Add a high-frequency chaotic modulation term
        for i in range(self.dim):
            result += 0.4 * np.sin(20 * x[i] + np.sin(5 * x[i])) * np.cos(15 * x[i] + np.cos(3 * x[i]))
            
        # Add a multi-scale oscillation component with varying amplitudes and frequencies
        for i in range(self.dim):
            result += 0.2 * np.sum([0.5**k * np.sin(2**(k+1) * x[i]) for k in range(3)])
            
        return result