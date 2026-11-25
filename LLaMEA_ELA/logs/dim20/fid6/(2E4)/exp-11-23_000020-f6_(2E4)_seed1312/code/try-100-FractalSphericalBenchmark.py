import numpy as np

class FractalSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-inspired harmonic coefficients
        self.quantum_coeffs = np.random.randn(dim, 3)
        # Hyperbolic tangent chaotic parameters
        self.tanh_params = np.random.rand(dim) * 3.0 + 2.0
        # Quaternion-based radial coupling
        self.quat_weights = np.random.randn(dim, 4)
        # Dynamic condition number variation
        self.condition_factors = np.random.rand(dim) * 4.0 + 2.0
        # Fractal Brownian motion parameters
        self.hurst = 0.3 + 0.4 * np.random.rand()
        self.fractal_dim = 2.0 + 2.0 * np.random.rand()
        # Stochastic perturbations
        self.perturbation_scale = 0.15 + 0.25 * np.random.rand()
        self.perturbation_freq = 1.5 + 3.0 * np.random.rand()
        # Cross-dimensional interaction terms
        self.cross_dim_weights = np.random.randn(dim, dim) * 0.7
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Quantum-inspired harmonic component with modified frequencies
        quantum_harm = 0.0
        for i in range(self.dim):
            for l in range(1, 4):
                quantum_harm += self.quantum_coeffs[i, l-1] * np.sin(l * x_norm[i]) * np.exp(-l * x_norm[i]**2)
        
        # Hyperbolic tangent chaotic component with enhanced nonlinearity
        tanh_chaos = 0.0
        for i in range(self.dim):
            tanh_chaos += np.tanh(self.tanh_params[i] * x_norm[i]) * np.sin(15 * x_norm[i])
            
        # Quaternion-based radial coupling with modified normalization
        quat_radial = 0.0
        for i in range(self.dim):
            # Normalize quaternion weights with squared norm
            quat_norm = np.linalg.norm(self.quat_weights[i])**2
            if quat_norm > 0:
                normalized_weights = self.quat_weights[i] / quat_norm
                quat_radial += np.sum(normalized_weights * np.sin(x_norm[i] * np.arange(4)))
        
        # Fractal Brownian motion component with enhanced scaling
        fbm = 0.0
        for i in range(self.dim):
            scale = 1.0
            for _ in range(8):
                fbm += scale * np.cos(x_norm[i] * (2**_)) * np.exp(-scale)
                scale *= self.hurst
        
        # Dynamic condition number scaling with polynomial terms
        cond_scaled = 0.0
        for i in range(self.dim):
            cond_scaled += x_norm[i]**3 * self.condition_factors[i]
            
        # Multi-scale polynomial with radial basis coupling and enhanced interaction
        poly_radial = 0.0
        for i in range(self.dim):
            poly_radial += (x_norm[i]**6 + 0.5 * x_norm[i]**5 + 0.3 * x_norm[i]**4 + 
                           0.15 * x_norm[i]**3 + 0.1 * x_norm[i] * x_norm[(i+1) % self.dim] * np.exp(-x_norm[i]**2))
        
        # Cross-dimensional interaction terms with enhanced coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_interaction += self.cross_dim_weights[i, j] * x_norm[i] * x_norm[j] * np.cos(x_norm[i] - x_norm[j])
        
        # Stochastic perturbations with enhanced frequency
        stochastic_pert = 0.0
        for i in range(self.dim):
            stochastic_pert += self.perturbation_scale * np.sin(self.perturbation_freq * x_norm[i]) * np.random.randn()
        
        # Combined landscape with improved weighting and enhanced multimodality
        return (0.25 * quantum_harm + 0.3 * tanh_chaos + 0.18 * quat_radial + 
                0.12 * fbm + 0.08 * cond_scaled + 0.06 * poly_radial + 
                0.04 * cross_interaction + 0.03 * stochastic_pert + 1.2)