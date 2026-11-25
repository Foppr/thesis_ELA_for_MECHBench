import numpy as np

class ChaoticPolynomialPenaltyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic tent map parameters
        self.tent_r = np.random.uniform(1.5, 3.9, size=dim)
        self.tent_x0 = np.random.uniform(0.1, 0.9, size=dim)
        # Polynomial chaos expansion parameters
        self.poly_degree = np.random.randint(2, 6, size=dim)
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, size=(dim, 5))
        # Dynamic penalty parameters
        self.penalty_weights = np.random.uniform(0.5, 3.0, size=dim)
        self.penalty_exponents = np.random.uniform(1.0, 4.0, size=dim)
        # Multi-scale interaction terms
        self.interaction_matrix = np.random.uniform(-2.0, 2.0, size=(dim, dim))
        # Basin-like regions with chaotic dynamics
        self.basin_centers = np.random.uniform(-4.0, 4.0, size=5)
        self.basin_radii = np.random.uniform(0.5, 2.0, size=5)
        self.basin_depths = np.random.uniform(1.0, 5.0, size=5)
        # Chaotic landscape modulation
        self.modulation_freq = np.random.uniform(0.1, 2.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component
        chaotic_component = 0.0
        for i in range(self.dim):
            # Generate chaotic sequence
            tent_val = self.tent_x0[i]
            for _ in range(10):  # Iterate to reach chaotic regime
                if tent_val < 0.5:
                    tent_val = self.tent_r[i] * tent_val
                else:
                    tent_val = self.tent_r[i] * (1 - tent_val)
            chaotic_component += tent_val
            
        # Polynomial chaos expansion component
        poly_component = 0.0
        for i in range(self.dim):
            # Evaluate polynomial using coefficients
            poly_val = 0.0
            for j in range(self.poly_degree[i]):
                poly_val += self.poly_coeffs[i, j] * (x[i] ** j)
            poly_component += poly_val
            
        # Dynamic penalty component
        penalty_component = 0.0
        for i in range(self.dim):
            # Apply dynamic penalty based on distance from boundaries
            dist_to_boundary = min(np.abs(x[i] - (-5.0)), np.abs(x[i] - 5.0))
            penalty_component += self.penalty_weights[i] * (dist_to_boundary ** self.penalty_exponents[i])
            
        # Multi-scale interaction terms
        interaction_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_component += self.interaction_matrix[i, j] * np.sin(x[i]) * np.cos(x[j])
                    
        # Basin-like regions component with chaotic modulation
        basin_component = 0.0
        for i in range(self.dim):
            min_dist = float('inf')
            for k in range(5):
                dist = np.abs(x[i] - self.basin_centers[k])
                if dist < min_dist:
                    min_dist = dist
            if min_dist <= self.basin_radii[k]:
                basin_component += self.basin_depths[k] * (1 - min_dist / self.basin_radii[k])
        
        # Chaotic modulation of the landscape
        modulation_component = 0.0
        for i in range(self.dim):
            modulation_val = np.sin(self.modulation_freq[i] * x[i]) + np.cos(self.modulation_freq[i] * x[i])
            modulation_component += modulation_val
            
        # Combined fitness function with balanced weights
        return (1.0 * chaotic_component + 
                1.5 * poly_component + 
                0.8 * penalty_component + 
                1.2 * interaction_component + 
                0.7 * basin_component + 
                0.5 * modulation_component)