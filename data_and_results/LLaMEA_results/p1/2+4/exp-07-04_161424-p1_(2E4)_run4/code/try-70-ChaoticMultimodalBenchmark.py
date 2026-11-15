import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic logistic map sequence with quantum-like interference
        self.logistic_seq = np.array([0.5])
        for i in range(dim * 20):
            next_val = 4 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1])
            self.logistic_seq = np.append(self.logistic_seq, next_val)
        self.logistic_seq = self.logistic_seq[:dim]
        
        # Quantum-inspired phase factors for interference
        self.phase_factors = np.random.uniform(-np.pi, np.pi, dim)
        
        # Adaptive polynomial coupling coefficients
        self.poly_couplings = np.random.uniform(-2.0, 2.0, dim)
        
        # Dynamic basin boundaries
        self.basin_centers = np.random.uniform(-5.0, 5.0, dim)
        self.basin_widths = np.random.uniform(0.5, 2.0, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Quantum interference RBFs with phase modulation
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            dist = np.sum((x_norm - self.logistic_seq[i])**2)
            phase = np.sin(self.phase_factors[i] * x_norm[i])
            weight = np.abs(np.sin(self.logistic_seq[i] * np.pi)) + 0.5
            rbfs[i] = weight * np.exp(-dist / (2 * 0.02**2)) * np.abs(phase)
        
        # Chaotic interaction with quantum coupling
        chaotic = np.sum(np.sin(self.logistic_seq * x_norm + self.phase_factors) * 
                        np.cos(3 * self.logistic_seq * x_norm))
        
        # Adaptive polynomial interactions with quantum-like coupling
        poly_interaction = np.sum(self.poly_couplings * (x_norm**5 + 0.3 * x_norm**7 + 0.05 * x_norm**9))
        
        # Dynamic basin boundary effects
        basin_effects = np.sum(1.0 / (1.0 + np.exp(-10 * (x_norm - self.basin_centers) / self.basin_widths)))
        
        # Quantum tunneling noise
        noise = np.sum(np.abs(np.sin(x_norm * np.pi)) * np.random.uniform(0.5, 2.5, self.dim))
        
        # Sharp basin transitions with chaotic modulation
        transitions = np.sum(np.abs(np.sin(x_norm * np.pi * 2)) > 0.8)
        
        # Combine all components with quantum-inspired weights
        total = 0.25 * np.sum(rbfs) + 0.25 * chaotic + 0.15 * noise + 0.15 * poly_interaction + 0.2 * transitions + 0.05 * basin_effects
        
        # Add quantum scaling factor
        quantum_scale = 1 + 0.8 * np.sin(np.sum(x_norm**3))
        
        # Add dynamic conditioning based on input magnitude
        conditioning = 1 + 0.5 * np.tanh(np.sum(np.abs(x_norm)))
        
        return total * quantum_scale * conditioning