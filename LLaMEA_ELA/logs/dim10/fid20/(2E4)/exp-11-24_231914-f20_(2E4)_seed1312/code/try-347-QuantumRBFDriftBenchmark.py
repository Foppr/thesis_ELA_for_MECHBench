import numpy as np

class QuantumRBFDriftBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum harmonic oscillator parameters
        self.omega = np.random.uniform(0.5, 3.0, size=dim)
        self.phase = np.random.uniform(0, 2*np.pi, size=dim)
        self.amplitude = np.random.uniform(0.5, 2.0, size=dim)
        
        # Radial basis function cluster centers and widths
        self.rbf_centers = np.random.uniform(-4.5, 4.5, size=(15, dim))
        self.rbf_widths = np.random.uniform(0.3, 2.0, size=15)
        
        # Drift parameters for time-varying landscape
        self.drift_magnitude = np.random.uniform(0.1, 0.5, size=dim)
        self.drift_frequency = np.random.uniform(0.1, 0.3, size=dim)
        self.drift_phase = np.random.uniform(0, 2*np.pi, size=dim)
        
        # Quantum tunneling parameters
        self.tunnel_prob = np.random.uniform(0.01, 0.2, size=dim)
        self.tunnel_strength = np.random.uniform(0.5, 2.0, size=dim)
        
        # Multi-scale frequency components
        self.freq_scales = np.random.uniform(0.1, 2.0, size=dim)
        self.freq_amplitudes = np.random.uniform(0.5, 3.0, size=dim)
        
        # Temporal correlation effects
        self.temporal_corr = np.random.uniform(0.1, 0.8, size=dim)
        
        # Interaction coupling between dimensions
        self.coupling_strength = np.random.uniform(0.1, 1.0, size=(dim, dim))
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator component
        quantum_component = 0.0
        for i in range(self.dim):
            oscillator = self.amplitude[i] * np.sin(self.omega[i] * x[i] + self.phase[i])
            quantum_component += oscillator
            
        # Radial basis function clustering component
        rbf_component = 0.0
        for i in range(15):
            dist = np.sum((x - self.rbf_centers[i]) ** 2)
            rbf_val = np.exp(-dist / (2 * self.rbf_widths[i] ** 2))
            rbf_component += rbf_val
            
        # Drift dynamics component
        drift_component = 0.0
        for i in range(self.dim):
            drift_val = self.drift_magnitude[i] * np.sin(self.drift_frequency[i] * x[i] + self.drift_phase[i])
            drift_component += drift_val
            
        # Quantum tunneling effect
        tunnel_component = 0.0
        for i in range(self.dim):
            tunnel_val = self.tunnel_strength[i] * np.exp(-self.tunnel_prob[i] * np.abs(x[i]))
            tunnel_component += tunnel_val
            
        # Multi-scale frequency modulation
        freq_component = 0.0
        for i in range(self.dim):
            freq_val = self.freq_amplitudes[i] * np.sin(self.freq_scales[i] * x[i])
            freq_component += freq_val
            
        # Temporal correlation effects
        temporal_component = 0.0
        for i in range(self.dim):
            temporal_val = self.temporal_corr[i] * np.cos(x[i])
            temporal_component += temporal_val
            
        # Cross-dimensional coupling
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_component += self.coupling_strength[i, j] * x[i] * x[j]
                    
        # Combined function with time-varying drift
        t = np.sum(x)  # Time parameter based on input sum
        return (2.0 * quantum_component + 
                1.5 * rbf_component + 
                1.2 * drift_component + 
                0.8 * tunnel_component + 
                0.6 * freq_component + 
                0.4 * temporal_component + 
                0.3 * coupling_component)