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
        
        # Fractal basin coefficients for dynamic landscape
        self.fractal_coeffs = np.random.uniform(-2.0, 2.0, dim)
        
        # Adaptive noise scaling factors
        self.noise_scales = np.random.uniform(0.5, 2.5, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Quantum superposition RBFs with phase modulation
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            dist = np.sum((x_norm - self.quantum_seq[i])**2)
            phase = np.sin(self.quantum_seq[i] * np.pi * 2)
            weight = np.abs(phase) + 0.5
            rbfs[i] = weight * np.exp(-dist / (2 * 0.02**2)) * np.cos(dist * phase)
        
        # Fractal basin landscape with dynamic scaling
        fractal = np.sum(self.fractal_coeffs * np.sin(x_norm * np.pi * 4) * np.cos(x_norm * np.pi * 2))
        
        # Adaptive noise with dynamic scaling
        noise = np.sum(self.noise_scales * np.abs(x_norm) * np.random.uniform(0.1, 2.0, self.dim))
        
        # Hyperchaotic polynomial interactions with dynamic exponents
        exponents = 2 + np.sin(self.quantum_seq) * 3
        poly_interaction = np.sum((x_norm**exponents) * self.fractal_coeffs)
        
        # Dynamic transition zones with quantum tunneling probability
        tunnel_prob = 0.1 + 0.4 * np.sin(np.sum(x_norm**2))
        transitions = np.sum(np.abs(np.sin(x_norm * np.pi * 3)) > (0.7 + tunnel_prob * 0.3))
        
        # Combine all components with quantum weights
        total = 0.25 * np.sum(rbfs) + 0.25 * fractal + 0.2 * noise + 0.2 * poly_interaction + 0.1 * transitions
        
        # Add quantum-inspired global scaling with dynamic phase
        phase_factor = np.sin(np.sum(x_norm**3) * 0.5) + 1.5
        return total * phase_factor * (1 + 0.8 * np.sin(np.sum(x_norm**4)))