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
            
            # Quantum harmonic oscillator potential with entanglement
            oscillator = np.sin(xi)**2 + 0.5 * np.cos(2 * xi) + 0.3 * np.sin(3 * xi)
            
            # Probabilistic tunneling wells (quantum-like behavior) - modified coefficients
            tunneling = 0.0
            for k in range(1, 7):
                tunneling += (1.0 / k**3.0) * np.exp(-k * np.abs(xi)) * np.cos(k * xi + 0.6 * i)
            
            # Adaptive energy landscape with phase transitions - altered frequencies
            energy_factor = 1.0 + 0.7 * np.sin(self.dim * 0.4 + i * 0.3) + 0.4 * np.cos(self.dim * 0.5 + i * 0.2)
            
            # Cross-dimensional entanglement term with fractal interference - modified interaction
            entanglement = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    entanglement += (1.0 / (1.0 + distance**3.0)) * np.sin(xi + x_norm[j] + 0.4 * np.sin(i * j))
            
            # Combine all components with quantum-inspired weighting - modified weights
            weight = 1.0 + 0.3 * np.sin(i * 0.7) * np.cos(self.dim * 0.15)
            result += weight * (energy_factor * oscillator + tunneling + 0.7 * entanglement)**2
            
        # Add global scaling factor with dimension-dependent quantum correction - modified correction
        quantum_correction = 1.0 + 0.15 * np.sin(np.log(self.dim + 1) * 2.5)
        return quantum_correction * result / self.dim