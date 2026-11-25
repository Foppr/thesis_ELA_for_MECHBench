import numpy as np

class ChaoticFractionalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Tent map chaos parameters
        self.tent_r = np.random.uniform(1.5, 3.9, size=dim)
        self.tent_offset = np.random.uniform(-0.5, 0.5, size=dim)
        # Fractional Brownian motion parameters
        self.hurst = np.random.uniform(0.1, 0.9, size=dim)
        self.fb_scale = np.random.uniform(0.5, 2.0, size=dim)
        # Adaptive penalty parameters
        self.penalty_strength = np.random.uniform(1.0, 5.0, size=dim)
        self.penalty_width = np.random.uniform(0.1, 1.0, size=dim)
        # Multi-scale harmonic components
        self.freq_scales = np.random.uniform(0.5, 5.0, size=dim)
        self.amplitude_scales = np.random.uniform(0.5, 3.0, size=dim)
        # Cross-dimensional coupling weights
        self.coupling_weights = np.random.uniform(-1.0, 1.0, size=(dim, dim))
        # Adaptive conditioning parameters
        self.conditioning = np.random.uniform(0.1, 2.0, size=dim)
        # Fractal dimension scaling
        self.fractal_dim = np.random.uniform(1.1, 2.9, size=dim)
        # Dynamic noise parameters
        self.noise_amplitude = np.random.uniform(0.01, 0.5, size=dim)
        self.noise_frequency = np.random.uniform(0.1, 2.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Tent map chaotic component
        tent_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Tent map iteration with offset
            tent_map = self.tent_r[i] * xi * (1 - xi) + self.tent_offset[i]
            tent_component += np.sin(tent_map * self.freq_scales[i]) * self.amplitude_scales[i]
        
        # Fractional Brownian motion component
        fb_component = 0.0
        for i in range(self.dim):
            # Approximate fractional Brownian motion using Hurst parameter
            fb_term = np.sin(x[i] * (1 + self.hurst[i]) * self.fb_scale[i])
            fb_component += fb_term * np.exp(-self.hurst[i] * x[i]**2)
        
        # Adaptive penalty function
        penalty_component = 0.0
        for i in range(self.dim):
            # Multi-modal penalty with adaptive width
            penalty = self.penalty_strength[i] * np.exp(-0.5 * ((x[i] - np.sin(i)) / self.penalty_width[i])**2)
            penalty_component += penalty
        
        # Cross-dimensional coupling
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_term = self.coupling_weights[i, j] * np.sin(x[i]) * np.cos(x[j])
                    coupling_component += coupling_term
        
        # Adaptive conditioning
        conditioning_component = 0.0
        for i in range(self.dim):
            conditioning_component += self.conditioning[i] * x[i]**3
        
        # Fractal dimension scaling
        fractal_component = 0.0
        for i in range(self.dim):
            fractal_term = np.sin(x[i] * self.fractal_dim[i]) * np.cos(x[i]**2)
            fractal_component += fractal_term
        
        # Dynamic noise component
        noise_component = 0.0
        for i in range(self.dim):
            noise_term = self.noise_amplitude[i] * np.sin(self.noise_frequency[i] * x[i])
            noise_component += noise_term
        
        # Combine all components with different weights
        return (1.5 * tent_component + 
                1.2 * fb_component + 
                0.8 * penalty_component + 
                0.6 * coupling_component + 
                0.4 * conditioning_component + 
                0.3 * fractal_component + 
                0.2 * noise_component)