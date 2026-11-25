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
            
            # Probabilistic tunneling wells (quantum-like behavior)
            tunneling = 0.0
            for k in range(1, 6):
                tunneling += (1.0 / k**2) * np.exp(-k * np.abs(xi)) * np.cos(k * xi)
            
            # Adaptive energy landscape with phase transitions
            energy_factor = 1.0 + 0.5 * np.sin(self.dim * 0.3 + i * 0.2) + 0.3 * np.cos(self.dim * 0.4 + i * 0.1)
            
            # Cross-dimensional entanglement term
            entanglement = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    entanglement += (1.0 / (1.0 + (xi - x_norm[j])**2)) * np.sin(xi + x_norm[j])
            
            # Combine all components with quantum-inspired weighting
            weight = 1.0 + 0.2 * np.sin(i * 0.5) * np.cos(self.dim * 0.1)
            result += weight * (energy_factor * oscillator + tunneling + 0.5 * entanglement)**2
            
        # Add global scaling factor with dimension-dependent quantum correction
        quantum_correction = 1.0 + 0.1 * np.sin(np.log(self.dim + 1) * 2.0)
        return quantum_correction * result / self.dim