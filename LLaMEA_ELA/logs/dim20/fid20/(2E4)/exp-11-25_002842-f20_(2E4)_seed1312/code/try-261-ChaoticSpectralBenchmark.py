import numpy as np

class ChaoticSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic logistic map parameters for each dimension
        self.logistic_params = np.random.uniform(3.5, 4.0, dim)
        # Spectral clustering inspired energy coefficients
        self.energy_coeffs = np.random.uniform(-1.0, 1.0, (dim, 10))
        # Fractal basin parameters
        self.fractal_dims = np.random.uniform(1.2, 1.8, dim)
        # Dynamic attractor centers
        self.attractor_centers = np.random.uniform(-5.0, 5.0, (dim, 5))
        # Coupling strengths between dimensions with directional bias
        self.coupling_strengths = np.random.uniform(0.05, 0.8, (dim, dim))
        # Adaptive scaling factors
        self.scaling_factors = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic logistic map component
        for i in range(self.dim):
            # Initialize chaotic sequence
            logistic_value = x[i]
            logistic_sum = 0.0
            for _ in range(15):  # Iterate logistic map 15 times for more complexity
                logistic_value = self.logistic_params[i] * logistic_value * (1 - logistic_value)
                logistic_sum += np.sin(logistic_value) ** 2
                
            result += logistic_sum / 15.0
            
        # Spectral clustering inspired energy function with polynomial terms
        spectral_energy = 0.0
        for i in range(self.dim):
            energy_term = 0.0
            for j in range(10):
                energy_term += self.energy_coeffs[i, j] * np.sin((x[i] ** (j + 1)) / (j + 1))
            spectral_energy += energy_term
            
        # Fractal basin boundary component with modified distance metric
        fractal_boundary = 0.0
        for i in range(self.dim):
            # Compute weighted distances to multiple attractor centers
            distances = np.abs(x[i] - self.attractor_centers[i, :])
            # Use inverse distance weighting
            weights = 1.0 / (distances + 1e-8)
            weighted_dist = np.sum(weights * distances) / np.sum(weights)
            # Fractal scaling based on dimension
            fractal_boundary += weighted_dist ** self.fractal_dims[i]
            
        # Cross-dimensional coupling with non-linear interaction terms
        coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Non-linear coupling with adaptive strength
                    coupling_term = self.coupling_strengths[i, j] * np.sin(x[i] - x[j]) * np.cos(x[i] + x[j])
                    coupling_energy += coupling_term
                    
        # Combine all components with modified weights
        total = 0.25 * result + 0.35 * spectral_energy + 0.25 * fractal_boundary + 0.15 * coupling_energy
        
        # Add adaptive scaling based on dimension and input values
        adaptive_scaling = np.prod(np.abs(x) + 1.0)
        total *= (1.0 + 0.2 * np.sin(adaptive_scaling))
        
        # Add a dynamic penalty term to improve convergence behavior
        norm_x = np.linalg.norm(x)
        penalty = 0.1 * norm_x ** 2 * np.exp(-norm_x / 5.0)
        total += penalty
        
        return total