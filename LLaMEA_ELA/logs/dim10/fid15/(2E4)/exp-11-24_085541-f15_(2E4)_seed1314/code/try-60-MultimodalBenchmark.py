import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add exponentially decaying sinusoidal components with rotation
        for i in range(self.dim):
            rotated_x = np.sum(x * np.roll(np.eye(self.dim), i, axis=1), axis=1)
            result += 2.0 * np.exp(-0.1 * np.abs(x[i])) * np.sin(10.0 * x[i]) * np.cos(7.0 * x[i])
            
        # Add fractal-like oscillations with varying scales
        for i in range(self.dim):
            scale = 1.0
            fractal_sum = 0.0
            for k in range(1, 8):
                scale *= 0.5
                fractal_sum += scale * np.sin(2**(k) * x[i])
            result += 0.5 * fractal_sum
            
        # Add polynomial modulations with cross-dimensional interactions
        for i in range(self.dim):
            result += 0.3 * x[i]**6 - 0.8 * x[i]**5 + 0.7 * x[i]**4 - 0.4 * x[i]**3
            
        # Add rotation-invariant chaotic component
        rotation_invariant = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                rotation_invariant += np.sin(x[i] * x[j]) * np.cos(2.0 * (x[i]**2 + x[j]**2))
        result += 0.6 * rotation_invariant
        
        # Add exponential penalty with adaptive scaling
        result += 0.1 * np.sum(np.exp(0.5 * np.abs(x)) - 1)
        
        # Add hyperbolic sine polynomial interactions
        for i in range(self.dim):
            result += 0.4 * np.sinh(2.0 * x[i]) * x[i]**2
            
        # Add sharp ridge-like components
        ridge_sum = 0.0
        for i in range(self.dim):
            ridge_sum += np.exp(-5.0 * (x[i] - 1.0)**2) + np.exp(-3.0 * (x[i] + 2.0)**2)
        result += 0.8 * ridge_sum
        
        # Add multi-scale chaotic oscillations
        for i in range(self.dim):
            chaotic_component = 0.0
            for k in range(1, 6):
                chaotic_component += 0.2**k * np.sin(3**(k) * x[i])
            result += chaotic_component
            
        # Add conditioning factor based on dimensionality
        condition_factor = 1.0 + 0.2 * self.dim
        result *= condition_factor
        
        return result