import numpy as np

class NestedChaoticAttractors:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Base nested harmonic structure with increasing frequency
        f = 0.0
        for i in range(self.dim):
            f += 0.5 * np.sin(2 * x_norm[i]) + 0.3 * np.sin(5 * x_norm[i]) + 0.2 * np.sin(10 * x_norm[i])
            
        # Gradient-based attraction fields with position-dependent strength
        for i in range(self.dim):
            # Attraction towards multiple fixed points
            attraction_points = np.array([0.0, 1.0, -1.0, 2.0, -2.0])
            attraction_strength = 0.0
            for point in attraction_points:
                dist = np.abs(x[i] - point)
                attraction_strength += np.exp(-dist**2 / 0.5) / (dist + 0.1)
            f += 0.5 * attraction_strength
            
        # Multi-scale chaotic perturbations with coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Chaotic interaction term with exponential coupling
                coupling = np.exp(-0.1 * (x[i]**2 + x[j]**2)) * np.sin(x[i] * x[j])
                f += 0.3 * coupling
                
        # Dimensional coupling with fractal-like scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal coupling with recursive scaling
                scale_factor = 1.0 / (1.0 + np.exp(-0.5 * (i + j)))
                f += 0.2 * scale_factor * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Nested oscillatory components with varying amplitudes
        for i in range(self.dim):
            f += 0.1 * np.sin(15 * x_norm[i]) * np.cos(20 * x_norm[i]) * np.sin(25 * x_norm[i])
            
        # Asymmetric saddle points with dynamic weights
        for i in range(self.dim):
            # Dynamic weight based on dimension index
            weight = 0.4 * np.sin(i * 0.7) + 0.3 * np.cos(i * 1.1)
            f += weight * (x[i]**3 - 0.5 * x[i]**2 + 0.1 * x[i])
            
        # Multi-modal structure with irregular peaks
        for i in range(self.dim):
            f += 0.3 * np.sin(6 * x[i]) * np.cos(9 * x[i]) * np.sin(12 * x[i])
            
        # Basin boundary complexity with exponential decay
        boundary_complexity = 0.0
        for i in range(self.dim):
            # Create complex boundaries around local minima
            boundary_term = 0.0
            for center in [-2.0, -1.0, 0.0, 1.0, 2.0]:
                dist = np.abs(x[i] - center)
                boundary_term += np.exp(-dist**2 / 0.3) * np.sin(dist * 5)
            boundary_complexity += boundary_term
        f += 0.2 * boundary_complexity
        
        # Additional chaotic modulation with time-like progression
        chaotic_mod = 0.0
        for i in range(self.dim):
            chaotic_mod += np.sin(31 * x_norm[i]) * np.cos(37 * x_norm[i]) * np.sin(41 * x_norm[i]) * np.cos(43 * x_norm[i])
        f += 0.15 * chaotic_mod
        
        # Final scaling and polynomial curvature
        f *= 1.0 + 0.2 * np.sum(np.abs(x))
        f += 0.1 * np.sum(x**4) + 0.05 * np.sum(x**6)
        
        return f