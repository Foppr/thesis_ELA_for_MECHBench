import numpy as np

class ChaoticAdaptiveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        self.scale_factors = np.random.uniform(0.5, 2.0, dim)
        self.frequency_factors = np.random.uniform(2.0, 10.0, dim)
        self.amplitude_factors = np.random.uniform(1.0, 5.0, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        self.coupling_matrix = np.random.uniform(-0.3, 0.3, (dim, dim))
        self.adaptive_exponents = np.random.uniform(1.0, 3.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Multi-scale sinusoidal components with adaptive frequencies and amplitudes
        for i in range(self.dim):
            freq = self.frequency_factors[i] * (1.0 + 0.2 * np.sin(x[i]))
            amp = self.amplitude_factors[i] * (1.0 + 0.1 * np.cos(x[i]))
            result += amp * np.sin(freq * x[i] + self.phase_shifts[i]) * self.scale_factors[i]
        
        # Dynamic cross-dimension coupling with adaptive weights
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_matrix[i, j] * np.sin(x[i] * x[j])
            result += coupling_sum * (1.0 + 0.3 * np.sin(x[i]))
        
        # Adaptive conditioning based on dimension and position
        for i in range(self.dim):
            adaptive_factor = 1.0 + 0.5 * np.sin(x[i]) * np.cos(x[i]) * self.adaptive_exponents[i]
            result += 2.0 * adaptive_factor * (x[i]**2) * np.exp(-0.1 * np.abs(x[i]))
        
        # Chaotic perturbation with dynamic scaling
        chaotic_sum = 0.0
        for i in range(self.dim):
            chaotic_sum += np.sin(15 * x[i] + np.sin(10 * x[i])) * np.cos(8 * x[i])
        result += 0.5 * chaotic_sum
        
        # Multi-scale noise with exponential decay
        noise = 0.0
        for i in range(self.dim):
            noise += 0.3 * np.sin(5 * x[i]) * np.exp(-0.05 * x[i]**2)
        result += noise
        
        # Boundary penalty with dynamic strength
        boundary_penalty = 0.0
        for i in range(self.dim):
            dist = 5.0 - np.abs(x[i])
            if dist > 0:
                boundary_penalty += 10 * dist**3 * np.exp(-0.3 * dist)
        result += boundary_penalty
        
        return result