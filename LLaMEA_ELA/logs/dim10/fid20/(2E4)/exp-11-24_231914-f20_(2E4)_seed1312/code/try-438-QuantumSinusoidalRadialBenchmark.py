import numpy as np

class QuantumSinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic sinusoidal components with quantum-like frequencies
        self.sin_freq = np.random.uniform(5.0, 20.0, size=dim)
        self.sin_amp = np.random.uniform(1.0, 5.0, size=dim)
        # Quantum-inspired radial basis functions with complex coupling
        self.rbf_centers = np.random.uniform(-4.5, 4.5, size=(dim, 5))
        self.rbf_widths = np.random.uniform(0.2, 3.0, size=(dim, 5))
        self.rbf_weights = np.random.uniform(-2.0, 2.0, size=(dim, 5))
        # Enhanced quantum penalty mechanisms
        self.penalty_strength = np.random.uniform(2.0, 8.0, size=dim)
        self.penalty_exponent = np.random.uniform(3.0, 10.0, size=dim)
        # Dynamic scaling with quantum phase factors
        self.scale_factor = np.random.uniform(0.1, 3.0, size=dim)
        # Cross-dimensional coupling with quantum interference terms
        self.coupling_coeffs = np.random.uniform(-1.0, 1.0, size=(dim, dim))
        # Phase shifts with quantum-like randomness
        self.phase_shifts = np.random.uniform(0, 4*np.pi, size=dim)
        # Quantum tunneling parameters
        self.tunnel_prob = np.random.uniform(0.01, 0.5, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sinusoidal component with quantum interference
        sin_component = 0.0
        for i in range(self.dim):
            sin_val = self.sin_amp[i] * np.sin(self.sin_freq[i] * x[i] + self.phase_shifts[i])
            # Add quantum-like interference term
            if i > 0:
                sin_val += 0.5 * np.sin(self.sin_freq[i-1] * x[i] + self.phase_shifts[i-1]) * np.cos(x[i-1])
            sin_component += sin_val
            
        # Quantum-inspired radial basis function component
        rbf_component = 0.0
        for i in range(self.dim):
            rbf_val = 0.0
            for j in range(5):
                dist = np.sum((x - self.rbf_centers[i, j]) ** 2)
                # Add quantum-like weighting
                weight = self.rbf_weights[i, j] * np.exp(-dist / (2 * self.rbf_widths[i, j] ** 2))
                rbf_val += weight
            rbf_component += rbf_val
            
        # Enhanced quantum penalty component
        penalty_component = 0.0
        for i in range(self.dim):
            dist_from_center = np.abs(x[i])
            penalty_val = self.penalty_strength[i] * (dist_from_center ** self.penalty_exponent[i])
            # Add quantum tunneling effect
            if np.random.random() < self.tunnel_prob[i]:
                penalty_val *= 0.1
            penalty_component += penalty_val
            
        # Dynamic scaling with quantum phase factors
        scale_component = 0.0
        for i in range(self.dim):
            # Add quantum-like scaling factor
            scale_val = self.scale_factor[i] * x[i] * np.sin(x[i])
            scale_component += scale_val
            
        # Cross-dimensional coupling with quantum interference
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Add quantum interference term
                    interference = np.sin(x[i] * x[j]) * self.coupling_coeffs[i, j]
                    coupling_component += interference
                    
        # Combine all components with enhanced weights
        return (2.0 * sin_component + 
                1.5 * rbf_component + 
                1.2 * penalty_component + 
                1.0 * scale_component + 
                0.8 * coupling_component)