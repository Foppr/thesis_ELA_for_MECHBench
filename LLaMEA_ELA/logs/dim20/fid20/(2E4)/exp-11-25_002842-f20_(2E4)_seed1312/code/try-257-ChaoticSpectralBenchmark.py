import numpy as np

class ChaoticSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic tent map parameters for each dimension
        self.tent_params = np.random.uniform(1.5, 2.0, dim)
        # Spectral clustering inspired energy coefficients
        self.energy_coeffs = np.random.uniform(-1.0, 1.0, (dim, 10))
        # Fractal basin parameters
        self.fractal_dims = np.random.uniform(1.1, 2.0, dim)
        # Dynamic attractor centers
        self.attractor_centers = np.random.uniform(-5.0, 5.0, (dim, 5))
        # Coupling strengths between dimensions
        self.coupling_strengths = np.random.uniform(0.1, 1.0, (dim, dim))
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic tent map component
        for i in range(self.dim):
            # Initialize chaotic sequence
            chaotic_value = x[i]
            tent_sum = 0.0
            for _ in range(10):  # Iterate tent map 10 times
                if chaotic_value < 0.5:
                    chaotic_value = self.tent_params[i] * chaotic_value
                else:
                    chaotic_value = self.tent_params[i] * (1 - chaotic_value)
                tent_sum += chaotic_value ** 2
                
            result += tent_sum / 10.0
            
        # Spectral clustering inspired energy function
        spectral_energy = 0.0
        for i in range(self.dim):
            energy_term = 0.0
            for j in range(10):
                energy_term += self.energy_coeffs[i, j] * np.sin((x[i] ** (j + 1)) / (j + 1))
            spectral_energy += energy_term
            
        # Fractal basin boundary component
        fractal_boundary = 0.0
        for i in range(self.dim):
            # Compute distance to multiple attractor centers
            distances = np.abs(x[i] - self.attractor_centers[i, :])
            min_dist = np.min(distances)
            # Fractal scaling based on dimension
            fractal_boundary += min_dist ** self.fractal_dims[i]
            
        # Cross-dimensional coupling with dynamic weights
        coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_energy += self.coupling_strengths[i, j] * np.cos(x[i] - x[j])
                    
        # Combine all components with time-varying weights
        total = 0.3 * result + 0.4 * spectral_energy + 0.2 * fractal_boundary + 0.1 * coupling_energy
        
        # Add a dynamic scaling factor based on x norm and chaotic behavior
        norm_x = np.linalg.norm(x)
        dynamic_factor = 1.0 + 0.3 * np.sin(norm_x) * np.cos(np.sum(x))
        total *= dynamic_factor
        
        return total