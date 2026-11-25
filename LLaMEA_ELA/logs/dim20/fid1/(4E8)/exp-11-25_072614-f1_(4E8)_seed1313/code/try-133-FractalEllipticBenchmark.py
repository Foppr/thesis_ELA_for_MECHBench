import numpy as np

class FractalEllipticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like periodic components with chaotic frequency modulation
        fractal_terms = []
        for i in range(min(10, self.dim)):
            freq = 2 ** (i % 3) * (1 + 0.3 * np.sin(i * 1.7) * np.cos(i * 0.9))
            term = np.sin(freq * x[i]) * np.cos(freq * x[i] ** 2) * np.exp(-0.1 * np.abs(x[i]))
            fractal_terms.append(term)
        
        # Adaptive elliptic distortion with asymmetric scaling
        ellipse_scale = 1.0 + 0.4 * np.mean(np.abs(x)) / 5.0
        ellipse_distortion = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.2 * np.sin(i * 0.5)
            ellipse_distortion += (x[i] ** 2) / (1 + ellipse_scale * (i + 1) * scale_factor)
        
        # Temporal coupling with asymmetric interaction
        temporal_coupling = 0.0
        if self.dim > 1:
            for i in range(1, self.dim):
                asym_factor = 1.0 + 0.3 * np.sin(i * 0.7)
                temporal_coupling += asym_factor * np.sin(x[i-1] - x[i]) * np.cos(x[i-1] + x[i])
        
        # Chaotic modulation with nonlinear interaction
        chaotic_modulation = 0.0
        if self.dim > 2:
            for i in range(2, self.dim):
                chaotic_modulation += np.sin(x[i-2] * x[i-1] * x[i]) * np.cos(x[i-2] + x[i-1] - x[i])
        
        # Combine all components with altered weights
        total = 0.35 * np.sum(fractal_terms) + 0.35 * ellipse_distortion + 0.2 * temporal_coupling + 0.1 * chaotic_modulation
        
        return total