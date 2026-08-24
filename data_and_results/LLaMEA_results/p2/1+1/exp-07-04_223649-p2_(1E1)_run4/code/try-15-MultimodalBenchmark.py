import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        result = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal interactions
        result += 0.8 * np.sum(np.sin(3.0 * x)**3) + 0.6 * np.sum(np.cos(4.0 * x)**3)
        
        # Increased polynomial distortion with chaotic coefficients
        poly_term = 0.02 * np.sum((x**4 + 0.3 * x**6) * np.sin(x**2))
        
        # Stronger cross-dimensional coupling with chaotic interaction
        coupling = 0.3 * np.sum(np.sin(x[:-2] + x[1:-1] + x[2:]) * np.cos(x[:-2] - x[1:-1] + x[2:]) * np.sin(x[:-1]))
        
        # Enhanced chaotic perturbations with exponential and logarithmic components
        chaotic = 0.15 * np.sum(np.sin(np.exp(x**2)) * np.cos(np.log(np.abs(x) + 1e-8)) * np.tan(x))
        
        # Additional multimodal component with Gaussian-like peaks
        gaussian_peaks = 0.2 * np.sum(np.exp(-0.5 * (x**2 - 1)**2) * np.sin(2.0 * x)**2)
        
        # Combine all terms
        result = result + poly_term + coupling + chaotic + gaussian_peaks
        
        return result