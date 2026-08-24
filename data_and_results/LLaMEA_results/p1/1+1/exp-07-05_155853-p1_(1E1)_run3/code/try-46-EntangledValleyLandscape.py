import numpy as np

class EntangledValleyLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis functions with varying centers and widths
        rbfs = 0
        centers = np.linspace(-4.5, 4.5, min(10, self.dim))
        for i in range(min(10, self.dim)):
            center = centers[i] if self.dim > 1 else 0.0
            width = 1.0 + 0.5 * np.sin(i * 0.5)
            rbfs += np.exp(-0.5 * ((x[0] - center)**2 + (x[1] - center)**2) / width**2)
        
        # Gradient-based attraction fields creating entangled valleys
        attraction = 0
        for i in range(self.dim - 1):
            dx = x[i+1] - x[i]
            attraction += 0.5 * (dx**2 + 0.1 * np.sin(5 * dx))
        
        # Higher-order polynomial terms with alternating signs
        poly = 0
        for i in range(self.dim):
            poly += (-1)**i * (0.05 * x[i]**6 + 0.1 * x[i]**5 - 0.2 * x[i]**4 + 
                              0.15 * x[i]**3 - 0.05 * x[i]**2 + 0.01 * x[i])
        
        # Cross-dimensional coupling with trigonometric interaction
        coupling = 0
        for i in range(self.dim - 2):
            coupling += np.sin(x[i] + x[i+1]) * np.cos(x[i+2])
        
        # Add a global periodic modulation
        periodic_mod = np.sin(0.5 * np.sum(x**2)) * np.cos(0.3 * np.sum(x))
        
        # Combine all components
        return 2.0 * rbfs + 0.5 * attraction + poly + 0.3 * coupling + 0.1 * periodic_mod