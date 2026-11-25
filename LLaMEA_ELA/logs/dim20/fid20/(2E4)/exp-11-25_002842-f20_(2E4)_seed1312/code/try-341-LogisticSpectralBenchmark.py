import numpy as np

class LogisticSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Logistic map chaotic parameters with varying control values
        self.logistic_params = np.random.uniform(3.5, 4.0, dim)
        # Spectral frequency couplings with dynamic phase shifts
        self.spectral_coeffs = np.random.uniform(-0.8, 0.8, (dim, dim))
        # Adaptive penalty weights with dynamic scaling factors
        self.penalty_weights = np.random.uniform(0.1, 1.5, dim)
        # Multi-frequency spectral components for complex oscillatory behavior
        self.spectral_freqs = np.random.uniform(1.0, 10.0, dim)
        # Basins of attraction with clustered positions and varying radii
        self.basins = np.random.uniform(-5.0, 5.0, (dim, 6))
        self.basin_radii = np.random.uniform(0.3, 1.5, 6)
        # Nonlinear interaction terms with sparse connectivity
        self.interaction_terms = np.random.uniform(-0.2, 0.2, (dim, dim))
        
    def logistic_map(self, x, param):
        """Logistic map function for chaotic dynamics"""
        return param * x * (1 - x)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Logistic map chaotic component
        for i in range(self.dim):
            logistic_val = self.logistic_map(x[i], self.logistic_params[i])
            result += logistic_val ** 2
            
        # Spectral frequency coupling between dimensions
        spectral_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    spectral_energy += self.spectral_coeffs[i, j] * np.cos(self.spectral_freqs[i] * x[i] + self.spectral_freqs[j] * x[j])
                    
        # Adaptive penalty landscape with dynamic scaling
        penalty_energy = 0.0
        for i in range(self.dim):
            dist_from_center = np.abs(x[i])
            penalty_energy += self.penalty_weights[i] * (dist_from_center - 2.5) ** 3
            
        # Multi-frequency spectral oscillatory behavior
        spectral_energy_2 = 0.0
        for i in range(self.dim):
            spec_term = np.cos(self.spectral_freqs[i] * x[i])
            spec_term += 0.6 * np.cos(2 * self.spectral_freqs[i] * x[i])
            spec_term += 0.3 * np.cos(3 * self.spectral_freqs[i] * x[i])
            spectral_energy_2 += spec_term ** 2
            
        # Basin attraction forces
        basin_energy = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x[i] - self.basins[i, :]))
            basin_energy += min_dist ** 2
            
        # Sparse nonlinear interactions
        interaction_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j and np.random.rand() > 0.8:
                    interaction_energy += self.interaction_terms[i, j] * x[i] ** 3 * x[j]
                    
        # Combine all components with carefully balanced weights
        total = 0.25 * result + 0.2 * spectral_energy + 0.15 * penalty_energy + 0.2 * spectral_energy_2 + 0.1 * basin_energy + 0.1 * interaction_energy
        
        return total