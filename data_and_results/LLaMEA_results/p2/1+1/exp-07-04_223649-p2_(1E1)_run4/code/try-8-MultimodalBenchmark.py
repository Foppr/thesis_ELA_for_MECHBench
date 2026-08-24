import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Core quadratic + sinusoidal components
        result = np.sum(x**2) + 0.5 * np.sum(np.sin(5.0 * x)**2) + 0.3 * np.sum(np.cos(2.0 * x)**2)
        
        # Enhanced polynomial distortion with variable coefficients
        poly_term = 0.02 * np.sum((x**3 + 0.3 * x**5 + 0.1 * x**7) * np.sin(x))
        
        # Cross-dimensional coupling with more complex interaction terms
        coupling = 0.15 * np.sum(np.sin(x[:-2] + x[1:-1] + x[2:]) * np.cos(x[:-2] - x[1:-1] + x[2:]) * np.sin(x[1:-1]))
        
        # Chaotic perturbations with exponential and logarithmic interactions
        chaotic = 0.12 * np.sum(np.sin(np.exp(x)) * np.cos(np.log(np.abs(x) + 1e-8)) * np.tan(x / 2.0))
        
        # Additional multimodal component with Gaussian-like peaks
        gaussian_peaks = 0.08 * np.sum(np.exp(-0.5 * (x - np.sin(x))**2))
        
        # Add noise-like perturbations to increase ruggedness
        noise = 0.05 * np.sum(np.sin(10.0 * x) * np.cos(7.0 * x))
        
        # Combine all terms
        result = result + poly_term + coupling + chaotic + gaussian_peaks + noise
        
        return result