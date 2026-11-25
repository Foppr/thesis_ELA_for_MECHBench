import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay term with variable rate
        exp_term = np.sum(np.exp(-0.3 * x**2))
        
        # Trigonometric modulation with chaotic frequency modulation
        freq_mod = np.sin(0.5 * np.pi * x) + 1.5
        trig_term = np.sum(np.sin(freq_mod * x) * np.cos(freq_mod * x * 1.7))
        
        # Polynomial distortion with radial component and noise
        radial = np.sqrt(np.sum(x**2, axis=0, keepdims=True))
        poly_term = np.sum((x**4 + 0.3 * x**3 - 0.4 * x**2 + 0.1 * x + 1.0)**2 + 0.05 * radial**2)
        
        # Chaotic component with multiple sine waves
        chaotic_term = np.sum(np.sin(np.exp(x)) + 0.5 * np.sin(3 * np.exp(x)) + 0.3 * np.sin(7 * np.exp(x)))
        
        # Add noise to increase multimodality
        noise = np.random.normal(0, 0.1, x.shape)
        
        # Combine all terms with different weights
        return 0.4 * exp_term + 0.25 * trig_term + 0.2 * poly_term + 0.15 * chaotic_term + 1.5 + np.sum(noise)