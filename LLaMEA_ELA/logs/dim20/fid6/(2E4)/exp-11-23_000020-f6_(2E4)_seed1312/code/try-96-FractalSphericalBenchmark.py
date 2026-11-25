import numpy as np

class FractalSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-inspired harmonic coefficients
        self.quantum_coeffs = np.random.randn(dim, 4)
        # Hyperbolic tangent chaotic parameters
        self.tanh_params = np.random.rand(dim) * 3.0 + 0.5
        # Quaternion-based radial coupling
        self.quat_weights = np.random.randn(dim, 5)
        # Dynamic condition number variation
        self.condition_factors = np.random.rand(dim) * 4.0 + 0.5
        # Fractal Brownian motion parameters
        self.hurst = 0.1 + 0.4 * np.random.rand()
        self.fractal_dim = 2.0 + 1.0 * np.random.rand()
        # Stochastic resonance parameters
        self.resonance_freq = np.random.rand(dim) * 2.0 + 0.1
        self.resonance_amp = np.random.rand(dim) * 0.5 + 0.1
        # Saddle-point modulation
        self.saddle_params = np.random.randn(dim, 3)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Quantum-inspired harmonic component
        quantum_harm = 0.0
        for i in range(self.dim):
            for l in range(1, 5):
                quantum_harm += self.quantum_coeffs[i, l-1] * np.sin(l * x_norm[i]) * np.exp(-l * x_norm[i]**2)
        
        # Hyperbolic tangent chaotic component
        tanh_chaos = 0.0
        for i in range(self.dim):
            tanh_chaos += np.tanh(self.tanh_params[i] * x_norm[i]) * np.sin(15 * x_norm[i])
            
        # Quaternion-based radial coupling
        quat_radial = 0.0
        for i in range(self.dim):
            # Normalize quaternion weights
            quat_norm = np.linalg.norm(self.quat_weights[i])
            if quat_norm > 0:
                normalized_weights = self.quat_weights[i] / quat_norm
                quat_radial += np.sum(normalized_weights * np.sin(x_norm[i] * np.arange(5)))
        
        # Fractal Brownian motion component with dynamic scaling
        fbm = 0.0
        for i in range(self.dim):
            scale = 1.0
            for _ in range(8):
                fbm += scale * np.cos(x_norm[i] * (2**_)) * np.exp(-scale)
                scale *= self.hurst
        
        # Dynamic condition number scaling
        cond_scaled = 0.0
        for i in range(self.dim):
            cond_scaled += x_norm[i]**2 * self.condition_factors[i]
            
        # Multi-scale polynomial with radial basis coupling
        poly_radial = 0.0
        for i in range(self.dim):
            poly_radial += (x_norm[i]**6 + 0.5 * x_norm[i]**5 + 0.3 * x_norm[i]**4 + 
                           0.2 * x_norm[i]**3 + 0.1 * x_norm[i] * x_norm[(i+1) % self.dim] * np.exp(-x_norm[i]**2))
            
        # Stochastic resonance component
        stoch_res = 0.0
        for i in range(self.dim):
            stoch_res += self.resonance_amp[i] * np.sin(self.resonance_freq[i] * x_norm[i] + 
                                                       np.random.rand() * 2 * np.pi)
            
        # Saddle-point modulation
        saddle_mod = 0.0
        for i in range(self.dim):
            saddle_mod += (self.saddle_params[i, 0] * x_norm[i]**3 + 
                          self.saddle_params[i, 1] * x_norm[i]**2 + 
                          self.saddle_params[i, 2] * x_norm[i])
            
        # Combined landscape with enhanced multimodality and conditioning
        return (0.25 * quantum_harm + 0.2 * tanh_chaos + 0.18 * quat_radial + 
                0.17 * fbm + 0.08 * cond_scaled + 0.07 * poly_radial + 
                0.06 * stoch_res + 0.05 * saddle_mod + 1.3)