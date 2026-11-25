import numpy as np

class ChaoticRadialModulationBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Radial component with chaotic sinusoidal modulations
        r = np.sqrt(np.sum(x**2))
        radial_term = r * (1.0 + 0.5 * np.sin(3.0 * r) * np.cos(7.0 * r))
        
        # Angular components with adaptive conditioning
        angular_sum = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x[i], x[(i+1) % self.dim]) if self.dim > 1 else 0.0
            # Adaptive conditioning based on position
            cond_factor = 1.0 + 0.3 * np.sin(x[i] * 2.0)
            angular_sum += cond_factor * np.sin(5.0 * angle + x[i]) * np.cos(3.0 * angle - x[i])
        
        # Multi-scale chaotic modulation
        chaos_mod = 0.0
        for i in range(self.dim):
            # Different frequencies and phases for each dimension
            freq1 = 2.0 + 0.5 * np.sin(i)
            freq2 = 3.0 + 0.7 * np.cos(i)
            chaos_mod += (np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) + 
                         0.8 * np.sin(freq2 * x[i]) * np.cos(freq1 * x[i]))
        
        # Cross-dimensional interaction with radial coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Radial coupling with dimension-specific weights
                weight = 0.5 + 0.5 * np.sin((i+j) * 0.3)
                cross_term += weight * x[i] * x[j] * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Basin structure with multiple local minima
        basin_term = 0.0
        for i in range(self.dim):
            # Multiple asymmetric wells
            well1 = (x[i] - 2.0)**2 * (x[i] + 2.0)**2
            well2 = (x[i] - 1.0)**4 + (x[i] + 1.0)**4
            basin_term += well1 + 0.5 * well2
        
        # Combine all components with dynamic weighting
        total = 0.3 * radial_term + 0.4 * angular_sum + 0.2 * chaos_mod + 0.05 * cross_term + 0.05 * basin_term
        
        # Global scaling and noise addition for increased complexity
        scaling = 1.0 + 0.2 * np.sin(self.dim)
        noise = 0.05 * np.sum(np.random.rand(self.dim) * x**2)
        
        return total * scaling + noise