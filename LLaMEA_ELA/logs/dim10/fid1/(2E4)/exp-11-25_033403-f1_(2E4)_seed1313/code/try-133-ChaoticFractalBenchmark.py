import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension
        self.chaos_params = np.random.uniform(3.5, 4.0, dim)
        self.fractal_dims = np.random.uniform(1.1, 2.9, dim)
        self.bifurcation_points = np.random.uniform(-3.0, 3.0, dim)
        self.saddle_weights = np.random.uniform(0.5, 2.0, dim)
        self.scale_factors = np.random.uniform(0.8, 1.5, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic dynamical component with logistic map
        chaotic_term = 0.0
        for i in range(self.dim):
            # Initialize chaotic sequence
            z = 0.5
            chaos_sum = 0.0
            for _ in range(20):  # Iterate to reach chaotic regime
                z = self.chaos_params[i] * z * (1 - z)
                if _ > 5:  # Only consider later iterations
                    chaos_sum += np.sin(z * x[i])
            chaotic_term += chaos_sum / 15.0
            
        # Fractal dimension modulation component
        fractal_term = 0.0
        for i in range(self.dim):
            # Multi-scale fractal structure using fractional Brownian motion approximation
            scale = self.fractal_dims[i]
            fractal_val = np.sin(x[i] ** scale) * np.cos(x[i] ** (scale - 0.5))
            fractal_term += fractal_val
            
        # Saddle-node bifurcation landscape
        saddle_term = 0.0
        for i in range(self.dim):
            # Create saddle points with varying strength
            bif_point = self.bifurcation_points[i]
            saddle_val = (x[i] - bif_point) ** 2 * np.exp(-0.5 * (x[i] - bif_point)**2)
            # Add negative contribution to create saddle structure
            saddle_term += self.saddle_weights[i] * saddle_val
            
        # Multi-scale interaction term with cross-dimension coupling
        multi_scale_term = 0.0
        for i in range(self.dim):
            # Interaction with neighboring dimensions
            neighbor_interaction = 0.0
            for j in range(i+1, min(i+4, self.dim)):  # Limited range for non-separability
                dist = np.abs(x[i] - x[j])
                interaction = np.exp(-dist * self.scale_factors[i]) * np.sin(dist)
                neighbor_interaction += interaction
            
            multi_scale_term += (x[i]**3 + neighbor_interaction) * np.cos(0.1 * x[i])
            
        # Combined fitness with adaptive weights
        total = 0.8 * chaotic_term + 0.6 * fractal_term + 0.7 * saddle_term + 0.9 * multi_scale_term
        
        return total