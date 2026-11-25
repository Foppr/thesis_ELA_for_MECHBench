import numpy as np

class ChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic sine wave base with exponential frequency growth
        for i in range(self.dim):
            freq = 2 * np.pi * (2 ** (i % 4)) * (1 + 0.3 * np.sin(x[i] * 0.7))
            wave = np.sin(freq * x[i])
            result += 0.6 * wave**5
        
        # Fractal-like ridge structure with self-similar chaotic patterns
        for i in range(self.dim):
            ridge = (np.sin(3 * x[i]) + 
                    0.4 * np.sin(9 * x[i]) + 
                    0.1 * np.sin(27 * x[i]) + 
                    0.05 * np.sin(81 * x[i]))
            result += 0.5 * ridge**4
        
        # Multi-scale phase coupling with dynamic interaction
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for complexity
                phase = np.sin(0.3 * x[i] + 0.7 * x[j])
                coupling = 1.0 + 0.2 * np.cos(x[i] * x[j])
                interference = np.cos(coupling * (x[i] - x[j]) + phase)
                result += 0.15 * interference**3
        
        # Chaotic boundary conditioning with non-linear penalty
        boundary_penalty = 0.0
        for i in range(self.dim):
            dist_to_bound = 5.0 - abs(x[i])
            penalty = dist_to_bound**3 if dist_to_bound > 0 else 0.0
            boundary_penalty += penalty
        result += 0.2 * boundary_penalty
        
        # Adaptive frequency modulation with chaotic coupling
        for i in range(self.dim):
            mod_freq = 1.5 + 0.8 * np.sin(x[i] * 0.4 + i * 0.3)
            coupling_term = 1.0 + 0.4 * np.cos(x[i] * 0.6 + i * 0.2)
            result += 0.25 * np.sin(mod_freq * coupling_term * x[i])**4
        
        # Cross-dimensional chaotic interaction with exponential scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Exponentially increasing chaos factor
                chaos_factor = 3**(abs(i-j))
                interaction = np.sin(chaos_factor * (x[i] + x[j]))
                result += 0.1 * interaction**2
        
        # Multi-scale noise with chaotic amplitude modulation
        noise = 0.0
        for i in range(self.dim):
            amp_mod = 1.0 + 0.3 * np.sin(i * 0.5)
            noise += amp_mod * (np.sin(5 * x[i]) + 
                               0.5 * np.sin(23 * x[i]) + 
                               0.2 * np.sin(113 * x[i]))
        result += 0.18 * noise**2
        
        # Hierarchical fractal scaling with chaotic dimensionality
        scale_factor = 1.0 + 0.3 * np.sin(np.sum(x) * 0.1)
        result *= scale_factor
        
        # Final chaotic regularization and normalization
        result /= self.dim
        result += 0.008 * np.sum(np.abs(x)**7) / self.dim
        
        return result