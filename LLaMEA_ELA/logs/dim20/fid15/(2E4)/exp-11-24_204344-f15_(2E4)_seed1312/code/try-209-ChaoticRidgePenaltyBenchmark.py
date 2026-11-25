import numpy as np

class ChaoticRidgePenaltyBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Phase-modulated chaotic landscape with dynamic ridge structures
        result = 0.0
        for i in range(self.dim):
            # Base quadratic term with chaotic phase modulation
            phase = np.sin(x[i] * (2.0 + 0.5 * np.sin(i * 0.3)))
            ridge_term = x[i]**2 + 0.3 * x[i]**3 * phase
            
            # Dynamic ridge scaling based on position
            scale = 1.0 + 0.4 * np.cos(x[i] * 1.5)
            result += ridge_term * scale
        
        # Adaptive penalty landscape with varying severity
        penalty = 0.0
        for i in range(self.dim):
            # Penalty activated when variables approach boundaries
            boundary_dist = min(np.abs(x[i] - 5.0), np.abs(x[i] + 5.0))
            penalty_factor = 1.0 + 2.0 * np.exp(-boundary_dist * 2.0)
            
            # Variable penalty strength based on dimension index
            strength = 0.5 + 0.3 * np.sin(i * 0.8)
            penalty += penalty_factor * strength * (x[i]**2)
        
        # Cross-dimensional coupling with dynamic phase interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Phase-coupled interaction with adaptive coupling strength
                coupling_phase = np.sin((x[i] + x[j]) * (0.5 + 0.2 * np.cos(i * 0.4)))
                coupling_strength = 0.8 + 0.3 * np.sin(j * 0.6)
                cross_term += coupling_strength * np.sin(x[i] * x[j] * coupling_phase) * (x[i]**2 + x[j]**2)
        
        # Multi-scale chaotic modulation with varying frequencies
        chaos = 0.0
        for i in range(self.dim):
            # Multiple chaotic modulation frequencies
            freqs = [3.0, 5.0, 7.0, 9.0]
            modulations = []
            for f in freqs:
                mod = np.sin(x[i] * f + i * 0.2) * np.cos(x[i] * f * 0.7)
                modulations.append(mod)
            
            chaos += np.mean(modulations) * (1.0 + 0.2 * np.sin(i * 0.5))
        
        # Combined landscape with weighted components
        total = 0.3 * result + 0.4 * penalty + 0.2 * cross_term + 0.1 * chaos
        
        # Global scaling factor that increases with dimensionality
        scaling = 1.0 + 0.1 * self.dim
        
        return total * scaling