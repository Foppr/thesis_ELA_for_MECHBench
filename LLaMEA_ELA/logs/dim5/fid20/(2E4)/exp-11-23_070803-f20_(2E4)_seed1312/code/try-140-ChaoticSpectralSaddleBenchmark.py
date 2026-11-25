import numpy as np

class ChaoticSpectralSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Chaotic tent map component with dynamic parameter
        chaotic_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Tent map with time-varying parameter based on dimension and position
            r = 1.95 + 0.05 * np.sin(i * np.pi / self.dim + np.sum(x_norm[:i+1]) if i > 0 else 0)
            tent_value = r * xi if xi < 0.5 else r * (1 - xi)
            chaotic_component += tent_value * (1 + 0.2 * np.sin(i * np.pi / self.dim))
        
        # Radial basis function component with multi-scale Gaussians and spectral decomposition
        radial_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple Gaussian centers with varying widths, heights, and spectral weights
            centers = np.linspace(-0.9, 0.9, 7)
            widths = np.logspace(-1.2, 0.1, 7)
            heights = np.linspace(0.3, 2.5, 7)
            # Spectral weighting based on dimension position
            spectral_weight = 1.0 + 0.3 * np.cos(i * np.pi / self.dim)
            for center, width, height in zip(centers, widths, heights):
                radial_component += height * np.exp(-0.5 * ((xi - center) / width)**2) * spectral_weight
        
        # Saddle-point gradient interactions with enhanced cross-dimensional coupling
        saddle_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Enhanced gradient-based saddle with multi-scale curvature and asymmetry
            curvature = 1.0 + 0.4 * np.sin(i * np.pi / self.dim)
            asymmetry = 0.6 * np.cos(i * np.pi / self.dim)
            saddle_component += (xi**2 - 1)**3 * curvature + \
                               asymmetry * xi**4 + \
                               0.3 * np.sin(xi * 7) * (1 + 0.15 * i) + \
                               0.1 * np.cos(xi * 3) * np.sin(i)
        
        # Enhanced cross-dimensional coupling with spectral interactions
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Spectral coupling with frequency modulation and dimension-dependent scaling
                freq_i = 1.5 + 0.5 * np.sin(i * np.pi / self.dim)
                freq_j = 1.5 + 0.5 * np.cos(j * np.pi / self.dim)
                coupling_strength = 1.0 + 0.3 * np.sin(i + j) * np.cos(i - j)
                cross_coupling += coupling_strength * np.sin(freq_i * x_norm[i] + freq_j * x_norm[j]) * \
                                 np.cos(freq_i * x_norm[i] - freq_j * x_norm[j]) * \
                                 (1 + 0.25 * np.sin(i + j) * np.cos(i - j))
        
        # Multi-scale fractal-like radial modulation with spectral decomposition
        fractal_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Radial fractal with multiple frequency components and dimension-dependent scaling
            freqs = [1, 2, 4, 8, 16, 32]
            for k, freq in enumerate(freqs):
                scale_factor = 1.0 + 0.2 * np.sin(i * np.pi / self.dim + k)
                fractal_component += scale_factor * np.sin(freq * xi) * (1.0 / freq**1.5) * \
                                   (1 + 0.15 * np.cos(i * freq))
        
        # Enhanced dimensionality-adaptive gradient field with spectral components
        gradient_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Adaptive scaling based on dimension and spectral components
            scale_factor = 1.0 + 0.6 * np.sin(i * np.pi / self.dim) * np.cos(xi)
            gradient_component += scale_factor * (xi**4 - xi**2) * (1 + 0.1 * np.cos(i)) + \
                                0.15 * np.sin(xi * 4) * np.cos(i)
        
        # Combine all components with dynamic weights
        weights = [1.5, 1.2, 1.8, 1.0, 1.4, 1.3]
        result = weights[0] * chaotic_component + \
                 weights[1] * radial_component + \
                 weights[2] * saddle_component + \
                 weights[3] * cross_coupling + \
                 weights[4] * fractal_component + \
                 weights[5] * gradient_component
        
        # Add adaptive noise based on function value and input with enhanced complexity
        noise_amplitude = 0.01 * (1 + 0.02 * np.abs(result)) * (1 + 0.03 * np.sum(np.abs(x_norm))) * \
                         (1 + 0.05 * np.sin(np.sum(x_norm)))
        noise = np.random.normal(0, noise_amplitude)
        
        return result + noise