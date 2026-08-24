import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-inspired chaotic sequence with superposition
        self.quantum_seq = np.array([0.5])
        for i in range(dim * 20):
            next_val = 4 * self.quantum_seq[-1] * (1 - self.quantum_seq[-1])
            self.quantum_seq = np.append(self.quantum_seq, next_val)
        self.quantum_seq = self.quantum_seq[:dim]
        
        # Phase modulation coefficients for dynamic landscape
        self.phase_coeffs = np.random.uniform(-2.0, 2.0, dim)
        
        # Adaptive ridge parameters
        self.ridge_params = np.random.uniform(0.1, 2.0, dim)
        
        # Superposition weights
        self.superposition_weights = np.random.uniform(0.5, 1.5, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Quantum superposition RBFs with phase modulation
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            dist = np.sum((x_norm - self.quantum_seq[i])**2)
            phase = np.sin(self.phase_coeffs[i] * x_norm[i])
            weight = np.abs(np.sin(self.quantum_seq[i] * np.pi)) * self.superposition_weights[i]
            rbfs[i] = weight * np.exp(-dist / (2 * (0.02 + 0.01 * np.abs(phase))**2))
        
        # Chaotic interaction with quantum phase coupling
        chaotic = np.sum(np.sin(self.quantum_seq * x_norm) * np.cos(3 * self.quantum_seq + np.pi * x_norm))
        
        # Adaptive ridge structure with dynamic scaling
        ridges = np.sum(self.ridge_params * np.exp(-0.5 * (x_norm / 0.3)**2) * np.cos(2 * np.pi * x_norm))
        
        # Multi-scale noise with quantum tunneling effect
        noise = np.sum(np.abs(x_norm) * np.random.uniform(0.1, 2.5, self.dim) * 
                      np.sin(10 * x_norm + np.random.rand()))
        
        # Higher-order polynomial with quantum coefficient modulation
        poly_interaction = np.sum(self.superposition_weights * (x_norm**5 + 0.3 * x_norm**7 + 0.02 * x_norm**9))
        
        # Sharp transition zones with quantum tunneling probability
        transitions = np.sum(np.abs(np.sin(x_norm * np.pi)) > 0.85)
        
        # Quantum phase interference pattern
        interference = np.sum(np.sin(x_norm * np.pi * 2) * np.cos(x_norm * np.pi * 3))
        
        # Combine all components with quantum-inspired weights
        total = 0.25 * np.sum(rbfs) + 0.2 * chaotic + 0.15 * ridges + 0.1 * noise + 0.15 * poly_interaction + 0.1 * transitions + 0.05 * interference
        
        # Add quantum scaling factor with dynamic phase
        phase_factor = 1 + 0.5 * np.sin(np.sum(x_norm**3) * np.pi)
        return total * phase_factor * (1 + 0.4 * np.sin(np.sum(x_norm**2)))