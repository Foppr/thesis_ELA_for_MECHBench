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
            
            # Enhanced quantum harmonic oscillator potential with increased nonlinearity
            oscillator = 0.9 * np.sin(xi)**3 + 0.7 * np.cos(2 * xi) + 0.5 * np.sin(3 * xi) + 0.3 * np.sin(4 * xi)
            
            # Modified probabilistic tunneling wells with enhanced decay rates
            tunneling = 0.0
            for k in range(1, 9):
                tunneling += (1.0 / k**2.7) * np.exp(-k * np.abs(xi)) * np.cos(k * xi + 0.5 * i)
            
            # Enhanced adaptive energy landscape with more pronounced phase transitions
            energy_factor = 1.0 + 0.9 * np.sin(self.dim * 0.38 + i * 0.27) + 0.6 * np.cos(self.dim * 0.48 + i * 0.17)
            
            # Stronger cross-dimensional entanglement with fractal interference patterns
            entanglement = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    entanglement += (1.0 / (1.0 + distance**2.7)) * np.sin(xi + x_norm[j] + 0.35 * np.sin(i * j) + 0.25 * np.cos(i + j))
            
            # Combined quantum-inspired components with modified weighting scheme
            weight = 1.0 + 0.5 * np.sin(i * 0.65) * np.cos(self.dim * 0.22)
            result += weight * (energy_factor * oscillator + tunneling + 0.85 * entanglement)**2
            
        # Enhanced global scaling with more significant dimension-dependent quantum correction
        quantum_correction = 1.0 + 0.25 * np.sin(np.log(self.dim + 1) * 3.2)
        return quantum_correction * result / self.dim