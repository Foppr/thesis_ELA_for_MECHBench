import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute quantum-inspired chaotic sequence with superposition
        self.quantum_seq = np.array([0.5])
        for i in range(dim * 20):
            next_val = 4 * self.quantum_seq[-1] * (1 - self.quantum_seq[-1])
            self.quantum_seq = np.append(self.quantum_seq, next_val)
        self.quantum_seq = self.quantum_seq[:dim]
        
        # Precompute adaptive ridge coefficients
        self.ridge_coeffs = np.random.uniform(-2.0, 2.0, dim)
        
        # Precompute phase shift parameters
        self.phase_shifts = np.random.uniform(-np.pi, np.pi, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Quantum superposition RBFs with complex phase modulation
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            dist = np.sum((x_norm - self.quantum_seq[i])**2)
            phase = np.sin(self.quantum_seq[i] * np.pi + self.phase_shifts[i])
            weight = np.abs(phase) + 0.5
            rbfs[i] = weight * np.exp(-dist / (2 * 0.02**2)) * np.cos(self.quantum_seq[i] * 2 * np.pi)
        
        # Adaptive ridge structure with chaotic modulation
        ridges = np.sum(self.ridge_coeffs * np.sin(x_norm * self.quantum_seq + self.phase_shifts) * np.exp(-0.5 * x_norm**2))
        
        # Dynamic phase-shifted chaotic interaction
        chaotic = np.sum(np.sin(self.quantum_seq * x_norm + self.phase_shifts) * np.cos(2 * self.quantum_seq * x_norm))
        
        # Multi-scale noise with quantum tunneling effect
        noise = np.sum(np.abs(x_norm) * np.random.uniform(0.1, 2.0, self.dim) * np.sin(x_norm * 10))
        
        # Higher-order polynomial with quantum coefficients
        poly_interaction = np.sum(np.abs(self.quantum_seq) * (x_norm**5 + 0.3 * x_norm**7 + 0.02 * x_norm**9))
        
        # Sharp ridge transitions with quantum probability
        transitions = np.sum(np.abs(np.cos(x_norm * np.pi)) > 0.85)
        
        # Combine all components with quantum-inspired weights
        total = 0.25 * np.sum(rbfs) + 0.2 * ridges + 0.15 * chaotic + 0.15 * noise + 0.1 * poly_interaction + 0.15 * transitions
        
        # Add quantum scaling factor with dynamic phase
        phase_factor = 1 + 0.8 * np.sin(np.sum(x_norm**2) * np.pi / 4)
        return total * phase_factor * (1 + 0.5 * np.sin(np.sum(x_norm**3)))