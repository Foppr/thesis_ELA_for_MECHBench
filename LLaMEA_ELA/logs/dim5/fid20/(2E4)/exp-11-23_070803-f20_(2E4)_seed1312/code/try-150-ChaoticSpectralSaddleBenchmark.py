import numpy as np

class ChaoticSpectralSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Chaotic tent map component with dynamic parameter and multi-scale modulation
        chaotic_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Tent map with time-varying parameter based on dimension and position
            r = 1.95 + 0.08 * np.cos(i * np.pi / self.dim + np.sum(x_norm[:i+1]) if i > 0 else 0)
            tent_value = r * xi if xi < 0.5 else r * (1 - xi)
            chaotic_component += tent_value * (1 + 0.2 * np.cos(i * np.pi / self.dim + xi))
        
        # Radial basis function component with multi-scale Gaussians, spectral decomposition and phase modulation
        radial_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple Gaussian centers with varying widths, heights, and spectral weights
            centers = np.linspace(-0.9, 0.9, 7)
            widths = np.logspace(-1.2, 0.3, 7)
            heights = np.linspace(0.3, 2.5, 7)
            # Spectral weighting based on dimension position and phase modulation
            spectral_weight = 1.0 + 0.3 * np.sin(i * np.pi / self.dim + xi)
            phase_mod = 0.15 * np.cos(xi * 3 + i * 0.5)
            for center, width, height in zip(centers, widths, heights):
                radial_component += height * np.exp(-0.5 * ((xi - center) / width)**2) * spectral_weight * (1 + phase_mod)
        
        # Saddle-point gradient interactions with enhanced cross-dimensional coupling and asymmetry
        saddle_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Enhanced gradient-based saddle with multi-scale curvature, asymmetry and harmonic modulation
            curvature = 1.2 + 0.4 * np.cos(i * np.pi / self.dim)
            asymmetry = 0.6 * np.sin(i * np.pi / self.dim + xi)
            harmonic_mod = 0.3 * np.sin(xi * 8 + i * 0.7)
            saddle_component += (xi**2 - 1)**4 * curvature + \
                               asymmetry * xi**6 + \
                               0.3 * np.sin(xi * 7) * (1 + 0.15 * i) + \
                               0.15 * np.cos(xi * 5) * np.sin(i) * harmonic_mod
        
        # Enhanced cross-dimensional coupling with spectral interactions and frequency modulation
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Spectral coupling with frequency modulation, dimension-dependent scaling and phase interaction
                freq_i = 1.5 + 0.4 * np.cos(i * np.pi / self.dim + x_norm[i])
                freq_j = 1.5 + 0.4 * np.sin(j * np.pi / self.dim + x_norm[j])
                coupling_strength = 1.2 + 0.3 * np.cos(i + j) * np.sin(i - j) * (1 + 0.1 * np.abs(xi - x_norm[j]))
                phase_interaction = np.cos(freq_i * x_norm[i] + freq_j * x_norm[j] + i * 0.3 + j * 0.2)
                cross_coupling += coupling_strength * np.cos(freq_i * x_norm[i] + freq_j * x_norm[j]) * \
                                 np.sin(freq_i * x_norm[i] - freq_j * x_norm[j]) * \
                                 phase_interaction * (1 + 0.15 * np.cos(i + j))
        
        # Multi-scale fractal-like radial modulation with spectral decomposition and harmonic components
        fractal_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Radial fractal with multiple frequency components, dimension-dependent scaling and harmonic modulation
            freqs = [1, 3, 6, 12, 24]
            harmonic_mod = 0.2 * np.sin(xi * 4 + i * 0.5)
            for k, freq in enumerate(freqs):
                scale_factor = 1.0 + 0.2 * np.cos(i * np.pi / self.dim + k) * (1 + 0.1 * xi)
                fractal_component += scale_factor * np.cos(freq * xi) * (1.0 / freq**1.5) * \
                                   (1 + 0.15 * np.sin(i * freq + xi)) * harmonic_mod
        
        # Enhanced dimensionality-adaptive gradient field with spectral components and dynamic scaling
        gradient_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Adaptive scaling based on dimension, spectral components and dynamic modulation
            scale_factor = 1.0 + 0.6 * np.cos(i * np.pi / self.dim) * np.sin(xi) * (1 + 0.2 * np.abs(xi))
            gradient_component += scale_factor * (xi**4 - xi**2) * (1 + 0.1 * np.sin(i)) + \
                                0.15 * np.cos(xi * 4) * np.sin(i) * (1 + 0.1 * np.cos(xi))
        
        # Combine all components with dynamic weights
        weights = [1.5, 1.7, 1.8, 1.3, 1.6, 1.4]
        result = weights[0] * chaotic_component + \
                 weights[1] * radial_component + \
                 weights[2] * saddle_component + \
                 weights[3] * cross_coupling + \
                 weights[4] * fractal_component + \
                 weights[5] * gradient_component
        
        # Add adaptive noise based on function value and input with enhanced complexity
        noise_amplitude = 0.02 * (1 + 0.02 * np.abs(result)) * (1 + 0.03 * np.sum(np.abs(x_norm))) * \
                         (1 + 0.05 * np.cos(np.sum(x_norm))) * (1 + 0.02 * np.sin(np.sum(x_norm**2)))
        noise = np.random.normal(0, noise_amplitude)
        
        return result + noise