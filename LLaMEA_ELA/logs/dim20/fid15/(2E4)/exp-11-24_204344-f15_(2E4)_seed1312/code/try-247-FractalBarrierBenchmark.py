import numpy as np

class FractalBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Fractal geometric component with self-similarity
        fractal_term = 0.0
        for i in range(self.dim):
            # Create fractal-like pattern using recursive scaling
            scale = 1.0 + 0.5 * np.sin(i * 0.3) + 0.3 * np.cos(i * 0.7)
            pos = x[i] * scale
            # Nested sinusoidal patterns at different scales
            fractal_term += (np.sin(pos) + 0.5 * np.sin(2 * pos) + 0.3 * np.sin(4 * pos)) ** 2
        
        # Logarithmic barrier component with multiple local minima
        barrier_term = 0.0
        for i in range(self.dim):
            # Create logarithmic barriers around specific points
            barrier_points = [-3.0, -1.0, 1.0, 3.0]
            local_barrier = 0.0
            for point in barrier_points:
                # Logarithmic barrier function
                dist = np.abs(x[i] - point)
                if dist < 0.1:
                    local_barrier += 100.0  # High penalty for being too close
                else:
                    local_barrier += 1.0 / (dist + 0.1)  # Logarithmic decay
            barrier_term += local_barrier
        
        # Deterministic chaos component with exponential coupling
        chaos_term = 0.0
        for i in range(self.dim):
            # Exponential coupling between dimensions
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_sum += np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(x[i] + x[j])
            chaos_term += coupling_sum
        
        # Multi-scale oscillation with varying frequencies
        oscillation_term = 0.0
        for i in range(self.dim):
            freq_base = 1.0 + 0.5 * np.sin(i * 0.4)
            scale_factor = 1.0 + 0.3 * np.cos(i * 0.6)
            # Combine multiple oscillation frequencies
            oscillation_term += (np.sin(freq_base * x[i]) + 
                               0.7 * np.sin(2 * freq_base * x[i]) + 
                               0.3 * np.sin(4 * freq_base * x[i])) ** 2
        
        # Nested optimization wells with varying depths
        well_term = 0.0
        for i in range(self.dim):
            # Multiple nested wells with different characteristics
            well1 = (x[i] - 2.0)**2 * np.exp(-0.5 * (x[i] - 2.0)**2)
            well2 = (x[i] + 1.5)**4 * np.exp(-0.3 * (x[i] + 1.5)**2)
            well3 = x[i]**6 * np.exp(-0.1 * x[i]**2)
            well_term += 0.5 * well1 + 0.3 * well2 + 0.2 * well3
        
        # Condition number variation across dimensions
        condition_term = 0.0
        for i in range(self.dim):
            # Varying condition numbers for each dimension
            cond_factor = 1.0 + 2.0 * np.sin(i * 0.5)
            condition_term += cond_factor * x[i]**2
        
        # Final weighted combination
        total = (0.3 * fractal_term + 
                0.25 * barrier_term + 
                0.2 * chaos_term + 
                0.15 * oscillation_term + 
                0.08 * well_term + 
                0.02 * condition_term)
        
        # Global scaling factor based on dimensionality
        global_scale = 1.0 + 0.1 * np.sin(self.dim * 0.3) * np.cos(self.dim * 0.2)
        
        return total * global_scale