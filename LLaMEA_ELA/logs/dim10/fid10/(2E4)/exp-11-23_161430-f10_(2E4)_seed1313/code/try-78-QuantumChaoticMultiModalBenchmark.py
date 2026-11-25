import numpy as np

class QuantumChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-inspired parameters
        self.quantum_angles = np.pi * np.random.rand(dim)
        self.phase_shifts = np.random.uniform(-np.pi, np.pi, dim)
        # Chaos parameters for temporal dynamics
        self.chaos_params = 3.8 + 0.2 * np.sin(np.arange(dim) * 0.3)
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.rbf_widths = 0.5 + 1.5 * np.random.rand(10)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired phase transition component
        quantum_term = 0.0
        for i in range(self.dim):
            angle = self.quantum_angles[i] + x[i] * 0.1
            phase = self.phase_shifts[i]
            quantum_term += np.sin(angle) * np.cos(phase) * np.exp(-0.05 * x[i]**2)
        
        # Radial basis functions with temporal chaos modulation
        rbf_sum = 0.0
        for i in range(10):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            diff = x - center
            rbf_sum += np.exp(-np.sum(diff**2) / (2 * width**2))
        
        # Chaotic temporal component with dynamic parameters
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_param = self.chaos_params[i]
            # Tent map dynamics
            tent_val = chaos_param * np.abs(x[i] - 0.5)
            if tent_val > 0.5:
                tent_val = 1.0 - tent_val
            chaos_term += tent_val * np.sin(x[i]**2) * np.cos(x[i])
        
        # Multi-modal interaction term with adaptive coupling
        modal_interaction = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            # Adaptive coupling weights based on chaotic dynamics
            weight_ij = 0.5 + 0.3 * np.sin(x[i] * x[j])
            weight_ik = 0.4 + 0.2 * np.cos(x[i] * x[k])
            modal_interaction += weight_ij * np.sin(3 * x[i]) * np.cos(2 * x[j]) + \
                               weight_ik * np.cos(4 * x[i]) * np.sin(x[k])
        
        # Combined fitness with dynamic scaling
        result = 0.15 * np.sum(x**2) + 0.35 * quantum_term + 0.25 * rbf_sum + \
                 0.18 * chaos_term + 0.07 * modal_interaction
        
        return result