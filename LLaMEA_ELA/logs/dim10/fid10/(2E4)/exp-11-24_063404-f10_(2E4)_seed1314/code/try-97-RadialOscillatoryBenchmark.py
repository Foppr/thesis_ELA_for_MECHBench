import numpy as np

class RadialOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for enhanced complexity
        self.chaotic_params = 2.0 + 3.0 * np.random.rand(dim)
        self.radial_centers = np.random.uniform(-2, 2, (dim, dim))
        self.radial_widths = 0.1 + 0.9 * np.random.rand(dim)
        self.frequency_modulators = 0.5 + 2.0 * np.random.rand(dim)
        self.decay_rates = 0.1 + 1.5 * np.random.rand(dim)
        
    def f(self, x):
        # Scale input to [-2, 2] for broader exploration
        x_scaled = x / 2.5
        
        # Chaotic sine wave component with varying frequencies and amplitudes
        chaotic_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            freq = self.frequency_modulators[i]
            amp = self.chaotic_params[i]
            chaotic_component += amp * np.sin(freq * xi + np.sin(freq * xi**2)) * np.cos(freq * xi**3)
        
        # Radial coupling with exponential decay
        radial_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            for j in range(self.dim):
                center = self.radial_centers[i, j]
                width = self.radial_widths[j]
                decay = self.decay_rates[j]
                radial_component += np.exp(-width * (xi - center)**2) * np.exp(-decay * abs(xi))
        
        # Cross-dimensional coupling with adaptive modulation
        coupling_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            for j in range(i+1, self.dim):
                xj = x_scaled[j]
                mod_factor = np.sin(xi) * np.cos(xj) + np.cos(xi) * np.sin(xj)
                coupling_component += mod_factor * (xi**2 + xj**2)
        
        # Adaptive exponential decay component
        decay_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            decay_rate = self.decay_rates[i]
            decay_component += np.exp(-decay_rate * abs(xi)) * np.sin(xi**3)
        
        # High-frequency oscillatory component with phase shifts
        oscillatory_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            oscillatory_component += np.sin(15 * xi + np.sin(7 * xi) + np.cos(3 * xi)) * np.cos(12 * xi + np.cos(5 * xi))
        
        # Combine all components with different weights
        return 0.3 * chaotic_component + 0.25 * radial_component + 0.2 * coupling_component + 0.15 * decay_component + 0.1 * oscillatory_component