import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine-wave interactions with multiple frequencies
        chaotic_term = np.sum(np.sin(3.2 * np.sin(1.7 * x)) + np.cos(2.9 * np.cos(1.8 * x)))
        
        # Polynomial chaos with higher-order terms and variable exponents
        poly_term = np.sum((x**5.1 + 0.7 * x**4.3 - 0.6 * x**3.2 + 0.9 * x**2.1 - 0.3 * x + 1.4)**1.5)
        
        # Exponential modulation with adaptive scaling and chaotic distortion
        exp_term = np.sum(np.exp(-0.5 * np.abs(x)) * np.cos(0.8 * x) * np.sin(1.2 * x))
        
        # Nested trigonometric modulation with increased frequency and amplitude
        trig_term = np.sum(np.sin(3.1 * np.pi * x) * np.cos(7.3 * np.pi * x) * np.sin(2.4 * np.pi * x) * np.cos(1.9 * np.pi * x))
        
        # Additional harmonic modulation with exponential decay
        harm_term = np.sum(np.sin(5.8 * x) * np.exp(-0.17 * x**2) * np.cos(3.6 * x))
        
        # Combined weighted function with altered coefficients for increased complexity
        return 0.25 * exp_term + 0.22 * trig_term + 0.25 * poly_term + 0.20 * chaotic_term + 0.08 * harm_term + 1.8