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
        
        # Fractal basin coefficients for dynamic landscape modulation
        self.fractal_coeffs = np.random.uniform(-2.0, 2.0, dim)
        
        # Adaptive noise corridors with time-varying amplitudes
        self.noise_amplitudes = np.random.uniform(0.5, 2.5, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Quantum superposition RBFs with phase modulation
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            dist = np.sum((x_norm - self.quantum_seq[i])**2)
            phase = np.sin(self.quantum_seq[i] * np.pi * 2)
            weight = np.abs(phase) + 0.5
            rbfs[i] = weight * np.exp(-dist / (2 * 0.02**2)) * np.cos(5 * self.quantum_seq[i])
        
        # Dynamic fractal landscape with multi-scale interactions
        fractal = np.sum(self.fractal_coeffs * np.sin(x_norm * np.pi * 3) * np.cos(x_norm * np.pi * 7))
        
        # Adaptive noise corridors with directional bias
        noise = np.sum(self.noise_amplitudes * np.sin(x_norm * np.pi) * np.random.uniform(0.1, 2.0, self.dim))
        
        # Multi-scale polynomial interactions with chaotic modulation
        poly_interaction = np.sum((x_norm**3 + 0.3 * x_norm**5 + 0.02 * x_norm**7) * self.quantum_seq)
        
        # Sharp fractal transition zones with quantum tunneling effects
        transitions = np.sum(np.abs(np.sin(x_norm * np.pi * 4)) > 0.85)
        
        # Superposition of multiple chaotic attractors
        attractor = np.sum(np.sin(self.quantum_seq * x_norm) * np.cos(2 * self.quantum_seq * x_norm))
        
        # Combine all components with quantum-weighted dynamic scaling
        total = 0.25 * np.sum(rbfs) + 0.2 * fractal + 0.15 * noise + 0.1 * poly_interaction + 0.15 * transitions + 0.15 * attractor
        
        # Add quantum-inspired global scaling with fractal dimension modulation
        fractal_dim = 1.5 + 0.5 * np.sin(np.sum(x_norm**2) * 0.5)
        return total * (1 + 0.8 * np.sin(np.sum(x_norm**2) * fractal_dim))