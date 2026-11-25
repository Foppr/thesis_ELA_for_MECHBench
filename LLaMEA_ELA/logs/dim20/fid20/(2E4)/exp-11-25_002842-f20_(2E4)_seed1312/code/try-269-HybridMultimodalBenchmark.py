import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-inspired polynomial chaos expansion coefficients
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, (dim, 10))
        # Chaotic radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 40))
        self.rbf_widths = np.random.uniform(0.1, 5.0, (dim, 40))
        # Hyperbolic tangent bifurcation parameters
        self.bifurcation_params = np.random.uniform(-4.0, 4.0, dim)
        # Adaptive cross-dimensional coupling weights (slightly modified)
        self.coupling_weights = np.random.uniform(-2.0, 2.0, (dim, dim))
        # Fractal noise parameters
        self.fractal_amplitudes = np.random.uniform(0.05, 0.6, dim)
        self.fractal_frequencies = np.random.uniform(1.0, 12.0, dim)
        # Stochastic resonance parameters
        self.resonance_strength = np.random.uniform(0.1, 0.8, dim)
        self.resonance_frequency = np.random.uniform(0.5, 3.0, dim)
        # Memory-dependent energy terms
        self.memory_weights = np.random.uniform(-0.5, 0.5, (dim, 3))
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Quantum-inspired polynomial chaos expansion component
        for i in range(self.dim):
            poly_term = 0.0
            for j in range(10):
                poly_term += self.poly_coeffs[i, j] * (x[i] ** j)
            result += poly_term * np.sin(x[i])
            
        # Chaotic radial basis function network component
        rbf_sum = 0.0
        for i in range(self.dim):
            rbf_inner_sum = 0.0
            for j in range(40):
                distance = (x[i] - self.rbf_centers[i, j]) ** 2
                width = self.rbf_widths[i, j] ** 2
                rbf_inner_sum += np.exp(-distance / (2 * width)) * np.sin(distance)
            rbf_sum += rbf_inner_sum
            
        # Hyperbolic tangent bifurcation dynamics with stochastic resonance (enhanced nonlinearity)
        bifurcation_sum = 0.0
        for i in range(self.dim):
            # Enhanced bifurcation term with additional cubic nonlinearity
            bifurcation_term = self.bifurcation_params[i] * np.tanh(x[i] ** 3 - x[i] + 0.5 * x[i] ** 4)
            # Add stochastic resonance component
            resonance = self.resonance_strength[i] * np.sin(self.resonance_frequency[i] * x[i])
            # Add fractal noise to bifurcation
            fractal_noise = 0.0
            for k in range(7):
                fractal_noise += self.fractal_amplitudes[i] * np.sin(self.fractal_frequencies[i] * x[i] * (k + 1))
            bifurcation_sum += bifurcation_term + resonance + fractal_noise
            
        # Adaptive cross-dimensional coupling with memory effects (modified weights)
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Enhanced coupling with additional sinusoidal modulation
                    coupling_sum += self.coupling_weights[i, j] * np.cos(x[i] * x[j]) * np.sin(0.5 * (x[i] + x[j]))
        
        # Memory-dependent energy terms
        memory_sum = 0.0
        for i in range(self.dim):
            memory_term = 0.0
            for k in range(3):
                memory_term += self.memory_weights[i, k] * np.sin((k + 1) * x[i])
            memory_sum += memory_term
            
        # Combine all components with different weights
        total = 0.3 * result + 0.25 * rbf_sum + 0.25 * bifurcation_sum + 0.15 * coupling_sum + 0.1 * memory_sum
        
        # Add a global scaling factor based on the norm of x with fractal modulation
        norm_x = np.linalg.norm(x)
        fractal_modulation = 1.0 + 0.3 * np.sin(norm_x * 2.0) * np.cos(norm_x * 0.5)
        total *= (1.0 + 0.2 * fractal_modulation)
        
        return total