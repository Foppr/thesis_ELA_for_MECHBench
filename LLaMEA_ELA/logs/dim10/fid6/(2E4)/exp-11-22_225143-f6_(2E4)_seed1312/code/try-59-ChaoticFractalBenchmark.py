import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
        
        # Enhanced chaotic map parameters with higher sensitivity
        self.r_values = np.random.uniform(3.8, 4.0, dim)
        
        # Increased fractal complexity with higher dimensionality effects
        self.fractal_dimensions = np.random.uniform(0.5, 2.0, dim)
        self.noise_amplitudes = np.random.uniform(0.5, 2.5, dim)
        
        # Expanded spectral filtering with more frequency components and non-linear weights
        self.filter_frequencies = np.random.uniform(0.1, 20.0, (dim, 8))
        self.filter_weights = np.random.uniform(-2.0, 2.0, (dim, 8))
        
        # Enhanced basin boundary complexity with multi-scale irregularities
        self.boundary_strength = np.random.uniform(0.5, 3.0, dim)
        self.boundary_exponents = np.random.uniform(1.5, 4.0, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Enhanced chaotic logistic map components with higher sensitivity
        for i in range(self.dim):
            logistic_val = 0.5
            chaotic_sum = 0.0
            
            # Extended transient period
            for _ in range(150):
                logistic_val = self.r_values[i] * logistic_val * (1 - logistic_val)
            
            # Generate longer chaotic trajectory
            for _ in range(30):
                logistic_val = self.r_values[i] * logistic_val * (1 - logistic_val)
                chaotic_sum += np.sin(logistic_val * np.pi * x_norm[i]) * np.exp(-0.5 * logistic_val**2)
            
            f_val += 0.2 * chaotic_sum**2
        
        # Fractal noise with enhanced complexity
        for i in range(self.dim):
            noise_val = 0.0
            for j in range(15):
                scale = np.power(0.4, j)
                freq = np.power(2, j)
                noise_val += scale * np.sin(freq * x_norm[i] + j * 0.1)
            
            f_val += self.noise_amplitudes[i] * np.abs(noise_val)**self.fractal_dimensions[i]
        
        # Enhanced spectral filtering with non-linear combinations
        for i in range(self.dim):
            spectral_sum = 0.0
            for j in range(8):
                # Non-linear interaction between frequency components
                spectral_sum += self.filter_weights[i, j] * np.sin(self.filter_frequencies[i, j] * x_norm[i]) * np.cos(self.filter_frequencies[i, j] * x_norm[i] * 0.5)
            f_val += 0.4 * spectral_sum**2
        
        # Complex basin boundary with multi-scale nonlinearity
        for i in range(self.dim):
            if x_norm[i] < -0.7:
                f_val += self.boundary_strength[i] * np.exp(-x_norm[i]**self.boundary_exponents[i])
            elif x_norm[i] > 0.7:
                f_val += self.boundary_strength[i] * np.exp(-(x_norm[i] - 1.0)**self.boundary_exponents[i])
            else:
                # Higher-order polynomial basin boundary
                f_val += 0.5 * self.boundary_strength[i] * (x_norm[i]**6 + x_norm[i]**4)
        
        # Multi-scale periodic components with chaotic modulation
        for scale in [0.1, 0.3, 0.7, 1.5, 2.5]:
            periodic_sum = 0.0
            for i in range(self.dim):
                # Chaotic modulation of periodic components
                modulator = np.sin(10 * x_norm[i]) + 0.5 * np.cos(5 * x_norm[i])
                periodic_sum += np.sin(scale * 2 * np.pi * x_norm[i] * modulator) * np.cos(scale * 3 * np.pi * x_norm[i] * modulator)
            f_val += 0.3 * periodic_sum**2
        
        # Enhanced cross-dimensional coupling with multi-scale interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Multi-scale chaotic coupling
                coupling = np.sin(x_norm[i] * x_norm[j]) * np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * np.cos(0.3 * x_norm[i] * x_norm[j])
                f_val += 0.4 * coupling**2
        
        # Additional high-frequency perturbations for increased complexity
        perturbation = 0.02 * np.sum(np.sin(20 * x_norm) + np.cos(15 * x_norm) + np.sin(8 * x_norm)**2)
        f_val += perturbation
        
        return f_val