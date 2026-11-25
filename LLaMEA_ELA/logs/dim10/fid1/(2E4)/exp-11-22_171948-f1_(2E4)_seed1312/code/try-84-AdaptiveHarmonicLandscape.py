import numpy as np

class AdaptiveHarmonicLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Exponentially decaying harmonic components with dynamic phase modulation
        for i in range(self.dim):
            freq = 2 ** (i % 5 + 1)
            phase = np.pi * (i / self.dim) ** 2
            harmonic = np.sin(freq * x[i] + phase) * np.exp(-0.1 * np.abs(x[i]))
            result += 0.5 * harmonic**2
        
        # Dynamic phase coupling between dimensions
        for i in range(self.dim - 1):
            coupling = np.sin(3 * (x[i] - x[i+1]) + 0.5 * i) * np.cos(2 * (x[i] + x[i+1]))
            result += 0.3 * coupling
        
        # Adaptive ridge structure with dimensionality-dependent curvature
        for i in range(self.dim):
            ridge_freq = 10 + i * 2
            ridge = np.sin(ridge_freq * x[i]) * np.exp(-0.05 * x[i]**2)
            result += 0.7 * ridge**2
        
        # Exponentially weighted cross-dimensional interactions
        for i in range(self.dim - 1):
            weight = np.exp(-0.2 * (i + 1))
            interaction = (x[i]**2 + x[i+1]**2) * np.sin(5 * (x[i] - x[i+1]))
            result += weight * interaction
        
        # Multi-scale oscillatory behavior with varying amplitude decay
        for i in range(self.dim):
            scale = 1.0 / (1.0 + 0.1 * i)
            oscillation = np.sin(20 * x[i]) * np.cos(15 * x[i]) * scale
            result += 0.4 * oscillation**2
        
        # Adaptive conditioning based on local gradient magnitude
        grad_magnitude = 0.0
        for i in range(self.dim):
            grad_magnitude += np.abs(np.cos(x[i]))
        conditioning = 1.0 + 0.5 * np.tanh(grad_magnitude)
        result *= conditioning
        
        # Asymmetric basin structure with modified symmetry breaking
        asymmetry = 0.0
        for i in range(self.dim):
            asymmetry += (x[i] ** 3) * np.sin(0.5 * x[i])
        result += 0.2 * asymmetry
        
        # Final normalization and regularization
        result /= self.dim
        result += 0.05 * np.sum(x**4) / self.dim
        
        return result