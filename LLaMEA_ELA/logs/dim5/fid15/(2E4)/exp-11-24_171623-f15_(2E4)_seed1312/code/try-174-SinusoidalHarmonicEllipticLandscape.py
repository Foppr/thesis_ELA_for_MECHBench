import numpy as np

class SinusoidalHarmonicEllipticLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Generate spiral parameters for each dimension
        self.spiral_amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.spiral_frequencies = np.random.uniform(1.0, 6.0, dim)
        self.spiral_phases = np.random.uniform(0, 2*np.pi, dim)
        
        # Radial harmonic potential centers and strengths
        self.potential_centers = np.random.uniform(-3, 3, (dim, 10))
        self.potential_strengths = np.random.uniform(0.5, 3.0, 10)
        
        # Elliptic decoupling parameters with varying conditioning
        self.ellipse_axes = np.random.uniform(0.5, 3.0, (dim, dim))
        self.ellipse_rotation = np.random.uniform(0, np.pi, (dim, dim))
        
        # Add multiple local minima with different characteristics
        self.minima_centers = np.random.uniform(-4, 4, (dim, 8))
        self.minima_depths = np.random.uniform(0.5, 2.0, 8)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal spiral component
        spiral_sum = 0.0
        for i in range(self.dim):
            spiral_sum += self.spiral_amplitudes[i] * np.sin(
                self.spiral_frequencies[i] * x_norm[i] + self.spiral_phases[i]
            ) * np.cos(self.spiral_frequencies[i] * x_norm[i] + self.spiral_phases[i])
        
        # Radial harmonic potential component
        potential_sum = 0.0
        for i in range(self.dim):
            dists = np.linalg.norm(x_norm[i] - self.potential_centers[i], axis=1)
            potential_sum += np.sum(self.potential_strengths * np.exp(-dists**2))
        
        # Elliptic decoupling component with adaptive conditioning
        ellipse_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    ellipse_sum += self.ellipse_axes[i, j] * (x_norm[i] - x_norm[j])**2
        
        # Multiple local minima with varying depths
        minima_sum = 0.0
        for i in range(8):
            dist = np.linalg.norm(x_norm - self.minima_centers[:, i])
            minima_sum += self.minima_depths[i] * np.exp(-dist**2)
        
        # Combine all components with dynamic weights
        result = 0.3 * spiral_sum + 0.4 * potential_sum + 0.2 * ellipse_sum + 0.1 * minima_sum
        
        # Apply nonlinear transformation to increase complexity and create plateaus
        result = np.tanh(result) * (1.0 + 0.3 * np.abs(result)) + 0.1 * np.sin(10 * result)
        
        return result