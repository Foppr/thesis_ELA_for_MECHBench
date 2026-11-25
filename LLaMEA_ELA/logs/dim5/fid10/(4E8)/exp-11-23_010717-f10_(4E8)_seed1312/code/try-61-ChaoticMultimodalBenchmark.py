import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like basin term with chaotic scaling and higher-order polynomial
        basin = 0.1 * np.sum(x**2) + 0.05 * np.sum(np.sin(3.0 * x)**2) + \
                0.02 * np.sum(np.cos(2.5 * x)**4) + 0.01 * np.sum(x**4)
        
        # Multi-frequency sine-cosine wave interactions with chaotic modulation
        wave_terms = 0.0
        frequencies = [1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0]
        for i in range(self.dim):
            term = 0.0
            for freq in frequencies:
                term += np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
            wave_terms += term
        
        # Enhanced cross-dimensional coupling with chaotic interaction coefficients
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff1 = 0.3 * np.sin(1.2 * x[i] + 0.5 * x[j])
                coeff2 = 0.2 * np.cos(2.0 * x[i] + 0.8 * x[j])
                cross_terms += coeff1 * np.sin(1.8 * x[j]) + coeff2 * np.cos(1.5 * x[i])
        
        # Chaotic noise term with higher frequency components and non-linear scaling
        noise = 0.05 * np.sum(np.sin(7.0 * x) * np.cos(4.0 * x) * np.tan(1.3 * x))
        
        # Add a chaotic perturbation component
        perturbation = 0.03 * np.sum(np.sin(6.0 * x + np.cos(3.0 * x))**2)
        
        return basin + wave_terms + cross_terms + noise + perturbation