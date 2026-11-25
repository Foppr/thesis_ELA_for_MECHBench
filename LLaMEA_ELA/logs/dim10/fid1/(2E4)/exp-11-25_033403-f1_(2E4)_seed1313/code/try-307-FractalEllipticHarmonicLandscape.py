import numpy as np

class FractalEllipticHarmonicLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize fractal pattern parameters
        self.fractal_centers = np.random.uniform(-4.0, 4.0, (5, dim))
        self.fractal_scales = np.random.uniform(0.5, 2.0, (5, dim))
        self.fractal_weights = np.random.uniform(0.5, 2.0, 5)
        # Initialize elliptic structures
        self.ellipse_centers = np.random.uniform(-3.0, 3.0, (3, dim))
        self.ellipse_axes = np.random.uniform(0.5, 2.0, (3, dim))
        self.ellipse_rotation = np.random.uniform(0, 2*np.pi, 3)
        self.ellipse_weights = np.random.uniform(1.0, 3.0, 3)
        # Initialize harmonic potential components
        self.harm_frequencies = np.random.uniform(1.0, 5.0, dim)
        self.harm_amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.harm_phases = np.random.uniform(0, 2*np.pi, dim)
        # Initialize noise parameters
        self.noise_magnitude = np.random.uniform(0.1, 0.5, dim)
        self.noise_frequency = np.random.uniform(0.1, 0.3, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute fractal-based self-similarity pattern
        fractal_potential = 0.0
        for i in range(5):
            fractal_dist = 0.0
            for j in range(self.dim):
                scaled_x = (x[j] - self.fractal_centers[i, j]) / self.fractal_scales[i, j]
                fractal_dist += scaled_x**2
            fractal_potential += self.fractal_weights[i] * np.exp(-0.5 * fractal_dist)
        
        # Compute elliptic structures
        ellipse_potential = 0.0
        for i in range(3):
            # Rotate coordinates
            rotated_x = np.zeros(self.dim)
            for j in range(self.dim):
                if j == 0:
                    rotated_x[j] = (x[0] - self.ellipse_centers[i, 0]) * np.cos(self.ellipse_rotation[i]) + \
                                   (x[1] - self.ellipse_centers[i, 1]) * np.sin(self.ellipse_rotation[i])
                elif j == 1:
                    rotated_x[j] = -(x[0] - self.ellipse_centers[i, 0]) * np.sin(self.ellipse_rotation[i]) + \
                                   (x[1] - self.ellipse_centers[i, 1]) * np.cos(self.ellipse_rotation[i])
                else:
                    rotated_x[j] = x[j] - self.ellipse_centers[i, j]
            
            # Compute elliptic distance
            ellipse_dist = 0.0
            for j in range(self.dim):
                ellipse_dist += (rotated_x[j] / self.ellipse_axes[i, j])**2
            ellipse_potential += self.ellipse_weights[i] * np.exp(-0.5 * ellipse_dist)
        
        # Compute harmonic potential with noise modulation
        harm_potential = 0.0
        for j in range(self.dim):
            # Base harmonic term
            base_harm = self.harm_amplitudes[j] * np.sin(
                self.harm_frequencies[j] * x[j] + self.harm_phases[j]
            )
            # Noise modulation
            noise_mod = self.noise_magnitude[j] * np.sin(
                self.noise_frequency[j] * x[j] + np.random.randn() * 0.1
            )
            harm_potential += base_harm + noise_mod
        
        # Combine all components with adaptive weighting
        total = 0.7 * fractal_potential + 1.3 * ellipse_potential + 0.5 * harm_potential
        
        return total