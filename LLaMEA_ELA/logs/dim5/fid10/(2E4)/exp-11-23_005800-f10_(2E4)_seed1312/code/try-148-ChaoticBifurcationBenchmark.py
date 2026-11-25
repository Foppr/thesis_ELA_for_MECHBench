import numpy as np

class ChaoticBifurcationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.time = 0.0
        self.coupling_strength = 0.5
        self.bifurcation_range = np.random.uniform(3.5, 4.0, dim)
        self.initial_conditions = np.random.uniform(0.1, 0.9, dim)
        self.damping_factor = np.random.uniform(0.8, 0.99, dim)
        self.saddle_node_shift = np.random.uniform(-0.5, 0.5, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        self.time += 0.01
        
        # Initialize logistic map dynamics
        logistic_values = self.initial_conditions.copy()
        total_energy = 0.0
        
        # Time-varying bifurcation parameters
        varying_params = self.bifurcation_range + 0.2 * np.sin(self.time * 0.5)
        
        for i in range(self.dim):
            # Apply logistic map with varying parameter
            r = varying_params[i]
            x_i = x[i]
            
            # Saddle-node bifurcation effect
            bifurcation_shift = self.saddle_node_shift[i] * np.sin(self.time + i)
            shifted_r = r + bifurcation_shift
            
            # Logistic map iteration with chaotic dynamics
            for _ in range(10):  # Discard initial transient
                logistic_values[i] = shifted_r * logistic_values[i] * (1 - logistic_values[i])
            
            # Add chaotic energy contribution
            energy = logistic_values[i]**2 + x_i**2
            total_energy += energy
            
        # Coupling between dimensions
        coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = self.coupling_strength * np.sin(logistic_values[i] - logistic_values[j])
                coupling_energy += coupling**2
        
        # Add damping effect over time
        damping = np.prod(self.damping_factor)
        
        # Combine all components with time modulation
        result = total_energy * damping + coupling_energy * 0.5
        
        # Add periodic noise for additional complexity
        noise = 0.01 * np.sin(self.time * 3.0) * np.cos(self.time * 2.0)
        
        return result + noise