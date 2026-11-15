import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        result = np.sum(x**2)
        
        # Enhanced periodic sinusoidal components with varying frequencies
        result += 1.5 * np.sum(np.sin(3.0 * np.pi * x) * np.cos(2.0 * np.pi * x))
        
        # Modified asymmetric polynomial distortions with stronger nonlinearity
        poly_distortion = 0.8 * np.sum(x**3 + 0.35 * x**5 + 0.12 * x**7)
        
        # Modified interdimensional coupling with exponential interaction
        coupling = 0.5 * np.sum(np.exp(-0.5 * (x[:-1] - x[1:])**2) * np.sin(x[:-1] * x[1:]))
        
        # Additional multimodal peaks using modified Gaussian and cosine combinations
        peaks = 0.55 * np.sum(np.exp(-0.3 * (x**2 - 1.5)**2) * np.cos(3.0 * x)**2)
        
        # Enhanced chaotic perturbation with logarithmic decay
        chaotic = 0.3 * np.sum(np.sin(np.exp(-0.5 * x**2)) * np.cos(np.log(np.abs(x) + 1e-5)))
        
        # Additional saddle point perturbations
        saddle = 0.12 * np.sum(np.sin(0.5 * x) * np.cos(0.3 * x) * np.sin(x**2))
        
        # Combine all terms
        result = result + poly_distortion + coupling + peaks + chaotic + saddle
        
        return result