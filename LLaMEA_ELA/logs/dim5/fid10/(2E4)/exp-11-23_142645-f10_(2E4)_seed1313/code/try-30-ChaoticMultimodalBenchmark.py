import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced logistic map chaotic component with feedback and phase shifts
        chaos = 0.0
        r = 3.99
        x_shifted = np.roll(x, 1)
        for i in range(7):
            chaos += np.sum(r * x * (1 - x) + 0.1 * x_shifted * (1 - x_shifted) * np.sin(0.5 * i))
            x_shifted = np.roll(x_shifted, 1)
        
        # Modified multiquadratic terms with variable exponents and conditioning factors
        quad_terms = np.sum(0.5 * x**2 + 0.3 * x**4 + 0.1 * x**6 + 0.05 * x**8 + 0.01 * x**10)
        
        # Asymmetric sine-wave perturbations with varying frequencies and amplitude modulation
        asym_sine = np.sum(np.sin(3.0 * x) * np.cos(5.0 * x) * (np.abs(x) + 0.5 * np.sin(2.0 * x)) + 
                          0.5 * np.sin(7.0 * x) * np.cos(9.0 * x) * (np.abs(x) + 0.3 * np.cos(1.5 * x)))
        
        # Enhanced cross-term interactions with exponential decay, cosine modulation, and interaction weights
        cross_terms = np.sum(np.exp(-0.2 * np.abs(x)) * (x**3 + 0.3 * x**5 + 0.1 * x**7) * 
                            np.cos(0.5 * x) * (1 + 0.1 * np.sin(0.3 * x)))
        
        # Improved noise-like component with phase shifts, amplitude modulation, and harmonic mixing
        noise = np.sum(0.8 * np.sin(2.0 * x + 1.0) + 0.6 * np.cos(3.0 * x - 1.0) + 
                      0.4 * np.sin(4.0 * x + 2.0) + 0.2 * np.cos(5.0 * x + 0.5))
        
        # Global shaping term with improved conditioning and gradient control
        global_term = 0.01 * np.sum(x**2 * np.sin(0.1 * x) * (1 + 0.05 * np.cos(0.2 * x)))
        
        return quad_terms + asym_sine + cross_terms + noise + 0.03 * chaos + global_term