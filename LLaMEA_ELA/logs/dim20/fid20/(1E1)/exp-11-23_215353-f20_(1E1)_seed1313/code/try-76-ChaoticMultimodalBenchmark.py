import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with adaptive scaling
        exp_term = np.sum(np.exp(-0.4 * np.abs(x)) * np.cos(0.6 * x))
        
        # Nested trigonometric modulation with multiple frequencies
        trig_term = np.sum(np.sin(2.5 * np.pi * x) * np.cos(6 * np.pi * x) * np.sin(1.5 * np.pi * x))
        
        # Adaptive polynomial distortion with higher variable exponents
        poly_term = np.sum((x**4.2 + 0.9 * x**3.1 - 0.4 * x**2.3 + 0.8 * x + 1.1)**1.3)
        
        # Enhanced chaotic component using nested sine, exponential and logarithmic functions
        chaotic_term = np.sum(np.sin(np.exp(np.cos(1.3 * x))) + np.cos(np.exp(np.sin(1.4 * x))) + 
                              np.log(1.1 + 0.5 * np.sin(2.7 * x)**2))
        
        # Additional harmonic modulation for increased multimodality
        harm_term = np.sum(np.sin(4.7 * x) * np.exp(-0.13 * x**2))
        
        # New cosine modulation term to increase landscape complexity
        cos_mod_term = np.sum(np.cos(3.2 * x) * np.sin(0.8 * x**2))
        
        # Multi-scale Gaussian modulation for enhanced multimodality
        gauss_mod_term = np.sum(np.exp(-0.5 * (x - 1.5)**2) * np.sin(3.0 * x) + 
                               np.exp(-0.5 * (x + 2.0)**2) * np.cos(2.0 * x))
        
        # Combine all terms with optimized weights
        return 0.30 * exp_term + 0.28 * trig_term + 0.18 * poly_term + 0.15 * chaotic_term + 0.06 * harm_term + 0.03 * cos_mod_term + 0.00 * gauss_mod_term + 1.5