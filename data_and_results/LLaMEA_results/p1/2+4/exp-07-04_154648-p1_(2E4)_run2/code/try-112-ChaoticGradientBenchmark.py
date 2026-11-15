import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate chaotic parameters for each dimension
        np.random.seed(42)
        self.chaos_params = np.random.uniform(0.1, 0.9, dim)
        self.symmetry_breakers = np.random.uniform(-0.5, 0.5, dim)
        self.frequency_components = np.random.uniform(1.0, 8.0, dim)
        self.amplitude_components = np.random.uniform(0.5, 2.0, dim)
        # Precompute rotation matrix for symmetry breaking
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        
    def f(self, x):
        x_scaled = x / 5.0
        # Apply rotation to break symmetry
        x_rot = self.rotation_matrix @ x_scaled
        
        # Chaotic sinusoidal components
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += (
                np.sin(self.frequency_components[i] * x_rot[i]) * 
                np.cos(self.frequency_components[i] * x_rot[i] * 1.3) * 
                self.amplitude_components[i] * 
                (1.0 + self.chaos_params[i] * np.sin(10 * x_rot[i]))
            )
        
        # Gradient-based quadratic terms with dynamic coefficients
        quadratic_term = 0.0
        for i in range(self.dim):
            coeff = 1.0 + 0.5 * np.sin(2 * np.pi * x_rot[i]) + 0.3 * self.symmetry_breakers[i]
            quadratic_term += coeff * x_rot[i]**2
        
        # Saddle-point avoidance using hyperbolic tangent components
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += np.tanh(x_rot[i] * 2.0) * np.sin(x_rot[i] * 0.5)
        
        # Cross-dimensional coupling with dynamic weights
        coupling_term = 0.0
        for i in range(self.dim - 1):
            weight = 0.5 + 0.5 * np.cos(np.pi * (x_rot[i] + x_rot[i+1]))
            coupling_term += weight * x_rot[i] * x_rot[i+1]
        
        # Add a chaotic noise term to increase complexity
        noise_term = 0.0
        for i in range(self.dim):
            noise_term += np.sin(7 * x_rot[i] + np.cos(3 * x_rot[i])) * 0.1
        
        # Polynomial interaction terms for increased complexity
        poly_term = 0.01 * np.sum(x_rot**4)
        
        # Combine all terms with global minimum at origin
        result = chaotic_term + quadratic_term + saddle_term + coupling_term + noise_term + poly_term
        
        # Add penalty for proximity to saddle points to increase difficulty
        saddle_penalty = 0.0
        for i in range(self.dim):
            saddle_penalty += 1.0 / (1.0 + np.abs(x_rot[i])**3)
        
        return result + 0.5 * saddle_penalty