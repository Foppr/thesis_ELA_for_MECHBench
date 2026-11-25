import numpy as np

class ChaoticPolynomialPenaltyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic tent map parameters with increased complexity
        self.tent_r = np.random.uniform(1.5, 3.9, size=dim)
        self.tent_x0 = np.random.uniform(0.1, 0.9, size=dim)
        # Polynomial chaos expansion parameters with higher degrees
        self.poly_degree = np.random.randint(3, 8, size=dim)
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, size=(dim, 8))
        # Dynamic penalty parameters with adaptive scaling
        self.penalty_weights = np.random.uniform(1.0, 5.0, size=dim)
        self.penalty_exponents = np.random.uniform(2.0, 6.0, size=dim)
        # Multi-scale interaction terms with enhanced complexity
        self.interaction_matrix = np.random.uniform(-3.0, 3.0, size=(dim, dim))
        # Basin-like regions with multiple nested structures
        self.basin_centers = np.random.uniform(-4.5, 4.5, size=8)
        self.basin_radii = np.random.uniform(0.3, 2.5, size=8)
        self.basin_depths = np.random.uniform(0.5, 6.0, size=8)
        # Chaotic landscape modulation with frequency modulation
        self.modulation_freq = np.random.uniform(0.05, 3.0, size=dim)
        # Additional gradient-based modulation components
        self.gradient_weights = np.random.uniform(0.1, 2.0, size=dim)
        self.gradient_exponents = np.random.uniform(1.5, 4.5, size=dim)
        # Additional chaotic feedback loops for dynamic behavior
        self.feedback_coeff = np.random.uniform(-0.5, 0.5, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component with feedback
        chaotic_component = 0.0
        for i in range(self.dim):
            # Generate chaotic sequence with feedback
            tent_val = self.tent_x0[i]
            for _ in range(15):  # Iterate longer to reach chaotic regime
                if tent_val < 0.5:
                    tent_val = self.tent_r[i] * tent_val
                else:
                    tent_val = self.tent_r[i] * (1 - tent_val)
            # Add feedback component
            tent_val += self.feedback_coeff[i] * np.sin(x[i])
            chaotic_component += tent_val
            
        # Polynomial chaos expansion component with higher order terms
        poly_component = 0.0
        for i in range(self.dim):
            # Evaluate polynomial using coefficients with higher degrees
            poly_val = 0.0
            for j in range(self.poly_degree[i]):
                poly_val += self.poly_coeffs[i, j] * (x[i] ** j)
            poly_component += poly_val
            
        # Dynamic penalty component with adaptive scaling
        penalty_component = 0.0
        for i in range(self.dim):
            # Apply dynamic penalty based on distance from boundaries
            dist_to_boundary = min(np.abs(x[i] - (-5.0)), np.abs(x[i] - 5.0))
            penalty_component += self.penalty_weights[i] * (dist_to_boundary ** self.penalty_exponents[i])
            
        # Multi-scale interaction terms with enhanced complexity
        interaction_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_component += self.interaction_matrix[i, j] * np.sin(x[i]) * np.cos(x[j])
                    
        # Basin-like regions component with nested structures
        basin_component = 0.0
        for i in range(self.dim):
            min_dist = float('inf')
            for k in range(8):  # Increased number of basins
                dist = np.abs(x[i] - self.basin_centers[k])
                if dist < min_dist:
                    min_dist = dist
            if min_dist <= self.basin_radii[k]:
                basin_component += self.basin_depths[k] * (1 - min_dist / self.basin_radii[k])
        
        # Chaotic modulation of the landscape with gradient enhancement
        modulation_component = 0.0
        for i in range(self.dim):
            modulation_val = np.sin(self.modulation_freq[i] * x[i]) + np.cos(self.modulation_freq[i] * x[i])
            # Add gradient-based modulation
            grad_mod = self.gradient_weights[i] * (np.sin(x[i]) ** self.gradient_exponents[i])
            modulation_component += modulation_val + grad_mod
            
        # Combined fitness function with balanced weights
        return (1.5 * chaotic_component + 
                2.0 * poly_component + 
                1.0 * penalty_component + 
                1.5 * interaction_component + 
                1.0 * basin_component + 
                0.8 * modulation_component)