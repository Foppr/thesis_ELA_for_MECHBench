import numpy as np

class ChaoticSpectralSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Chaotic tent map component with parameter modulation
        chaotic_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Tent map with varying parameter based on dimension
            r = 1.8 + 0.3 * np.sin(i * np.pi / self.dim)
            if xi < 0.5:
                tent_value = r * xi
            else:
                tent_value = r * (1 - xi)
            chaotic_component += tent_value * (1 + 0.15 * np.cos(i))
        
        # Spectral decomposition using discrete cosine transform-like interactions
        spectral_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Sum of cosine harmonics with varying frequencies and amplitudes
            freqs = [1, 2, 3, 4, 5]
            for k, freq in enumerate(freqs):
                amplitude = 0.6 + 0.2 * np.sin(i * freq * np.pi / self.dim)
                spectral_component += amplitude * np.cos(freq * np.pi * xi) * (1 + 0.05 * np.sin(freq * i))
        
        # Saddle-point interaction component with asymmetric potentials
        saddle_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Create asymmetric saddle points using polynomial and exponential terms
            saddle_component += (xi**4 - 2*xi**2) * (1 + 0.25 * np.sin(i)) + \
                               0.6 * np.exp(-xi**2) * (1 + 0.35 * np.cos(i))
        
        # Enhanced cross-dimensional coupling with nonlinear interactions
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Nonlinear coupling with varying interaction strength and phase shifts
                strength = 0.5 + 0.25 * np.sin((i + j) * np.pi / self.dim)
                phase_shift = 0.3 * np.cos(i * j * np.pi / self.dim)
                cross_coupling += strength * np.sin(np.pi * (x_norm[i] + x_norm[j]) + phase_shift) * \
                                 np.cos(np.pi * (x_norm[i] - x_norm[j]) + phase_shift)
        
        # Multi-scale fractal-like modulation with varying roughness
        fractal_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple scales of sinusoidal modulation
            scales = [1, 2, 3, 4, 6]
            for scale in scales:
                fractal_component += np.sin(scale * xi) * (1.0 / scale**1.2) * \
                                   (1 + 0.12 * np.cos(i * scale))
        
        # Modified gradient field with enhanced asymmetry and dimensionality
        gradient_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Enhanced gradient field with stronger asymmetry and nonlinearity
            strength = 1.3 + 0.35 * np.sin(i * np.pi / self.dim)
            asymmetry = 0.6 * np.cos(i * np.pi / self.dim)
            gradient_component += strength * (xi**3 + asymmetry * xi**2 + 0.12 * xi) * (1 + 0.15 * np.sin(i))
        
        # Add a new hyperbolic tangent component to increase complexity
        tanh_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            tanh_component += 0.8 * np.tanh(2 * xi) * (1 + 0.2 * np.cos(i))
        
        # Combine all components with adaptive weights
        result = 0.9 * chaotic_component + 1.3 * spectral_component + 1.0 * saddle_component + \
                0.7 * cross_coupling + 1.2 * fractal_component + 1.1 * gradient_component + \
                0.5 * tanh_component
        
        # Add controlled noise for robustness with modified variance
        noise = np.random.normal(0, 0.003)
        
        return result + noise