import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-inspired polynomial chaos expansion coefficients
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, (dim, 8))
        # Chaotic radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 30))
        self.rbf_widths = np.random.uniform(0.1, 4.0, (dim, 30))
        # Hyperbolic tangent bifurcation parameters
        self.bifurcation_params = np.random.uniform(-3.0, 3.0, dim)
        # Adaptive cross-dimensional coupling weights
        self.coupling_weights = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Fractal noise parameters
        self.fractal_amplitudes = np.random.uniform(0.05, 0.5, dim)
        self.fractal_frequencies = np.random.uniform(1.0, 10.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Quantum-inspired polynomial chaos expansion component
        for i in range(self.dim):
            poly_term = 0.0
            for j in range(8):
                poly_term += self.poly_coeffs[i, j] * (x[i] ** j)
            result += poly_term * np.sin(x[i])
            
        # Chaotic radial basis function network component
        rbf_sum = 0.0
        for i in range(self.dim):
            rbf_inner_sum = 0.0
            for j in range(30):
                distance = (x[i] - self.rbf_centers[i, j]) ** 2
                width = self.rbf_widths[i, j] ** 2
                rbf_inner_sum += np.exp(-distance / (2 * width)) * np.sin(distance)
            rbf_sum += rbf_inner_sum
            
        # Hyperbolic tangent bifurcation dynamics
        bifurcation_sum = 0.0
        for i in range(self.dim):
            # Bifurcation term with hyperbolic tangent nonlinearity
            bifurcation_term = self.bifurcation_params[i] * np.tanh(x[i] ** 3 - x[i])
            # Add fractal noise to bifurcation
            fractal_noise = 0.0
            for k in range(5):
                fractal_noise += self.fractal_amplitudes[i] * np.sin(self.fractal_frequencies[i] * x[i] * (k + 1))
            bifurcation_sum += bifurcation_term + fractal_noise
            
        # Adaptive cross-dimensional coupling
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_weights[i, j] * np.cos(x[i] * x[j])
                    
        # Combine all components with different weights
        total = 0.35 * result + 0.3 * rbf_sum + 0.25 * bifurcation_sum + 0.1 * coupling_sum
        
        # Add a global scaling factor based on the norm of x with fractal modulation
        norm_x = np.linalg.norm(x)
        fractal_modulation = 1.0 + 0.2 * np.sin(norm_x * 2.0) * np.cos(norm_x * 0.5)
        total *= (1.0 + 0.15 * fractal_modulation)
        
        return total