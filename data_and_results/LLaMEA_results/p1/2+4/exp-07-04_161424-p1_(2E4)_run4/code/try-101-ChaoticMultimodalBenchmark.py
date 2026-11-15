import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-inspired chaotic sequence with superposition states
        self.quantum_seq = np.array([0.5])
        for i in range(dim * 20):
            next_val = 4 * self.quantum_seq[-1] * (1 - self.quantum_seq[-1])
            self.quantum_seq = np.append(self.quantum_seq, next_val)
        self.quantum_seq = self.quantum_seq[:dim]
        
        # Phase-shifted polynomial coefficients for dynamic interactions
        self.phase_coeffs = np.random.uniform(-2.0, 2.0, dim)
        self.basin_params = np.random.uniform(0.1, 1.0, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Quantum superposition RBFs with phase modulation
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            dist = np.sum((x_norm - self.quantum_seq[i])**2)
            phase = np.sin(self.quantum_seq[i] * np.pi * 2)
            weight = np.abs(phase) + 0.5
            rbfs[i] = weight * np.exp(-dist / (2 * (0.02 + 0.03 * np.abs(phase))**2))
        
        # Dynamic phase-shifted chaotic interaction
        phase_shifts = np.sin(self.quantum_seq * np.pi * 0.5)
        chaotic = np.sum(np.sin(x_norm * phase_shifts) * np.cos(2 * x_norm * phase_shifts))
        
        # Adaptive basin boundaries with quantum tunneling effect
        basins = np.sum(self.basin_params * np.exp(-0.5 * (x_norm / 0.3)**2))
        
        # Higher-order polynomial with quantum coefficient modulation
        poly_interaction = np.sum(self.phase_coeffs * (x_norm**5 + 0.3 * x_norm**7 + 0.02 * x_norm**9))
        
        # Quantum tunneling noise with dynamic scaling
        tunneling = np.sum(np.abs(x_norm) * np.random.uniform(0.1, 2.5, self.dim) * np.sin(x_norm * np.pi))
        
        # Multi-scale transition zones with quantum interference
        transitions = np.sum(np.abs(np.sin(x_norm * np.pi * 3)) > 0.85)
        
        # Combine all components with quantum-inspired weights
        total = 0.25 * np.sum(rbfs) + 0.2 * chaotic + 0.15 * basins + 0.15 * poly_interaction + 0.1 * tunneling + 0.15 * transitions
        
        # Add quantum phase factor for global scaling
        phase_factor = 1 + 0.7 * np.sin(np.sum(x_norm**3))
        
        return total * phase_factor