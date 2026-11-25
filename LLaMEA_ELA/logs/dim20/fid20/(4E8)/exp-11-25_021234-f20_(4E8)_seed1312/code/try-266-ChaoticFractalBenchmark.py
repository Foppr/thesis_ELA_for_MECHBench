import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave potential terms with varying frequencies and amplitudes
        f1 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.3 * i + 0.1 * np.sum(x**2))
            amp = 1.5 + 0.5 * np.cos(0.2 * i + 0.15 * np.sum(x**2))
            f1 += amp * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Radial fractal coupling with self-similar interaction patterns
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(0.5 * i + 0.2 * r)
            f2 += scale * np.sin(3.0 * x[i] + 0.4 * r) * np.cos(2.0 * x[i] - 0.3 * r)
            
        # Adaptive gradient modulation with dynamic scaling factors
        f3 = 0.0
        for i in range(self.dim):
            grad_scale = 1.2 + 0.8 * np.sin(0.4 * i + 0.2 * r + 0.1 * np.random.uniform(-1, 1))
            f3 += grad_scale * x[i]**3 * np.exp(-0.05 * x[i]**2)
            
        # Dynamic penalty functions with time-varying thresholds
        f4 = 0.0
        for i in range(self.dim):
            threshold = 4.0 + 1.0 * np.sin(0.2 * i + 0.1 * r)
            if np.abs(x[i]) > threshold:
                penalty = 2.0 * (np.abs(x[i]) - threshold)**2 + 0.5 * (np.abs(x[i]) - threshold)**3
                f4 += penalty * np.exp(-0.1 * x[i]**2)
                
        # Multi-scale fractal interactions with varying coupling strengths
        f5 = 0.0
        for i in range(self.dim):
            strength = 0.8 + 0.4 * np.cos(0.3 * i + 0.2 * r + 0.1 * np.random.uniform(-1, 1))
            f5 += strength * np.sin(5.0 * x[i] + 0.3 * r) * np.exp(-0.08 * x[i]**2)
            
        # Cross-dimensional nonlinear correlations with exponential decay
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                correlation = np.sin(x[i] * x[j]) + np.cos(x[i] + x[j])
                decay = np.exp(-0.1 * (x[i]**2 + x[j]**2))
                f6 += correlation * decay
                
        # Boundary repulsion with adaptive strength based on distance from center
        f7 = 0.0
        for i in range(self.dim):
            dist_from_center = np.abs(x[i])
            if dist_from_center > 4.2:
                repulsion_strength = 1.5 + 0.5 * np.sin(0.3 * i + 0.1 * r)
                f7 += repulsion_strength * (dist_from_center - 4.2)**3
                
        # Time-varying chaotic modulation with frequency shifts
        f8 = 0.0
        for i in range(self.dim):
            freq_shift = 1.0 + 0.5 * np.sin(0.25 * i + 0.1 * r + 0.3 * np.random.uniform(-1, 1))
            f8 += np.sin(freq_shift * x[i]) * np.cos(0.5 * x[i]) * np.exp(-0.06 * x[i]**2)
            
        # Polynomial cross-terms with dynamic weights and radial conditioning
        f9 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.5 + 0.3 * np.sin(0.2 * (i - j) + 0.1 * r)
                f9 += weight * x[i]**2 * x[j]**4 * np.exp(-0.07 * (x[i]**2 + x[j]**2))
                
        # Enhanced harmonic components with phase modulation
        f10 = 0.0
        for i in range(self.dim):
            phase = 0.5 * np.sin(0.3 * i + 0.2 * r)
            f10 += np.sin(4.0 * x[i] + phase) * (x[i]**2 + 0.8) * np.exp(-0.09 * x[i]**2)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10