import numpy as np

class QuantumHarmonicRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum harmonic field parameters
        self.quantum_freq = np.random.uniform(1.0, 10.0, size=dim)
        self.quantum_amp = np.random.uniform(0.5, 3.0, size=dim)
        self.quantum_phase = np.random.uniform(0, 2*np.pi, size=dim)
        self.quantum_coupling = np.random.uniform(0.1, 2.0, size=dim)
        
        # Adaptive radial basis functions
        self.rbf_centers = np.random.uniform(-4.5, 4.5, size=(15, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, size=15)
        self.rbf_weights = np.random.uniform(-2.0, 2.0, size=15)
        
        # Dynamic gradient corridors
        self.corridor_centers = np.random.uniform(-4.0, 4.0, size=(8, dim))
        self.corridor_widths = np.random.uniform(0.3, 2.0, size=8)
        self.corridor_strengths = np.random.uniform(1.0, 5.0, size=8)
        
        # Time-varying topology parameters
        self.time_freq = np.random.uniform(0.1, 0.5, size=dim)
        self.time_amp = np.random.uniform(0.1, 1.0, size=dim)
        self.time_phase = np.random.uniform(0, 2*np.pi, size=dim)
        
        # Adaptive basin parameters
        self.basin_centers = np.random.uniform(-4.8, 4.8, size=(10, dim))
        self.basin_radii = np.random.uniform(0.2, 2.5, size=10)
        self.basin_depths = np.random.uniform(0.5, 6.0, size=10)
        
        # Multi-scale harmonic components
        self.harmonic_freqs = np.random.uniform(0.5, 15.0, size=dim)
        self.harmonic_amps = np.random.uniform(0.3, 4.0, size=dim)
        
        # Cross-dimensional coupling with varying strengths
        self.coupling_matrix = np.random.uniform(-1.0, 1.0, size=(dim, dim))
        np.fill_diagonal(self.coupling_matrix, 0.0)
        
        # Quantum interference terms
        self.quantum_interference = np.random.uniform(0.2, 1.5, size=dim)
        
        # Dynamic scaling factors
        self.scaling_factors = np.random.uniform(0.5, 2.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic field component
        quantum_field = 0.0
        for i in range(self.dim):
            freq = self.quantum_freq[i] + self.time_amp[i] * np.sin(self.time_freq[i] * x[i] + self.time_phase[i])
            amp = self.quantum_amp[i] * (1 + 0.5 * np.sin(2 * self.time_freq[i] * x[i]))
            phase = self.quantum_phase[i] + self.quantum_coupling[i] * np.cos(x[i])
            quantum_field += amp * np.sin(freq * x[i] + phase)
        
        # Radial basis function component
        rbf_component = 0.0
        for i in range(15):
            dist = np.sum((x - self.rbf_centers[i]) ** 2)
            rbf_component += self.rbf_weights[i] * np.exp(-dist / (2 * self.rbf_widths[i]**2))
        
        # Gradient corridor component
        corridor_component = 0.0
        for i in range(8):
            dist = np.sum((x - self.corridor_centers[i]) ** 2)
            corridor_component += self.corridor_strengths[i] * np.exp(-dist / (2 * self.corridor_widths[i]**2))
        
        # Basin interaction component
        basin_component = 0.0
        for i in range(10):
            dist = np.sum((x - self.basin_centers[i]) ** 2)
            if dist <= self.basin_radii[i]**2:
                basin_component += self.basin_depths[i] * (1 - dist / self.basin_radii[i]**2)
        
        # Multi-scale harmonic component
        harmonic_component = 0.0
        for i in range(self.dim):
            freq = self.harmonic_freqs[i]
            amp = self.harmonic_amps[i]
            harmonic_component += amp * np.sin(freq * x[i])
        
        # Cross-dimensional coupling
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_component += self.coupling_matrix[i, j] * x[i] * x[j]
        
        # Quantum interference component
        interference_component = 0.0
        for i in range(self.dim):
            freq = self.quantum_freq[i] + self.quantum_interference[i] * np.cos(x[i])
            interference_component += self.quantum_amp[i] * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Time-varying topology effect
        time_component = 0.0
        for i in range(self.dim):
            time_component += self.time_amp[i] * np.cos(self.time_freq[i] * x[i] + self.time_phase[i])
        
        # Dynamic scaling component
        scale_component = 0.0
        for i in range(self.dim):
            scale_component += self.scaling_factors[i] * np.sin(x[i])
        
        # Combine all components with appropriate weights
        return (1.5 * quantum_field + 
                1.2 * rbf_component + 
                1.3 * corridor_component + 
                1.4 * basin_component + 
                1.1 * harmonic_component + 
                0.8 * coupling_component + 
                0.6 * interference_component + 
                0.5 * time_component + 
                0.4 * scale_component)