import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Polynomial chaos component with varying exponents
        for i in range(self.dim):
            result += 2.0 * (x[i]**6 + 0.5 * x[i]**5 + 0.3 * x[i]**4 + 0.1 * x[i]**3)
            
        # Radial basis function with dynamic centers and widths
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(self.dim):
            if i < len(centers):
                result += 3.0 * np.exp(-0.5 * (x[i] - centers[i])**2) + 1.5 * np.exp(-0.3 * (x[i] + centers[i])**2)
                
        # Dynamic cross-dimensional coupling with time-varying sinusoids
        t = 1.0 + 0.1 * self.dim  # Time parameter
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                coupling = np.sin(t * x[i] * x[j]) * np.cos(0.5 * t * (x[i]**2 + x[j]**2))
                result += 1.5 * coupling
                
        # Multi-modal sine-polynomial interactions
        for i in range(self.dim):
            result += 2.5 * np.sin(3.0 * x[i]) * (x[i]**4 - 2.0 * x[i]**2 + 1.0)
            
        # Fractional power chaotic component
        for i in range(self.dim):
            result += 1.8 * np.power(np.abs(x[i]), 1.7) * np.sin(5.0 * x[i])
            
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        result *= condition_factor
        
        # Complex hyperbolic interactions
        for i in range(self.dim):
            result += 1.2 * np.sinh(1.5 * x[i]) * np.cos(2.0 * x[i]) + 0.8 * np.cosh(1.2 * x[i]) * np.sin(1.8 * x[i])
            
        # Nested trigonometric component with recursive structure
        for i in range(self.dim):
            nested = 0.0
            for k in range(1, 10):
                nested += 0.3**k * np.sin(2**(k) * x[i])
            result += nested
            
        # Penalty term with logarithmic scaling
        result += 0.7 * np.sum(np.log(np.abs(x) + 1.5))
        
        # Multi-modal component with exponential decay interactions
        for i in range(self.dim):
            result += 1.0 * np.exp(-0.5 * x[i]**2) * np.sin(4.0 * x[i])
            
        # Cross-dimensional polynomial coupling with dynamic coefficients
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 0.5 + 0.3 * np.sin(0.1 * (i + j))
                result += coeff * (x[i]**2 + x[j]**2) * np.cos(x[i] * x[j])
                
        # Time-varying chaotic modulation
        for i in range(self.dim):
            result += 0.9 * np.sin(np.pi * np.sin(4.0 * x[i])) * np.cos(np.pi * np.cos(3.0 * x[i]))
            
        return result