import numpy as np

class ChaoticMultimodalBenchmark:
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
        
        # Precompute sinusoidal frequencies and amplitudes
        self.freqs = np.random.uniform(1.0, 5.0, dim)
        self.amps = np.random.uniform(0.5, 2.0, dim)
        
        # Precompute radial basis function centers and variances
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        self.rbf_vars = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Sinusoidal oscillation component with chaotic modulation
        sin_component = np.sum(self.amps * np.sin(self.freqs * x_norm + self.attractor))
        
        # Radial basis function component
        rbf_component = 0.0
        for i in range(self.dim):
            dist = np.sum((x_norm - self.rbf_centers[i])**2)
            rbf_component += np.exp(-dist / (2 * self.rbf_vars[i]**2))
        
        # Chaotic interaction term using the attractor
        chaotic_interaction = np.sum(x_norm * self.attractor)
        
        # Polynomial interaction term with varying degrees
        poly_interaction = np.sum(x_norm**3 + 0.3 * x_norm**5 + 0.05 * x_norm**7)
        
        # Combine components with dynamic weights
        total = 0.4 * sin_component + 0.3 * rbf_component + 0.2 * chaotic_interaction + 0.1 * poly_interaction
        
        # Add a conditioning factor that increases with dimensionality
        conditioning = 1.0 + 0.1 * self.dim + 0.01 * np.sum(x_norm**2)
        
        return total * conditioning