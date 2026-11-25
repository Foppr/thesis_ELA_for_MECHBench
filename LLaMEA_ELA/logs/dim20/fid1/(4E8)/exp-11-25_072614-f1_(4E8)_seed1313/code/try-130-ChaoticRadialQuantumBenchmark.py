import numpy as np

class ChaoticRadialQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic radial basis functions with quantum interference patterns
        rbfs = []
        centers = np.linspace(-4.8, 4.8, min(20, self.dim))
        widths = np.logspace(-1.5, 1.8, min(20, self.dim))
        phases = np.sin(np.linspace(0, 6*np.pi, min(20, self.dim)))
        quantum_phases = np.cos(np.linspace(0, 5*np.pi, min(20, self.dim)))
        
        for i, (center, width, phase, q_phase) in enumerate(zip(centers, widths, phases, quantum_phases)):
            if i < self.dim:
                # Add chaotic modulation with quantum interference
                rbf = np.exp(-np.sum((x - center)**2) / (2 * width**2)) * \
                      np.sin(phase * np.sum(x**2)) * \
                      np.cos(q_phase * np.prod(x[:min(i+1, len(x))])) * \
                      np.sin(np.sum(x) * np.pi / 4.0)
                rbfs.append(rbf)
        
        # Asymmetric gradient field with multi-scale sine-cosine interactions
        grad_field = 0.0
        for scale in [1, 2, 3, 4]:
            grad_field += np.sum(np.sin(scale * x) * np.cos(scale * x)) / (self.dim * scale**1.5)
        
        # Dynamic noise injection with hyperchaotic amplitude modulation and temporal correlation
        noise_level = 0.3 * (1 + np.mean(np.abs(x)) / 5.0) * \
                      np.sin(np.sum(x)**2) * \
                      np.cos(np.mean(x)**3) * \
                      np.tanh(np.sum(np.sin(x)))
        noise = np.random.normal(0, max(0, noise_level), self.dim)
        
        # Add temporal correlation to noise
        if self.dim > 1:
            for i in range(1, self.dim):
                noise[i] += 0.4 * noise[i-1] + 0.1 * np.sin(i * np.pi / self.dim) * noise[i-1]**2
        
        # Cross-term interaction component with fractal-like self-similarity
        cross_interaction = np.sum(np.sin(x[:-1]) * np.cos(x[1:])) / (self.dim - 1) if self.dim > 1 else 0
        
        # Add fractal-like self-similarity pattern
        fractal_pattern = 0.0
        for i in range(1, min(6, self.dim)):
            fractal_pattern += np.sin(np.sum(x[:i]) / i) * np.cos(np.sum(x[-i:]) / i) * \
                               np.exp(-np.abs(i - self.dim/2) / (self.dim/4))
        
        # Adaptive conditioning based on input characteristics
        condition_factor = 1.0 + 0.6 * np.std(x) / 5.0
        
        # Add quantum-inspired polynomial chaos expansion with interaction terms
        poly_chaos = 0.0
        for i in range(self.dim):
            poly_chaos += (x[i]**5 - 10*x[i]**3 + 25*x[i]) * np.sin(x[i] / 2.0)
        
        # Add quantum tunneling component for enhanced exploration
        tunneling = 0.0
        for i in range(self.dim):
            tunneling += np.exp(-np.abs(x[i]) / (1.0 + np.abs(x[i]))) * np.cos(x[i]**2)
        
        # Combine components with dynamic weighting based on input characteristics
        rbf_sum = np.sum(rbfs) if rbfs else 0
        total = 0.3 * rbf_sum + 0.2 * grad_field + 0.15 * np.sum(noise**2) / self.dim + \
                0.15 * cross_interaction + 0.1 * poly_chaos + 0.08 * fractal_pattern + 0.02 * tunneling
        
        # Apply adaptive conditioning
        total *= condition_factor
        
        return total