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
        
        # New: Increased complexity with additional trigonometric and exponential interactions
        extra_complexity = 0.4 * np.sum(np.sin(3.0 * x) * np.cos(2.0 * x) * np.exp(-0.5 * x**2))
        
        # New: Multi-scale chaotic modulation with nested sine-cosine patterns
        nested_modulation = 0.3 * np.sum(np.sin(np.pi * x) * np.cos(2.0 * np.pi * x) * np.tanh(x**2))
        
        # New: Fractional polynomial coupling with inverse distance weighting
        fractional_coupling = 0.2 * np.sum((x[:-1]**1.5 - x[1:]**1.5) * np.sin(x[:-1] + x[1:]))
        
        # New: Hyperbolic sine-cosine interaction with exponential decay
        hyperbolic_interaction = 0.25 * np.sum(np.sinh(x) * np.cosh(x) * np.exp(-0.3 * x**2))
        
        # Combine all terms
        result = result + poly_distortion + coupling + peaks + chaotic + saddle + novel_interaction + extra_complexity + nested_modulation + fractional_coupling + hyperbolic_interaction
        
        return result