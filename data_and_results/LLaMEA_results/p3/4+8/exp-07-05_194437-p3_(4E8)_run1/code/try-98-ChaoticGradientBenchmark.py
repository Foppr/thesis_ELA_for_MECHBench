import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        self.coupling_matrix = np.random.uniform(-0.3, 0.3, (dim, dim))
        self.frequency_matrix = np.random.uniform(2.0, 6.0, (dim, dim))
        self.amplitude_matrix = np.random.uniform(0.5, 2.0, (dim, dim))
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        self.curvature_factors = np.random.uniform(0.1, 2.0, dim)
        self.scale_factors = np.random.uniform(0.5, 1.5, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Multi-scale periodic components with dynamic coupling
        for i in range(self.dim):
            term = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling = self.coupling_matrix[i, j]
                    freq = self.frequency_matrix[i, j]
                    amp = self.amplitude_matrix[i, j]
                    term += amp * np.sin(freq * x[j] + coupling * x[i] + self.phase_shifts[j])
            result += (x[i]**2) * (1.0 + 0.3 * np.sin(2.0 * x[i])) + term * self.curvature_factors[i]
        
        # Chaotic gradient modulation with implicit constraint
        gradient_mod = 0.0
        for i in range(self.dim):
            grad_term = 0.0
            for j in range(self.dim):
                if i != j:
                    grad_term += np.cos(x[i] + x[j]) * self.coupling_matrix[i, j]
            gradient_mod += grad_term * np.exp(-0.1 * x[i]**2)
        result += 0.5 * gradient_mod**2
        
        # Dynamic curvature and multi-scale modulation
        curvature = 0.0
        for i in range(self.dim):
            curvature += self.curvature_factors[i] * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
        result += 0.3 * curvature**2
        
        # Multi-scale harmonic interference
        interference = 0.0
        for i in range(self.dim):
            for k in range(1, 4):
                interference += np.sin(k * x[i]) * np.cos(k * x[i]) * self.scale_factors[i]
        result += 0.2 * interference**2
        
        # Boundary penalty with exponential scaling
        penalty = 0.0
        for i in range(self.dim):
            dist = 5.0 - np.abs(x[i])
            if dist < 0:
                penalty += 100 * dist**2
            else:
                penalty += 2 * dist**2 * np.exp(-0.5 * dist)
        result += penalty
        
        # Global scaling with chaotic modulation
        global_scale = 1.0 + 0.2 * np.sin(np.sum(x**2) / 10.0)
        result *= global_scale
        
        return result