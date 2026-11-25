import numpy as np

class ChaoticSpectralSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Chaotic tent map component with parameter modulation and time-delayed feedback
        chaotic_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Tent map with varying parameter based on dimension and delayed feedback
            r = 1.9 + 0.2 * np.sin(i * np.pi / self.dim) + 0.05 * np.cos(i * 0.5)
            if xi < 0.5:
                tent_value = r * xi
            else:
                tent_value = r * (1 - xi)
            # Add time-delayed feedback term
            delay_term = 0.1 * np.sin(xi + 0.3 * np.cos(i))
            chaotic_component += (tent_value + delay_term) * (1 + 0.2 * np.cos(i * 2))
        
        # Spectral decomposition using discrete cosine transform-like interactions with frequency warping
        spectral_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Sum of cosine harmonics with varying frequencies, amplitudes, and phase shifts
            freqs = [1, 2, 3, 4, 5, 6, 7]
            for k, freq in enumerate(freqs):
                amplitude = 0.7 + 0.3 * np.sin(i * freq * np.pi / self.dim)
                phase_shift = 0.2 * np.cos(i * freq * np.pi / self.dim)
                spectral_component += amplitude * np.cos(freq * np.pi * xi + phase_shift) * (1 + 0.1 * np.sin(freq * i))
        
        # Saddle-point interaction component with asymmetric potentials and higher-order terms
        saddle_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Create asymmetric saddle points using polynomial, exponential, and trigonometric terms
            saddle_component += (xi**4 - 2*xi**2) * (1 + 0.3 * np.sin(i)) + \
                               0.7 * np.exp(-xi**2) * (1 + 0.4 * np.cos(i)) + \
                               0.15 * xi**5 * np.cos(xi) + \
                               0.05 * np.sin(3*xi) * (1 + 0.1 * np.tanh(xi))
        
        # Enhanced cross-dimensional coupling with multi-scale interactions
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Nonlinear coupling with varying interaction strength and phase shifts
                strength = 0.4 + 0.3 * np.sin((i + j) * np.pi / self.dim)
                phase_shift = 0.2 * np.cos(i * j * np.pi / self.dim)
                cross_coupling += strength * np.sin(np.pi * (x_norm[i] + x_norm[j]) + phase_shift) * \
                                 np.cos(np.pi * (x_norm[i] - x_norm[j]) + phase_shift) * \
                                 (1 + 0.15 * np.sin(i * j)) * \
                                 np.exp(-0.5 * (i - j)**2)
        
        # Multi-scale fractal-like modulation with varying roughness and self-similarity
        fractal_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple scales of sinusoidal modulation with varying amplitudes
            scales = [1, 2, 3, 6, 12, 24]
            for scale in scales:
                fractal_component += np.sin(scale * xi) * (1.0 / scale**1.5) * \
                                   (1 + 0.15 * np.cos(i * scale)) * \
                                   np.exp(-0.1 * scale)
        
        # Modified gradient field with enhanced asymmetry, dimensionality, and nonlinearity
        gradient_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Enhanced gradient field with stronger asymmetry and higher-order terms
            strength = 1.5 + 0.4 * np.sin(i * np.pi / self.dim)
            asymmetry = 0.7 * np.cos(i * np.pi / self.dim)
            gradient_component += strength * (xi**3 + asymmetry * xi**2 + 0.2 * xi + 0.08 * xi**4 + 0.05 * xi**6) * (1 + 0.15 * np.sin(i))
        
        # Add coupling between components to increase complexity with dynamic weights
        coupling_factor = 0.15 * np.sum(np.abs(x_norm)) / self.dim
        
        # Combine all components with adaptive weights and dynamic scaling
        result = 1.1 * chaotic_component + 1.5 * spectral_component + 1.2 * saddle_component + \
                0.8 * cross_coupling + 1.4 * fractal_component + 1.3 * gradient_component + \
                coupling_factor * (chaotic_component + spectral_component + saddle_component)
        
        # Add controlled noise for robustness with dynamic amplitude and correlation
        noise_amplitude = 0.005 + 0.003 * np.sin(np.sum(x_norm))
        # Correlated noise between dimensions
        noise = np.random.normal(0, noise_amplitude)
        correlated_noise = 0.2 * np.sum(np.random.normal(0, noise_amplitude, self.dim) * x_norm)
        
        return result + noise + correlated_noise