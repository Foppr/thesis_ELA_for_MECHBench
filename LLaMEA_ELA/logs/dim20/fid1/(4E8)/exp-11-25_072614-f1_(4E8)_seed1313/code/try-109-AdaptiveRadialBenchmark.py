import numpy as np

class AdaptiveRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperchaotic radial basis functions with multiple phase modulations and cross-terms
        rbfs = []
        centers = np.linspace(-4.5, 4.5, min(20, self.dim))
        widths = np.logspace(-1.5, 1.5, min(20, self.dim))
        phases = np.sin(np.linspace(0, 8*np.pi, min(20, self.dim)))
        cross_terms = np.cos(np.linspace(0, 6*np.pi, min(20, self.dim)))
        
        for i, (center, width, phase, cross) in enumerate(zip(centers, widths, phases, cross_terms)):
            if i < self.dim:
                # Add hyperchaotic modulation with cross-term interactions
                rbf = np.exp(-np.sum((x - center)**2) / (2 * width**2)) * \
                      np.sin(phase * np.sum(x**2)) * \
                      np.cos(cross * np.prod(x[:min(i+1, len(x))]))
                rbfs.append(rbf)
        
        # Asymmetric gradient field with multi-scale sine-cosine interactions
        grad_field = 0.0
        for scale in [1, 2, 3, 4]:
            grad_field += np.sum(np.sin(scale * x) * np.cos(scale * x)) / (self.dim * scale**1.5)
        
        # Dynamic noise injection with hyperchaotic amplitude modulation and temporal correlation
        noise_level = 0.3 * (1 + np.mean(np.abs(x)) / 5.0) * \
                      np.sin(np.sum(x)**2) * \
                      np.cos(np.mean(x)**3) * \
                      np.exp(-np.std(x)**2)
        noise = np.random.normal(0, max(0, noise_level), self.dim)
        
        # Add temporal correlation to noise
        if self.dim > 1:
            for i in range(1, self.dim):
                noise[i] += 0.4 * noise[i-1]
        
        # Cross-term interaction component with higher-order polynomial interactions
        cross_interaction = np.sum(np.sin(x[:-2]) * np.cos(x[2:])) / (self.dim - 2) if self.dim > 2 else 0
        
        # Add a new component for improved fitness: polynomial chaos expansion with interaction terms
        poly_chaos = 0.0
        for i in range(self.dim):
            poly_chaos += (x[i]**5 - 10*x[i]**3 + 15*x[i]) * np.sin(x[i]**2)
        
        # Add a new component: fractal-like self-similarity with multi-scale periodicity
        fractal_component = 0.0
        for scale in [0.5, 1.0, 2.0, 4.0]:
            fractal_component += np.sum(np.sin(scale * x) * np.cos(scale * x)) / (self.dim * scale)
        
        # Combine components with dynamic weighting based on input characteristics
        rbf_sum = np.sum(rbfs) if rbfs else 0
        total = 0.3 * rbf_sum + 0.2 * grad_field + 0.15 * np.sum(noise**2) / self.dim + 0.2 * cross_interaction + 0.1 * poly_chaos + 0.05 * fractal_component
        
        return total