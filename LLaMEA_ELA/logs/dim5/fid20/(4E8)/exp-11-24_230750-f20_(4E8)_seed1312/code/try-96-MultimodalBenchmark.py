import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal-like self-similarity with hyperbolic tangent scaling
        fractal = 0.0
        for i in range(1, min(5, self.dim + 1)):
            scale = 2 ** (-i)
            fractal += scale * np.sum(np.tanh(scale * x) * np.cos(scale * x**2))
        
        # Modified quantum harmonic oscillator with complex coupling and phase shifts
        quantum_potential = 0.5 * np.sum(x**2 + 0.4 * np.sin(3 * np.pi * x) * np.cos(3 * np.pi * x) + 
                                        0.1 * np.tanh(x) * np.sin(x))
        
        # Adaptive gradient field with direction-dependent scaling and exponential coupling
        grad_field = 0.0
        for i in range(self.dim - 1):
            grad_field += np.exp(-0.5 * (x[i] - x[i+1])**2) * (1.0 + 0.2 * np.sin(x[i] * x[i+1]))
        
        # Multi-scale Gaussian ridges with varying amplitudes, widths, and phase shifts
        ridge_sum = 0.0
        for i in range(min(5, self.dim)):
            amplitude = 1.0 + 0.6 * np.sin(i * 0.4)
            width = 0.4 + 0.2 * np.cos(i * 0.2)
            phase = 0.1 * i
            ridge_sum += amplitude * np.exp(-0.5 * ((x[i] - 2 * np.sin(i + phase)) / width)**2)
        
        # Augmented polynomial chaos expansion with mixed monomial terms and trigonometric coupling
        chaos_poly = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited cross-terms for better conditioning
                chaos_poly += x[i]**3 * x[j]**2 * np.sin(0.15 * (x[i] + x[j])) * np.cos(0.05 * x[i] * x[j])
        
        # Dynamic conditioning with enhanced dimension-adaptive scaling and non-linear feedback
        condition = 1.0 + 0.4 * np.sin(self.dim * 0.25) * np.mean(np.abs(x)) + \
                   0.3 * np.cos(self.dim * 0.15) * np.std(x) + \
                   0.1 * np.tanh(np.sum(x**2) / self.dim)
        
        # Combined function with improved conditioning and enhanced multimodality
        base_value = condition * (np.sum(x**4) + 0.6 * np.sum(x**3) + 0.15 * np.sum(x**2))
        
        # Add controlled noise component with adaptive variance and multi-frequency components
        noise = 0.08 * np.random.rand() * np.sum(np.sin(7 * x) * np.cos(4 * x)) * (1.0 + 0.15 * np.sin(self.dim))
        
        # Enhanced multimodality through coupled sine waves, periodic shifts, and hyperbolic coupling
        coupled_terms = 0.0
        for i in range(self.dim):
            coupled_terms += np.sin(x[i] * np.pi / 2) * np.cos(x[i] * np.pi / 4) * \
                            np.sin(0.6 * x[i] + i * 0.12) * np.cos(0.35 * x[i] - i * 0.07) * \
                            np.tanh(0.5 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Add a novel hyperbolic tangent coupling term to increase basin complexity
        ht_coupling = 0.0
        for i in range(self.dim):
            ht_coupling += np.tanh(x[i] * (1.0 + 0.2 * np.sin(i))) * np.cos(0.3 * x[i])
        
        return base_value + fractal + quantum_potential + grad_field + ridge_sum + chaos_poly + noise + coupled_terms + ht_coupling