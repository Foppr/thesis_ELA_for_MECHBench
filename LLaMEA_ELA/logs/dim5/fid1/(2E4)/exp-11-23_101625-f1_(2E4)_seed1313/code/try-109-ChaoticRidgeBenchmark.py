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
            freq = 2.8 + 1.5 * np.sin(i * 0.7 + np.sum(x) * 0.15)
            ridge_term = 3.0 * np.exp(-0.5 * ((x[i] - 3.8 * np.sin(freq * np.sum(x))) / (1.0 + 0.15 * np.abs(x[i])))**2)
            result += ridge_term
            
        # Asymmetric coupling with chaotic modulation
        for i in range(self.dim):
            coupling = 0.0
            for j in range(min(i+3, self.dim)):
                if i != j:
                    # Chaotic coupling strength with dynamic modulation
                    coupling_strength = 2.1 + 1.1 * np.sin(i * j * 0.5 + np.sum(x) * 0.25)
                    coupling += coupling_strength * (x[i]**2 + x[j]**2) * np.cos(0.7 * (x[i] - x[j]))
            result += 0.3 * coupling
            
        # Multi-scale harmonic interference with dynamic phases
        for i in range(self.dim):
            scale = 2**(i % 4 + 1)
            phase = 0.7 * np.sin(i * 0.4 + np.sum(x) * 0.18)
            result += 1.6 * np.sin(scale * x[i] + phase) * np.cos(scale * x[i] * 0.5 + phase)
            
        # Time-varying penalty terms with chaotic positioning
        penalty_positions = 4.5 * np.cos(np.arange(self.dim) * 0.8 + np.sum(x) * 0.25)
        penalty_heights = 2.2 + 1.2 * np.sin(np.arange(self.dim) * 0.6 + np.sum(x) * 0.35)
        
        for i in range(self.dim):
            distance_to_penalty = np.abs(np.abs(x[i]) - np.abs(penalty_positions[i]))
            if distance_to_penalty < 1.8:
                result += penalty_heights[i] * (distance_to_penalty**2 + 0.15 * np.sin(distance_to_penalty * 12))
                
        # Adaptive radial harmonic interference
        r = np.sqrt(np.sum(x**2))
        radial_freq = 3.8 + 2.5 * np.cos(r * 0.18)
        result += 2.0 * np.sin(radial_freq * r) * np.cos(radial_freq * r * 0.35)
        
        # Asymmetric exponential barrier with dynamic scaling
        barrier_scale = 1.2 + 0.6 * np.sin(self.dim * 0.35 + r * 0.25)
        for i in range(self.dim):
            result += barrier_scale * np.exp(2.5 * abs(x[i]) / 5.0) * (1 + 0.25 * np.sin(x[i] * 3.5))
            
        # Additional chaotic modulation with cross-dimensional interaction
        chaos_mod = 0.25 * np.sin(np.sum(x) * 0.45 + r * 0.35)
        for i in range(self.dim):
            result += 0.5 * np.sin(5.5 * x[i] + chaos_mod) * np.cos(3.0 * x[i] + chaos_mod)
            
        return result