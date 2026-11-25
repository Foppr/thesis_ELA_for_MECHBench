import numpy as np

class TentChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Tent map chaotic parameters with varying control values
        self.tent_params = np.random.uniform(1.1, 1.9, dim)
        # Trigonometric coupling coefficients with dynamic phase shifts
        self.coupling_coeffs = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Dynamic penalty weights with time-varying exponents
        self.penalty_weights = np.random.uniform(0.5, 2.0, dim)
        # Multi-scale frequency components for complex oscillatory behavior
        self.freq_components = np.random.uniform(0.5, 5.0, dim)
        # Basins of attraction with clustered positions and varying radii
        self.basins = np.random.uniform(-5.0, 5.0, (dim, 8))
        self.basin_radii = np.random.uniform(0.5, 2.0, 8)
        # Nonlinear interaction terms with sparse connectivity
        self.interaction_terms = np.random.uniform(-0.3, 0.3, (dim, dim))
        
    def tent_map(self, x, param):
        """Tent map function for chaotic dynamics"""
        return np.where(x < 0.5, param * x, param * (1 - x))
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Tent map chaotic component
        for i in range(self.dim):
            tent_val = self.tent_map(x[i], self.tent_params[i])
            result += tent_val ** 2
            
        # Trigonometric coupling between dimensions
        coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_energy += self.coupling_coeffs[i, j] * np.sin(x[i] + x[j])
                    
        # Dynamic penalty landscape with varying exponents
        penalty_energy = 0.0
        for i in range(self.dim):
            dist_from_center = np.abs(x[i])
            penalty_energy += self.penalty_weights[i] * (dist_from_center - 3.0) ** 4
            
        # Multi-scale oscillatory behavior
        oscillation_energy = 0.0
        for i in range(self.dim):
            osc_term = np.sin(self.freq_components[i] * x[i])
            osc_term += 0.7 * np.sin(2 * self.freq_components[i] * x[i])
            osc_term += 0.3 * np.sin(3 * self.freq_components[i] * x[i])
            oscillation_energy += osc_term ** 2
            
        # Basin attraction forces
        basin_energy = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x[i] - self.basins[i, :]))
            basin_energy += min_dist ** 2
            
        # Sparse nonlinear interactions
        interaction_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j and np.random.rand() > 0.7:
                    interaction_energy += self.interaction_terms[i, j] * x[i] ** 2 * x[j]
                    
        # Combine all components with carefully balanced weights
        total = 0.3 * result + 0.25 * coupling_energy + 0.15 * penalty_energy + 0.15 * oscillation_energy + 0.1 * basin_energy + 0.05 * interaction_energy
        
        return total