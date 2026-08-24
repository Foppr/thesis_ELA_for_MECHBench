import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        result = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal interactions with variable frequencies
        result += 1.2 * np.sum(np.sin(5.0 * x)**3) + 0.9 * np.sum(np.cos(6.0 * x)**3)
        
        # Increased polynomial distortion with chaotic coefficients and higher-order terms
        poly_term = 0.03 * np.sum((x**4 + 0.4 * x**6 + 0.1 * x**8) * np.sin(x**2))
        
        # Stronger cross-dimensional coupling with chaotic interaction and additional coupling terms
        coupling = 0.4 * np.sum(np.sin(x[:-2] + x[1:-1] + x[2:]) * np.cos(x[:-2] - x[1:-1] + x[2:]) * np.sin(x[:-1]))
        coupling += 0.2 * np.sum(np.tan(x[:-1] * x[1:]) * np.exp(-x**2))
        
        # Enhanced chaotic perturbations with exponential and logarithmic components
        chaotic = 0.2 * np.sum(np.sin(np.exp(x**2)) * np.cos(np.log(np.abs(x) + 1e-8)) * np.tan(x))
        
        # Additional multimodal component with Gaussian-like peaks and saddle points
        gaussian_peaks = 0.25 * np.sum(np.exp(-0.5 * (x**2 - 1)**2) * np.sin(2.0 * x)**2)
        saddle_points = 0.1 * np.sum(np.sin(x) * np.cos(x**2) * np.tan(x**3))
        
        # Add a new term for increased complexity with cross-dimensional interactions
        cross_term = 0.15 * np.sum(np.sin(x[:-1]) * np.cos(x[1:]) * np.exp(-np.abs(x[:-1] - x[1:])))
        
        # Combine all terms
        result = result + poly_term + coupling + chaotic + gaussian_peaks + saddle_points + cross_term
        
        return result