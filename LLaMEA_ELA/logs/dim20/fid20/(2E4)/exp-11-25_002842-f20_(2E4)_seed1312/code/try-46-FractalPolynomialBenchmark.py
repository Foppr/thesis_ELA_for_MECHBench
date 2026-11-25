import numpy as np

class FractalPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base polynomial component with varying degrees
        poly_base = np.sum(x_norm**3 + 0.5 * x_norm**4 + 0.3 * x_norm**5)
        
        # Fractal-like recursive structure using self-similar patterns
        fractal_term = 0.0
        for i in range(1, min(6, self.dim + 1)):
            if i < self.dim:
                fractal_term += (x_norm[i-1]**2) * np.sin(x_norm[i] * np.pi * 2**i) * 0.1
        
        # Multi-scale sinusoidal modulation with varying amplitudes
        modulated_sine = 0.0
        for k in range(1, 8):
            modulated_sine += np.sin(k * x_norm * (1 + 0.1 * np.sin(k * np.pi / 4))) * (0.5 / k**1.5)
        
        # Discontinuous jump components at specific points to create non-smooth regions
        discontinuity = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                discontinuity += np.abs(x_norm[i] - x_norm[i+1]) * np.sin(x_norm[i] * 10)
        
        # Chaotic interaction term using tent map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            if i < self.dim - 2:
                chaotic += (np.sin(x_norm[i] * 7) + np.cos(x_norm[i+1] * 5)) * x_norm[i+2]
        
        # Ridge-like structure with varying curvature
        ridge = 0.0
        for i in range(self.dim):
            ridge += 0.05 * (x_norm[i]**2 + 0.1 * np.sin(x_norm[i] * 20)**2)
        
        # Asymmetric bell-shaped components to create skewed optima
        asymmetric = 0.0
        for i in range(self.dim):
            asymmetric += 0.03 * np.exp(-0.5 * ((x_norm[i] - 0.5) / 0.3)**2) * (1 + 0.2 * np.sin(x_norm[i] * 15))
        
        # Combined final function value
        return poly_base + fractal_term + modulated_sine + discontinuity + chaotic + ridge + asymmetric