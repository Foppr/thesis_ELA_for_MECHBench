import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        result = np.sum(x**2)
        
        # Periodic sinusoidal components with varying frequencies
        result += 2.0 * np.sum(np.sin(2.0 * np.pi * x) * np.cos(3.0 * np.pi * x))
        
        # Asymmetric polynomial distortions
        poly_distortion = 0.5 * np.sum(x**3 + 0.2 * x**5 + 0.05 * x**7)
        
        # Interdimensional coupling with modified non-linear interaction
        coupling = 0.4 * np.sum(np.sin(x[:-1] * x[1:] * 0.5) * np.cos(x[:-1] + x[1:] * 1.5))
        
        # Additional multimodal peaks using Gaussian and cosine combinations
        peaks = 0.4 * np.sum(np.exp(-0.5 * (x**2 - 2)**2) * np.cos(4.0 * x)**2)
        
        # Enhanced chaotic perturbation with different exponential decay
        chaotic = 0.3 * np.sum(np.sin(np.exp(-x**2 * 0.5)) * np.cos(np.log(np.abs(x) + 1e-6) * 2.0))
        
        # Add a small shift to increase problem difficulty
        shift = 0.1 * np.sum(np.sin(x + 0.5) * np.cos(x - 0.3))
        
        # Combine all terms
        result = result + poly_distortion + coupling + peaks + chaotic + shift
        
        return result