import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute quantum-like chaotic phase sequence
        self.phase_seq = np.array([0.5])
        for i in range(dim * 20):
            next_val = 4 * self.phase_seq[-1] * (1 - self.phase_seq[-1])
            self.phase_seq = np.append(self.phase_seq, next_val)
        self.phase_seq = self.phase_seq[:dim]
        
        # Precompute adaptive ridge coefficients
        self.ridge_coeffs = np.random.uniform(-2.0, 2.0, dim)
        
        # Precompute quantum superposition weights
        self.superposition_weights = np.random.uniform(0.5, 1.5, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Quantum-inspired superposition RBFs with phase modulation
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            dist = np.sum((x_norm - self.phase_seq[i])**2)
            phase_factor = np.sin(self.phase_seq[i] * np.pi * 2) + 1.5
            weight = self.superposition_weights[i] * phase_factor
            rbfs[i] = weight * np.exp(-dist / (2 * 0.02**2))
        
        # Dynamic phase-shifted chaotic interaction
        phase_shifted = np.sum(np.sin(self.phase_seq * x_norm + np.pi/4) * np.cos(2 * self.phase_seq * x_norm))
        
        # Adaptive ridge structure with chaotic scaling
        ridges = np.sum(self.ridge_coeffs * np.sin(x_norm * np.pi * 3) * np.exp(-0.5 * x_norm**2))
        
        # Multi-scale noise with quantum tunneling effect
        noise = np.sum(np.abs(x_norm) * np.random.uniform(0.1, 2.0, self.dim) * np.sin(x_norm * np.pi * 5))
        
        # Higher-order polynomial with quantum interference terms
        poly_interaction = np.sum(self.ridge_coeffs * (x_norm**5 + 0.3 * x_norm**7 + 0.02 * x_norm**9 + 
                                                       0.4 * np.sin(x_norm * np.pi * 4) * np.cos(x_norm * np.pi * 3)))
        
        # Adaptive sharp transition zones with quantum-like probability
        transitions = np.sum(np.abs(np.sin(x_norm * np.pi * 2)) > 0.85)
        
        # Combine all components with quantum-inspired weights
        total = 0.25 * np.sum(rbfs) + 0.25 * phase_shifted + 0.15 * ridges + 0.1 * noise + 0.15 * poly_interaction + 0.1 * transitions
        
        # Add quantum-like global scaling factor with dynamic phase
        phase_global = np.sin(np.sum(x_norm**2) * np.pi / 2)
        return total * (1 + 0.8 * phase_global + 0.3 * np.cos(np.sum(x_norm**3)))