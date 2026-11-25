import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
        
        # Logistic map parameters for chaotic behavior
        self.r_values = np.random.uniform(3.57, 4.0, dim)
        
        # Fractal noise parameters
        self.fractal_dimensions = np.random.uniform(0.1, 1.9, dim)
        self.noise_amplitudes = np.random.uniform(0.5, 2.0, dim)
        
        # Spectral filtering components
        self.filter_frequencies = np.random.uniform(0.1, 10.0, (dim, 5))
        self.filter_weights = np.random.uniform(-1.0, 1.0, (dim, 5))
        
        # Basin boundary complexity
        self.boundary_strength = np.random.uniform(0.5, 2.0, dim)
        
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
            
            f_val += 0.15 * chaotic_sum**2
        
        # Fractal noise components with altered scaling
        for i in range(self.dim):
            noise_val = 0.0
            for j in range(10):
                # Fractional Brownian motion-like scaling with modified exponents
                scale = np.power(0.3, j)  # Reduced scaling factor
                freq = np.power(2.5, j)   # Increased frequency base
                noise_val += scale * np.sin(freq * x_norm[i])
            
            f_val += self.noise_amplitudes[i] * np.abs(noise_val)**self.fractal_dimensions[i]
        
        # Spectral filtering with modified weights and frequencies
        for i in range(self.dim):
            spectral_sum = 0.0
            for j in range(5):
                # Increased frequency and altered weight scaling
                spectral_sum += self.filter_weights[i, j] * 1.5 * np.sin(self.filter_frequencies[i, j] * 1.2 * x_norm[i])
            f_val += 0.3 * spectral_sum**2
        
        # Basin boundary complexity with enhanced piecewise nonlinearity
        for i in range(self.dim):
            if x_norm[i] < -0.5:
                f_val += self.boundary_strength[i] * np.exp(-1.5 * x_norm[i]**2)  # Increased exponential decay
            elif x_norm[i] > 0.5:
                f_val += self.boundary_strength[i] * np.exp(-1.2 * (x_norm[i] - 1.0)**2)  # Modified shift
            else:
                f_val += 0.4 * self.boundary_strength[i] * (x_norm[i]**4)  # Increased nonlinearity
        
        # Multi-scale periodic components with varying amplitudes
        for scale in [0.1, 0.5, 1.0, 2.0]:
            periodic_sum = 0.0
            for i in range(self.dim):
                periodic_sum += np.sin(scale * 2.5 * np.pi * x_norm[i]) * np.cos(scale * 3.5 * np.pi * x_norm[i])  # Modified frequencies
            f_val += 0.2 * periodic_sum**2
        
        # Cross-dimensional coupling with enhanced chaotic interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced coupling strength and modified interaction
                coupling = np.sin(1.5 * x_norm[i] * x_norm[j]) * np.exp(-0.3 * (x_norm[i] - x_norm[j])**2)
                f_val += 0.35 * coupling**2  # Increased coupling weight
        
        # Add small random perturbations for increased complexity
        perturbation = 0.015 * np.sum(np.sin(15 * x_norm) + np.cos(9 * x_norm))
        f_val += perturbation
        
        return f_val