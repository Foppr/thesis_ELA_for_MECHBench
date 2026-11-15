import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic logistic map sequence with quantum-like phase shifts
        self.logistic_seq = np.array([0.5])
        for i in range(dim * 20):
            next_val = 4 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1])
            self.logistic_seq = np.append(self.logistic_seq, next_val)
        self.logistic_seq = self.logistic_seq[:dim]
        
        # Quantum-inspired interference pattern coefficients
        self.quantum_coeffs = np.random.uniform(-2.0, 2.0, dim)
        
        # Adaptive basin boundaries
        self.basin_shifts = np.random.uniform(-1.0, 1.0, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Quantum interference RBFs with dynamic phase
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            dist = np.sum((x_norm - self.logistic_seq[i])**2)
            phase = np.sin(self.logistic_seq[i] * np.pi * 2) * 0.5
            weight = np.abs(np.sin(self.logistic_seq[i] * np.pi)) + 0.5
            rbfs[i] = weight * np.exp(-dist / (2 * 0.02**2)) * np.cos(phase * dist)
        
        # Chaotic interaction with quantum phase modulation
        chaotic = np.sum(np.sin(self.logistic_seq * x_norm + np.pi/4) * np.cos(5 * self.logistic_seq))
        
        # Adaptive basin boundaries with dynamic scaling
        basins = np.sum(np.abs(x_norm - self.basin_shifts) < 0.3) * 0.5
        
        # Quantum-inspired noise with superposition
        noise = np.sum(np.abs(x_norm) * np.random.uniform(0.5, 2.5, self.dim) * 
                      np.sin(x_norm * np.pi * 3))
        
        # Higher-order polynomial interactions with quantum coefficients
        poly_interaction = np.sum(self.quantum_coeffs * (x_norm**5 + 0.3 * x_norm**7 + 0.05 * x_norm**9))
        
        # Dynamic phase transitions with quantum tunneling effect
        transitions = np.sum(np.abs(np.sin(x_norm * np.pi * 2)) > 0.8) * 0.3
        
        # Combine all components with quantum weights
        total = 0.25 * np.sum(rbfs) + 0.25 * chaotic + 0.2 * basins + 0.15 * noise + 0.1 * poly_interaction + 0.05 * transitions
        
        # Add quantum scaling factor with dynamic phase
        phase_factor = 1 + 0.8 * np.sin(np.sum(x_norm**3))
        return total * phase_factor * (1 + 0.5 * np.sin(np.sum(x_norm**2) * 0.5))