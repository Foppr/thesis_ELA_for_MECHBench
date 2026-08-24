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
        result += 2.0 * np.sum(np.sin(2.7 * np.pi * x) * np.cos(1.3 * np.pi * x))
        
        # Modified asymmetric polynomial distortions with higher-order terms
        poly_distortion = 0.95 * np.sum(x**3 + 0.45 * x**5 + 0.16 * x**7 + 0.06 * x**9)
        
        # Modified interdimensional coupling with logarithmic interaction
        coupling = 0.65 * np.sum(np.log(1.0 + 0.55 * (x[:-1] - x[1:])**2) * np.sin(x[:-1] * x[1:]))
        
        # Additional multimodal peaks using modified Gaussian and cosine combinations
        peaks = 0.65 * np.sum(np.exp(-0.22 * (x**2 - 2.1)**2) * np.cos(4.2 * x)**2)
        
        # Enhanced chaotic perturbation with hyperbolic tangent decay
        chaotic = 0.37 * np.sum(np.tanh(np.exp(-0.42 * x**2)) * np.cos(np.log(np.abs(x) + 1e-6)))
        
        # Additional saddle point perturbations with modified trigonometric functions
        saddle = 0.16 * np.sum(np.sin(0.72 * x) * np.cos(0.42 * x) * np.sin(x**3))
        
        # Novel interaction term combining exponential and polynomial components
        novel_interaction = 0.27 * np.sum(np.exp(-0.11 * np.abs(x)) * x**4)
        
        # Combine all terms
        result = result + poly_distortion + coupling + peaks + chaotic + saddle + novel_interaction
        
        return result