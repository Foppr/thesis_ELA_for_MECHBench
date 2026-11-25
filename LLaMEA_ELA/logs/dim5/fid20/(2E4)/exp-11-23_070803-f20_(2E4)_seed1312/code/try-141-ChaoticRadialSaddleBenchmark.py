import numpy as np

class ChaoticRadialSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Chaotic logistic map component with dynamic parameter
        chaotic_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Logistic map with time-varying r parameter based on dimension - slightly modified
            r = 3.85 + 0.15 * np.sin(i * np.pi / self.dim)
            logistic_value = r * xi * (1 - xi)
            chaotic_component += logistic_value * (1 + 0.2 * np.cos(i))
        
        # Radial basis function component with multi-scale Gaussians - weights altered
        radial_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple Gaussian centers with varying widths and heights
            centers = np.linspace(-0.8, 0.8, 5)
            widths = np.logspace(-1, 0, 5)
            heights = np.linspace(0.3, 1.8, 5)  # Slightly reduced range
            for center, width, height in zip(centers, widths, heights):
                radial_component += height * np.exp(-0.5 * ((xi - center) / width)**2)
        
        # Saddle-point gradient interactions with dimensionally scaled potentials
        saddle_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Gradient-based saddle with varying curvature and asymmetry
            curvature = 1.2 + 0.2 * np.sin(i * np.pi / self.dim)
            asymmetry = 0.3 * np.cos(i * np.pi / self.dim)
            saddle_component += (xi**2 - 1)**2 * curvature + \
                               asymmetry * xi**3 + \
                               0.3 * np.sin(xi * 5) * (1 + 0.15 * i)
        
        # Cross-dimensional coupling with harmonic interactions
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Harmonic coupling with frequency modulation
                freq_i = 1.2 + 0.3 * np.sin(i * np.pi / self.dim)
                freq_j = 0.8 + 0.4 * np.cos(j * np.pi / self.dim)
                cross_coupling += np.sin(freq_i * x_norm[i] + freq_j * x_norm[j]) * \
                                 np.cos(freq_i * x_norm[i] - freq_j * x_norm[j]) * \
                                 (1 + 0.15 * np.sin(i + j))
        
        # Multi-scale fractal-like radial modulation
        fractal_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Radial fractal with multiple frequency components
            freqs = [1, 3, 7, 11, 15]
            for freq in freqs:
                fractal_component += np.sin(freq * xi) * (1.0 / freq**1.3) * \
                                   (1 + 0.15 * np.cos(i * freq))
        
        # Dimensionality-adaptive gradient field
        gradient_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Adaptive scaling based on dimension
            scale_factor = 1.2 + 0.3 * np.sin(i * np.pi / self.dim)
            gradient_component += scale_factor * (xi**3 - xi) * (1 + 0.15 * np.cos(i))
        
        # Combine all components with dynamic weights - slightly altered
        weights = [1.0, 1.2, 1.4, 0.9, 1.1, 1.3]
        result = weights[0] * chaotic_component + \
                 weights[1] * radial_component + \
                 weights[2] * saddle_component + \
                 weights[3] * cross_coupling + \
                 weights[4] * fractal_component + \
                 weights[5] * gradient_component
        
        # Add adaptive noise based on function value and input
        noise_amplitude = 0.007 * (1 + 0.015 * np.abs(result)) * (1 + 0.025 * np.sum(np.abs(x_norm)))
        noise = np.random.normal(0, noise_amplitude)
        
        return result + noise