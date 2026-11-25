import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced logistic map chaotic component with feedback
        chaos = 0.0
        r = 3.99
        x_shifted = np.roll(x, 1)
        for i in range(5):
            chaos += np.sum(r * x * (1 - x) + 0.1 * x_shifted * (1 - x_shifted))
            x_shifted = np.roll(x_shifted, 1)
        
        # Modified multiquadratic terms with variable exponents
        quad_terms = np.sum(0.5 * x**2 + 0.3 * x**4 + 0.1 * x**6 + 0.05 * x**8)
        
        # Asymmetric sine-wave perturbations with varying frequencies
        asym_sine = np.sum(np.sin(3.0 * x) * np.cos(5.0 * x) * np.abs(x) + 
                          0.5 * np.sin(7.0 * x) * np.cos(9.0 * x) * np.abs(x))
        
        # Enhanced cross-term interactions with exponential decay and cosine modulation
        cross_terms = np.sum(np.exp(-0.2 * np.abs(x)) * (x**3 + 0.3 * x**5 + 0.1 * x**7) * 
                            np.cos(0.5 * x))
        
        # Improved noise-like component with phase shifts and amplitude modulation
        noise = np.sum(0.8 * np.sin(2.0 * x + 1.0) + 0.6 * np.cos(3.0 * x - 1.0) + 
                      0.4 * np.sin(4.0 * x + 2.0))
        
        # Add a global shaping term to improve conditioning
        global_term = 0.01 * np.sum(x**2 * np.sin(0.1 * x))
        
        return quad_terms + asym_sine + cross_terms + noise + 0.02 * chaos + global_term