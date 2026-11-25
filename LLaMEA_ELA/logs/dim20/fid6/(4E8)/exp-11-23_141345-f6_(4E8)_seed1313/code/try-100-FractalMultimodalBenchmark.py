import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logarithmic barrier potentials with fractal scaling
        log_barrier = np.sum(np.log(1.0 + 0.1 * x**2) * np.sin(0.5 * x))
        
        # Self-similar structure using recursive trigonometric components
        self_similar = np.sum(np.sin(2.0 * x) * np.cos(3.0 * x) * np.sin(0.7 * x) * np.cos(0.4 * x))
        
        # Chaotic phase interactions with varying frequencies
        chaotic_phase = np.sum(np.sin(x * np.exp(-0.1 * x)) * np.cos(x * np.exp(-0.05 * x)))
        
        # Nested exponential decay with fractal-like behavior
        nested_decay = np.sum(np.exp(-0.2 * np.abs(x)) * np.sin(0.3 * x) * np.cos(0.1 * x))
        
        # Multi-scale radial components with irregular scaling
        r = np.sqrt(np.sum(x**2))
        multi_scale = r * np.exp(-0.1 * r) * np.sin(0.2 * r)
        
        # Cross-dimensional coupling with fractal dimensionality
        cross_coupling = np.sum((x[:-1]**2 + x[1:]**2) * np.sin(0.1 * x[:-1]) * np.cos(0.15 * x[1:]))
        
        # Combined function with adaptive weights for fractal complexity
        return 0.20 * log_barrier + 0.25 * self_similar + 0.20 * chaotic_phase + 0.15 * nested_decay + 0.10 * multi_scale + 0.10 * cross_coupling