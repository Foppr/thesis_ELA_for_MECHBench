import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Chaotic sinusoidal interactions with varying frequencies
        result += 0.8 * np.sum(np.sin(3.0 * x)**3) + 0.5 * np.sum(np.cos(4.0 * x)**3)
        
        # Polynomial distortion with chaotic coefficients
        poly_term = 0.02 * np.sum((x**4 + 0.3 * x**6) * np.sin(x**2))
        
        # Enhanced cross-dimensional coupling with chaotic interaction
        coupling = 0.3 * np.sum(np.sin(x[:-2] * x[1:-1] + x[2:]) * np.cos(x[:-2] * x[1:-1] - x[2:]))
        
        # Improved chaotic perturbations with exponential and logarithmic components
        chaotic = 0.15 * np.sum(np.sin(np.exp(x**2)) * np.cos(np.log(np.abs(x) + 1e-6)))
        
        # Additional multimodal component with Gaussian-like peaks
        gaussian_peaks = 0.2 * np.sum(np.exp(-0.5 * (x - 1.0)**2) + np.exp(-0.5 * (x + 1.0)**2))
        
        # Combine all terms
        result = result + poly_term + coupling + chaotic + gaussian_peaks
        
        return result