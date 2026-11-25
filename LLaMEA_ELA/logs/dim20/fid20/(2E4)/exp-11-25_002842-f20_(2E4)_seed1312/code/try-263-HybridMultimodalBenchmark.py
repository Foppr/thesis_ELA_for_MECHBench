import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-inspired polynomial chaos coefficients
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, (dim, 15))
        # Chaotic radial basis function centers and widths
        self.rb_centers = np.random.uniform(-5.0, 5.0, (dim, 8))
        self.rb_widths = np.random.uniform(0.5, 2.0, (dim, 8))
        # Hyperbolic tangent bifurcation parameters
        self.tanh_params = np.random.uniform(0.5, 3.0, dim)
        # Adaptive coupling weights between dimensions
        self.adaptive_weights = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Fractal noise coefficients for each dimension
        self.fractal_coeffs = np.random.uniform(-0.5, 0.5, (dim, 6))
        # Dynamic scaling factors
        self.scaling_factors = np.random.uniform(0.8, 1.2, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Quantum-inspired polynomial chaos component
        for i in range(self.dim):
            poly_sum = 0.0
            for j in range(15):
                poly_sum += self.poly_coeffs[i, j] * np.polynomial.hermite.hermval(x[i], [0]*j + [1])
            result += poly_sum ** 2
            
        # Chaotic radial basis function component
        rbf_sum = 0.0
        for i in range(self.dim):
            for j in range(8):
                rbf_sum += self.rb_widths[i, j] * np.exp(-0.5 * ((x[i] - self.rb_centers[i, j]) / self.rb_widths[i, j]) ** 2)
        result += rbf_sum
        
        # Hyperbolic tangent bifurcation dynamics
        tanh_energy = 0.0
        for i in range(self.dim):
            tanh_energy += np.tanh(self.tanh_params[i] * x[i]) ** 3
            
        # Adaptive coupling with dynamic weights
        coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_energy += self.adaptive_weights[i, j] * np.sin(x[i] * x[j])
                    
        # Fractal noise component
        fractal_noise = 0.0
        for i in range(self.dim):
            noise_sum = 0.0
            for j in range(6):
                noise_sum += self.fractal_coeffs[i, j] * np.sin((x[i] ** (j + 1)) / (j + 1))
            fractal_noise += noise_sum ** 2
            
        # Combine all components with dynamic weighting
        total = 0.25 * result + 0.3 * tanh_energy + 0.2 * coupling_energy + 0.25 * fractal_noise
        
        # Apply dynamic scaling based on x values and chaotic behavior
        scale_factor = 1.0
        for i in range(self.dim):
            scale_factor *= self.scaling_factors[i] * (1.0 + 0.2 * np.sin(x[i]))
            
        total *= scale_factor
        
        return total