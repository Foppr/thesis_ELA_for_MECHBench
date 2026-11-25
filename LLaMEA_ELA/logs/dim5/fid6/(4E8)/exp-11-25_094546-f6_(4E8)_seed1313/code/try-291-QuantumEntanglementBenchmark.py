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
            for k in range(1, 20):
                tunneling += (1.0 / k**3.2) * np.exp(-k * np.abs(xi)) * np.cos(k * xi + 0.5 * i + 0.1 * np.sin(k * xi))
            
            # Enhanced adaptive energy landscape with phase transitions
            energy_factor = 1.0 + 0.8 * np.sin(self.dim * 0.4 + i * 0.3) + 0.5 * np.cos(self.dim * 0.5 + i * 0.2) + 0.3 * np.sin(self.dim * 0.7 + i * 0.4) + 0.2 * np.sin(xi * 8.0)
            
            # Improved cross-dimensional entanglement term with fractal interference
            entanglement = 0.0
            for j in range(max(0, i-5), min(self.dim, i+6)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    entanglement += (1.0 / (1.0 + distance**4.0)) * np.sin(xi + x_norm[j] + 0.4 * np.sin(i * j) + 0.15 * np.cos(xi * x_norm[j]) + 0.08 * np.sin(6 * xi + 4 * x_norm[j]))
            
            # Enhanced quantum-inspired weighting with additional dimension-dependent factor
            weight = 1.0 + 0.4 * np.sin(i * 0.7) * np.cos(self.dim * 0.15) + 0.2 * np.cos(i * 0.5) + 0.15 * np.cos(xi * 6.0)
            
            # Add chaotic resonance terms for increased complexity
            chaotic_term = 0.08 * np.sin(15 * xi + 3.0 * i) * np.cos(8 * xi - 1.5 * i) + 0.05 * np.sin(19 * xi + 3.5 * i) + 0.03 * np.sin(23 * xi + 4.1 * i)
            
            # Add hyperdimensional fractal interference patterns
            fractal_pattern = 0.03 * np.sin(self.dim * 3.0 * xi + 0.6 * i) * np.cos(self.dim * 2.0 * xi - 0.4 * i)
            
            # Additional nonlinear cross-dimensional interaction term for increased complexity
            nonlinear_interaction = 0.12 * np.sin(2.5 * xi + 0.6 * i) * np.cos(3.5 * xi - 0.4 * i) * np.sin(0.8 * xi**2 + 0.3 * i)
            
            # New mutation: increased entanglement strength and added cross-term coupling
            cross_coupling = 0.05 * np.sin(xi + 0.5 * x_norm[(i+1) % self.dim]) * np.cos(xi - 0.3 * x_norm[(i+2) % self.dim])
            
            result += weight * (energy_factor * oscillator + tunneling + 0.8 * entanglement + chaotic_term + fractal_pattern + nonlinear_interaction + cross_coupling)**2
            
        # Mutated global scaling factor with enhanced quantum correction
        quantum_correction = 1.0 + 0.2 * np.sin(np.log(self.dim + 1) * 2.5) + 0.08 * np.cos(np.log(self.dim + 1) * 3.5) + 0.15 * np.sin(self.dim * 0.6) + 0.05 * np.cos(self.dim * 0.8)
        return quantum_correction * result / self.dim