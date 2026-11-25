import numpy as np

class FractalSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-inspired harmonic coefficients
        self.quantum_coeffs = np.random.randn(dim, 3)
        # Hyperbolic tangent chaotic parameters
        self.tanh_params = np.random.rand(dim) * 2.0 + 1.0
        # Quaternion-based radial coupling
        self.quat_weights = np.random.randn(dim, 4)
        # Dynamic condition number variation
        self.condition_factors = np.random.rand(dim) * 3.0 + 1.0
        # Fractal Brownian motion parameters
        self.hurst = 0.2 + 0.3 * np.random.rand()
        self.fractal_dim = 1.5 + 1.5 * np.random.rand()
        # Stochastic perturbations
        self.perturbation_scale = 0.1 + 0.2 * np.random.rand()
        self.perturbation_freq = 1.0 + 2.0 * np.random.rand()
        # Cross-dimensional interaction terms
        self.cross_dim_weights = np.random.randn(dim, dim) * 0.5
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Quantum-inspired harmonic component
        quantum_harm = 0.0
        for i in range(self.dim):
            for l in range(1, 4):
                quantum_harm += self.quantum_coeffs[i, l-1] * np.sin(l * x_norm[i]) * np.exp(-l * x_norm[i]**2)
        
        # Hyperbolic tangent chaotic component
        tanh_chaos = 0.0
        for i in range(self.dim):
            tanh_chaos += np.tanh(self.tanh_params[i] * x_norm[i]) * np.sin(10 * x_norm[i])
            
        # Quaternion-based radial coupling
        quat_radial = 0.0
        for i in range(self.dim):
            # Normalize quaternion weights
            quat_norm = np.linalg.norm(self.quat_weights[i])
            if quat_norm > 0:
                normalized_weights = self.quat_weights[i] / quat_norm
                quat_radial += np.sum(normalized_weights * np.sin(x_norm[i] * np.arange(4)))
        
        # Fractal Brownian motion component with dynamic scaling
        fbm = 0.0
        for i in range(self.dim):
            scale = 1.0
            for _ in range(6):
                fbm += scale * np.cos(x_norm[i] * (2**_)) * np.exp(-scale)
                scale *= self.hurst
        
        # Dynamic condition number scaling
        cond_scaled = 0.0
        for i in range(self.dim):
            cond_scaled += x_norm[i]**2 * self.condition_factors[i]
            
        # Multi-scale polynomial with radial basis coupling
        poly_radial = 0.0
        for i in range(self.dim):
            poly_radial += (x_norm[i]**5 + 0.4 * x_norm[i]**4 + 0.2 * x_norm[i]**3 + 
                           0.1 * x_norm[i] * x_norm[(i+1) % self.dim] * np.exp(-x_norm[i]**2))
        
        # Cross-dimensional interaction terms
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_interaction += self.cross_dim_weights[i, j] * x_norm[i] * x_norm[j]
        
        # Stochastic perturbations
        stochastic_pert = 0.0
        for i in range(self.dim):
            stochastic_pert += self.perturbation_scale * np.sin(self.perturbation_freq * x_norm[i]) * np.random.randn()
        
        # Combined landscape with enhanced multimodality and conditioning
        return (0.3 * quantum_harm + 0.25 * tanh_chaos + 0.2 * quat_radial + 
                0.15 * fbm + 0.05 * cond_scaled + 0.05 * poly_radial + 
                0.03 * cross_interaction + 0.02 * stochastic_pert + 1.5)