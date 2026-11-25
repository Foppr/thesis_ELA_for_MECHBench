import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Adaptive conditioning parameters per dimension
        self.conditioning_factors = np.random.uniform(0.5, 2.0, dim)
        self.frequency_multipliers = np.random.uniform(1.0, 8.0, dim)
        self.amplitude_factors = np.random.uniform(0.5, 3.0, dim)
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.5, 10)
        # Sinusoidal components
        self.sin_frequencies = np.random.uniform(0.5, 6.0, dim)
        self.sin_amplitudes = np.random.uniform(0.3, 2.0, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Radial basis function components
        for i in range(10):
            rbf_sum = 0.0
            for j in range(self.dim):
                rbf_sum += (x_norm[j] - self.rbf_centers[i, j])**2
            f_val += np.exp(-rbf_sum / (2 * self.rbf_widths[i]**2))
        
        # Sinusoidal components with adaptive frequencies and amplitudes
        for i in range(self.dim):
            f_val += self.sin_amplitudes[i] * np.sin(self.sin_frequencies[i] * x_norm[i])**2
        
        # Adaptive conditioning terms
        for i in range(self.dim):
            f_val += self.conditioning_factors[i] * x_norm[i]**4
        
        # Cross-dimension coupling with radial interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.01)
                f_val += 0.5 * np.exp(-dist**2 / (2 * 0.5**2))
        
        # Multi-scale periodic components
        for scale in [0.1, 0.3, 1.0, 3.0]:
            periodic_sum = 0.0
            for i in range(self.dim):
                periodic_sum += np.sin(scale * x_norm[i]) * np.cos(scale * x_norm[i])
            f_val += 0.3 * periodic_sum**2
        
        # Add noise-like perturbations
        noise_perturbation = 0.05 * np.sum(np.sin(17 * x_norm) + np.cos(11 * x_norm))
        f_val += noise_perturbation
        
        return f_val