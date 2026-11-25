import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
        
        # Logistic map parameters for chaotic behavior
        self.r_values = np.random.uniform(3.57, 4.0, dim)
        
        # Fractal noise parameters
        self.fractal_dimensions = np.random.uniform(0.1, 1.9, dim)
        self.noise_amplitudes = np.random.uniform(0.3, 2.5, dim)  # Increased amplitude range
        
        # Spectral filtering components - enhanced with more frequencies and weights
        self.filter_frequencies = np.random.uniform(0.1, 20.0, (dim, 8))  # Increased frequency range
        self.filter_weights = np.random.uniform(-2.0, 2.0, (dim, 8))  # Wider weight range
        
        # Basin boundary complexity with enhanced nonlinearity
        self.boundary_strength = np.random.uniform(0.5, 3.5, dim)  # Extended strength range
        self.boundary_exponents = np.random.uniform(2.0, 6.0, dim)  # Added exponent variation
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Chaotic logistic map components with enhanced coupling
        for i in range(self.dim):
            # Initialize chaotic sequence
            logistic_val = 0.5
            chaotic_sum = 0.0
            
            for _ in range(100):  # Discard initial transient
                logistic_val = self.r_values[i] * logistic_val * (1 - logistic_val)
            
            # Generate chaotic trajectory with multi-scale interactions
            for _ in range(30):
                logistic_val = self.r_values[i] * logistic_val * (1 - logistic_val)
                chaotic_sum += np.sin(logistic_val * np.pi * x_norm[i])
            
            f_val += 0.2 * chaotic_sum**2  # Increased weight
        
        # Fractal noise components with enhanced scaling
        for i in range(self.dim):
            noise_val = 0.0
            for j in range(15):  # More iterations for richer fractal structure
                scale = np.power(0.5, j)
                freq = np.power(2, j)
                noise_val += scale * np.sin(freq * x_norm[i])
            
            f_val += self.noise_amplitudes[i] * np.abs(noise_val)**self.fractal_dimensions[i]
        
        # Spectral filtering with enhanced multiple frequency components
        for i in range(self.dim):
            spectral_sum = 0.0
            for j in range(8):  # More frequency components
                spectral_sum += self.filter_weights[i, j] * np.sin(self.filter_frequencies[i, j] * x_norm[i])
            f_val += 0.4 * spectral_sum**2  # Increased weight
        
        # Basin boundary complexity with piecewise nonlinearity and exponent variation
        for i in range(self.dim):
            if x_norm[i] < -0.5:
                f_val += self.boundary_strength[i] * np.exp(-x_norm[i]**self.boundary_exponents[i])
            elif x_norm[i] > 0.5:
                f_val += self.boundary_strength[i] * np.exp(-(x_norm[i] - 1.0)**self.boundary_exponents[i])
            else:
                f_val += 0.5 * self.boundary_strength[i] * (x_norm[i]**self.boundary_exponents[i])  # Increased weight
        
        # Multi-scale periodic components with varying amplitudes and more scales
        for scale in [0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 4.0]:
            periodic_sum = 0.0
            for i in range(self.dim):
                periodic_sum += np.sin(scale * 2 * np.pi * x_norm[i]) * np.cos(scale * 3 * np.pi * x_norm[i])
            f_val += 0.25 * periodic_sum**2  # Increased weight
        
        # Cross-dimensional coupling with enhanced chaotic interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling between dimensions - modified decay and interaction
                coupling = np.sin(x_norm[i] * x_norm[j]) * np.exp(-0.3 * (x_norm[i] - x_norm[j])**2)  # Changed decay
                f_val += 0.45 * coupling**2  # Increased weight
        
        # Add larger random perturbations for increased complexity
        perturbation = 0.025 * np.sum(np.sin(17 * x_norm) + np.cos(11 * x_norm))
        f_val += perturbation
        
        return f_val