import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        result = np.sum(x**2)
        
        # Enhanced periodic sinusoidal components with varying frequencies and amplitudes
        result += 2.0 * np.sum(np.sin(2.5 * np.pi * x) * np.cos(1.5 * np.pi * x))
        
        # Modified asymmetric polynomial distortions with higher-order terms
        poly_distortion = 0.9 * np.sum(x**3 + 0.4 * x**5 + 0.15 * x**7 + 0.05 * x**9)
        
        # Modified interdimensional coupling with logarithmic interaction
        coupling = 0.6 * np.sum(np.log(1.0 + 0.5 * (x[:-1] - x[1:])**2) * np.sin(x[:-1] * x[1:]))
        
        # Additional multimodal peaks using modified Gaussian and cosine combinations
        peaks = 0.6 * np.sum(np.exp(-0.2 * (x**2 - 2.0)**2) * np.cos(4.0 * x)**2)
        
        # Enhanced chaotic perturbation with hyperbolic tangent decay
        chaotic = 0.35 * np.sum(np.tanh(np.exp(-0.4 * x**2)) * np.cos(np.log(np.abs(x) + 1e-6)))
        
        # Additional saddle point perturbations with modified trigonometric functions
        saddle = 0.15 * np.sum(np.sin(0.7 * x) * np.cos(0.4 * x) * np.sin(x**3))
        
        # Novel interaction term combining exponential and polynomial components
        novel_interaction = 0.25 * np.sum(np.exp(-0.1 * np.abs(x)) * x**4)
        
        # Additional complex multimodal structure with fractional powers and cross-terms
        complex_structure = 0.4 * np.sum(np.sin(3.0 * x) * np.cos(2.0 * x) * (1.0 + 0.3 * np.abs(x)**1.5) * np.exp(-0.1 * x**2))
        
        # Add a new type of noise-like perturbation using a modified logistic map
        logistic_noise = 0.2 * np.sum(1.0 / (1.0 + np.exp(-5.0 * (x - np.roll(x, 1))**2)) * np.sin(1.2 * x))
        
        # Combine all terms
        result = result + poly_distortion + coupling + peaks + chaotic + saddle + novel_interaction + complex_structure + logistic_noise
        
        return result