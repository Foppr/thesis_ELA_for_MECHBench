import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
        
        # Logistic map parameters for chaotic behavior
        self.r_values = np.random.uniform(3.57, 4.0, dim)
        
        # Fractal noise parameters
        self.fractal_dimensions = np.random.uniform(0.1, 1.9, dim)
        self.noise_amplitudes = np.random.uniform(0.3, 1.8, dim)  # Reduced amplitude range
        
        # Spectral filtering components
        self.filter_frequencies = np.random.uniform(0.1, 12.0, (dim, 5))  # Increased frequency range
        self.filter_weights = np.random.uniform(-1.5, 1.5, (dim, 5))  # Wider weight range
        
        # Basin boundary complexity
        self.boundary_strength = np.random.uniform(0.3, 2.5, dim)  # Extended strength range
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Chaotic logistic map components
        for i in range(self.dim):
            # Initialize chaotic sequence
            logistic_val = 0.5
            chaotic_sum = 0.0
            
            for _ in range(100):  # Discard initial transient
                logistic_val = self.r_values[i] * logistic_val * (1 - logistic_val)
            
            # Generate chaotic trajectory
            for _ in range(20):
                logistic_val = self.r_values[i] * logistic_val * (1 - logistic_val)
                chaotic_sum += np.sin(logistic_val * np.pi * x_norm[i])
            
            f_val += 0.15 * chaotic_sum**2  # Increased weight
        
        # Fractal noise components
        for i in range(self.dim):
            noise_val = 0.0
            for j in range(10):
                # Fractional Brownian motion-like scaling
                scale = np.power(0.5, j)
                freq = np.power(2, j)
                noise_val += scale * np.sin(freq * x_norm[i])
            
            f_val += self.noise_amplitudes[i] * np.abs(noise_val)**self.fractal_dimensions[i]
        
        # Spectral filtering with multiple frequency components
        for i in range(self.dim):
            spectral_sum = 0.0
            for j in range(5):
                spectral_sum += self.filter_weights[i, j] * np.sin(self.filter_frequencies[i, j] * x_norm[i])
            f_val += 0.3 * spectral_sum**2  # Increased weight
        
        # Basin boundary complexity with piecewise nonlinearity
        for i in range(self.dim):
            if x_norm[i] < -0.5:
                f_val += self.boundary_strength[i] * np.exp(-x_norm[i]**2)
            elif x_norm[i] > 0.5:
                f_val += self.boundary_strength[i] * np.exp(-(x_norm[i] - 1.0)**2)
            else:
                f_val += 0.4 * self.boundary_strength[i] * (x_norm[i]**4)  # Increased weight
        
        # Multi-scale periodic components with varying amplitudes
        for scale in [0.1, 0.5, 1.0, 2.0]:
            periodic_sum = 0.0
            for i in range(self.dim):
                periodic_sum += np.sin(scale * 2 * np.pi * x_norm[i]) * np.cos(scale * 3 * np.pi * x_norm[i])
            f_val += 0.2 * periodic_sum**2  # Increased weight
        
        # Cross-dimensional coupling with chaotic interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling between dimensions - modified decay and interaction
                coupling = np.sin(x_norm[i] * x_norm[j]) * np.exp(-0.5 * (x_norm[i] - x_norm[j])**2)  # Changed decay
                f_val += 0.35 * coupling**2  # Increased weight
        
        # Add small random perturbations for increased complexity
        perturbation = 0.015 * np.sum(np.sin(13 * x_norm) + np.cos(7 * x_norm))
        f_val += perturbation
        
        return f_val