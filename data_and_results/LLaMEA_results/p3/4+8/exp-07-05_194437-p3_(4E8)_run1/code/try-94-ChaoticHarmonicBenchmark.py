import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        self.frequency_scalers = np.random.uniform(0.5, 3.0, dim)
        self.harmonic_weights = np.random.uniform(0.1, 2.0, dim)
        self.basin_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.basin_strengths = np.random.uniform(1.0, 5.0, 10)
        self.cross_coupling = np.random.uniform(-0.3, 0.3, (dim, dim))
        self.adaptive_factors = np.random.uniform(0.5, 2.0, dim)
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Basin-based harmonic components with adaptive scaling
        for i in range(10):
            diff = x - self.basin_centers[i]
            distance = np.sum(diff**2)
            basin_value = self.basin_strengths[i] * np.exp(-distance / (2 * (0.5 + 0.2 * i)**2))
            result += basin_value
        
        # Chaotic harmonic modulation with phase shifts and frequency scaling
        for i in range(self.dim):
            freq = self.frequency_scalers[i] * (1.0 + 0.2 * np.sin(0.5 * x[i]))
            phase = self.phase_shifts[i] + 0.3 * np.cos(0.7 * x[i])
            harmonic = np.sin(freq * x[i] + phase) * self.harmonic_weights[i]
            result += harmonic * self.adaptive_factors[i]
            
            # Add cross-dimension coupling
            for j in range(self.dim):
                if i != j:
                    coupling = self.cross_coupling[i, j] * np.cos(0.4 * x[i]) * np.sin(0.6 * x[j])
                    result += coupling
        
        # Dynamic boundary penalty with logarithmic decay
        boundary_penalty = 0.0
        for i in range(self.dim):
            dist_from_boundary = 5.0 - np.abs(x[i])
            if dist_from_boundary > 0:
                boundary_penalty += 10 * np.log(1 + dist_from_boundary) * np.exp(-dist_from_boundary)
        result += boundary_penalty
        
        # Adaptive conditioning based on dimensionality and input norm
        norm = np.linalg.norm(x)
        cond_factor = 1.0 + 0.5 * np.sin(norm / 4.0) * np.cos(norm / 6.0)
        result *= cond_factor
        
        # Chaotic noise component with multi-scale sinusoidal perturbations
        noise = 0.0
        for i in range(self.dim):
            noise += 2.5 * np.sin(3 * x[i] + np.sin(2 * x[i])) * np.cos(1.5 * x[i])
        result += noise
        
        # Add structured chaotic oscillation
        chaotic_osc = 0.0
        for i in range(self.dim):
            chaotic_osc += 1.5 * np.sin(8 * x[i] + np.sin(5 * x[i]) + np.sin(3 * x[i]))
        result += chaotic_osc
        
        return result