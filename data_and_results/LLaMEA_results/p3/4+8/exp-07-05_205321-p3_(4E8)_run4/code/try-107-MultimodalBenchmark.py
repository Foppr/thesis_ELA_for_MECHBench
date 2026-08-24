import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal-like radial component with self-similar harmonic patterns
        r = np.sqrt(np.sum(x_norm**2))
        fractal_radial = np.exp(-r**1.5) * (1.0 + 0.5 * np.sin(12 * r) + 0.3 * np.cos(9 * r) + 0.2 * np.sin(15 * r**2))
        
        # Quantum harmonic angular terms with phase shifts
        angular = 0.0
        for i in range(self.dim):
            angular += np.sin((i + 1) * np.pi * x_norm[i] * 1.2) * np.cos((i + 1) * np.pi * x_norm[i] * 1.2)
            if i > 0:
                angular += 0.2 * np.sin(4 * np.pi * x_norm[i-1]) * np.sin(4 * np.pi * x_norm[i]) * np.cos(2 * np.pi * (x_norm[i-1] + x_norm[i]))
        
        # Adaptive noise component that varies with dimensionality
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(20 * np.pi * x_norm[i] + i * 0.5) * np.cos(18 * np.pi * x_norm[i] - i * 0.3)
        
        # Cross-dimensional quantum coupling terms
        quantum_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for computational efficiency
                quantum_coupling += 0.15 * np.sin(7 * np.pi * x_norm[i]) * np.cos(6 * np.pi * x_norm[j]) * np.sin(3 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Fractal periodicity with multiple scales
        periodic = 0.0
        scales = [3, 5, 7, 9]
        for scale in scales:
            periodic += np.sum(np.sin(scale * np.pi * x_norm + 0.5) * np.cos(scale * np.pi * x_norm - 0.3))
        
        # Power-law interaction terms for long-range dependencies
        power_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                power_interaction += 0.05 * np.sin(8 * np.pi * dist) / (1.0 + dist**2)
        
        # Combine all components with adjusted weights
        return 0.25 * fractal_radial + 0.2 * angular + 0.2 * noise + 0.15 * quantum_coupling + 0.1 * periodic + 0.1 * power_interaction + 1.0