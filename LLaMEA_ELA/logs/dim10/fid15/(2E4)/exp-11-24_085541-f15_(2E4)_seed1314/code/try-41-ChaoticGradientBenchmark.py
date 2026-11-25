import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add fractional polynomial terms with varying exponents
        for i in range(self.dim):
            result += 0.5 * (x[i]**1.7 + x[i]**2.3) + 0.3 * x[i]**3.1
            
        # Add chaotic gradient component using nested sine functions
        for i in range(self.dim):
            result += 2.0 * np.sin(np.pi * np.sin(np.pi * x[i])) * np.cos(0.5 * x[i])
            
        # Dynamic coupling with sine-wave interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                freq = 2.0 + 0.5 * (i + j) % 3
                result += 0.8 * np.sin(freq * x[i]) * np.cos(freq * x[j])
                
        # Adaptive conditioning based on dimensionality and position
        condition_factor = 1.0 + 0.2 * self.dim + 0.1 * np.mean(np.abs(x))
        result *= condition_factor
        
        # Add a hyperbolic tangent component for smooth transitions
        for i in range(self.dim):
            result += 0.6 * np.tanh(1.5 * x[i]) ** 2
            
        # Multi-modal with exponential decay and oscillatory behavior
        for i in range(self.dim):
            result += 1.2 * np.exp(-0.5 * (x[i] - 1.0)**2) * np.sin(4.0 * x[i])
            
        # Add a component that introduces fractal-like sensitivity to small changes
        for i in range(self.dim):
            frac_part = np.mod(x[i], 1.0)
            result += 0.5 * np.sin(10.0 * frac_part) * np.cos(15.0 * frac_part)
            
        # Penalty term for values far from the origin
        result += 0.3 * np.sum(np.abs(x)**3)
        
        return result