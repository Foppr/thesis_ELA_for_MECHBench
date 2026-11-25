import numpy as np

class QuantumRadialExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-inspired sinusoidal components with complex amplitudes and phases
        self.sin_freq = np.random.uniform(2.0, 15.0, size=dim)
        self.sin_amp = np.random.uniform(1.0, 4.0, size=dim)
        self.sin_phase = np.random.uniform(0, 2*np.pi, size=dim)
        # Enhanced radial basis functions with Gaussian and multiquadric combinations
        self.rbf_centers = np.random.uniform(-4.5, 4.5, size=(dim, 5))
        self.rbf_widths = np.random.uniform(0.3, 2.5, size=(dim, 5))
        self.rbf_weights = np.random.uniform(-1.5, 1.5, size=(dim, 5))
        # Exponential penalty mechanisms with multi-scale dynamics
        self.exp_penalty_strength = np.random.uniform(2.0, 8.0, size=dim)
        self.exp_penalty_rate = np.random.uniform(1.5, 4.0, size=dim)
        # Quantum coupling coefficients with complex interactions
        self.quantum_coupling = np.random.uniform(-1.0, 1.0, size=(dim, dim))
        # Dynamic scaling with logarithmic and power-law transformations
        self.scale_base = np.random.uniform(0.1, 3.0, size=dim)
        self.scale_exponent = np.random.uniform(0.5, 2.5, size=dim)
        # Cross-dimensional exponential interactions
        self.exp_interaction_coeffs = np.random.uniform(-0.8, 0.8, size=(dim, dim))
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum sinusoidal component
        sin_component = 0.0
        for i in range(self.dim):
            sin_val = self.sin_amp[i] * np.sin(self.sin_freq[i] * x[i] + self.sin_phase[i])
            sin_component += sin_val
            
        # Enhanced radial basis function component with mixed kernels
        rbf_component = 0.0
        for i in range(self.dim):
            rbf_val = 0.0
            for j in range(5):
                dist = np.sum((x - self.rbf_centers[i, j]) ** 2)
                # Combine Gaussian and multiquadric RBFs
                gaussian = np.exp(-dist / (2 * self.rbf_widths[i, j] ** 2))
                multiquadric = np.sqrt(dist + self.rbf_widths[i, j] ** 2)
                rbf_val += self.rbf_weights[i, j] * (0.6 * gaussian + 0.4 * multiquadric)
            rbf_component += rbf_val
            
        # Exponential penalty component
        penalty_component = 0.0
        for i in range(self.dim):
            dist_from_center = np.abs(x[i])
            penalty_val = self.exp_penalty_strength[i] * np.exp(self.exp_penalty_rate[i] * dist_from_center)
            penalty_component += penalty_val
            
        # Quantum scaling component
        scale_component = 0.0
        for i in range(self.dim):
            scale_val = self.scale_base[i] ** (self.scale_exponent[i] * x[i])
            scale_component += scale_val
            
        # Quantum coupling component with complex interactions
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_component += self.quantum_coupling[i, j] * np.sin(x[i] * x[j])
                    
        # Exponential interaction component
        exp_interaction_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    exp_interaction_component += self.exp_interaction_coeffs[i, j] * np.exp(-np.abs(x[i] - x[j]))
                    
        # Combine all components with appropriate weights
        return (2.0 * sin_component + 
                1.8 * rbf_component + 
                1.5 * penalty_component + 
                1.2 * scale_component + 
                0.9 * coupling_component + 
                0.7 * exp_interaction_component)