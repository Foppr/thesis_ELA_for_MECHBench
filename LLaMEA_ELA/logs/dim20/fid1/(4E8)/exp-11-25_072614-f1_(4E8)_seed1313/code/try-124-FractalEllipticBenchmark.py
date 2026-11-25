import numpy as np

class FractalEllipticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like periodic components with varying frequencies
        fractal_terms = []
        for i in range(min(10, self.dim)):
            freq = 2 ** (i % 3) * (1 + 0.5 * np.sin(i))
            term = np.sin(freq * x[i]) * np.cos(freq * x[i] ** 2)
            fractal_terms.append(term)
        
        # Adaptive elliptic distortion with dynamic scaling
        ellipse_scale = 1.0 + 0.3 * np.mean(np.abs(x)) / 5.0
        ellipse_distortion = 0.0
        for i in range(self.dim):
            ellipse_distortion += (x[i] ** 2) / (1 + ellipse_scale * (i + 1))
        
        # Temporal coupling terms with delayed feedback
        temporal_coupling = 0.0
        if self.dim > 1:
            for i in range(1, self.dim):
                temporal_coupling += np.sin(x[i-1] - x[i]) * np.cos(x[i-1] + x[i])
        
        # Dynamic noise with periodic amplitude modulation
        noise_amplitude = 0.1 * (1 + np.sin(np.sum(x) / 5.0))
        noise = np.random.normal(0, max(0, noise_amplitude), self.dim)
        
        # Combine all components
        total = 0.4 * np.sum(fractal_terms) + 0.3 * ellipse_distortion + 0.2 * temporal_coupling + 0.1 * np.sum(noise**2) / self.dim
        
        return total