import numpy as np

class AdaptiveRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperchaotic radial basis functions with multiple phase modulations and cross-terms
        rbfs = []
        centers = np.linspace(-4.5, 4.5, min(15, self.dim))
        widths = np.logspace(-2, 2, min(15, self.dim))
        phases = np.sin(np.linspace(0, 4*np.pi, min(15, self.dim)))
        cross_terms = np.cos(np.linspace(0, 3*np.pi, min(15, self.dim)))
        
        for i, (center, width, phase, cross) in enumerate(zip(centers, widths, phases, cross_terms)):
            if i < self.dim:
                # Add hyperchaotic modulation with cross-term interactions
                rbf = np.exp(-np.sum((x - center)**2) / (2 * width**2)) * \
                      np.sin(phase * np.sum(x**2)) * \
                      np.cos(cross * np.prod(x[:min(i+1, len(x))]))
                rbfs.append(rbf)
        
        # Asymmetric gradient field with multi-scale sine-cosine interactions
        grad_field = 0.0
        for scale in [1, 2, 3]:
            grad_field += np.sum(np.sin(scale * x) * np.cos(scale * x)) / (self.dim * scale)
        
        # Dynamic noise injection with hyperchaotic amplitude modulation and temporal correlation
        noise_level = 0.2 * (1 + np.mean(np.abs(x)) / 5.0) * \
                      np.sin(np.sum(x)**2) * \
                      np.cos(np.mean(x)**3)
        noise = np.random.normal(0, max(0, noise_level), self.dim)
        
        # Add temporal correlation to noise
        if self.dim > 1:
            for i in range(1, self.dim):
                noise[i] += 0.3 * noise[i-1]
        
        # Cross-term interaction component with fractal-like self-similarity - modified frequency
        cross_interaction = np.sum(np.sin(1.5 * x[:-1]) * np.cos(1.5 * x[1:])) / (self.dim - 1) if self.dim > 1 else 0
        
        # Add fractal-like self-similarity pattern - modified scaling
        fractal_pattern = 0.0
        for i in range(1, min(5, self.dim)):
            fractal_pattern += np.sin(1.2 * np.sum(x[:i]) / i) * np.cos(1.3 * np.sum(x[-i:]) / i)
        
        # Adaptive conditioning based on input characteristics
        condition_factor = 1.0 + 0.5 * np.std(x) / 5.0
        
        # Add a new component for improved fitness: polynomial chaos expansion with interaction terms - modified exponents
        poly_chaos = 0.0
        for i in range(self.dim):
            poly_chaos += (x[i]**5 - 7*x[i]**3 + 12*x[i]) * np.sin(x[i])
        
        # Combine components with dynamic weighting based on input characteristics
        rbf_sum = np.sum(rbfs) if rbfs else 0
        total = 0.35 * rbf_sum + 0.25 * grad_field + 0.2 * np.sum(noise**2) / self.dim + 0.15 * cross_interaction + 0.05 * poly_chaos + 0.05 * fractal_pattern
        
        # Apply adaptive conditioning
        total *= condition_factor
        
        return total