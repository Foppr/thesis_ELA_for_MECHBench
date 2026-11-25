import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic modulation parameters
        self.chaos_params = np.linspace(0.1, 2.0, min(8, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive conditioning
        result = 0.2 * np.sum(x**2)
        
        # Chaotic modulation with radial basis functions
        for i in range(self.dim):
            # Modified RBF with chaotic center positions
            center = 5.0 * np.sin(self.chaos_params[min(i, len(self.chaos_params)-1)] * x[i])
            sigma = 0.5 + 0.3 * np.cos(i * np.pi / (self.dim + 1))
            result += 2.0 * np.exp(-0.5 * ((x[i] - center) / sigma)**2)
        
        # Enhanced sinusoidal components with chaotic frequencies
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(self.chaos_params[min(i, len(self.chaos_params)-1)] * x[i])
            result += 1.5 * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
            result += 1.0 * np.cos(freq * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Adaptive saddle-point potentials with dynamic steepness
        for i in range(self.dim):
            # Dynamic steepness based on chaotic parameters
            steepness = 1.5 + 0.8 * np.sin(i * np.pi / (self.dim + 1))
            # Modified saddle potential with additional harmonic terms
            result += steepness * (x[i]**2 - 0.3 * np.sin(4 * x[i]) + 0.1 * x[i]**4)
        
        # Cross-dimensional coupling with chaotic strength modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling strength based on both dimensions
                coupling_strength = 0.8 + 0.4 * np.sin(i * x[j] + j * x[i])
                # Phase-modulated coupling with chaotic frequency
                phase = np.sin(2 * i * x[j] - 3 * j * x[i] + self.chaos_params[min(i, len(self.chaos_params)-1)])
                result += coupling_strength * np.exp(-0.1 * (x[i]**2 + x[j]**2)) * phase
        
        # Multi-scale chaotic oscillations with adaptive amplitudes
        for i in range(self.dim):
            # Adaptive amplitude based on chaotic modulation
            amp_factor = 1.0 + 0.5 * np.sin(self.chaos_params[min(i, len(self.chaos_params)-1)] * x[i])
            result += amp_factor * (np.sin(3 * x[i]) + 0.5 * np.cos(7 * x[i]))
        
        # Boundary regularization with chaotic penalty scaling
        boundary_penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.0:
                # Chaotic penalty scaling factor
                penalty_scale = 1.0 + 0.3 * np.sin(i * np.pi / (self.dim + 1))
                boundary_penalty += penalty_scale * (abs(x[i]) - 4.0)**2
        result += boundary_penalty
        
        # Global conditioning with chaotic scaling factor
        global_conditioning = 1.0 + 0.5 * np.sin(np.sum(x) * np.pi / (self.dim + 1))
        result *= global_conditioning
        
        return result