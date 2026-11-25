import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with mixed exponents
        f = np.sum(0.5 * x**2 + 0.3 * x**4 + 0.1 * x**6)
        
        # Add chaotic trigonometric interactions with varying frequencies
        for i in range(self.dim):
            f += 0.8 * np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[(i + 1) % self.dim]) * np.sin(5 * np.pi * x[(i + 2) % self.dim])
            
        # Add radial basis function components with varying centers and widths
        for i in range(self.dim):
            center = 2.0 * np.sin(i * np.pi / self.dim)
            width = 0.5 + 0.3 * np.cos(i * np.pi / self.dim)
            f += 0.4 * np.exp(-width * (x[i] - center)**2) * np.sin(4 * x[i])
            
        # Add cross-dimensional polynomial coupling
        for i in range(self.dim):
            f += 0.2 * x[i]**3 * x[(i + 1) % self.dim]**2 + 0.15 * x[i]**2 * x[(i + 2) % self.dim]**3
            
        # Add chaotic phase-shifted sinusoidal terms
        for i in range(self.dim):
            f += 0.3 * np.sin(7 * x[i] + 0.5 * np.sin(3 * x[(i + 1) % self.dim])) * np.cos(4 * x[(i + 2) % self.dim])
            
        # Add multi-modal penalty terms with varying scales
        f += 0.25 * np.sum(np.abs(x)**3.5) + 0.1 * np.sum(np.sin(2 * x)**4)
        
        # Add radial basis components with dynamic centers
        for i in range(self.dim):
            center = 3.0 * np.cos(i * np.pi / (self.dim + 1))
            f += 0.35 * np.exp(-0.5 * (x[i] - center)**2) * np.cos(6 * x[i])
            
        # Add chaotic higher-order interactions
        for i in range(self.dim):
            f += 0.1 * np.sin(9 * x[i]) * np.cos(7 * x[(i + 1) % self.dim]) * np.sin(5 * x[(i + 2) % self.dim]) * np.cos(3 * x[(i + 3) % self.dim])
            
        return f