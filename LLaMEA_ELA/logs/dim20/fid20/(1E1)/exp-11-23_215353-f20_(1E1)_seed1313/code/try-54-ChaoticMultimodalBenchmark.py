import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with adaptive scaling
        exp_term = np.sum(np.exp(-0.3 * np.abs(x)) * np.cos(0.7 * x))
        
        # Nested trigonometric modulation with multiple frequencies
        trig_term = np.sum(np.sin(3.0 * np.pi * x) * np.cos(5.5 * np.pi * x) * np.sin(2.0 * np.pi * x))
        
        # Adaptive polynomial distortion with variable exponents
        poly_term = np.sum((x**4.0 + 0.9 * x**2.8 - 0.2 * x**1.8 + 0.6 * x + 1.3)**1.2)
        
        # Enhanced chaotic component using nested sine and exponential
        chaotic_term = np.sum(np.sin(np.exp(np.sin(1.3 * x))) + np.cos(np.exp(np.cos(1.4 * x))))
        
        # Additional harmonic modulation for increased multimodality
        harm_term = np.sum(np.sin(5.0 * x) * np.exp(-0.15 * x**2))
        
        # Add a new component: logarithmic barrier to encourage boundary exploration
        barrier_term = np.sum(np.log(1.0 + 0.1 * x**2))
        
        # Combine all terms with optimized weights
        return 0.32 * exp_term + 0.26 * trig_term + 0.24 * poly_term + 0.14 * chaotic_term + 0.02 * harm_term - 0.06 * barrier_term + 1.5