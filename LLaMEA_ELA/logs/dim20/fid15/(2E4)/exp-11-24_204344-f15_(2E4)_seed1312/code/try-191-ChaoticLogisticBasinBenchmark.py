import numpy as np

class ChaoticLogisticBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize logistic map parameters
        self.r_min = 3.5
        self.r_max = 4.0
        self.alpha = 0.1
        self.beta = 0.05
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize input to [0, 1] for logistic map
        x_norm = (x + 5.0) / 10.0
        
        # Initialize chaotic dynamics
        chaos_energy = 0.0
        logistic_values = np.zeros(self.dim)
        
        # Coupled logistic maps with time-varying parameters
        for i in range(self.dim):
            r = self.r_min + (self.r_max - self.r_min) * x_norm[i]
            x_prev = x_norm[i]
            
            # Run logistic map for several iterations to reach chaotic state
            for _ in range(10):
                x_prev = r * x_prev * (1.0 - x_prev)
            
            logistic_values[i] = x_prev
            
        # Dynamic basin energy wells with position-dependent shifts
        basin_energy = 0.0
        for i in range(self.dim):
            # Position-dependent well depth and shift
            well_depth = 2.0 + 0.5 * np.sin(x[i] * 0.5)
            well_shift = 0.3 * np.cos(x[i] * 0.3)
            
            # Basin energy contribution
            basin_energy += well_depth * (logistic_values[i] - well_shift)**2
        
        # Cross-dimensional coupling with dynamic interaction strength
        cross_energy = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Dynamic coupling strength based on population density
                density_factor = np.exp(-0.5 * (x[i]**2 + x[j]**2) / 2.0)
                coupling_strength = 1.0 + 0.3 * density_factor
                
                cross_energy += coupling_strength * (logistic_values[i] - logistic_values[j])**2
        
        # Time-varying chaotic modulation
        time_modulation = 0.0
        for i in range(self.dim):
            # Add dynamic modulation based on neighbor positions
            if i > 0:
                mod = np.sin(x[i-1] * x[i] * 0.1)
                time_modulation += mod
            
        # Combine all energy components
        total_energy = 0.5 * basin_energy + 0.3 * cross_energy + 0.2 * time_modulation
        
        # Add dimensionality scaling and global noise
        scaling = 1.0 + 0.05 * self.dim
        noise = 0.01 * np.sum(np.sin(x * 10.0))
        
        return total_energy * scaling + noise