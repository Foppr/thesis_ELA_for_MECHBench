import numpy as np

class GeodesicPenaltyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to hypersphere of radius 5
        norm = np.linalg.norm(x)
        if norm > 0:
            x_norm = x * 5.0 / norm
        else:
            x_norm = x.copy()
            
        # Geodesic distance on hypersphere with cosine similarity
        geodesic_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dot_product = np.dot(x_norm[i:i+1], x_norm[j:j+1].T)
                if dot_product > 1.0:
                    dot_product = 1.0
                elif dot_product < -1.0:
                    dot_product = -1.0
                angle = np.arccos(dot_product)
                geodesic_term += angle**2
        
        # Adaptive penalty based on distance from origin and dimensionality
        penalty_term = 0.0
        for i in range(self.dim):
            penalty_term += (5.0 - np.abs(x[i]))**4 * (1.0 + 0.1 * np.sin(0.3 * x[i]))
        penalty_term /= self.dim
        
        # Dynamic gradient modulation with frequency-dependent damping
        grad_mod = 0.0
        for i in range(self.dim):
            grad_mod += np.cos(x[i] * np.pi / 2.0) * np.sin(x[i] * np.pi / 4.0) * (1.0 + 0.2 * np.cos(0.5 * x[i]))
        grad_mod /= self.dim
        
        # Multi-scale harmonic oscillation with varying amplitudes
        harmonic_term = 0.0
        for i in range(self.dim):
            harmonic_term += np.sin(x[i] * np.pi) * np.cos(x[i] * np.pi / 3.0) * np.exp(-0.1 * x[i]**2)
        harmonic_term /= self.dim
        
        # Cross-dimensional coupling with inverse distance weighting
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                cross_coupling += np.sin(2.0 * x[i]) * np.cos(2.0 * x[j]) / (dist + 1e-8)
        cross_coupling /= (self.dim * (self.dim - 1) / 2.0)
        
        # Asymmetric exponential decay with parameter adaptation
        exp_term = 0.0
        for i in range(self.dim):
            if x[i] >= 0:
                exp_term += np.exp(-0.5 * x[i]) * (1.0 + 0.3 * np.sin(0.4 * x[i]))
            else:
                exp_term += np.exp(-0.3 * x[i]) * (1.0 + 0.2 * np.cos(0.6 * x[i]))
        exp_term /= self.dim
        
        # Fractal-like basin structure with recursive scaling
        basin_term = 0.0
        for i in range(self.dim):
            basin_term += np.sin(x[i] * np.pi / 4.0) * np.cos(x[i] * np.pi / 8.0) * (1.0 + 0.1 * np.sin(0.2 * x[i]))
        basin_term /= self.dim
        
        # Add chaotic sine terms for increased complexity
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(x[i] * np.pi * 3.0) * np.cos(x[i] * np.pi * 1.5) * (0.5 + 0.5 * np.sin(x[i] * np.pi * 2.0))
        chaotic_term /= self.dim
        
        # Combine all terms with carefully tuned weights
        total = 0.18 * geodesic_term + 0.20 * penalty_term + 0.14 * grad_mod + 0.13 * harmonic_term + 0.12 * cross_coupling + 0.15 * exp_term + 0.16 * basin_term + 0.12 * chaotic_term
        
        return total