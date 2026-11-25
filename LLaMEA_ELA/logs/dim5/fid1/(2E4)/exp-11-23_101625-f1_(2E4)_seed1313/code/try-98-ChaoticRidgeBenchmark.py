import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        result = 0.1 * np.sum(x**2)
        
        # Chaotic ridge structures with time-varying frequencies
        for i in range(self.dim):
            # Dynamic frequency modulation based on position and dimension
            freq = 2.5 + 1.2 * np.sin(i * 0.6 + np.sum(x) * 0.12)
            ridge_term = 2.5 * np.exp(-0.5 * ((x[i] - 3.5 * np.sin(freq * np.sum(x))) / (1.0 + 0.12 * np.abs(x[i])))**2)
            result += ridge_term
            
        # Asymmetric coupling with chaotic modulation
        for i in range(self.dim):
            coupling = 0.0
            for j in range(min(i+3, self.dim)):
                if i != j:
                    # Chaotic coupling strength with dynamic modulation
                    coupling_strength = 1.8 + 0.9 * np.sin(i * j * 0.45 + np.sum(x) * 0.22)
                    coupling += coupling_strength * (x[i]**2 + x[j]**2) * np.cos(0.6 * (x[i] - x[j]))
            result += 0.25 * coupling
            
        # Multi-scale harmonic interference with dynamic phases
        for i in range(self.dim):
            scale = 2**(i % 4 + 1)
            phase = 0.6 * np.sin(i * 0.35 + np.sum(x) * 0.16)
            result += 1.4 * np.sin(scale * x[i] + phase) * np.cos(scale * x[i] * 0.45 + phase)
            
        # Time-varying penalty terms with chaotic positioning
        penalty_positions = 4.2 * np.cos(np.arange(self.dim) * 0.75 + np.sum(x) * 0.22)
        penalty_heights = 2.0 + 1.0 * np.sin(np.arange(self.dim) * 0.55 + np.sum(x) * 0.32)
        
        for i in range(self.dim):
            distance_to_penalty = np.abs(np.abs(x[i]) - np.abs(penalty_positions[i]))
            if distance_to_penalty < 1.6:
                result += penalty_heights[i] * (distance_to_penalty**2 + 0.12 * np.sin(distance_to_penalty * 11))
                
        # Adaptive radial harmonic interference
        r = np.sqrt(np.sum(x**2))
        radial_freq = 3.5 + 2.2 * np.cos(r * 0.16)
        result += 1.7 * np.sin(radial_freq * r) * np.cos(radial_freq * r * 0.32)
        
        # Asymmetric exponential barrier with dynamic scaling
        barrier_scale = 1.1 + 0.55 * np.sin(self.dim * 0.32 + r * 0.22)
        for i in range(self.dim):
            result += barrier_scale * np.exp(2.2 * abs(x[i]) / 5.0) * (1 + 0.22 * np.sin(x[i] * 3.2))
            
        # Additional chaotic modulation with cross-dimensional interaction
        chaos_mod = 0.22 * np.sin(np.sum(x) * 0.42 + r * 0.32)
        for i in range(self.dim):
            result += 0.45 * np.sin(5.2 * x[i] + chaos_mod) * np.cos(2.7 * x[i] + chaos_mod)
            
        return result