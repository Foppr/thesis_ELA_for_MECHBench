import numpy as np

class ChaoticRotationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Generate rotation matrix for dimensionality
        rotation = np.eye(self.dim)
        if self.dim > 1:
            angle = np.pi / 4.0 * (self.dim % 8)
            cos_a, sin_a = np.cos(angle), np.sin(angle)
            rotation[:2, :2] = [[cos_a, -sin_a], [sin_a, cos_a]]
        
        # Apply rotation to input
        x_rot = rotation @ x_norm
        
        # Polynomial conditioning with varying exponents
        poly_term = np.sum((x_rot**4 + 0.5 * x_rot**3 + 0.2 * x_rot**2 + 0.1 * x_rot) ** 1.5)
        
        # Composite sinusoidal waves with multiple frequencies and amplitudes
        wave1 = np.sum(np.sin(2 * np.pi * x_rot) * np.cos(3 * np.pi * x_rot))
        wave2 = np.sum(np.sin(5 * np.pi * x_rot**2) * np.cos(4 * np.pi * x_rot))
        wave3 = np.sum(np.sin(7 * np.pi * x_rot) * np.cos(6 * np.pi * x_rot**2))
        
        # Chaotic modulation with logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(10 * np.pi * (x_rot[i] + 0.1 * np.sin(5 * x_rot[(i+1) % self.dim])))
        
        # Saddle-point attraction with harmonic repulsion
        saddle = np.sum(x_rot**2 * np.exp(-0.5 * np.sum(x_rot**2)))
        
        # Cross-dimensional coupling with exponential interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.exp(-0.1 * (x_rot[i] - x_rot[j])**2) * np.sin(2 * np.pi * (x_rot[i] + x_rot[j]))
        
        # Final combined function with diverse curvature and multiple local minima
        return 2.0 * poly_term + 1.5 * wave1 + 1.2 * wave2 + 0.8 * wave3 + 0.6 * chaotic + 0.4 * saddle + 0.3 * cross_term