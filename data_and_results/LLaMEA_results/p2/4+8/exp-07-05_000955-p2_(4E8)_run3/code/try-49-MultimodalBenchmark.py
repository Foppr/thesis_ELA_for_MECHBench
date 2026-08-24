import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with sinusoidal modulation
        r = np.sqrt(np.sum(x**2))
        radial = r * np.sin(3.0 * r) * np.exp(-0.1 * r**2)
        
        # Multi-modal sinusoidal terms
        modal = 0.0
        for i in range(self.dim):
            modal += np.sin(2.0 * x[i]) * np.cos(4.0 * x[i]) * np.sin(6.0 * x[i])
        
        # Cross-dimensional interaction terms
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += np.sin(x[i] * x[j]) * np.exp(-0.5 * (x[i]**2 + x[j]**2))
        
        # Polynomial coupling with trigonometric modulation
        poly = 0.0
        for i in range(self.dim):
            poly += x[i]**4 * np.cos(2.0 * x[i]) + x[i]**3 * np.sin(3.0 * x[i])
        
        # Central attraction with repulsion zones
        center_attraction = 0.0
        for i in range(self.dim):
            center_attraction += (x[i] - np.sin(x[i]))**2
        
        # Asymmetric landscape with varying curvature
        asym = 0.0
        for i in range(self.dim):
            asym += x[i]**5 * np.exp(-0.5 * x[i]**2)
        
        return radial + modal + cross + poly + center_attraction + asym