import numpy as np

class HybridChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate a chaotic attractor sequence using a modified Lorenz system
        self.attractor = np.zeros(dim)
        x, y, z = 0.1, 0.0, 0.0
        for i in range(dim * 100):
            dx = 10 * (y - x)
            dy = x * (28 - z) - y
            dz = x * y - (8/3) * z
            x, y, z = x + 0.01 * dx, y + 0.01 * dy, z + 0.01 * dz
            if i >= dim * 99:
                self.attractor[i - dim * 99] = x
        
        # Precompute oscillation frequencies
        self.freqs = np.linspace(1, 10, dim)
        
        # Precompute radial basis function centers and widths
        self.centers = np.random.uniform(-1, 1, (dim, dim))
        self.widths = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Sinusoidal oscillation component
        sin_comp = np.sum(np.sin(self.freqs * x_norm) * np.cos(self.freqs * x_norm))
        
        # Radial basis function component with chaotic centers
        rbf_comp = 0.0
        for i in range(self.dim):
            dist = np.sum((x_norm - self.centers[i])**2)
            rbf_comp += np.exp(-dist / (2 * self.widths[i]**2)) * (1 + 0.5 * self.attractor[i])
        
        # Chaotic interaction term using attractor values
        chaotic_term = np.sum(self.attractor * x_norm**2)
        
        # Asymmetric penalty based on input magnitude
        penalty = np.sum(np.abs(x_norm)**3 * np.exp(-np.abs(x_norm)))
        
        # Dynamic conditioning factor
        cond_factor = 1 + 0.5 * np.sin(np.sum(x_norm**2) / self.dim)
        
        # Combine all components
        total = 0.4 * sin_comp + 0.3 * rbf_comp + 0.2 * chaotic_term + 0.1 * penalty
        
        return total * cond_factor