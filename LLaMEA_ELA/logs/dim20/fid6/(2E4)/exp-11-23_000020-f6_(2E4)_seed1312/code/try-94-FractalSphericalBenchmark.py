import numpy as np

class FractalSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-inspired harmonic coefficients with modified frequencies
        self.quantum_coeffs = np.random.randn(dim, 3)
        # Hyperbolic tangent chaotic parameters with altered scaling
        self.tanh_params = np.random.rand(dim) * 3.0 + 2.0
        # Quaternion-based radial coupling with increased complexity
        self.quat_weights = np.random.randn(dim, 4)
        # Dynamic condition number variation with higher contrast
        self.condition_factors = np.random.rand(dim) * 5.0 + 2.0
        # Fractal Brownian motion parameters
        self.hurst = 0.3 + 0.2 * np.random.rand()
        self.fractal_dim = 2.0 + 1.0 * np.random.rand()
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Quantum-inspired harmonic component with modified frequencies
        quantum_harm = 0.0
        for i in range(self.dim):
            for l in range(2, 6):  # Changed from 1 to 2, and 4 to 6
                quantum_harm += self.quantum_coeffs[i, l-2] * np.sin(l * x_norm[i]) * np.exp(-l * x_norm[i]**2)
        
        # Hyperbolic tangent chaotic component with altered interaction
        tanh_chaos = 0.0
        for i in range(self.dim):
            tanh_chaos += np.tanh(self.tanh_params[i] * x_norm[i]) * np.sin(15 * x_norm[i])  # Increased frequency
            
        # Quaternion-based radial coupling with enhanced nonlinearity
        quat_radial = 0.0
        for i in range(self.dim):
            # Normalize quaternion weights
            quat_norm = np.linalg.norm(self.quat_weights[i])
            if quat_norm > 0:
                normalized_weights = self.quat_weights[i] / quat_norm
                quat_radial += np.sum(normalized_weights * np.sin(x_norm[i] * np.arange(1, 5)))  # Changed range from 0-3 to 1-4
        
        # Fractal Brownian motion component with dynamic scaling
        fbm = 0.0
        for i in range(self.dim):
            scale = 1.0
            for _ in range(5):  # Reduced iterations
                fbm += scale * np.cos(x_norm[i] * (2**_)) * np.exp(-scale)
                scale *= self.hurst
        
        # Dynamic condition number scaling with enhanced variation
        cond_scaled = 0.0
        for i in range(self.dim):
            cond_scaled += x_norm[i]**3 * self.condition_factors[i]  # Changed from x^2 to x^3
            
        # Multi-scale polynomial with radial basis coupling and additional interaction
        poly_radial = 0.0
        for i in range(self.dim):
            poly_radial += (x_norm[i]**6 + 0.5 * x_norm[i]**5 + 0.3 * x_norm[i]**4 + 
                           0.15 * x_norm[i] * x_norm[(i+1) % self.dim] * np.exp(-x_norm[i]**3))  # Changed exp term
            
        # Combined landscape with enhanced multimodality and conditioning
        return (0.25 * quantum_harm + 0.3 * tanh_chaos + 0.25 * quat_radial + 
                0.1 * fbm + 0.05 * cond_scaled + 0.05 * poly_radial + 2.0)