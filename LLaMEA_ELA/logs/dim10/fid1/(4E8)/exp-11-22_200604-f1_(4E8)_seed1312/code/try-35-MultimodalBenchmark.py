import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Spherical harmonics-inspired component with varying frequencies
        harmonic_term = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm))
        
        # Exponential decay terms with random offsets for complexity
        exp_decay = np.sum(np.exp(-np.abs(x_norm)) * np.sin(5 * x_norm))
        
        # Adaptive polynomial weights based on dimensionality
        poly_weights = np.array([i + 1 for i in range(self.dim)])
        poly_term = np.sum(poly_weights * (x_norm**4))
        
        # Cross-dimensional interaction using Gaussian-like decay
        gaussian_interaction = 0.05 * np.sum(np.exp(-0.5 * np.sum((x_norm.reshape(1, -1) - x_norm.reshape(-1, 1))**2, axis=0)))
        
        # Sinusoidal modulation with varying amplitudes
        modulated_sine = np.sum(np.sin(7 * x_norm) * (1 + 0.5 * np.cos(3 * x_norm)))
        
        # Quadratic base with added noise-like perturbations
        quadratic_base = np.sum(x_norm**2)
        
        # Combine all components
        result = quadratic_base + harmonic_term + exp_decay + poly_term + gaussian_interaction + modulated_sine
        
        return result