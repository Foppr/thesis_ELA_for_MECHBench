import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine-wave interactions with multi-scale frequencies
        chaotic_wave = np.sum(np.sin(3.2 * np.sin(1.7 * x)) * np.cos(2.9 * np.cos(1.4 * x)))
        
        # Adaptive radial basis function distortion with variable spread
        radial_term = np.sum((np.exp(-0.5 * np.sum((x[:, None] - np.linspace(-5, 5, self.dim)[None, :])**2, axis=1)) + 
                              0.3 * np.exp(-0.3 * np.sum((x[:, None] - np.linspace(-3, 3, self.dim)[None, :])**2, axis=1))) ** 1.8)
        
        # Cross-dimensional coupling with polynomial interactions
        cross_term = np.sum(np.prod(x**2.7 + 0.5 * x + 1.1, axis=0))
        
        # Nested trigonometric modulation with dynamic phase shifts
        trig_mod = np.sum(np.sin(4.1 * x) * np.cos(3.8 * x) * np.sin(2.3 * x) * np.cos(1.9 * x))
        
        # Exponential chaos with logistic map-inspired distortion
        exp_chaos = np.sum(np.exp(-np.abs(x)) * np.sin(np.pi * np.exp(np.sin(x))))
        
        # Additional harmonic and Gaussian noise modulation for increased multimodality
        noise_mod = np.sum(np.sin(5.3 * x) * np.exp(-0.15 * x**2) + 0.1 * np.random.randn(self.dim))
        
        # Combine all terms with optimized weights and add global offset
        return 0.25 * chaotic_wave + 0.20 * radial_term + 0.18 * cross_term + 0.15 * trig_mod + 0.12 * exp_chaos + 0.08 * noise_mod + 1.8