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
        result += 2.0 * np.sum(np.sin(3.0 * np.pi * x) * np.cos(2.0 * np.pi * x))
        
        # Modified asymmetric polynomial distortions with higher-order terms
        poly_distortion = 0.8 * np.sum(x**3 + 0.3 * x**5 + 0.1 * x**7 + 0.03 * x**9)
        
        # Modified interdimensional coupling with logarithmic interaction
        coupling = 0.5 * np.sum(np.log(1.0 + 0.4 * (x[:-1] - x[1:])**2) * np.sin(x[:-1] * x[1:]))
        
        # Additional multimodal peaks using modified Gaussian and cosine combinations
        peaks = 0.5 * np.sum(np.exp(-0.15 * (x**2 - 2.0)**2) * np.cos(3.5 * x)**2)
        
        # Enhanced chaotic perturbation with hyperbolic tangent decay
        chaotic = 0.3 * np.sum(np.tanh(np.exp(-0.3 * x**2)) * np.cos(np.log(np.abs(x) + 1e-6)))
        
        # Additional saddle point perturbations with modified trigonometric functions
        saddle = 0.12 * np.sum(np.sin(0.6 * x) * np.cos(0.3 * x) * np.sin(x**3))
        
        # Novel interaction term combining exponential and polynomial components
        novel_interaction = 0.2 * np.sum(np.exp(-0.08 * np.abs(x)) * x**4)
        
        # Additional high-frequency oscillation component for increased complexity
        high_freq = 0.15 * np.sum(np.sin(10.0 * x) * np.cos(7.0 * x))
        
        # Combine all terms
        result = result + poly_distortion + coupling + peaks + chaotic + saddle + novel_interaction + high_freq
        
        return result