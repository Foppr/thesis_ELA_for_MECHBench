import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic logistic map sequence with quantum-like phase modulation
        self.logistic_seq = np.array([0.5])
        for i in range(dim * 20):
            next_val = 4 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1])
            self.logistic_seq = np.append(self.logistic_seq, next_val)
        self.logistic_seq = self.logistic_seq[:dim]
        
        # Precompute quantum-inspired interference coefficients
        self.quantum_coeffs = np.random.uniform(-2.0, 2.0, dim)
        
        # Fractional Brownian motion parameters
        self.hurst = 0.7 + np.random.rand() * 0.2
        self.bm_scale = 1.0 + np.random.rand() * 2.0
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Quantum interference RBFs with phase modulation
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            dist = np.sum((x_norm - self.logistic_seq[i])**2)
            phase = np.sin(self.logistic_seq[i] * np.pi * 2) * np.cos(self.logistic_seq[i] * np.pi)
            weight = np.abs(np.sin(self.logistic_seq[i] * np.pi)) + 0.5 + phase * 0.2
            rbfs[i] = weight * np.exp(-dist / (2 * 0.02**2))
        
        # Chaotic interaction with fractional Brownian motion
        fbm = np.sum(np.sin(self.logistic_seq * x_norm * 2) * np.cos(2 * self.logistic_seq * x_norm))
        
        # Quantum-inspired noise with dynamic scaling
        quantum_noise = np.sum(np.abs(x_norm) * np.random.uniform(0.1, 2.5, self.dim) * 
                              np.sin(x_norm * np.pi * 3) * np.cos(x_norm * np.pi * 3))
        
        # Higher-order polynomial with quantum coefficients
        poly_interaction = np.sum(self.quantum_coeffs * (x_norm**5 + 0.3 * x_norm**7 + 0.02 * x_norm**9))
        
        # Adaptive basin connectivity with dynamic thresholds
        connectivity = np.sum(np.abs(np.sin(x_norm * np.pi * 4)) > 0.85)
        
        # Add quantum tunneling effects
        tunneling = np.sum(np.exp(-np.abs(x_norm) * 0.5) * np.sin(x_norm * np.pi * 5))
        
        # Combine all components with quantum weights
        total = 0.25 * np.sum(rbfs) + 0.2 * fbm + 0.15 * quantum_noise + 0.15 * poly_interaction + \
                0.1 * connectivity + 0.15 * tunneling
        
        # Add dynamic global scaling with quantum harmonic modulation
        quantum_scale = 1 + 0.8 * np.sin(np.sum(x_norm**2) * np.pi * 0.5) * np.cos(np.sum(x_norm**2) * np.pi * 0.3)
        return total * quantum_scale