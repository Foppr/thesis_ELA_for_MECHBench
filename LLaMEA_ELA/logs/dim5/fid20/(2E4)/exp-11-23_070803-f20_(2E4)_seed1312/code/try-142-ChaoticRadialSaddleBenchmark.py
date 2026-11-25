import numpy as np

class ChaoticRadialSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Chaotic tent map component with dynamic parameter - more chaotic behavior
        chaotic_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Tent map with time-varying parameter based on dimension
            r = 1.8 + 0.4 * np.sin(i * np.pi / self.dim)
            if xi < 0.5:
                tent_value = r * xi
            else:
                tent_value = r * (1 - xi)
            chaotic_component += tent_value * (1 + 0.3 * np.cos(i * 0.5))
        
        # Radial basis function component with multi-scale Gaussians - altered weights and centers
        radial_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple Gaussian centers with varying widths and heights
            centers = np.linspace(-0.9, 0.9, 7)
            widths = np.logspace(-1.2, 0.1, 7)
            heights = np.linspace(0.4, 2.0, 7)  # Slightly increased range
            for center, width, height in zip(centers, widths, heights):
                radial_component += height * np.exp(-0.5 * ((xi - center) / width)**2)
        
        # Saddle-point gradient interactions with dimensionally scaled potentials
        saddle_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Gradient-based saddle with varying curvature and asymmetry
            curvature = 1.5 + 0.3 * np.sin(i * np.pi / self.dim)
            asymmetry = 0.4 * np.cos(i * np.pi / self.dim)
            saddle_component += (xi**2 - 1)**2 * curvature + \
                               asymmetry * xi**3 + \
                               0.4 * np.sin(xi * 6) * (1 + 0.2 * i)
        
        # Cross-dimensional coupling with harmonic interactions
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Harmonic coupling with frequency modulation
                freq_i = 1.5 + 0.2 * np.sin(i * np.pi / self.dim)
                freq_j = 1.0 + 0.3 * np.cos(j * np.pi / self.dim)
                cross_coupling += np.sin(freq_i * x_norm[i] + freq_j * x_norm[j]) * \
                                 np.cos(freq_i * x_norm[i] - freq_j * x_norm[j]) * \
                                 (1 + 0.2 * np.sin(i + j))
        
        # Multi-scale fractal-like radial modulation
        fractal_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Radial fractal with multiple frequency components
            freqs = [1, 2, 5, 9, 13, 17]
            for freq in freqs:
                fractal_component += np.sin(freq * xi) * (1.0 / freq**1.4) * \
                                   (1 + 0.2 * np.cos(i * freq))
        
        # Dimensionality-adaptive gradient field
        gradient_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Adaptive scaling based on dimension
            scale_factor = 1.3 + 0.2 * np.sin(i * np.pi / self.dim)
            gradient_component += scale_factor * (xi**3 - xi) * (1 + 0.2 * np.cos(i))
        
        # Combine all components with dynamic weights - slightly altered
        weights = [1.2, 1.0, 1.5, 1.0, 1.2, 1.1]
        result = weights[0] * chaotic_component + \
                 weights[1] * radial_component + \
                 weights[2] * saddle_component + \
                 weights[3] * cross_coupling + \
                 weights[4] * fractal_component + \
                 weights[5] * gradient_component
        
        # Add adaptive noise based on function value and input
        noise_amplitude = 0.008 * (1 + 0.02 * np.abs(result)) * (1 + 0.03 * np.sum(np.abs(x_norm)))
        noise = np.random.normal(0, noise_amplitude)
        
        return result + noise