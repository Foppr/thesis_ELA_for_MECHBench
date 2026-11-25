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
            # Tent map with time-varying mu parameter based on dimension
            mu = 1.9 + 0.1 * np.sin(i * np.pi / self.dim)
            if xi < 0.5:
                tent_value = mu * xi
            else:
                tent_value = mu * (1 - xi)
            chaotic_component += tent_value * (1 + 0.2 * np.sin(i * np.pi / self.dim))
        
        # Radial basis function component with multi-scale Gaussians and hyperbolic terms
        radial_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple Gaussian centers with varying widths and heights
            centers = np.linspace(-0.9, 0.9, 7)
            widths = np.logspace(-1.5, 0.2, 7)
            heights = np.linspace(0.3, 2.5, 7)
            for center, width, height in zip(centers, widths, heights):
                radial_component += height * np.exp(-0.5 * ((xi - center) / width)**2)
            # Add hyperbolic tangent components for additional complexity
            radial_component += 0.5 * np.tanh(3 * xi) * (1 + 0.1 * np.cos(i))
        
        # Saddle-point gradient interactions with dimensionally scaled potentials and hyperbolic terms
        saddle_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Gradient-based saddle with varying curvature, asymmetry, and hyperbolic modifications
            curvature = 1.2 + 0.4 * np.sin(i * np.pi / self.dim)
            asymmetry = 0.3 * np.cos(i * np.pi / self.dim)
            saddle_component += (xi**2 - 1)**2 * curvature + \
                               asymmetry * xi**3 + \
                               0.15 * np.sinh(xi) * (1 + 0.05 * i) + \
                               0.2 * np.cos(xi * 4)
        
        # Cross-dimensional coupling with enhanced harmonic and trigonometric interactions
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced coupling with hyperbolic and polynomial terms
                freq_i = 1.5 + 0.8 * np.sin(i * np.pi / self.dim)
                freq_j = 1.5 + 0.8 * np.cos(j * np.pi / self.dim)
                cross_coupling += (np.sin(freq_i * x_norm[i] + freq_j * x_norm[j]) * 
                                   np.cos(freq_i * x_norm[i] - freq_j * x_norm[j]) * 
                                   (1 + 0.25 * np.sin(i + j)) + 
                                   0.1 * np.tanh(x_norm[i] * x_norm[j]) * 
                                   (1 + 0.1 * np.cos(i - j)))
        
        # Multi-scale fractal-like radial modulation with hyperbolic and exponential components
        fractal_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Radial fractal with multiple frequency components including hyperbolic terms
            freqs = [1, 2, 5, 9, 13, 17]
            for freq in freqs:
                fractal_component += np.sin(freq * xi) * (1.0 / freq**1.5) * \
                                   (1 + 0.15 * np.cos(i * freq)) + \
                                   0.05 * np.cosh(xi * freq) * (1.0 / freq**0.8)
        
        # Dimensionality-adaptive gradient field with hyperbolic and trigonometric modifications
        gradient_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Adaptive scaling based on dimension with hyperbolic and trigonometric terms
            scale_factor = 1.0 + 0.6 * np.sin(i * np.pi / self.dim)
            gradient_component += scale_factor * (xi**3 - xi) * (1 + 0.15 * np.cos(i)) + \
                                0.1 * np.tanh(xi) * (1 + 0.05 * np.sin(i))
        
        # Combine all components with dynamic weights
        weights = [1.5, 1.2, 1.8, 1.0, 1.4, 1.3]
        result = weights[0] * chaotic_component + \
                 weights[1] * radial_component + \
                 weights[2] * saddle_component + \
                 weights[3] * cross_coupling + \
                 weights[4] * fractal_component + \
                 weights[5] * gradient_component
        
        # Add adaptive noise based on function value and input with enhanced modulation
        noise_amplitude = 0.008 * (1 + 0.02 * np.abs(result)) * (1 + 0.03 * np.sum(np.abs(x_norm))) * \
                         (1 + 0.01 * np.std(x_norm))
        noise = np.random.normal(0, noise_amplitude)
        
        return result + noise