import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic exponential with multi-scale modulation
        exp_term = np.sum(np.exp(-0.3 * np.abs(x)) * np.cos(0.7 * x) * np.sin(1.1 * x))
        
        # Nested trigonometric with higher frequency components and phase shifts
        trig_term = np.sum(np.sin(3.2 * np.pi * x) * np.cos(7.5 * np.pi * x) * 
                          np.sin(2.3 * np.pi * x) * np.cos(4.1 * np.pi * x))
        
        # Adaptive polynomial with non-integer exponents and cross-terms
        poly_term = np.sum((x**4.2 + 0.9 * x**3.7 - 0.4 * x**2.8 + 0.6 * x**1.9 + 1.3)**1.5 + 
                          0.2 * x * np.sin(2.5 * x))
        
        # Chaotic nested sine and cosine with varying amplitudes
        chaotic_term = np.sum(np.sin(np.exp(np.sin(1.5 * x) + 0.3 * np.cos(2.1 * x))) + 
                             np.cos(np.exp(np.cos(1.4 * x) - 0.2 * np.sin(1.9 * x))))
        
        # Multi-harmonic modulation with exponential decay
        harm_term = np.sum(np.sin(5.2 * x) * np.cos(3.8 * x) * np.exp(-0.15 * x**2))
        
        # Additional high-frequency oscillation component
        osc_term = np.sum(np.sin(10.0 * x) * np.cos(9.0 * x) * np.sin(8.0 * x))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.32 * exp_term + 0.25 * trig_term + 0.20 * poly_term + 0.15 * chaotic_term + 0.04 * harm_term + 0.04 * osc_term + 1.8