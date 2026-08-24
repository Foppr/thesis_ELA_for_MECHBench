import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Global minimum at center with slight chaotic perturbation
        self.global_min = np.full(dim, 0.0)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with chaotic modulation and multi-scale interference
        r = np.sqrt(np.sum(x**2))
        radial_term = r * (1 + 0.3 * np.sin(10 * r) + 0.2 * np.cos(5 * r))
        
        # Trigonometric chaos with dynamic phase shifts and adaptive scaling
        trig_term = np.sum(np.sin(x * np.pi / 2 + np.sin(x)) * np.cos(x * np.pi / 3 + np.cos(x)))
        
        # Multi-scale interference with fractal-like frequency progression
        interference = 0
        for i in range(1, min(6, self.dim + 1)):
            interference += np.sum(np.sin(i * x * np.exp(-i * 0.1)) * np.cos(i * x * np.exp(-i * 0.05)))
        
        # Adaptive conditioning with dynamic weights based on coordinate values
        cond_weights = 1 + 0.5 * np.abs(x) / 5.0
        conditioning = np.sum(cond_weights * x**2)
        
        # Dynamic noise modulation with chaotic amplitude scaling
        noise = np.sum(np.random.randn() * np.sin(x * np.exp(-np.abs(x))) * np.cos(x * np.exp(-np.abs(x))))
        
        # Cross-dimensional coupling with radial symmetry and chaotic phase
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.sin((x[i] - x[j]) * np.cos(r)) * np.cos((x[i] + x[j]) * np.sin(r))
        
        # Final combined function with chaotic scaling factors
        return 0.2 * radial_term + 0.3 * trig_term + 0.25 * interference + 0.15 * conditioning + 0.1 * noise + 0.05 * coupling