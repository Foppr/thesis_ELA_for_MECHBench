import numpy as np

class ChaoticSpectralSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Chaotic tent map component with enhanced dynamic parameter and multi-scale modulation
        chaotic_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Enhanced tent map with time-varying parameter based on dimension, position, and spectral frequency
            r = 1.95 + 0.2 * np.sin(i * np.pi / self.dim + np.sum(x_norm[:i+1]) if i > 0 else 0) + \
                0.08 * np.cos(xi * 3 + i)
            tent_value = r * xi if xi < 0.5 else r * (1 - xi)
            chaotic_component += tent_value * (1 + 0.4 * np.sin(i * np.pi / self.dim + xi * 2))
        
        # Radial basis function component with multi-scale Gaussians, spectral decomposition, and dynamic center modulation
        radial_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple Gaussian centers with varying widths, heights, spectral weights, and dynamic modulation
            centers = np.linspace(-0.9, 0.9, 7)
            widths = np.logspace(-1.2, 0.3, 7)
            heights = np.linspace(0.3, 3.2, 7)
            # Spectral weighting based on dimension position and dynamic frequency modulation
            spectral_weight = 1.0 + 0.5 * np.cos(i * np.pi / self.dim + xi * 1.5)
            center_mod = 0.2 * np.sin(xi * 4 + i * 0.5)
            for center, width, height in zip(centers, widths, heights):
                radial_component += height * np.exp(-0.5 * ((xi - (center + center_mod)) / width)**2) * spectral_weight
        
        # Saddle-point gradient interactions with enhanced cross-dimensional coupling and asymmetry
        saddle_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Enhanced gradient-based saddle with multi-scale curvature, asymmetry, and dynamic frequency modulation
            curvature = 1.0 + 0.6 * np.sin(i * np.pi / self.dim + xi * 0.5)
            asymmetry = 0.8 * np.cos(i * np.pi / self.dim + xi * 1.2)
            saddle_component += (xi**2 - 1)**3 * curvature + \
                               asymmetry * xi**4 + \
                               0.4 * np.sin(xi * 8) * (1 + 0.3 * i) + \
                               0.15 * np.cos(xi * 4) * np.sin(i * 1.3) + \
                               0.08 * np.sin(xi * 2 + i * 0.7)
        
        # Enhanced cross-dimensional coupling with spectral interactions and multi-scale frequency modulation
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Spectral coupling with frequency modulation, dimension-dependent scaling, and dynamic phase shifts
                freq_i = 1.7 + 0.5 * np.sin(i * np.pi / self.dim + x_norm[i] * 0.3)
                freq_j = 1.7 + 0.5 * np.cos(j * np.pi / self.dim + x_norm[j] * 0.4)
                coupling_strength = 1.0 + 0.3 * np.sin(i + j) * np.cos(i - j) + \
                                   0.15 * np.cos(i * 2 + j * 1.5)
                cross_coupling += coupling_strength * np.sin(freq_i * x_norm[i] + freq_j * x_norm[j] + i * 0.2) * \
                                 np.cos(freq_i * x_norm[i] - freq_j * x_norm[j] + j * 0.3) * \
                                 (1 + 0.4 * np.sin(i + j) * np.cos(i - j)) * \
                                 (1 + 0.1 * np.cos(i * 0.5 + j * 0.7))
        
        # Multi-scale fractal-like radial modulation with enhanced spectral decomposition and dynamic scaling
        fractal_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Radial fractal with multiple frequency components, dimension-dependent scaling, and phase modulation
            freqs = [1, 2, 4, 8, 16, 32]
            for k, freq in enumerate(freqs):
                scale_factor = 1.0 + 0.4 * np.sin(i * np.pi / self.dim + k * 0.5) + \
                              0.15 * np.cos(xi * freq + i * 0.3)
                fractal_component += scale_factor * np.sin(freq * xi + i * 0.2) * (1.0 / freq**1.6) * \
                                   (1 + 0.25 * np.cos(i * freq + xi * 0.4))
        
        # Enhanced dimensionality-adaptive gradient field with spectral components and dynamic modulation
        gradient_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Adaptive scaling based on dimension, spectral components, and dynamic phase shifts
            scale_factor = 1.0 + 0.8 * np.sin(i * np.pi / self.dim) * np.cos(xi) + \
                          0.2 * np.sin(xi * 5 + i * 0.3)
            gradient_component += scale_factor * (xi**4 - xi**2) * (1 + 0.2 * np.cos(i * 1.2)) + \
                                0.25 * np.sin(xi * 5) * np.cos(i * 0.8) + \
                                0.1 * np.cos(xi * 3) * np.sin(i * 0.6)
        
        # Combine all components with dynamic weights and enhanced spectral modulation
        weights = [1.7, 1.4, 1.8, 1.2, 1.6, 1.5]
        result = weights[0] * chaotic_component + \
                 weights[1] * radial_component + \
                 weights[2] * saddle_component + \
                 weights[3] * cross_coupling + \
                 weights[4] * fractal_component + \
                 weights[5] * gradient_component
        
        # Add adaptive noise based on function value, input, and enhanced complexity with multi-scale modulation
        noise_amplitude = 0.015 * (1 + 0.03 * np.abs(result)) * (1 + 0.04 * np.sum(np.abs(x_norm))) * \
                         (1 + 0.08 * np.sin(np.sum(x_norm) * 0.5)) * \
                         (1 + 0.02 * np.cos(np.sum(x_norm) * 0.3))
        noise = np.random.normal(0, noise_amplitude)
        
        return result + noise