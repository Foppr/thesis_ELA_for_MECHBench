import numpy as np

class FractalPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Polynomial coefficients for each dimension
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, (dim, 6))
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 15))
        self.rbf_widths = np.random.uniform(0.5, 3.0, (15,))
        # Fractal noise parameters
        self.fractal_params = np.random.uniform(0.1, 2.0, dim)
        # Dynamic conditioning factors that vary with dimension
        self.conditioning_factors = np.random.uniform(0.5, 5.0, dim)
        # Multiplier for polynomial terms
        self.poly_multipliers = np.random.uniform(0.5, 3.0, dim)
        # Local minima positions with varying density
        self.minima_positions = np.random.uniform(-5.0, 5.0, (dim, 10))
        # Coupling coefficients between dimensions
        self.coupling_coeffs = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Exponent parameters for fractal components
        self.fractal_exponents = np.random.uniform(0.3, 1.8, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Polynomial chaos expansion component
        for i in range(self.dim):
            poly_val = 0.0
            for j in range(6):
                poly_val += self.poly_coeffs[i, j] * (x[i] ** j)
            result += self.poly_multipliers[i] * (poly_val ** 2) * np.sin(x[i])
            
        # Radial basis function component with dynamic scaling
        rbf_sum = 0.0
        for j in range(15):
            dist = np.sum((x - self.rbf_centers[:, j]) ** 2)
            rbf_sum += np.exp(-dist / (2 * self.rbf_widths[j] ** 2))
        result += 0.5 * rbf_sum
        
        # Fractal noise component with dynamic parameters
        fractal_noise = 0.0
        for i in range(self.dim):
            noise_val = 0.0
            for k in range(1, 6):
                freq = 2 ** k
                amp = 1.0 / (freq ** self.fractal_exponents[i])
                noise_val += amp * np.sin(freq * x[i] * self.fractal_params[i])
            fractal_noise += noise_val ** 2
        result += 0.3 * fractal_noise
        
        # Coupling between dimensions with varying strength
        coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_energy += self.coupling_coeffs[i, j] * np.sin(x[i]) * np.cos(x[j])
        result += 0.2 * coupling_energy
        
        # Conditioning and local minima attraction
        conditioning_energy = 0.0
        for i in range(self.dim):
            conditioning_energy += self.conditioning_factors[i] * (x[i] ** 4) * np.cos(x[i])
            
        local_energy = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x[i] - self.minima_positions[i, :]))
            local_energy += min_dist ** 3
            
        # Combine all components
        total = result + 0.1 * conditioning_energy + 0.15 * local_energy
        
        return total