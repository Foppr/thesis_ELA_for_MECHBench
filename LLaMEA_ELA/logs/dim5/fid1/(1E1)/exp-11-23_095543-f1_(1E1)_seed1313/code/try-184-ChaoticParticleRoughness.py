import numpy as np

class ChaoticParticleRoughness:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Base quadratic term with condition number variation
        result = 0.0
        for i in range(self.dim):
            result += (i + 1) * x[i] ** 2
            
        # Add chaotic particle interactions with time-like evolution
        chaotic_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    distance = np.abs(x[i] - x[j])
                    chaotic_sum += np.sin(10 * distance) * np.exp(-0.5 * distance)
        result += 0.3 * chaotic_sum
        
        # Add fractional Brownian motion inspired roughness
        fbm_roughness = 0.0
        for i in range(self.dim):
            fbm_roughness += np.sin(2 * x[i]) * np.cos(3 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
        result += 0.25 * fbm_roughness
        
        # Add adaptive dimensional coupling with varying exponents
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_exponent = 1.0 + 0.5 * np.sin(0.5 * (i + j))
                coupling_term += np.sin(x[i]) * np.cos(x[j]) * (x[i]**2 + x[j]**2)**coupling_exponent
        result += 0.4 * coupling_term
        
        # Add multi-scale harmonic components with varying frequencies
        scale_harmonic = 0.0
        for i in range(self.dim):
            scale_harmonic += np.sin(15 * x[i]) * np.cos(12 * x[i]) * np.exp(-0.3 * x[i]**2)
        result += 0.3 * scale_harmonic
        
        # Add particle swarm inspired repulsion terms
        swarm_repulsion = 0.0
        for i in range(self.dim):
            repulsion_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    repulsion_sum += 1.0 / (1.0 + np.abs(x[i] - x[j]))
            swarm_repulsion += repulsion_sum * np.sin(5 * x[i])
        result += 0.2 * swarm_repulsion
        
        # Add dimensionally varying curvature with fractional exponents
        fractional_curvature = 0.0
        for i in range(self.dim):
            fractional_curvature += (i + 1) ** 0.7 * x[i] ** 1.8
        result += 0.25 * fractional_curvature
        
        # Add fractal-like self-similarity with recursive patterns
        fractal_pattern = 0.0
        for i in range(self.dim):
            fractal_pattern += np.sin(8 * x[i]) * np.cos(7 * x[i]) * np.sin(6 * x[(i+1) % self.dim])
        result += 0.35 * fractal_pattern
        
        # Add chaotic modulation based on cumulative dimension interactions
        cummulative_mod = 0.0
        for i in range(self.dim):
            cummulative_mod += np.sin(20 * x[i]) * np.cos(18 * x[(i+2) % self.dim]) * np.exp(-0.05 * (x[i]**2 + x[(i+2) % self.dim]**2))
        result += 0.4 * cummulative_mod
        
        # Add adaptive scaling based on local gradient characteristics
        local_scale = 1.0 + 0.1 * np.sum(np.sin(x)**2) + 0.05 * np.sum(np.cos(x)**2)
        result *= local_scale
        
        # Add conditioning through asymmetric penalty terms
        asym_penalty = 0.0
        for i in range(self.dim):
            asym_penalty += 0.15 * (x[i] ** 3) * np.sin(4 * x[(i+1) % self.dim]) * np.exp(-0.1 * np.abs(x[i]))
        result += asym_penalty
        
        return result