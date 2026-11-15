import numpy as np

class ChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic component using logistic map modulation
        chaotic_factor = np.sum(np.sin(np.pi * np.mod(3.8 * x, 1.0)) * np.cos(np.pi * np.mod(4.2 * x, 1.0)))
        
        # Multi-scale harmonic component with varying frequencies and amplitudes
        harmonic = np.sum((x**2 + 0.1) * np.sin(10.0 * x) * np.cos(15.0 * x) * np.exp(-0.1 * x**2))
        
        # Saddle point inducing term with controlled curvature
        saddle = np.sum((x**3 - 3.0 * x) * np.exp(-0.05 * x**2))
        
        # Fractal-like self-similar structure with recursive scaling
        fractal = np.sum(np.sin(20.0 * x) * np.cos(25.0 * x) * np.exp(-0.02 * np.abs(x)) * np.sin(0.5 * np.sum(x**2)))
        
        # Variable conditioning component with piecewise linear transitions
        conditioning = np.sum(np.where(np.abs(x) < 1.0, x**4, np.abs(x)**1.5) * np.cos(7.0 * x))
        
        # Mixed smooth and abrupt transition component
        mixed = np.sum(np.exp(-0.5 * (x - np.sin(x))**2) * np.sin(8.0 * x) * np.cos(12.0 * x))
        
        # Combined function with dynamic weighting based on input magnitude
        weight1 = 0.3 + 0.2 * np.tanh(np.sum(x**2) - 5.0)
        weight2 = 0.4 + 0.1 * np.cos(np.sum(x))
        weight3 = 0.3 + 0.2 * np.sin(np.sum(x**3))
        
        return weight1 * harmonic + weight2 * saddle + weight3 * fractal + conditioning + mixed + 0.1 * chaotic_factor