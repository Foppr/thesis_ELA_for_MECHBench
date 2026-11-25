import numpy as np

class QuantumEntanglementBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Enhanced quantum harmonic oscillator potential with entanglement
            oscillator = np.sin(xi)**2 + 0.5 * np.cos(2 * xi) + 0.3 * np.sin(3 * xi) + 0.1 * np.sin(4 * xi)
            
            # Modified probabilistic tunneling wells with enhanced quantum-like behavior
            tunneling = 0.0
            for k in range(1, 25):
                tunneling += (1.0 / k**3.5) * np.exp(-k * np.abs(xi)) * np.cos(k * xi + 0.5 * i + 0.1 * np.sin(k * xi))
            
            # Enhanced adaptive energy landscape with phase transitions
            energy_factor = 1.0 + 0.8 * np.sin(self.dim * 0.35 + i * 0.25) + 0.5 * np.cos(self.dim * 0.45 + i * 0.15) + 0.3 * np.sin(self.dim * 0.6 + i * 0.3) + 0.2 * np.sin(xi * 7.0)
            
            # Improved cross-dimensional entanglement term with fractal interference
            entanglement = 0.0
            for j in range(max(0, i-5), min(self.dim, i+6)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    entanglement += (1.0 / (1.0 + distance**4.0)) * np.sin(xi + x_norm[j] + 0.3 * np.sin(i * j) + 0.1 * np.cos(xi * x_norm[j]) + 0.05 * np.sin(5 * xi + 3 * x_norm[j]))
            
            # Enhanced quantum-inspired weighting with additional dimension-dependent factor
            weight = 1.0 + 0.4 * np.sin(i * 0.6) * np.cos(self.dim * 0.12) + 0.2 * np.cos(i * 0.4) + 0.15 * np.cos(xi * 5.0)
            
            # Add chaotic resonance terms for increased complexity
            chaotic_term = 0.08 * np.sin(13 * xi + 2.7 * i) * np.cos(7 * xi - 1.3 * i) + 0.05 * np.sin(17 * xi + 3.1 * i) + 0.03 * np.sin(23 * xi + 4.2 * i)
            
            # Add hyperdimensional fractal interference patterns
            fractal_pattern = 0.03 * np.sin(self.dim * 2.5 * xi + 0.5 * i) * np.cos(self.dim * 1.8 * xi - 0.3 * i) + 0.02 * np.sin(self.dim * 3.2 * xi + 0.7 * i)
            
            # Additional nonlinear cross-dimensional interaction term for increased complexity
            nonlinear_interaction = 0.1 * np.sin(2 * xi + 0.5 * i) * np.cos(3 * xi - 0.3 * i) * np.sin(0.7 * xi**2 + 0.2 * i) + 0.05 * np.cos(4 * xi + 0.1 * i)
            
            # Multi-scale fractal modulation term
            fractal_modulation = 0.04 * np.sin(11 * xi + 0.3 * i) * np.cos(9 * xi - 0.2 * i) * np.sin(5 * xi**3 + 0.1 * i)
            
            # Adaptive dimensionality scaling factor
            dim_scaling = 1.0 + 0.2 * np.sin(self.dim * 0.7) * np.cos(self.dim * 0.4) + 0.1 * np.sin(self.dim * 0.9)
            
            # Additional cross-dimensional coupling term with enhanced nonlinearity
            cross_coupling = 0.08 * np.sin(xi * 3.0 + 0.2 * i) * np.cos(xi * 2.0 - 0.1 * i) * np.sin(0.5 * xi**4 + 0.3 * i)
            
            # Enhanced hyperdimensional interaction term
            hyper_interaction = 0.06 * np.sin(self.dim * 0.8 * xi + 0.4 * i) * np.cos(self.dim * 0.6 * xi - 0.2 * i) + 0.04 * np.sin(self.dim * 1.2 * xi + 0.5 * i)
            
            # Increased nonlinearity in energy factor
            energy_factor = energy_factor * (1.0 + 0.3 * np.sin(xi * 8.0))
            
            result += weight * (energy_factor * oscillator + tunneling + 0.7 * entanglement + chaotic_term + fractal_pattern + nonlinear_interaction + fractal_modulation + cross_coupling + hyper_interaction)**2 * dim_scaling
            
        # Improved global scaling factor with dimension-dependent quantum correction
        quantum_correction = 1.0 + 0.2 * np.sin(np.log(self.dim + 1) * 2.2) + 0.08 * np.cos(np.log(self.dim + 1) * 3.1) + 0.15 * np.sin(self.dim * 0.5) + 0.05 * np.cos(self.dim * 0.3)
        return quantum_correction * result / self.dim