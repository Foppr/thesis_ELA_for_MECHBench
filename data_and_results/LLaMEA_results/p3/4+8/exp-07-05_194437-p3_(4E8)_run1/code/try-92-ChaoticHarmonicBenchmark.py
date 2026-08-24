import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        self.harmonic_frequencies = np.random.uniform(1.0, 10.0, dim)
        self.modulation_amplitudes = np.random.uniform(0.5, 3.0, dim)
        self.cross_coupling_strength = np.random.uniform(-0.8, 0.8, (dim, dim))
        self.boundary_exponents = np.random.uniform(2.0, 6.0, dim)
        self.adaptive_scaling = np.random.uniform(0.5, 2.0, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Multi-frequency harmonic components with dynamic modulation
        for i in range(self.dim):
            freq = self.harmonic_frequencies[i]
            amp = self.modulation_amplitudes[i]
            phase = self.phase_shifts[i]
            # Base harmonic with adaptive scaling
            result += amp * np.sin(freq * x[i] + phase) * self.adaptive_scaling[i]
            # Add cross-dimensional coupling
            for j in range(self.dim):
                if i != j:
                    coupling = self.cross_coupling_strength[i, j]
                    result += coupling * np.cos(0.5 * x[i]) * np.sin(0.3 * x[j])
        
        # Chaotic harmonic perturbations with exponential decay
        chaotic_perturbation = 0.0
        for i in range(self.dim):
            chaotic_perturbation += 5 * np.sin(15 * x[i] + np.cos(11 * x[i])) * np.exp(-0.1 * x[i]**2)
        result += chaotic_perturbation
        
        # Adaptive boundary penalty with variable exponents
        boundary_penalty = 0.0
        for i in range(self.dim):
            dist_from_boundary = 5.0 - np.abs(x[i])
            if dist_from_boundary > 0:
                penalty = 10 * dist_from_boundary**self.boundary_exponents[i] * np.exp(-0.5 * dist_from_boundary)
                boundary_penalty += penalty
        result += boundary_penalty
        
        # Dynamic conditioning based on normalized distance and dimensionality
        norm = np.linalg.norm(x)
        dynamic_factor = 1.0 + 0.7 * np.sin(norm / 4.0) * np.cos(norm / 6.0)
        result *= dynamic_factor
        
        # Structured noise with chaotic periodicity and dimensionally dependent components
        noise = 0.0
        for i in range(self.dim):
            noise += 3 * np.sin(1.2 * x[i]) * np.cos(0.7 * x[i]) * np.exp(-0.05 * x[i]**2)
        result += noise
        
        return result